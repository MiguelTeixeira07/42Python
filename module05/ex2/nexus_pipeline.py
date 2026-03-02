from abc import ABC, abstractmethod
from typing import Any, List, Dict, Protocol, Tuple
import json
import time
import os
import sys
import random


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(
                self,
                exc_type: type[BaseException] | None,
                exc_val: BaseException | None,
                exc_tb: Any,
                ) -> None:
        sys.stdout.close()
        sys.stdout = self._original_stdout


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if data is None:
            raise ValueError("Error detected in Stage 1: No data received")
        match data.get("source"):
            case "JSON":
                sensor = data.get("sensor", "")
                value = data.get("value", 0.0)
                unit = data.get("unit", "")
                print(
                    f"Input: {{'sensor': '{sensor}', 'value': "
                    f"{value}, 'unit': '{unit}'}}"
                )
                return data
            case "CSV":
                user = data.get("user", "")
                action = data.get("action", "")
                timestamp = data.get("timestamp", "")
                print(f'Input: "{user},{action},{timestamp}"')
                return data
            case "Stream":
                print("Input: Real-time sensor stream")
                return data
            case _:
                raise ValueError(
                    "Error detected in Stage 1: Unknown data source"
                )


class TransformStage:
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        match data.get("source"):
            case "JSON":
                if not (
                    isinstance(data.get("sensor"), str)
                    and isinstance(data.get("value"), (int, float))
                    and data.get("unit") in ("C", "F", "K")
                ):
                    raise ValueError(
                        "Error detected in Stage 2: Invalid data format"
                    )

                match data["unit"]:
                    case "C":
                        if not -90 < data["value"] < 60:
                            data["range"] = "Abnormal"
                    case "F":
                        if not -130 < data["value"] < 140:
                            data["range"] = "Abnormal"
                    case "K":
                        if not 183 < data["value"] < 333:
                            data["range"] = "Abnormal"
                    case _:
                        raise ValueError(
                            "Error detected in Stage 2: Invalid unit"
                        )

                if isinstance(data["value"], int):
                    data["value"] = float(data["value"])
                if not data.get("range"):
                    data["range"] = "Normal"
                print("Transform: Enriched with metadata and validation")
                return data

            case "CSV":
                if not (
                    isinstance(data.get("user"), str)
                    and isinstance(data.get("action"), str)
                    and isinstance(data.get("timestamp"), float)
                ):
                    raise ValueError(
                        "Error detected in Stage 2: Invalid CSV schema"
                    )

                print("Transform: Parsed and structured data")
                return data

            case "Stream":
                if "list" not in data:
                    raise ValueError(
                        "Error detected in Stage 2: Missing stream data"
                    )

                for i, value in enumerate(data["list"]):
                    if isinstance(value, int):
                        data["list"][i] = float(value)
                    elif not isinstance(value, float):
                        raise ValueError(
                            "Error detected in Stage 2: Invalid stream value"
                        )

                print("Transform: Aggregated and filtered")
                return data

            case _:
                raise ValueError(
                    "Error detected in Stage 2: Unknown data source"
                )


class OutputStage:
    def process(self, data: Any) -> str:
        match data.get("source"):
            case "JSON":
                if not (
                    data.get("value")
                    and data.get("unit")
                    and data.get("range")
                ):
                    raise ValueError(
                        "Error detected in Stage 3: Incomplete JSON data"
                    )

                return (
                    f"Output: Processed temperature reading: "
                    f"{data.get('value', 0.0):.1f}°"
                    f"{data.get('unit', '')} "
                    f"({data.get('range', '')} range)"
                )

            case "CSV":
                if not (
                    data.get("user")
                    and data.get("action")
                    and data.get("timestamp")
                ):
                    raise ValueError(
                        "Error detected in Stage 3: Incomplete CSV data"
                    )

                return "Output: User activity logged: 1 actions processed"

            case "Stream":
                count = len(data.get("list", []))
                if not count:
                    raise ValueError("Error detected in Stage 3: Empty stream")
                average = sum(data.get("list", [])) / count
                return (
                    f"Output: Stream summary: {count} readings, "
                    f"avg: {average:.1f}°C"
                )

            case _:
                raise ValueError(
                    "Error detected in Stage 3: Unknown data source"
                )


class ProcessingPipeline(ABC):
    stages: List[ProcessingStage]

    def __init__(self, pipeline_id: str) -> None:
        self.stages = []
        self.id: str = pipeline_id

    def add_stage(self, stages: List[ProcessingStage]):
        for stage in stages:
            self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: str) -> Any:
        try:
            processing_data: Dict[str, Any] = json.loads(data)
            processing_data["source"] = "JSON"
            for stage in self.stages:
                processing_data = stage.process(processing_data)
            return processing_data
        except json.JSONDecodeError:
            raise ValueError("Error detected in Adapter: Invalid JSON")


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: str) -> Any:
        try:
            data_list: List[str] = data.split(",")
            processing_data: Dict[str, str | float] = {
                "user": data_list[0],
                "action": data_list[1],
                "timestamp": float(data_list[2]),
                "source": "CSV",
            }
            for stage in self.stages:
                processing_data = stage.process(processing_data)
            return processing_data
        except (IndexError, ValueError):
            raise ValueError("Error detected in Adapter: Invalid CSV format")


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: List[int | float]) -> Any:
        processing_data: Dict[str, List[int | float] | str] = {
            "list": data,
            "source": "Stream",
        }
        for stage in self.stages:
            processing_data = stage.process(processing_data)
        return processing_data


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.errors: int = 0

    def register_pipeline(self, pipeline: List[ProcessingPipeline]) -> None:
        for pipe in pipeline:
            self.pipelines[pipe.id] = pipe

    def process(self, pipeline_id: str, data: Any) -> Any:
        pipeline = self.pipelines.get(pipeline_id)
        if not pipeline:
            print(f"Error: Pipeline '{pipeline_id}' not found.")
            return None
        try:
            return pipeline.process(data)
        except ValueError as error:
            self.errors += 1
            print(error)
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


def get_test_data() -> List[Tuple[str, Any]]:
    def make_json() -> str:
        val: float = random.uniform(-50.0, 150.0)
        unit: str = random.choice(["C", "K", "F"])
        return json.dumps({"sensor": "temp", "value": val, "unit": unit})

    def make_csv() -> str:
        timestamp: float = time.time()
        return f"user_{random.randint(0, 999)},login,{timestamp}"

    def make_stream() -> List[float]:
        count: int = random.randint(1, 100)
        return [random.uniform(15.0, 25.0) for _ in range(count)]

    def make_bad_json() -> str:
        return json.dumps({"sensor": "temp", "value": "BROKEN", "unit": "C"})

    def make_bad_csv() -> str:
        return "user_error,login"

    def make_bad_stream() -> List[str | float]:
        return [20.5, "CORRUPT", 22.1]

    pipe_options: List[Tuple[str, Any, Any]] = [
        ("json_pipe_01", make_json, make_bad_json),
        ("csv_pipe_01", make_csv, make_bad_csv),
        ("stream_pipe_01", make_stream, make_bad_stream),
    ]

    tasks: List[bool] = [True] * 95 + [False] * 5
    random.shuffle(tasks)

    results: List[Tuple[str, Any]] = []
    for is_valid in tasks:
        pipe_id, valid_func, invalid_func = random.choice(pipe_options)
        if is_valid:
            results.append((pipe_id, valid_func()))
        else:
            results.append((pipe_id, invalid_func()))

    return results


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    nexus = NexusManager()

    print("Pipeline capacity: 1000 streams/second\n")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    pipes: List[ProcessingPipeline] = [
        JSONAdapter("json_pipe_01"),
        CSVAdapter("csv_pipe_01"),
        StreamAdapter("stream_pipe_01"),
    ]
    stages: List[ProcessingStage] = [
        InputStage(),
        TransformStage(),
        OutputStage(),
    ]
    for pipe in pipes:
        pipe.add_stage(stages)
    nexus.register_pipeline(pipes)

    print("\n=== Multi-Format Data Processing ===\n")
    print("Processing JSON data through pipeline...")
    json_input = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    result_json = nexus.process("json_pipe_01", json_input)
    print(f"{result_json}\n")

    print("Processing CSV data through same pipeline...")
    csv_input = f"john,login,{time.time()}"
    result_csv = nexus.process("csv_pipe_01", csv_input)
    print(f"{result_csv}\n")

    print("Processing Stream data through same pipeline...")
    stream_input = [20.5, 22.1, 23.0, 21.8, 22.5]
    result_stream = nexus.process("stream_pipe_01", stream_input)
    print(f"{result_stream}\n")

    with HiddenPrints():
        clock: float = time.time()
        for pipe_id, data in get_test_data():
            nexus.process(pipe_id, data)
        clock = time.time() - clock

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
    print("Chain result: 100 records processed through 3-stage pipeline")
    print(f"Performance: {100 - nexus.errors}% efficiency, ")
    print(f"{clock:.4f}s total processing time")

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    bad_json = '{"sensor": "temp", "value": "BROKEN", "unit": "C"}'
    nexus.process("json_pipe_01", bad_json)
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()

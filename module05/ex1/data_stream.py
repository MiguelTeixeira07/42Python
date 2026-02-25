from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional as Opt


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._processed_count: int = 0

    @abstractmethod
    def process_batch(self, bat: List[Any]) -> str:
        pass

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        return bat

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, bat: List[Any]) -> str:
        pass

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        return super().filter_data(bat, crit)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, bat: List[Any]) -> str:
        pass

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        return super().filter_data(bat, crit)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, bat: List[Any]) -> str:
        pass

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        return super().filter_data(bat, crit)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        results: List[str] = []

        for stream, batch in zip(self.streams, batches):
            results.append(stream.process_batch(batch))

        return results


def main() -> None:
    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor()

    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    sensor_batch = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ]

    transaction_batch = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ]

    event_batch = [
        "login",
        "error",
        "logout"
    ]

    batches = [sensor_batch, transaction_batch, event_batch]

    results = processor.process_all(batches)

    for result in results:
        print(result)


if __name__ == '__main__':
    main()

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional as Opt


def print_dicts(dict_list: List[Dict]) -> str:
    output = '['
    for dict in dict_list:
        keys = []

        for key in dict:
            keys += [key]

        if keys[0] == 'type':
            output += f'{dict[keys[0]]}:{dict[keys[1]]}'
        else:
            output += f'{keys[0]}:{dict[keys[0]]}'
        output += ', '
    output = output[:-2]
    output += ']'

    return output

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._processed_count: int = 0

    @abstractmethod
    def process_batch(self, bat: List[Any]) -> str:
        pass

    @abstractmethod
    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        pass

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    keywords = {
        'temp',
        'humidity',
        'pressure'
    }

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, bat: List[Any]) -> str:
        output = ''
        filtered = self.filter_data(bat, '')
        sum_temp = 0
        total_temp = 0

        output += 'Initializing Sensor Stream...\n'
        output += f'Stream ID: {self.stream_id}, Type: Environmental Data\n'
        output += f'Processing sensor batch: {print_dicts(bat)}\n'

        for item in bat:
            if 'temp' in item.keys():
                sum_temp += item['temp']
                total_temp += 1

        avg_temp = sum_temp / total_temp

        output += f'Sensor analysis: {len(filtered)} readings processed'
        output += f', avg temp: {avg_temp}°C'

        return output

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        filtered = []

        for item in bat:
            if isinstance(item, Dict) and self.keywords & item.keys():
                if not crit:
                    filtered.append(item)
                elif crit in item:
                    filtered.append(item)

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, bat: List[Any]) -> str:
        output = ''
        filtered = self.filter_data(bat, '')
        buy_total = 0
        sell_total = 0

        output += 'Initializing Transaction Stream...\n'
        output += f'Stream ID: {self.stream_id}, Type: Financial Data\n'
        output += f'Processing transaction batch: {print_dicts(bat)}\n'

        for item in bat:
            if item['type'] == 'buy':
                buy_total += item['amount']
            else:
                sell_total += item['amount']

        net_flow = buy_total - sell_total

        output += f'Transaction analysis: {len(filtered)} operations'
        output += f', net flow: +{net_flow} units'

        return output

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        filtered = []

        for item in bat:
            if isinstance(item, Dict) and 'type' in item.keys():
                if item['type'] == 'buy' or item['type'] == 'sell':
                    filtered.append(item)

        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, bat: List[Any]) -> str:
        output = ''
        filtered = self.filter_data(bat, '')
        err_count = 0

        output += 'Initializing Event Stream...\n'
        output += f'Stream ID: {self.stream_id}, Type: System Events\n'
        output += f'Processing event batch: {bat}\n'

        for item in bat:
            if item == 'error':
                err_count += 1

        output += f'Event analysis: {len(filtered)} events, '
        output += f'{err_count} error{"s" if err_count > 1 else ""} detected'

        return output

    def filter_data(self, bat: List[Any], crit: Opt[str] = None) -> List[Any]:
        filtered = []

        for item in bat:
            if isinstance(item, str):
                filtered.append(item)

        return filtered

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
    print('=== CODE NEXUS - POLIMORPHIC STREAM SYSTEM ===\n')

    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()

    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    sensor_batch = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ]

    trans_batch = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75},
        {"type": "buy", "amount": 50}
    ]

    event_batch = [
        "login",
        "error",
        "logout"
    ]


    streams = [sensor, trans, event]
    batches = [sensor_batch, trans_batch, event_batch]

    results = processor.process_all(batches)

    for result in results:
        print(result)
        print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    print("Batch 1 Results:")

    for s, b in zip(streams, batches):
        filtered = s.filter_data(b)

        if isinstance(s, SensorStream):
            print(f"- Sensor data: {len(filtered)} readings processed")
        elif isinstance(s, TransactionStream):
            print(f"- Transaction data: {len(filtered)} operations processed")
        elif isinstance(s, EventStream):
            print(f"- Event data: {len(filtered)} events processed")
    print()
    print("Stream filtering active: High-priority data only")

    critical_sensor = sensor.filter_data(sensor_batch, "temp")
    large_trans = [
        t for t in trans_batch
        if t["type"] == "buy" and t["amount"] > 100
    ]

    print(
        f"Filtered results: "
        f"{len(critical_sensor)} critical sensor alerts, "
        f"{len(large_trans)} large transaction"
    )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == '__main__':
    main()

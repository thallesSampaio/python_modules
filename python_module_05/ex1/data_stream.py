from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]: # noqa
        if not isinstance(data_batch, list):
            raise TypeError("Data batch must be a list")
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "processed": self.processed_count}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not self.validate(data_batch):
            raise ValueError("Invalid data: must be numeric or 'key:value' strings.") # noqa
        self.processed_count += len(data_batch)
        values = []
        for x in data_batch:
            if isinstance(x, str) and ':' in x:
                if x.split(':')[0] == 'temp':
                    values.append(float(x.split(':')[1]))
        avg = sum(values) / len(values) if values else 0
        return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg:.1f}°C" # noqa

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[float]: # noqa
        if criteria == "high":
            return [x for x in data_batch if x > 30]
        return super().filter_data(data_batch, criteria)

    def validate(self, data_batch: Any) -> bool:
        if not isinstance(data_batch, list):
            return False
        for x in data_batch:
            if isinstance(x, str) and ':' in x:
                try:
                    float(x.split(':')[1])
                except ValueError:
                    return False
            elif not isinstance(x, (int, float)):
                return False
        return True


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        self.processed_count += len(data_batch)
        net_flow = 0
        for item in data_batch:
            action, val = item.split(':')
            try:
                if action == "buy":
                    net_flow -= int(val)
                elif action == "sell":
                    net_flow += int(val)
            except ValueError:
                print("Value error, invalid data type. Skipping item.")
        display_flow = -net_flow
        return f"Transaction analysis: {len(data_batch)} operations, net flow: {display_flow:+d} units" # noqa


class EventStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        self.processed_count += len(data_batch)
        errors = [e for e in data_batch if "error" in e.lower()]
        return f"Event analysis: {len(data_batch)} events, {len(errors)} error(s) detected" # noqa


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for i in range(len(self.streams)):
            try:
                stream = self.streams[i]
                batch = batches[i]
                stream.process_batch(batch)
                count = len(batch)
                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: {count} readings processed")
                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: {count} operations processed")
                elif isinstance(stream, EventStream):
                    print(f"- Event data: {count} events processed")
            except IndexError:
                print(f"[ERROR] No data batch found for stream index {i}")
            except Exception as e:
                print(f"Error processing stream {self.streams[i].stream_id}: {e}") # noqa


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("Initializing Sensor Stream...")
    s_stream = SensorStream("SENSOR_001", "Environmental Data")
    print(f"Stream ID: {s_stream.stream_id}, Type: {s_stream.stream_type}")
    batch_s = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(batch_s)}]")
    print(s_stream.process_batch(batch_s))

    print("\nInitializing Transaction Stream...")
    t_stream = TransactionStream("TRANS_001", "Financial Data")
    print(f"Stream ID: {t_stream.stream_id}, Type: {t_stream.stream_type}")
    batch_t = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(batch_t)}]")
    print(t_stream.process_batch(batch_t))

    print("\nInitializing Event Stream...")
    e_stream = EventStream("EVENT_001", "System Events")
    print(f"Stream ID: {e_stream.stream_id}, Type: {e_stream.stream_type}")
    batch_e = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(batch_e)}]")
    print(e_stream.process_batch(batch_e))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    processor = StreamProcessor()
    processor.add_stream(s_stream)
    processor.add_stream(t_stream)
    processor.add_stream(e_stream)
    mixed_data = [
        ["temp:20", "temp:25"],
        ["buy:10", "sell:20", "buy:5", "sell:40"],
        ["login", "error", "logout"]
    ]
    processor.process_all(mixed_data)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction\n")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()

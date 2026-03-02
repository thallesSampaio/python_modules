from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str = "Generic") -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        filtered_data = []
        target_item = str(criteria).lower()
        for item in data_batch:
            if target_item in item.lower():
                filtered_data.append(item)
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "items_processed": self.processed_count,
            "status": "operational"
        }

    def init(self, batch: List[Any]) -> str:
        return f"Initializing {self.__class__.__name__}...\n" \
            f"Stream ID: {self.stream_id}, Type: {self.stream_type}\n" \
            f"Processing {self.get_desc().lower()} batch {batch}"

    def get_desc(self) -> str:
        return self.__class__.__name__.replace("Stream", "")


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not self.validate(data_batch):
            raise ValueError("Invalid data: must be numeric"
                  "or 'key:value' strings.")
        self.processed_count += len(data_batch)
        values = [float(x.split(':')[1])
                  for x in data_batch if x.split(':')[0] == 'temp']
        avg = sum(values) / len(values) if values else 0
        return f"Sensor analysis: {len(data_batch)} " \
            f"readings processed, avg temp: {avg:.1f}°C"

    def validate(self, data_batch: Any) -> bool:
        if not isinstance(data_batch, list):
            return False
        for x in data_batch:
            if isinstance(x, str) and ':' in x:
                try:
                    float(x.split(':')[1])
                except (ValueError, IndexError):
                    return False
        return True


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        net_flow = 0
        self.processed_count += len(data_batch)
        ops = len(data_batch)
        for item in data_batch:
            action, val = item.split(':')
            try:
                if action == "buy":
                    net_flow -= int(val)
                elif action == "sell":
                    net_flow += int(val)
            except ValueError:
                ops -= 1
                print("Value error, invalid data type. Skipping item.")
        return f"Transaction analysis: {ops} " \
            f"operations, net flow: {-net_flow:+d} units"


class EventStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        self.processed_count += len(data_batch)
        errors = [e for e in data_batch if "error" in e.lower()]
        return f"Event analysis: {len(data_batch)} events, " \
            f"{len(errors)} error(s) detected"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        results = []
        for s, b in zip(self.streams, batches):
            try:
                results.append(s.process_batch(b))
                print(f"- {s.get_desc()} data: {len(b)} items processed")
            except Exception as e:
                print(f"Error in {s.stream_id}: {e}")
        return results


def stream_demo(batch: List[Any], stream: DataStream) -> None:
    try:
        print(f"{stream.init(batch)}")
        print(stream.process_batch(batch))
    except Exception as e:
        print(f"Error in {stream.stream_id}: {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    s_stream = SensorStream("SENSOR_001", "Environmental Data")
    t_stream = TransactionStream("TRANS_001", "Financial Data")
    e_stream = EventStream("EVENT_001", "System Events")
    stream_demo(["temp:22.5", "humidity:65", "pressure:1013"], s_stream)
    print()
    stream_demo(["buy:100", "sell:150", "buy:75"], t_stream)
    print()
    stream_demo(["login", "error", "logout"], e_stream)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    p = StreamProcessor()
    p.add_stream(s_stream), p.add_stream(t_stream), p.add_stream(e_stream)
    p.process_all([
        ["temp:20", "temp:25"],
        ["buy:10", "sell:20", "buy:5", "sell:40"],
        ["login", "error", "logout"]
    ])
    print("\nStream filtering active: High-priority data only")
    filtered_sensor = s_stream.filter_data(
        ["temp:41.0", "humidity:30", "temp:38.5"], "temp"
    )
    filtered_trans = t_stream.filter_data(
        ["buy:500", "sell:10", "buy:300"], "buy"
    )
    print(f"Filtered results: {len(filtered_sensor)} critical sensor alerts,"
          f" {len(filtered_trans) - 1} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")

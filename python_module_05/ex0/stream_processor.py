from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data.__class__ != list:
            return False
        for x in data:
            if x.__class__ not in (int, float):
                return False
        return True

    def process(self, data: List[int]) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data: must be a list of numeric values.")
        avg = sum(data) / len(data) if data else 0
        return f"Processed: {len(data)}" \
            f" numeric values, sum={sum(data)} avg={avg:.1f}"

    def msg(self) -> None:
        print("Validation: Numeric data verified")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data.__class__ != str:
            return False
        return True

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data: must be a string.")
        return f"Processed text: {len(data)}" \
            f" characters, {len(data.split())} words"

    def msg(self) -> None:
        print("Validation: Text data verified")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data.__class__ != str:
            return False
        if ":" not in data:
            return False
        return True

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data: must be a log string.")
        level, message = data.split(":", 1)
        return f"[{level}] level detected:{message}"

    def msg(self) -> None:
        print("Validation: Log entry data verified")

    def format_output(self, result: str) -> str:
        modified_result = f"{result}"
        return super().format_output(modified_result)


def processor_demo(data: Any, proc: DataProcessor):
    try:
        print(f"\nInitializing {proc.__class__.__name__}...")
        if data.__class__ == str:
            print(f'Processing data: "{data}"')
        else:
            print(f"Processing data: {data}")
        if proc.validate(data):
            proc.msg()
        print(proc.format_output(proc.process(data)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    processor_demo([1, 2, 3, 4, 5], NumericProcessor())
    processor_demo("Hello Nexus World", TextProcessor())
    processor_demo("ERROR: Connection timeout", LogProcessor())

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    ty = [(NumericProcessor(), [1, 2, 3]),
          (TextProcessor(), "hello world!"),
          (LogProcessor(), "INFO: System ready")]
    c = 1
    for t, d in ty:
        print(f"Result {c}: {t.process(d)}")
        c += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")

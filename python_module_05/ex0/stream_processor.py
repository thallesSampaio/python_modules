from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class for processing data."""
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return a result string."""
        print(f"It works! {data}")

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the input data."""
        pass

    def format_output(self, result: str) -> str:
        """Default implementation, that cant be override."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: List[int, float]) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data: must be a list of numeric values.")
        return f"Processed: {len(data)} numeric values, sum={sum(data)} avg={(sum(data) / len(data)):.1f}" # noqa

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for x in data:
            if not isinstance(x, (int, float)):
                return False
        return True


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data: must be a string.")
        return f"Processed text: {len(data)} characters, {len(data.split())} words" # noqa


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and (":" in data)

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data: must be a log string with format 'LEVEL: message'.") # noqa

        level, message = data.split(":", 1)
        return f"{level.strip()} level detected:{message}"

    def format_output(self, result: str) -> str:
        return f"Output: [ALERT] {result}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc = NumericProcessor()
    try:
        if num_proc.validate(num_data):
            print("Validation: Numeric data verified")
        print(num_proc.format_output(num_proc.process(num_data)))
    except ValueError as e:
        print(e)

    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    text_proc = TextProcessor()
    try:
        if text_proc.validate(text_data):
            print("Validation: Text data verified")
        print(text_proc.format_output(text_proc.process(text_data)))
    except ValueError as e:
        print(e)

    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    log_proc = LogProcessor()
    try:
        if log_proc.validate(log_data):
            print("Validation: Log entry verified")
        print(log_proc.format_output(log_proc.process(log_data)))
    except ValueError as e:
        print(e)

    print("\n=== Polymorphic Processing Demo ===")


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        return f"Processed{result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        ret_next = f"sum={sum(data)}, avg={sum(data) / len(data)}"
        return f" {len(data)} numeric values, {ret_next}"

    def validate(self, data: Any) -> bool:
        try:
            if data:
                for i in data:
                    int(i)
                return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        i = 0
        word = 0
        while i < len(data):
            if data[0] != ' ' and i == 0:
                word += 1
            elif data[i - 1] == ' ' and data[i] != ' ':
                word += 1
            i += 1
        return f" text: {len(data)} characters, {word} words"

    def validate(self, data: Any) -> bool:
        try:
            if data:
                str(data)
                return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        parts = data.split(":", 1)
        level = parts[0]
        message = parts[1].strip()

        tag = "[ALERT]" if level == "ERROR" else "[INFO]"
        return f"{tag} {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        try:
            if data:
                if not isinstance(data, str) or ":" not in data:
                    return False
                valid_levels = ["ERROR", "INFO", "CORRECT", "DEBUG"]
                prefix = data.split(":", 1)[0]
                return prefix in valid_levels
        except TypeError or ValueError:
            return False

    def format_output(self, result: str) -> str:
        return f"{result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    data = [0, 1, 2, 3, 4, 5]
    data_int = NumericProcessor()
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    if data_int.validate(data):
        print("Validation: Numeric data verified")
        result = data_int.process(data)
        print("Output:", data_int.format_output(result))
    else:
        print("False: Numeric data verified and it's not int")

    data = "Hello Nexus World"
    data_str = TextProcessor()
    print("\nInitializing Text Processor...")
    print(f"Processing data: {data}")
    if data_str.validate(data):
        print("Validation: Text data verified")
        result = data_str.process(data)
        print("Output:", data_str.format_output(result))
    else:
        print("False: Charactere data verified and it's not str")

    data = "ERROR: Connection timeout"
    data_log = LogProcessor()
    print("\nInitializing Log Processor...")
    print(f"Processing data: {data}")
    if data_log.validate(data):
        print("Validation: Log entry verified")
        result = data_log.process(data)
        print("Output:", data_log.format_output(result))
    else:
        print("False: Logs data verified and it's not logs")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    values = [[0, 1, 2], "Hello Wordene", "INFO: System ready"]
    output = [NumericProcessor(), TextProcessor(), LogProcessor()]
    i = 0
    for answer in output:
        rest = answer.process(values[i])
        print(f"Result {i+1} : {answer.format_output(rest)}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")

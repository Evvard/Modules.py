from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: any) -> str:
        pass

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: str) -> str:
        ret_next = f"sum={sum(data)}, avg={sum(data) / len(data)}"
        return f" Processed {len(data)} numeric values, {ret_next}"

    def validate(self, data):
        try:
            sum(data)
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        i = 0
        word = 0
        while i < len(data):
            if data[0] != ' ' and i == 0:
                word += 1
            elif data[i - 1] == ' ' and data[i] != ' ':
                word += 1
            i += 1
        return f"Processed text: {len(data)} characters, {word} words"

    def validate(self, data):
        try:
            str(data)
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:

        return f"Output: [ALERT] ERROR level detected: Connection timeout"                              wwwww

    def validate(self, data):
        try:
            str(data)
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)



if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    data = [1, 2, 3, 4, 5]
    data_int = NumericProcessor()
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    if data_int.validate(data):
        print("Validation: Numeric data verified")
        result = data_int.process(data)
        print(data_int.format_output(result))
    else:
        print("False: Numeric data verified and it's not int")

    data = "Hello Nexus World"
    data_str = TextProcessor()
    print("\nInitializing Text Processor...")
    print(f"Processing data: {data}")
    if data_str.validate(data):
        print("Validation: Text data verified")
        result = data_str.process(data)
        print(data_str.format_output(result))
    else:
        print("False: Charactere data verified and it's not str")

    data = "ERROR: Connection timeout"
    data_log = LogProcessor()
    print("Initializing Log Processor...")
    print(f"Processing data: {data}")
    if data_log.validate(data):
        print("Validation: Log entry verified")
        result = data_log.process(data)
        print(data_log.format_output(result))
    else:
        print("False: Logs data verified and it's not logs")


    print("=== Polymorphic Processing Demo ===")
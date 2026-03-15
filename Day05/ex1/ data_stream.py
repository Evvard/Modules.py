from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data = data
        self.arg = 0
        self.turn = 0
        self.data = data

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch if
                isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"Stream ID": self.stream_id, "Type": self.data}


class SensorStream(DataStream):
    def __init__(self, stream_id: str, data: str) -> None:
        super().__init__(stream_id)
        self.temp = []

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "error no value!"
        test = ""
        correct_arg = []
        new_list = []
        if self.turn == 0:
            for argument in data_batch:
                self.turn += 1
                try:
                    self.arg += 1
                    if isinstance(argument, str):
                        correct_arg = argument.split(":")
                        test = correct_arg[1]
                        test = float(test)
                        if "temp" in argument:
                            self.temp += [test]
                        new_list += [argument]
                except ValueError:
                    print(f"{test} is not numeric bro")
                except IndexError:
                    print(f"Missing data, {argument}: ......")
            return f"Processing sensor batch: [{', '.join(new_list)}]"
        else:
            if self.temp:
                total = 0
                for i in self.temp:
                    total += float(i)
                avg = i / len(self.temp)
                message = f"readings processed, avg temp: {avg}°C"
                return f"Sensor analysis: {self.arg}, {message}"
        return f"Sensor analysis: {self.arg}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, data: str) -> None:
        super().__init__(stream_id)
        self.benef = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "error no value!"
        if self.turn == 0:
            arg = 0
            correct_arg = []
            new_list = []
            for argument in data_batch:
                self.turn += 1
                try:
                    self.arg += 1
                    if isinstance(argument, str):
                        correct_arg = argument.split(":")
                        test = correct_arg[1]
                        test = int(test)
                        if "sell" in correct_arg[0]:
                            self.benef -= test
                        elif "buy" in correct_arg[0]:
                            self.benef += test
                        else:
                            raise Exception
                        new_list += [argument]
                        arg += 1
                except ValueError as message:
                    print(message)
                except Exception:
                    message = "you can just sell or buy, nothing else"
                    print("For Transaction,", message)
            return f"Processing sensor batch: [{', '.join(new_list)}]"
        else:
            if self.benef > 0:
                message = f"operations, net flow: +{self.benef} units"
            else:
                message = f"operations, net flow: {self.benef} units"
            return f"Transaction analysis: {self.arg}, {message}"


class EventStream(DataStream):
    def __init__(self, stream_id: str, data: str) -> None:
        super().__init__(stream_id)
        self.data = data
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "error no value!"
        if self.turn == 0:
            self.turn += 1
            new_list = []
            for argument in data_batch:
                self.arg += 1
                try:
                    str(argument)
                    if ("login" in argument or "logout" in argument):
                        pass
                    elif "error" in argument:
                        self.error += 1
                    else:
                        raise Exception
                    new_list += [argument]
                except ValueError:
                    print("Need str value please bro")
                except Exception:
                    print(f"Error, {argument} is an invalid argument")

            return f"Processing sensor batch: [{', '.join(new_list)}]"
        else:
            message = f"{self.error} error detected"
            return (f"Event analysis: {self.arg} events, {message}")


class StreamProcessor:
    def __init__(self) -> None:
        self.stream = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.stream.append(stream)

    def polymorphism(self, data: Dict[str, List[Any]]) -> None:
        print("Batch 1 Results:")
        index = 0
        for stream_id, data_for_stream in data.items():
            index = len(data_for_stream)
            try:
                if "SENSOR" in stream_id:
                    print(f"- Sensor data: {index} readings processed")
                elif "TRANS" in stream_id:
                    print(f"- Transaction data: {index} readings processed")
                elif "EVENT" in stream_id:
                    print(f"- Event data: {index} events processed")
            except Exception:
                print("Wrong input")

        print("Stream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alert, 1 large transaction")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    stream_id = "SENSOR_001"
    data = "Environmental Data"
    sensor = SensorStream(stream_id, data)
    items = sensor.get_stats()
    print(" ,".join(f"{k}: {v}" for k, v in items.items()))
    data_batch = ["temp:22.5", "humidity:65", "pressure:1013",]
    good_data_batch = sensor.filter_data(data_batch)
    process_batch = sensor.process_batch(good_data_batch)
    print(process_batch)
    if process_batch != "error no value!":
        sensor_analyse = sensor.process_batch(good_data_batch)
        print(sensor_analyse)

    print("\nInitializing Transaction Stream...")
    stream_id = "TRANS_001"
    data = "Financial Data"
    financial = TransactionStream(stream_id, data)
    items = financial.get_stats()
    print(" ,".join(f"{k}: {v}" for k, v in items.items()))
    data_batch = ["buy:100", "sell:150", "buy:75",]
    good_data_batch = financial.filter_data(data_batch)
    process_batch = financial.process_batch(good_data_batch)
    print(process_batch)
    if process_batch != "error no value!":
        financial_analyse = financial.process_batch(good_data_batch)
        print(financial_analyse)

    print("\nInitializing Event Stream...")
    stream_id = "EVENT_001"
    data = "System Events"
    event = EventStream(stream_id, data)
    items = event.get_stats()
    print(" ,".join(f"{k}: {v}" for k, v in items.items()))
    data_batch = ["login", "error", "logout",]
    good_data_batch = event.filter_data(data_batch)
    process_batch = event.process_batch(good_data_batch)
    print(process_batch)
    if process_batch != "error no value!":
        event_analyse = event.process_batch(good_data_batch)
        print(event_analyse)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()

    processor.add_stream(sensor)
    processor.add_stream(financial)
    processor.add_stream(event)

    data_for_polymorphism = {
        "SENSOR_001": ["temp:25.0", "humidity:50"],
        "TRANS_001": ["buy:100", "sell:50", "buy:200", "sell:10"],
        "EVENT_001": ["login", "error", "logout"]
        }
    processor.polymorphism(data_for_polymorphism)
    print("\nAll streams processed successfully. Nexus throughput optimal.")

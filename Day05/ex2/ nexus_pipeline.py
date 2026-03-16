from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        print("Input validation and parsing")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("Data transformation and enrichment")
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        print("Output formatting and delivery\n")
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        current_data = data
        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            return current_data
        except Exception as e:
            return f"Erreur: {e}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        current_data = data
        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            return current_data
        except Exception as e:
            return f"Erreur: {e}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        current_data = data
        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            return current_data
        except Exception as e:
            return f"Erreur: {e}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: Dict[str, ProcessingPipeline] = {}

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines[pipeline.pipeline_id] = pipeline

    def run_all(self, data: Any) -> Dict[str, Any]:
        results = {}
        for pipeline_id, pipeline in self.pipelines.items():
            results[pipeline_id] = pipeline.process(data)
        return results


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager..\n")

    input_st = InputStage()
    tranform_st = TransformStage()
    output_st = OutputStage()

    json_pipe = JSONAdapter("JSON")
    csv_pipe = CSVAdapter("CSV")
    stream_pipe = StreamAdapter("STREAM")

    json_pipe.add_stage(input_st)
    json_pipe.add_stage(tranform_st)
    json_pipe.add_stage(output_st)

    csv_pipe.add_stage(input_st)
    csv_pipe.add_stage(tranform_st)
    csv_pipe.add_stage(output_st)

    stream_pipe.add_stage(tranform_st)
    stream_pipe.add_stage(tranform_st)
    stream_pipe.add_stage(output_st)

    manager = NexusManager()
    manager.register_pipeline(json_pipe)
    manager.register_pipeline(csv_pipe)
    manager.register_pipeline(stream_pipe)

    raw_data = "Mes données secrètes"

    manager.run_all(raw_data)

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()

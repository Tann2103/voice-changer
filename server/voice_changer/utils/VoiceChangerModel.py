from typing import Any, Callable, Protocol, TypeAlias
import numpy as np


AudioInOut: TypeAlias = np.ndarray[Any, np.dtype[np.int16]]


class VoiceChangerModel(Protocol):
    loadModel: Callable[..., dict[str, Any]]
    def get_processing_sampling_rate(self) -> int: ...
    def get_info(self) -> dict[str, Any]: ...
    def inference(self, data: tuple[Any, ...]) -> Any: ...
    def generate_input(self, newData: AudioInOut, inputSize: int, crossfadeSize: int) -> tuple[Any, ...]: ...
    def update_settings(self, key: str, val: Any) -> bool: ...

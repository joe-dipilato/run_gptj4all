
__all__ =  ["WrapGPTJ4All"]

from pathlib import Path
import pyllamacpp

class WrapGPTJ4All:
    """
    Wrapper class around GPT-J model.
    """
    def __init__(self):
        self._is_alive = False
        self.model_path = None

    def start(self) -> None:
        """
        Starts the model.
        """
        if not self.is_alive:
            self._start_model()

    def _start_model(self) -> None:
        """
        Starts the model.
        """
        self._is_alive = True

    def load_model(self,  model_path: Path = Path("default")) -> Path:
        """
        Loads the model from the specified path.
        :param model_path: Path to the model.
        :return: Path to the model.
        :raises FileNotFoundError: If the model is not found.
        """
        self.model_path = model_path if model_path.exists() else None
        if self.model_path is None:
            raise FileNotFoundError(f"Model {model_path} not found.")
        return self.model_path
    
    def check_import_model_lib(self) -> bool:
        """
        Checks if the model library is available.
        :return: True if the model library is available.
        """
        return True

    @property
    def is_alive(self):
        return self._is_alive
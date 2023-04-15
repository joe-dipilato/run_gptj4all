
__all__ =  ["WrapGPTJ4All"]

class WrapGPTJ4All:
    """
    Wrapper class around GPT-J model.
    """
    def __init__(self):
        print("Loading GPT-J model...")
        self._is_alive = False

    def start(self):
        print("Starting GPT-J model...")
        self._is_alive = True

    @property
    def is_alive(self):
        return self._is_alive
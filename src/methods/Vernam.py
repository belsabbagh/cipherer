from .__base import EncMethod


class Vernam(EncMethod):
    def __init__(self, key: str) -> None:
        super().__init__()
        raise NotImplementedError("Vernam cipher is not implemented yet.")

    def encrypt(self, data: str) -> str:
        pass

    def decrypt(self, data: str) -> str:
        pass

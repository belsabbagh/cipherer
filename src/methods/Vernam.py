from .__base import EncMethod


class Vernam(EncMethod):
    def __init__(self) -> None:
        super().__init__()

    def encrypt(self, data: str) -> str:
        pass

    def decrypt(self, data: str) -> str:
        pass

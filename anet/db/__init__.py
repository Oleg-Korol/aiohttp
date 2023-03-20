from tortoise import fields, models
from typing import  TypeAlias
from anet.utils.crypto import Enigma


Model:TypeAlias = models.Model

class TextCryptoField(fields.TextField):
    def to_db_value(self,value:str,instance: Model)->str:
        value =super().to_db_value(value,instance)
        return Enigma.encrypt(value)

    def to_python_value(self, value: str) -> str:
        try:
            value = Enigma.decrypt(value)
        except ValueError:
            ...
        return super().to_python_value(value)
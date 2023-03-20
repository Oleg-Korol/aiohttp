import asyncio
import os

from tortoise import models, fields
from enum import IntEnum
from hashlib import sha3_224
from tortoise.signals import pre_save
from anet.db import TextCryptoField

class UserStatus(IntEnum):
    ADMIN = 5
    STAFF = 4
    SIMPLE = 3

    def __str__(self):
        return self.name


class User(models.Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=120, unique=True)
    password = TextCryptoField(validators=[])
    email = TextCryptoField(validators=[])
    is_active = fields.BooleanField(default=False)
    created = fields.DatetimeField(auto_now_add=True)
    status = fields.IntEnumField(UserStatus, default=UserStatus.SIMPLE)
    refresh = fields.TextField(validators=[], null=True)

    def __str__(self):
        return self.username

    class Meta:
        table = "users"
        ordering = ("-created",)

    def make_passwd(self):
        hashed_passwd = sha3_224(self.password.encode("utf-8")).hexdigest()
        salt = sha3_224(os.urandom(24).hex().encode("utf-8")).hexdigest()
        mix = "".join([a + b for a, b in zip(salt, hashed_passwd)])
        mixed_hash = sha3_224(mix.encode("utf-8")).hexdigest()
        self.password = "".join([a + b for a, b in zip(salt, mixed_hash)])

    async def check_password(self, password):
        salt = self.password[::2]
        passwd = self.password[1::2]
        hashed_passwd = sha3_224(passwd.encode("utf-8")).hexdigest()
        mix = "".join([a + b for a, b in zip(salt, hashed_passwd)])
        mixed_hash = sha3_224(mix.encode("utf-8")).hexdigest()
        if passwd == mixed_hash:
            return True

        await asyncio.sleep(3)
        return False


@pre_save(User)
async def hash_password(sender, instance, using_db, update_fields):
    if instance.id is None or "password" in update_fields:
        instance.make_passwd()

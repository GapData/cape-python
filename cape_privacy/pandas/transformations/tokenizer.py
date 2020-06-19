import hashlib
import secrets

from cape_privacy.pandas.transformations import base
from cape_privacy.pandas.transformations import dtypes


class Tokenizer(base.Transformation):
    def __init__(self, max_token_len: int = None, key: str = None):
        super().__init__(dtype=dtypes.String)
        self._max_token_len = max_token_len
        if isinstance(key, str):
            key = key.encode()
        self._key = key or secrets.token_bytes(8)

    def __call__(self, series):
        return series.apply(lambda x: self.to_token(x))

    def to_token(self, x):
        token = hashlib.sha256(x.encode() + self.key).hexdigest()
        if self._max_token_len is not None:
            return token[: self._max_token_len]
        else:
            return token

    @property
    def key(self):
        return self._key
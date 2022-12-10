import json

import msgpack
from httpie.plugins import ConverterPlugin

DEFAULT_INDENT = 4


class MsgpackPlugin(ConverterPlugin):
    @classmethod
    def supports(cls, mime):
        return 'msgpack' in mime

    def convert(self, body):
        loaded = msgpack.loads(body, raw=False)
        return "application/json", \
               json.dumps(loaded, sort_keys=True)

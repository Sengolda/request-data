from typing import Literal
from dataclasses import dataclass

@dataclass
class Request:
    url: str
    method: Literal["GET", "POST", "PUT", "DELETE"]
    headers = dict()
    params  = dict()
    data = dict()
    json  = dict()

    def to_dict(self):
        returning_dict = {a: getattr(self, a) for a in (
            'method', 'headers', 'params', 'data', 'json',)}
        returning_dict['url'] = self.url
        return returning_dict

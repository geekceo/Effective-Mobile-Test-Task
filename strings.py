import json
from typing import Any

class Strings(object):        

    def __getattribute__(self, name: str) -> Any:

        def __get_attr(name) -> Any:

            data: dict = json.loads(open('strings.json', 'r', encoding='utf-8').read())

            try:

                return data[name]

            except:

                raise AttributeError(f'Attribute {name} not found')

        attr: Any = __get_attr(name=name)

        return attr

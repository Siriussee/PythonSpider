json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

import json
parsed_json = json.loads(json_string)

print parsed_json

print(parsed_json['first_name'])
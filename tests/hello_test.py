import unittest
import json
from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename
from openapi_schema_validator import validate as validate_schema

from src.function.hello.handler import hello

class TestStringMethods(unittest.TestCase):

    def test_spec(self):
        spec_dict, base_uri = read_from_filename('doc/build/openapi.yaml')

        # If no exception is raised by validate(), the whole spec is valid.
        validate(spec_dict)

        hello_response_schema = spec_dict['components']['schemas']['HelloResponse']

        hello_response = hello({},{})
        hello_response_body = json.loads(hello_response['body'])

        # If no exception is raised by validate_schema(), the response is valid against the spec
        validate_schema(hello_response_body, hello_response_schema)

if __name__ == '__main__':
    unittest.main()

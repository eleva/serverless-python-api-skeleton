import unittest
import json
from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename
from openapi_schema_validator import validate as validate_schema
from src.function.hello.handler import hello

class TestStringMethods(unittest.TestCase):

    def test_hello_response_against_spec(self):

        # Get spec from file name
        spec_dict, base_uri = read_from_filename('doc/build/openapi.yaml')

        # If no exception is raised by validate(), the whole spec is valid as OpenApi.
        validate(spec_dict)

        # Get specific schema for this response
        hello_response_schema = spec_dict['components']['schemas']['HelloResponse']

        # Call your function
        hello_response = hello({},{})

        # Get the response body
        hello_response_body = json.loads(hello_response['body'])

        # If no exception is raised by validate_schema(), the response is valid against the spec
        validate_schema(hello_response_body, hello_response_schema)

if __name__ == '__main__':
    unittest.main()

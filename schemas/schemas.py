from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_schema(data: dict or list, schema: dict or list) \
  -> tuple[bool, str | None]:
    try:
        validate(data, schema)
    except ValidationError as e:
        return False, e.message
    return True, None


post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}
from pytest import mark
from jsonschema import validate
from schemas.schemas import (post_schema)

@mark.testomatio("@T2bef84a0")
@mark.smoke
def test_post_schema(session):
    response = session.get('/posts')
    assert response.ok
    assert response.json()
   
    for post in response.json():
        validate(post, post_schema)
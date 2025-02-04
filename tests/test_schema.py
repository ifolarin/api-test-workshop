from pytest import mark
from schemas.schemas import (validate_schema, post_schema)


#@mark.smoke
#def test_post_schema(session):
#    response = session.get('/posts')
#    for post in response.json():
#        result = validate_schema(post, post_schema)
#        print(f'{result[1]}')
#        assert result[0], f'post id = {[post["id"]]} ' + result[1]


@mark.testomatio("@T2bef84a0")
@mark.smoke
def test_post_schema(session):
    response = session.get('/posts')
    assert response.ok
    assert response.json()
   
    for post in response.json():
        result = validate_schema(post, post_schema)
        assert result[0], f'post id = {[post["id"]]} ' + result[1]
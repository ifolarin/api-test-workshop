from pytest import mark

@mark.testomatio("@T459fc7f7")
def test_create_post(session):
    response = session.post('/posts', json={"title": "foo", "body": "bar", "userId": 1})
    assert response.ok
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == 'bar'
    assert response.json()['userId'] == 1


@mark.testomatio("@Tf4d5dc2b")
def test_delete_post(session):
    response = session.delete('/posts/1')
    assert response.ok
    assert response.json() == {}


# TODO complete the tests for remaining endpoints
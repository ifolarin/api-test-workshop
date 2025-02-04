from pytest import mark


@mark.testomatio("@Tcc057fa9")
@mark.smoke
def test_posts(session):
    response = session.get('/posts/1')
    payload = response.json()
    assert payload['id'] == 1
    assert payload['title'] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert "expedita et cum\nreprehenderit molestiae ut ut quas"


@mark.testomatio("@Td45bf52d")
@mark.smoke
def test_header(session):
    response = session.get('/albums')
    assert response.headers.get('X-Powered-By') == "Express"


@mark.testomatio("@T5d6f8a4e")
def test_timing_post(session):
    response = session.get('/posts')
    assert response.elapsed.total_seconds() * 1000 < 300

# TODO complete the tests for remaining endpoints
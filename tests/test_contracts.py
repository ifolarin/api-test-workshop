from pytest import mark


@mark.testomatio("@Tcc057fa9")
@mark.smoke
def test_posts(session):
    response = session.get('/posts')
    assert response.ok

@mark.testomatio("@T56227395")
@mark.smoke
def test_post_25(session):
    response = session.get('/posts/25')
    assert response.ok


@mark.testomatio("@Ta3213e38")
@mark.smoke
def test_albums(session):
    response = session.get('/albums')
    assert response.ok

# TODO complete the tests for remaining endpoints
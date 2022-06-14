from app import app


def test_health_check_ok():
    result = app.health_check()
    assert result == 'OK'


# def test_health_check():
#     result = app.health_check_dummy('foo')
#     assert result == 'bar'



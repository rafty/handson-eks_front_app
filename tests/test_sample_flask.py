from samples.sample_flask import app

app.config['TESTING'] = True
client = app.test_client()


def test_flask_simple():
    result = client.get('/')

    assert b'root' == result.data


def test_flask_simple_2():
    result = client.get('//')

    assert {} == result.data

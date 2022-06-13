from app.app import app

app.config['TESTING'] = True
client = app.test_client()


def test_flask_simple():
    result = client.get('/')

    # assert b'root' == result

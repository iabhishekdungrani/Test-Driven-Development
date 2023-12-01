import json


def test_ping(test_app):
    #Given
    client = test_app.test_client()
    #when
    resp = client.get('/ping')
    data = json.loads(resp.data.decode())
    #then
    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']

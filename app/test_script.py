def test_handle(client):
    response = client.post('/', data={'input_text': 'Hello World'})

    assert response.status_code == 200
    assert b'dlroW olleH' in response.data
    assert 'result.html' in response.template.name

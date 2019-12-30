def test_get_image(client, path):
    response = client.get(path)
    assert response.status_code == 200

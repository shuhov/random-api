


def test_get_ipv4(client, path):
    response = client.get(f"{path}/ipv4_address")
    assert response.status_code == 200
    assert response.json['name'] == 'ip_address'

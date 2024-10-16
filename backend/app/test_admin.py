import pytest

def test_get_feedbacks(client):
    response = client.get('/admin/feedbacks')
    assert response.status_code == 200

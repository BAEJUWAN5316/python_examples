import pytest
from django.test import Client

@pytest.mark.django_db
def test_blog_index(client):
    # client = Client()
    res = client.get("/blog/")
    assert res.status_code == 200

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_view(client):
    url = reverse("home:index")
    response = client.get(url)
    assert response.status_code == 200

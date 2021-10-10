import pytest
import requests
from pytest_docker_ci_example import is_responsive


@pytest.fixture(scope="session")
def http_service(docker_ip, docker_services):
    """Ensure that HTTP service is up and responsive."""

    # `port_for` takes a container port and returns the corresponding host port
    url = "http://localhost:8899/health"
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


def test_status_code(http_service):
    response = requests.get(http_service)

    assert response.status_code == 200

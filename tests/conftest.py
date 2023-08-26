import os
import warnings
import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from testcontainers.postgres import PostgresContainer
from app.main import app


@pytest.fixture(scope='session', autouse=True)
def init_test_db():
    print("starting container")
    with PostgresContainer(image='postgres:11.5',
                           user='test_user',
                           password='test_pass',
                           dbname='test_db').with_bind_ports(5432, 5431):
        print('apply migrations')
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        os.environ["TESTING"] = "1"
        conf = Config("alembic.ini")
        command.upgrade(conf, "head")
        yield


@pytest.fixture(scope='session', autouse=True)
def setup_dbsession():
    """
    This is needed for tests be able to connect to the database if the app did not run previously.
    If any previous tests used the AppClient or TestClient, this middleware is already initialed, and does not need this
    That is why, moving this test after, specifically after any other test that makes requests using TestClient, make it
        work
    """
    app.build_middleware_stack()


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_user_headers():
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X3VzZXIiLCJleHAiOjEzMDU0MTU3MjEzM30.MUTkPxUHEihM5QzGsJcvPDWcJFXpGSijb0KuPFB0Ruw'}
    yield headers

from . import server
import pytest
# from multiprocessing import Process
from threading import Thread


@pytest.fixture(scope='module', autouse=True)
def server_setup():
    """Server instance for testing."""
    instance = server.create_server()
    process = Thread(target=instance.serve_forever)
    process.setDaemon(True)

    process.start()

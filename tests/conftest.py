import pytest

from reto import dependency_graph


@pytest.fixture
def clear_graph():
    dependency_graph.clear()

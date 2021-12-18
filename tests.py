from main import is_full_connected
from main import connection_type
import pytest
@pytest.mark.parametrize("v, r, links", [(4,12,[(1,2),(3,4)]),(3,6,[(1,3)]),(5,20,[(1,2),(1,3)])])
def test_is_full_connected(v, r, links):
    assert is_full_connected(v, r, links) is True

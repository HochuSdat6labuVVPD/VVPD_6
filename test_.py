"""Князьков Денис Алексеевич КИ21-17/1б
Практическая работа №5, 11 вариант"""

from main import is_full_connected
from main import connection_type
import pytest


@pytest.mark.parametrize("v, r, links", [(4, 12, [(1, 2), (3, 4)]), (3, 6, [(1, 3)]), (5, 20, [(1, 2), (1, 3)])])
def test_is_full_connected(v, r, links):
    """Проверяет работу функции is_full_connected"""
    assert is_full_connected(v, r, links) is True


@pytest.mark.parametrize("v, r, links, result",
                         [(6, 5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)],1), (4, 3, [(1, 2), (2, 3), (3, 4)],1)])
def test_connection_type_1(v, r, links, result):
    """Проверяет работу функции connection_type в случае, когда сеть является шиной. Должна возвращать 1 """
    assert connection_type(v, r, links,) == result


@pytest.mark.parametrize("v, r, links",
                         [(5, 5, [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)]), (3, 3, [(1, 2), (2, 3), (3, 1)])])
def test_connection_type_2(v, r, links):
    """Проверяет работу функции connection_type в случае, когда сеть является кольцом. Должна возвращать 2"""
    assert connection_type(v, r, links) == 2


@pytest.mark.parametrize("v, r, links", [(5, 4, [(1, 2), (1, 3), (1, 4), (1, 5)]), (4, 3, [(1, 2), (1, 3), (1, 4)])])
def test_connection_type_3(v, r, links):
    """Проверяет работу функции connection_type в случае, когда сеть является звездой. Должна возвращать 3"""
    assert connection_type(v, r, links) == 3


@pytest.mark.parametrize("v, r, links",
                         [(4, 5, [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3)]), (4, 4, [(1, 2), (1, 3), (2, 3), (2, 4)]),
                          (4, 6, [(1, 2), (1, 3), (1, 4), (3, 4), (2, 3)])])
def connection_type_4(v, r, links):
    """Проверяет работу функции connection_type в случае, когда сеть не принадлежит ни к одному из типов.
    Должна возвращать -1"""
    assert connection_type(v, r, links) == -1

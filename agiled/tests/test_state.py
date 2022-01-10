"""Tests for State class"""
from common import state


def test_calculate_mouse_angle():
    assert state.calculate_mouse_angle(0, 1) == 0
    assert state.calculate_mouse_angle(-1, 0) == 90
    assert state.calculate_mouse_angle(0, -1) == 180
    assert state.calculate_mouse_angle(1, 0) == 270

"""Tests for ActorAttributes Class"""
from common.actor_attributes import ActorAttributes


def test_actor_base_attributes():
    """Test that actor attributes are stored correctly."""
    stats = ActorAttributes(5, 10, 15,4)

    assert stats.base_defense == 5, "5 defense should equal 5"
    assert stats.base_hitpoints == 10, "10 hitpoints should equal 10"
    assert stats.base_strength == 15, "15 strength should equal 15"
    assert stats.base_speed == 4, "4 speed should equal 4"


def test_incorrect_actor_base_attributes():
    """Test that actor attributes don't match any supplied data."""
    stats = ActorAttributes(5, 10, 15,4)

    assert stats.base_defense != 1, "15 defense should not equal 1"
    assert stats.base_hitpoints != 2, "10 hitpoints should not equal 2"
    assert stats.base_strength != 3, "5 strength should not equal 3"
    assert not stats.base_speed == 3, "4 speed should not equal 3"


def test_actor_set_base_attributes():
    """Test that actor attributes are modified correctly."""
    stats = ActorAttributes(0, 0, 0,0)
    stats.base_defense = 5
    stats.base_hitpoints = 10
    stats.base_strength = 15
    stats.base_speed = 4

    assert stats.base_defense == 5, "5 defense should equal 5"
    assert stats.base_hitpoints == 10, "10 hitpoints should equal 10"
    assert stats.base_strength == 15, "15 strength should equal 5"
    assert stats.base_speed == 4, "4 speed should equal 4"


def test_actor_current_attributes():
    """Test that actor attributes are stored correctly."""
    stats = ActorAttributes(5, 10, 15,4)

    assert stats.current_defense == 5, "5 defense should equal 5"
    assert stats.current_hitpoints == 10, "10 hitpoints should equal 10"
    assert stats.current_strength == 15, "15 strength should equal 15"
    assert stats.current_speed == 4, "4 speed should equal 4"


def test_incorrect_actor_current_attributes():
    """Test that actor attributes don't match any supplied data."""
    stats = ActorAttributes(5, 10, 15,4)

    assert stats.current_defense != 1, "15 defense should not equal 1"
    assert stats.current_hitpoints != 2, "10 hitpoints should not equal 2"
    assert stats.current_strength != 3, "5 strength should not equal 3"
    assert stats.current_speed != 3, "4 speed should not equal 3"



def test_actor_set_current_attributes():
    """Test that actor attributes are modified correctly."""
    stats = ActorAttributes(0, 0, 0,0)
    stats.current_defense = 5
    stats.current_hitpoints = 10
    stats.current_strength = 15
    stats.current_speed = 4

    assert stats.current_defense == 5, "5 defense should equal 5"
    assert stats.current_hitpoints == 10, "10 hitpoints should equal 10"
    assert stats.current_strength == 15, "15 strength should equal 5"
    assert stats.current_speed == 4, "4 speed should equal 4"

"""Tests for Room objects"""
from common.map_generator import DungeonGenerator
from common.room import Room
import random


def test_north_connection():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()

    r_1.connect_room(r_2, 'north')

    assert (r_1.get_room_at_direction('north') == r_2 and r_2.get_room_at_direction('south') == r_1)


def test_south_connection():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()

    r_1.connect_room(r_2, 'south')

    assert (r_1.get_room_at_direction('south') == r_2 and r_2.get_room_at_direction('north') == r_1)


def test_east_connection():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()

    r_1.connect_room(r_2, 'east')

    assert (r_1.get_room_at_direction('east') == r_2 and r_2.get_room_at_direction('west') == r_1)


def test_west_connection():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()

    r_1.connect_room(r_2, 'west')

    assert (r_1.get_room_at_direction('west') == r_2 and r_2.get_room_at_direction('east') == r_1)

def test_north_connection_error():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()
    r_3 = map_generator.random_room()

    r_1.connect_room(r_2, 'north')

    try:
        r_1.connect_room(r_3, 'north')
    except:
        assert True
    else:
        assert False

def test_south_connection_error():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()
    r_3 = map_generator.random_room()

    r_1.connect_room(r_2, 'south')

    try:
        r_1.connect_room(r_3, 'south')
    except:
        assert True
    else:
        assert False

def test_east_connection_error():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()
    r_3 = map_generator.random_room()

    r_1.connect_room(r_2, 'east')

    try:
        r_1.connect_room(r_3, 'east')
    except:
        assert True
    else:
        assert False

def test_west_connection_error():
    map_generator = DungeonGenerator()

    r_1 = map_generator.random_room()
    r_2 = map_generator.random_room()
    r_3 = map_generator.random_room()

    r_1.connect_room(r_2, 'west')

    try:
        r_1.connect_room(r_3, 'west')
    except:
        assert True
    else:
        assert False

def test_available_directions():
    map_generator = DungeonGenerator()

    for _ in range(10):
        dirs = ["north", "south", "east", "west"]
        
        room = map_generator.random_room()

        rand = random.choice(dirs)
        dirs.remove(rand)

        room.connect_room(map_generator.random_room(), rand)

        assert dirs == room.get_available_directions()

def test_initialized():
    map_generator = DungeonGenerator()

    room = map_generator.random_room()
    room.set_initialized(True)

    assert room.is_initialized()

def test_get_wrong_room():
    map_generator = DungeonGenerator()
    room = map_generator.random_room()

    try:
        room.get_room_at_direction('northwest')
    except:
        assert True
    else:
        assert False

def test_set_wrong_room():
    map_generator = DungeonGenerator()
    room = map_generator.random_room()

    try:
        room.set_room('northwest', map_generator.random_room())
    except:
        assert True
    else:
        assert False

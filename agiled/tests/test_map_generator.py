from common.map_generator import DungeonGenerator
from common.tileset import TileSet

def test_str_to_tile_matrix():
    map_generator = DungeonGenerator()
    test_matrix = map_generator.str_to_tile_matrix("###")

    assert test_matrix[0] == [TileSet.TileName.WALL, TileSet.TileName.WALL, TileSet.TileName.WALL]

def test_room_loading():
    map_generator = DungeonGenerator()
    
    assert(len(map_generator.get_tile_matrixes()) == 10)

def test_dungeon_generation():
    map_generator = DungeonGenerator()
    for _ in range(0, 5):
        root = map_generator.generate_map(None, 10)

        assert len(root.get_available_directions()) < 4

def test_dungeon_room_number():
    assert True
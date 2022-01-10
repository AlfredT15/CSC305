"""Tests for audio class"""
import os
import common.audio as audio
from common import util


def test_get_absolute_path_of_audio():
    """Test generation of absolute paths for audio files"""
    function_result = util.get_absolute_path_of_asset("audio", "effects", "test.wav")
    expected_result = get_relative_audio_filename("effects", "test.wav")
    assert function_result == expected_result


def test_song():
    """Test Song enum"""
    assert audio.Music.Song.DUNGEON01.value == "dungeon01.ogg"
    assert audio.Music.Song.DUNGEON02.value == "dungeon02.ogg"


def test_get_current_song():
    """Test that Music object is created with the correct filename"""
    music = audio.Music(audio.Music.Song.DUNGEON01, -1)
    assert music.get_current_song() == audio.Music.Song.DUNGEON01


def test_get_loops():
    """Test that Music object is created with the correct number of loops"""
    music = audio.Music(audio.Music.Song.DUNGEON01, -1)
    assert music.get_loops() == -1

    music = audio.Music(audio.Music.Song.DUNGEON01, 1)
    assert music.get_loops() == 1


def test_get_current_song_path():
    """Test that Music object is created with the correct absolute path for its filename"""
    music = audio.Music(audio.Music.Song.DUNGEON01, -1)
    expected_path = get_relative_audio_filename("music", audio.Music.Song.DUNGEON01.value)
    assert music.get_current_song_path() == expected_path


def test_sound_effect():
    """Test Song enum"""
    assert audio.SoundEffect.Effect.LASER01.value == "laser01.wav"
    assert audio.SoundEffect.Effect.LASER02.value == "laser02.wav"


def get_relative_audio_filename(audio_type: str, filename: str):
    """Helper function to create absolute path from audio type and filename"""
    directory_name = os.path.dirname(os.path.realpath(__file__))
    relative_path = os.path.join(directory_name, "..", "assets", "audio", audio_type, filename)
    return os.path.abspath(relative_path)

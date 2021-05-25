import pytest
from video_library import *
@pytest.fixture
def default_rating():
    '''Returns a Wallet instance with a zero balance'''
    return LibraryItem("name","director")

@pytest.fixture
def rating():
    '''Returns a Wallet instance with a balance of 20'''
    return LibraryItem("name","director","four")

def test_default_rating(default_rating):
    assert default_rating.rating == 0

def test_setting_default_rating(rating):
    assert rating.rating == "4"
    assert rating.name == "name"
    assert rating.director == "director"



import pytest
from settings import Settings
from controls import Controls

@pytest.fixture
def control():
    """pytest fixture to create object for testing individual methods"""
    settings = Settings()
    control = Controls(settings)
    return control

# TEST INITIALIZATION OF CONTROLS CLASS (WITH DEFAULTS FROM SETTINGS)
def test___init__(control):
    assert control.do_what == 't'
    assert control.for_what == 'blue'
    assert control.how_many == 5

# TEST WHEN USER CHOOSES a TO SEARCH BY ARTIST
# def test__get_do_what_correct_option(control, monkeypatch, capsys):
#     expected = "Enter text to search for: [enter for default blue]"
#     monkeypatch.setattr("builtins.input", lambda prompt: "a")
#     control._get_do_what()
#     assert control._get_do_what().is_get_do_what_valid == False

# TEST WHAT HAPPENS IF USER QUITS
def test_do_menu_and_response_user_quits(control, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "q")
    r = control.do_menu_and_response()
    assert r == False
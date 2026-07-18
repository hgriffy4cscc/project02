import pytest
from griffy_project2_main import do_the_thing

# TEST WHAT HAPPENS IF USER QUITS
def test_do_the_thing(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "q")
    do_the_thing()
    cap, err = capsys.readouterr()
    assert cap.strip() == 'Thank you for playing!'
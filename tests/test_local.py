from weather_forecast.local import choose_file


def _scripted_input(answers):
    answers_iter = iter(answers)
    return lambda _prompt="": next(answers_iter)


def test_choose_file_returns_selected_json(monkeypatch):
    monkeypatch.setattr("builtins.input", _scripted_input(["2"]))

    result = choose_file(["a.json", "b.txt", "c.json"])

    assert result == "c.json"


def test_choose_file_no_json_returns_none():
    assert choose_file(["a.txt", "b.md"]) is None


def test_choose_file_empty_returns_none():
    assert choose_file([]) is None


def test_choose_file_retries_on_invalid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", _scripted_input(["abc", "99", "1"]))

    result = choose_file(["only.json", "other.txt"])

    assert result == "only.json"

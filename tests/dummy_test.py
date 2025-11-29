def test_dummy():
    import racelab  # noqa: PLC0415

    assert isinstance(racelab.__version__, str)

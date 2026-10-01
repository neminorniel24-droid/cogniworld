import pytest

from src.day_night import DayNightCycle


def test_phase_wraps_at_end_of_day():
    cycle = DayNightCycle(ticks_per_day=100)

    assert cycle.phase(0) == 0.0
    assert cycle.phase(100) == 0.0
    assert cycle.phase(125) == 0.25


def test_day_starts_at_sunrise_and_ends_at_sunset():
    cycle = DayNightCycle(ticks_per_day=100)

    assert cycle.is_day(25)
    assert cycle.is_day(74)
    assert not cycle.is_day(24)
    assert not cycle.is_day(75)


def test_sunlight_peaks_at_midday():
    cycle = DayNightCycle(ticks_per_day=100)

    assert cycle.sunlight(25) == pytest.approx(0.0)
    assert cycle.sunlight(50) == pytest.approx(1.0)
    assert cycle.sunlight(75) == pytest.approx(0.0)
    assert cycle.sunlight(0) == 0.0


def test_invalid_cycle_configuration_is_rejected():
    with pytest.raises(ValueError):
        DayNightCycle(ticks_per_day=0)

    with pytest.raises(ValueError):
        DayNightCycle(sunrise_phase=0.8, sunset_phase=0.2)

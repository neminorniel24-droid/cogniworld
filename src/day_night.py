"""Small deterministic day/night cycle for the simulation world."""

from dataclasses import dataclass
from math import sin, pi


@dataclass(frozen=True)
class DayNightCycle:
    """Convert simulation ticks into a repeating day/night cycle."""

    ticks_per_day: int = 240
    sunrise_phase: float = 0.25
    sunset_phase: float = 0.75

    def __post_init__(self) -> None:
        if self.ticks_per_day <= 0:
            raise ValueError("ticks_per_day must be positive")
        if not 0.0 <= self.sunrise_phase < self.sunset_phase <= 1.0:
            raise ValueError("sunrise_phase must be before sunset_phase")

    def phase(self, tick: int) -> float:
        """Return the current phase in the repeating [0, 1) day."""
        return (tick % self.ticks_per_day) / self.ticks_per_day

    def is_day(self, tick: int) -> bool:
        """Return whether the sun is above the horizon."""
        phase = self.phase(tick)
        return self.sunrise_phase <= phase < self.sunset_phase

    def sunlight(self, tick: int) -> float:
        """Return normalized sunlight intensity in the range [0, 1]."""
        phase = self.phase(tick)
        if not self.is_day(tick):
            return 0.0
        daylight = (phase - self.sunrise_phase) / (
            self.sunset_phase - self.sunrise_phase
        )
        return sin(pi * daylight)

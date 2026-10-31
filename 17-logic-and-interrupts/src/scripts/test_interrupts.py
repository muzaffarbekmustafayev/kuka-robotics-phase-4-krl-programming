"""Unit tests for KRL interrupt and event-driven motion simulator."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from interrupt_simulator import KrlInterruptSimulator


def test_interrupt_trips_and_brakes():
    sim = KrlInterruptSimulator(brake_decel_mm_s2=5000.0)
    sim.enable_interrupt()

    # Sensor at 150 mm
    res = sim.execute_search_motion(
        start_mm=0.0,
        target_mm=400.0,
        speed_mm_s=200.0,
        sensor_trip_condition=lambda x: x >= 150.0
    )

    assert res["sensor_triggered"] is True
    assert res["completed_to_target"] is False
    assert res["trip_position_mm"] >= 150.0
    assert res["final_position_mm"] < 400.0
    # Expected braking distance: v^2 / (2 * a) = 200^2 / (2 * 5000) = 4.0 mm
    assert res["stopping_overshoot_mm"] > 0.0
    assert np.isclose(res["stopping_overshoot_mm"], 4.0, atol=1.5)


def test_disabled_interrupt_reaches_target():
    sim = KrlInterruptSimulator()
    sim.disable_interrupt()  # Interrupt is OFF

    res = sim.execute_search_motion(
        start_mm=0.0,
        target_mm=300.0,
        speed_mm_s=200.0,
        sensor_trip_condition=lambda x: x >= 100.0
    )

    # Since interrupt was disabled, robot must ignore sensor and reach 300 mm
    assert res["sensor_triggered"] is False
    assert res["completed_to_target"] is True
    assert np.isclose(res["final_position_mm"], 300.0, atol=2.0)

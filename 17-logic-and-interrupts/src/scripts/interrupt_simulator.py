"""Event-Driven Control & KRL Interrupt / Trigger Simulator.

Simulates KRL INTERRUPT DECL, BRAKE, RESUME mechanisms, Advance Run Pointer (ADVANCE),
and fast sensor touch-sensing (part detection during motion).
"""

from dataclasses import dataclass
from typing import Callable, Optional, Dict, List
import numpy as np


@dataclass
class RobotState:
    position_mm: float
    velocity_mm_s: float
    is_moving: bool
    interrupted: bool
    interrupted_at_mm: Optional[float] = None


class KrlInterruptSimulator:
    r"""Simulates KUKA KRC event-driven interrupt handling during linear motions."""

    def __init__(self, brake_decel_mm_s2: float = 6000.0, dt_sec: float = 0.005):
        self.a_brake = brake_decel_mm_s2
        self.dt = dt_sec
        self.interrupt_active = False
        self.interrupt_triggered = False

    def enable_interrupt(self):
        """Equivalent to: INTERRUPT ON 1"""
        self.interrupt_active = True
        self.interrupt_triggered = False

    def disable_interrupt(self):
        """Equivalent to: INTERRUPT OFF 1"""
        self.interrupt_active = False

    def execute_search_motion(self,
                              start_mm: float,
                              target_mm: float,
                              speed_mm_s: float,
                              sensor_trip_condition: Callable[[float], bool]) -> Dict[str, any]:
        r"""Execute linear motion while monitoring fast digital input.

        Simulates:
            INTERRUPT DECL 10 WHEN $IN[5]==TRUE DO FOUND_PART()
            INTERRUPT ON 10
            LIN P_SEARCH
        """
        current_pos = start_mm
        total_dist = abs(target_mm - start_mm)
        direction = 1.0 if target_mm >= start_mm else -1.0
        v_current = speed_mm_s

        trajectory = [current_pos]
        interrupted_pos = None

        while abs(current_pos - start_mm) < total_dist:
            # Check sensor trigger if interrupt is enabled
            if self.interrupt_active and not self.interrupt_triggered:
                if sensor_trip_condition(current_pos):
                    # Trigger INTERRUPT! Execute BRAKE
                    self.interrupt_triggered = True
                    interrupted_pos = current_pos
                    # Simulating BRAKE deceleration to full stop
                    while v_current > 0.0:
                        v_current -= self.a_brake * self.dt
                        if v_current < 0.0:
                            v_current = 0.0
                        current_pos += direction * v_current * self.dt
                        trajectory.append(current_pos)
                    break

            current_pos += direction * v_current * self.dt
            trajectory.append(current_pos)

        return {
            "completed_to_target": not self.interrupt_triggered,
            "sensor_triggered": self.interrupt_triggered,
            "trip_position_mm": interrupted_pos,
            "final_position_mm": current_pos,
            "stopping_overshoot_mm": (current_pos - interrupted_pos) if interrupted_pos else 0.0,
            "trajectory": trajectory,
        }


def main():
    print("=" * 65)
    print("Lesson 17: Logic, Interrupts & Event-Driven Control (KRL)")
    print("=" * 65)

    sim = KrlInterruptSimulator(brake_decel_mm_s2=8000.0)
    sim.enable_interrupt()

    # Sensor is located at X = 250.0 mm
    sensor_barrier = 250.0
    res = sim.execute_search_motion(
        start_mm=0.0,
        target_mm=500.0,
        speed_mm_s=250.0,
        sensor_trip_condition=lambda pos: pos >= sensor_barrier
    )

    print(f"\nSearch motion from 0.0 mm to 500.0 mm at 250 mm/s:")
    print(f"  Sensor Trip Position: {res['trip_position_mm']:.2f} mm")
    print(f"  Braking Stop Position: {res['final_position_mm']:.2f} mm")
    print(f"  Braking Overshoot:     {res['stopping_overshoot_mm']:.2f} mm")


if __name__ == "__main__":
    main()

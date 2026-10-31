"""Industrial I/O & Fieldbus (PROFINET / EtherCAT) Handshaking Simulator.

Simulates KRL SIGNAL bit mapping, PLC handshake protocol (Ready, Request, Acknowledge, Busy),
and cyclic fieldbus packet exchange.
"""

from typing import Dict, List, Tuple
import numpy as np


class FieldbusIOManager:
    r"""Simulates KUKA KRC digital input/output image ($IN, $OUT) and PLC handshaking."""

    def __init__(self, num_inputs: int = 128, num_outputs: int = 128):
        self.inputs = np.zeros(num_inputs + 1, dtype=bool)   # 1-indexed KRL style ($IN[1..128])
        self.outputs = np.zeros(num_outputs + 1, dtype=bool) # 1-indexed KRL style ($OUT[1..128])

    def set_digital_input(self, index: int, value: bool) -> None:
        """Set digital input pin ($IN[index])."""
        self.inputs[index] = bool(value)

    def get_digital_output(self, index: int) -> bool:
        """Read digital output pin ($OUT[index])."""
        return bool(self.outputs[index])

    def write_signal_byte(self, start_out: int, length: int, value: int) -> None:
        r"""Simulate KRL: SIGNAL JobEcho $OUT[start] TO $OUT[start+length-1] = value."""
        for i in range(length):
            bit = bool((value >> i) & 1)
            self.outputs[start_out + i] = bit

    def read_signal_byte(self, start_in: int, length: int) -> int:
        r"""Simulate KRL: SIGNAL JobID $IN[start] TO $IN[start+length-1]."""
        val = 0
        for i in range(length):
            if self.inputs[start_in + i]:
                val |= (1 << i)
        return val

    def execute_plc_handshake(self, job_id: int) -> Dict[str, any]:
        r"""Simulate standard automotive 4-phase PLC handshaking sequence:

        Phase 1: PLC sets JobID on $IN[1..8] and sets StartRequest on $IN[9].
        Phase 2: Robot reads JobID, sets RobotBusy on $OUT[9], echoes JobID on $OUT[1..8].
        Phase 3: PLC verifies echo and clears StartRequest ($IN[9]=FALSE).
        Phase 4: Robot finishes job, sets JobDone on $OUT[10], clears RobotBusy ($OUT[9]=FALSE).
        """
        # Phase 1: PLC asserts inputs
        self.write_inputs_as_signal(start_in=1, length=8, value=job_id)
        self.inputs[9] = True  # StartRequest

        # Phase 2: Robot acknowledges
        received_job = self.read_signal_byte(start_in=1, length=8)
        self.outputs[9] = True  # RobotBusy
        self.write_signal_byte(start_out=1, length=8, value=received_job)  # JobEcho

        # Phase 3: PLC drops request
        self.inputs[9] = False

        # Phase 4: Robot completes
        self.outputs[9] = False  # Not busy
        self.outputs[10] = True  # JobDone

        return {
            "success": True,
            "job_id_received": received_job,
            "robot_echoed_job": self.read_signal_byte(start_in=1, length=8),
            "job_done_flag": bool(self.outputs[10]),
        }

    def write_inputs_as_signal(self, start_in: int, length: int, value: int) -> None:
        """Helper for test harness to write byte to input pins."""
        for i in range(length):
            self.inputs[start_in + i] = bool((value >> i) & 1)


def main():
    print("=" * 65)
    print("Lesson 18: Industrial I/O & Fieldbus (PROFINET / PLC Handshake)")
    print("=" * 65)

    fb = FieldbusIOManager()

    # Simulate PLC requesting Job #42
    target_job = 42
    result = fb.execute_plc_handshake(target_job)

    print(f"\nHandshake Simulation:")
    print(f"  Sent Job ID:       {target_job}")
    print(f"  Robot Read Job ID: {result['job_id_received']}")
    print(f"  Handshake Success: {result['success']}")
    print(f"  Job Done Signal:   {result['job_done_flag']}")


if __name__ == "__main__":
    main()

"""Unit tests for Industrial Fieldbus and PLC Handshake."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from fieldbus_io_controller import FieldbusIOManager


def test_signal_byte_encoding_decoding():
    fb = FieldbusIOManager()

    # Write number 173 (binary: 10101101) to $IN[1..8]
    test_val = 173
    fb.write_inputs_as_signal(start_in=1, length=8, value=test_val)

    # Read back through signal function
    read_val = fb.read_signal_byte(start_in=1, length=8)
    assert read_val == test_val

    # Verify individual bits
    assert fb.inputs[1] == True   # 2^0
    assert fb.inputs[2] == False  # 2^1
    assert fb.inputs[3] == True   # 2^2


def test_plc_handshake_flow():
    fb = FieldbusIOManager()
    res = fb.execute_plc_handshake(job_id=77)

    assert res["success"] is True
    assert res["job_id_received"] == 77
    assert res["job_done_flag"] is True

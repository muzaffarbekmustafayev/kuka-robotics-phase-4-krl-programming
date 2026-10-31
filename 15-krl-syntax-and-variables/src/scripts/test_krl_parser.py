"""Unit tests for KRL syntax and geometric operator simulator."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from krl_types_parser import KrlFrame, KrlVariableParser


def test_frame_matrix_roundtrip():
    f = KrlFrame(x=120.0, y=-45.0, z=310.0, a=30.0, b=-45.0, c=15.0)
    T = f.to_matrix()
    f_rec = KrlFrame.from_matrix(T)

    assert np.isclose(f_rec.x, f.x, atol=1e-4)
    assert np.isclose(f_rec.y, f.y, atol=1e-4)
    assert np.isclose(f_rec.z, f.z, atol=1e-4)
    assert np.isclose(f_rec.a, f.a, atol=1e-4)
    assert np.isclose(f_rec.b, f.b, atol=1e-4)
    assert np.isclose(f_rec.c, f.c, atol=1e-4)


def test_geometric_colon_operator_translation():
    # Translating base by X+100 and point by X+50 should give X=150
    base = KrlFrame(x=100.0, y=0.0, z=0.0)
    pt = KrlFrame(x=50.0, y=20.0, z=0.0)
    result = base @ pt

    assert np.isclose(result.x, 150.0, atol=1e-5)
    assert np.isclose(result.y, 20.0, atol=1e-5)


def test_parser_extracts_dat_variable():
    line = "DECL E6POS P_PALLET_START = {X 450.5, Y -120.0, Z 300.0, A 0.0, B 90.0, C 0.0, S 2, T 35}"
    res = KrlVariableParser.parse_line(line)

    assert res is not None
    vtype, name, frame = res
    assert vtype == "E6POS"
    assert name == "P_PALLET_START"
    assert np.isclose(frame.x, 450.5)
    assert np.isclose(frame.y, -120.0)
    assert np.isclose(frame.b, 90.0)

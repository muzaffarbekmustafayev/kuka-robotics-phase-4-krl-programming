"""Unit tests for Parametric 3D Palletizer."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from parametric_palletizer import ParametricPalletizer


def test_pallet_capacity_and_grid_indexing():
    pallet = ParametricPalletizer(
        origin_xyz=(300.0, 0.0, 50.0),
        count_xyz=(4, 3, 2),  # 24 total
        pitch_xyz_mm=(50.0, 50.0, 30.0)
    )
    assert pallet.total_capacity == 24

    # Index 0: (0, 0, 0)
    assert pallet.index_to_grid(0) == (0, 0, 0)
    # Index 1: (1, 0, 0)
    assert pallet.index_to_grid(1) == (1, 0, 0)
    # Index 4: (0, 1, 0)
    assert pallet.index_to_grid(4) == (0, 1, 0)
    # Index 12: (0, 0, 1) - start of layer 2
    assert pallet.index_to_grid(12) == (0, 0, 1)
    # Index 23: (3, 2, 1) - final part
    assert pallet.index_to_grid(23) == (3, 2, 1)


def test_position_calculation():
    pallet = ParametricPalletizer(
        origin_xyz=(400.0, 100.0, 50.0),
        count_xyz=(2, 2, 1),
        pitch_xyz_mm=(100.0, 50.0, 20.0),
        pallet_yaw_deg=0.0  # unrotated
    )

    # First corner
    p0 = pallet.compute_position(0)
    assert np.allclose(p0["placement_pos"], [400.0, 100.0, 50.0])
    assert np.allclose(p0["approach_pos"], [400.0, 100.0, 100.0])  # +50 mm Z

    # Final corner: ix=1 (X+100), iy=1 (Y+50), iz=0
    p3 = pallet.compute_position(3)
    assert np.allclose(p3["placement_pos"], [500.0, 150.0, 50.0])


def test_index_out_of_bounds_raises():
    pallet = ParametricPalletizer(
        origin_xyz=(0.0, 0.0, 0.0),
        count_xyz=(2, 2, 2),
        pitch_xyz_mm=(10.0, 10.0, 10.0)
    )
    with pytest.raises(IndexError):
        pallet.compute_position(8)

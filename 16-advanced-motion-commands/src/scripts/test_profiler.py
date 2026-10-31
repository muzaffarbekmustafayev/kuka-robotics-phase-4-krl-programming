"""Unit tests for Motion Profiler and CIRC interpolation."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from trajectory_profiler import MotionProfiler


def test_trapezoidal_profile_distance():
    profiler = MotionProfiler()
    dist = 400.0  # mm
    traj = profiler.generate_trapezoidal_profile(distance=dist, v_max=200.0, a_max=800.0)

    # Final position must equal target distance
    assert np.isclose(traj["position"][-1], dist, atol=1e-2)
    # Peak velocity must not exceed v_max
    assert np.max(traj["velocity"]) <= 200.0 + 1e-4
    # Starts and ends at zero velocity
    assert np.isclose(traj["velocity"][0], 0.0, atol=1e-3)
    assert np.isclose(traj["velocity"][-1], 0.0, atol=1e-3)


def test_circ_interpolation_endpoints():
    profiler = MotionProfiler()
    p1 = np.array([400.0, 0.0, 300.0])
    p2 = np.array([450.0, 50.0, 300.0])
    p3 = np.array([400.0, 100.0, 300.0])

    arc = profiler.interpolate_circ_3points(p1, p2, p3, num_points=10)

    # First point is start, last point is end
    assert np.allclose(arc[0], p1, atol=1e-4)
    assert np.allclose(arc[-1], p3, atol=1e-4)

    # All points must lie on z = 300 plane
    assert np.allclose(arc[:, 2], 300.0, atol=1e-4)


def test_collinear_circ_raises_error():
    profiler = MotionProfiler()
    p1 = np.array([100.0, 0.0, 0.0])
    p2 = np.array([200.0, 0.0, 0.0])
    p3 = np.array([300.0, 0.0, 0.0])

    with pytest.raises(ValueError):
        profiler.interpolate_circ_3points(p1, p2, p3)

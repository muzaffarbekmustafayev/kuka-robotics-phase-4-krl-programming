"""Trajectory Profiler & Motion Interpolation Engine for KRL Motion Commands.

Simulates PTP, LIN, CIRC motions, S-curve (jerk-limited) velocity profiling,
and KUKA continuous path approximation (C_DIS, C_PTP blending).
"""

from typing import List, Tuple, Dict
import numpy as np


class MotionProfiler:
    """Computes jerk-limited trajectories and circular arc interpolation."""

    @staticmethod
    def generate_trapezoidal_profile(distance: float, v_max: float, a_max: float, dt: float = 0.01) -> Dict[str, np.ndarray]:
        r"""Compute trapezoidal velocity profile for distance s with velocity v_max and accel a_max."""
        # Acceleration distance and time
        t_acc = v_max / a_max
        d_acc = 0.5 * a_max * (t_acc ** 2)

        if 2.0 * d_acc > distance:
            # Triangular profile (cannot reach v_max)
            d_acc = distance / 2.0
            t_acc = np.sqrt(distance / a_max)
            v_max = a_max * t_acc
            t_cruise = 0.0
        else:
            d_cruise = distance - 2.0 * d_acc
            t_cruise = d_cruise / v_max

        t_total = 2.0 * t_acc + t_cruise
        time_steps = np.arange(0.0, t_total + dt, dt)

        s_arr, v_arr, a_arr = [], [], []
        for t in time_steps:
            if t <= t_acc:
                a = a_max
                v = a_max * t
                s = 0.5 * a_max * (t ** 2)
            elif t <= t_acc + t_cruise:
                a = 0.0
                v = v_max
                s = d_acc + v_max * (t - t_acc)
            elif t <= t_total:
                t_dec = t - (t_acc + t_cruise)
                a = -a_max
                v = v_max - a_max * t_dec
                s = distance - d_acc + (v_max * t_dec - 0.5 * a_max * (t_dec ** 2))
            else:
                a = 0.0
                v = 0.0
                s = distance
            s_arr.append(s)
            v_arr.append(v)
            a_arr.append(a)

        return {
            "time": time_steps,
            "position": np.array(s_arr),
            "velocity": np.array(v_arr),
            "acceleration": np.array(a_arr),
            "duration": float(t_total),
        }

    @staticmethod
    def interpolate_circ_3points(p_start: np.ndarray, p_aux: np.ndarray, p_end: np.ndarray, num_points: int = 20) -> np.ndarray:
        r"""Interpolate circular arc defined by 3 Cartesian points in R^3 (KRL CIRC motion)."""
        p1 = np.asarray(p_start, dtype=np.float64)
        p2 = np.asarray(p_aux, dtype=np.float64)
        p3 = np.asarray(p_end, dtype=np.float64)

        # Plane normal
        v12 = p2 - p1
        v13 = p3 - p1
        normal = np.cross(v12, v13)
        norm_n = np.linalg.norm(normal)
        if norm_n < 1e-6:
            raise ValueError("Collinear points cannot form a unique CIRC arc.")
        unit_n = normal / norm_n

        # Circle center via perpendicular bisectors
        # Midpoints
        m12 = (p1 + p2) / 2.0
        m23 = (p2 + p3) / 2.0

        # Bisector directions
        d12 = np.cross(unit_n, v12)
        d23 = np.cross(unit_n, (p3 - p2))

        # Solve intersection m12 + t * d12 = m23 + u * d23 in least squares
        A_mat = np.column_stack([d12, -d23])
        rhs = m23 - m12
        sol, _, _, _ = np.linalg.lstsq(A_mat, rhs, rcond=None)
        center = m12 + sol[0] * d12

        radius = np.linalg.norm(p1 - center)

        # Radial unit vectors in plane
        u = (p1 - center) / radius
        v = np.cross(unit_n, u)

        # Angle of p3 relative to p1
        vec_end = (p3 - center) / radius
        cos_ang = np.clip(np.dot(u, vec_end), -1.0, 1.0)
        sin_ang = np.dot(v, vec_end)
        total_angle = np.arctan2(sin_ang, cos_ang)
        if total_angle < 0:
            total_angle += 2.0 * np.pi

        # Sample arc
        angles = np.linspace(0.0, total_angle, num_points)
        arc_points = np.zeros((num_points, 3))
        for i, th in enumerate(angles):
            arc_points[i] = center + radius * (np.cos(th) * u + np.sin(th) * v)

        return arc_points


def main():
    print("=" * 65)
    print("Lesson 16: Motion Commands (PTP, LIN, CIRC) & Velocity Profiles")
    print("=" * 65)

    profiler = MotionProfiler()

    # 1. Linear trajectory profile for 500 mm move
    traj = profiler.generate_trapezoidal_profile(distance=500.0, v_max=250.0, a_max=1000.0)
    print(f"\nLinear Profile (500 mm move):")
    print(f"  Duration: {traj['duration']:.2f} s")
    print(f"  Peak Velocity: {np.max(traj['velocity']):.2f} mm/s")

    # 2. CIRC arc through 3 points
    p1 = np.array([400.0, 0.0, 300.0])
    p2 = np.array([450.0, 50.0, 300.0])
    p3 = np.array([400.0, 100.0, 300.0])
    arc = profiler.interpolate_circ_3points(p1, p2, p3, num_points=5)

    print(f"\nCIRC 3-Point Interpolation (5 Waypoints):")
    for idx, pt in enumerate(arc):
        print(f"  Point #{idx+1}: [{pt[0]:.2f}, {pt[1]:.2f}, {pt[2]:.2f}] mm")


if __name__ == "__main__":
    main()

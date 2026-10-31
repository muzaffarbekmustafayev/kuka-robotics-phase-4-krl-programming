"""Parametric 3D Palletizing Engine & KRL Expert Subprogram Generator.

Calculates 3D grid stacking positions:
    P(i, j, k) = P_origin + i * dx + j * dy + k * dz
with coordinate rotation, approach vectors, and 1D index mapping.
"""

from typing import List, Dict, Tuple
import numpy as np


class ParametricPalletizer:
    r"""Calculates industrial 3D matrix palletizing positions with orientation transforms."""

    def __init__(self,
                 origin_xyz: Tuple[float, float, float],
                 count_xyz: Tuple[int, int, int],
                 pitch_xyz_mm: Tuple[float, float, float],
                 pallet_yaw_deg: float = 0.0):
        """
        Args:
            origin_xyz: [X, Y, Z] of first corner part (mm).
            count_xyz: [Nx, Ny, Nz] number of parts along X, Y, Z.
            pitch_xyz_mm: [dx, dy, dz] spacing between part centers (mm).
            pallet_yaw_deg: Pallet orientation angle about World Z.
        """
        self.origin = np.array(origin_xyz, dtype=np.float64)
        self.nx, self.ny, self.nz = count_xyz
        self.dx, self.dy, self.dz = pitch_xyz_mm
        self.yaw_deg = pallet_yaw_deg

        # Rotation matrix around Z
        th = np.radians(pallet_yaw_deg)
        self.R = np.array([
            [np.cos(th), -np.sin(th), 0.0],
            [np.sin(th),  np.cos(th), 0.0],
            [0.0,         0.0,        1.0]
        ], dtype=np.float64)

    @property
    def total_capacity(self) -> int:
        """Total number of parts in full pallet."""
        return self.nx * self.ny * self.nz

    def index_to_grid(self, index: int) -> Tuple[int, int, int]:
        r"""Convert sequential part index (0 .. N-1) to (ix, iy, iz) layer coordinates."""
        if not (0 <= index < self.total_capacity):
            raise IndexError(f"Index {index} out of range [0, {self.total_capacity - 1}].")

        parts_per_layer = self.nx * self.ny
        iz = index // parts_per_layer
        rem = index % parts_per_layer
        iy = rem // self.nx
        ix = rem % self.nx
        return ix, iy, iz

    def compute_position(self, index: int, approach_offset_z: float = 50.0) -> Dict[str, np.ndarray]:
        r"""Calculate target Cartesian placement position and safe pre-position (approach)."""
        ix, iy, iz = self.index_to_grid(index)

        # Local offset in pallet frame
        local_offset = np.array([ix * self.dx, iy * self.dy, iz * self.dz])

        # Rotate into base frame and add origin
        world_pos = self.origin + self.R @ local_offset

        # Safe approach point (directly above part along Z)
        approach_pos = world_pos.copy()
        approach_pos[2] += approach_offset_z

        return {
            "index": index,
            "grid_coord": (ix, iy, iz),
            "placement_pos": world_pos,
            "approach_pos": approach_pos,
        }


def main():
    print("=" * 65)
    print("Lesson 19: Parametric Palletizer & KRL Expert Subprograms")
    print("=" * 65)

    # Pallet: 3 along X, 2 along Y, 2 layers along Z (12 parts total)
    pallet = ParametricPalletizer(
        origin_xyz=(400.0, -150.0, 100.0),
        count_xyz=(3, 2, 2),
        pitch_xyz_mm=(60.0, 80.0, 40.0),
        pallet_yaw_deg=15.0
    )

    print(f"\nPallet Configuration: {pallet.nx}x{pallet.ny}x{pallet.nz} (Total: {pallet.total_capacity} parts)")

    # Sample part 0 (first), part 5 (last on layer 1), part 11 (last on layer 2)
    for idx in [0, 5, 11]:
        res = pallet.compute_position(idx)
        p = np.round(res["placement_pos"], 2)
        app = np.round(res["approach_pos"], 2)
        print(f"  Part #{idx:2d} (Grid {res['grid_coord']}): Place={p.tolist()} mm, Approach={app.tolist()} mm")


if __name__ == "__main__":
    main()

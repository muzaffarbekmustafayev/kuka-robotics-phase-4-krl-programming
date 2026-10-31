"""KRL Data Types, Geometric Operator, and Variable Parser.

Implements KRL data structures (FRAME, POS, E6POS, AXIS), variable parsing,
and the KRL geometric operator (colon operator ':') representing SE(3) transformation chaining.
"""

from dataclasses import dataclass
from typing import Dict, Optional, Tuple
import re
import numpy as np


@dataclass
class KrlFrame:
    """Represents KRL FRAME or POS struct: {X, Y, Z, A, B, C}."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    a: float = 0.0  # yaw (around Z) deg
    b: float = 0.0  # pitch (around Y') deg
    c: float = 0.0  # roll (around X'') deg

    def to_matrix(self) -> np.ndarray:
        """Convert KRL frame into 4x4 SE(3) homogeneous transformation matrix."""
        a_r, b_r, c_r = np.radians(self.a), np.radians(self.b), np.radians(self.c)
        ca, sa = np.cos(a_r), np.sin(a_r)
        cb, sb = np.cos(b_r), np.sin(b_r)
        cc, sc = np.cos(c_r), np.sin(c_r)

        R = np.array([
            [ca * cb, ca * sb * sc - sa * cc, ca * sb * cc + sa * sc],
            [sa * cb, sa * sb * sc + ca * cc, sa * sb * cc - ca * sc],
            [-sb,     cb * sc,                cb * cc]
        ], dtype=np.float64)

        T = np.eye(4, dtype=np.float64)
        T[:3, :3] = R
        T[:3, 3] = [self.x, self.y, self.z]
        return T

    @classmethod
    def from_matrix(cls, T: np.ndarray) -> "KrlFrame":
        """Convert 4x4 SE(3) homogeneous transformation matrix into KrlFrame."""
        x, y, z = float(T[0, 3]), float(T[1, 3]), float(T[2, 3])
        R = T[:3, :3]
        sb = -R[2, 0]
        sb = np.clip(sb, -1.0, 1.0)
        b_rad = np.arcsin(sb)
        cb = np.cos(b_rad)

        if np.abs(cb) > 1e-6:
            a_rad = np.arctan2(R[1, 0], R[0, 0])
            c_rad = np.arctan2(R[2, 1], R[2, 2])
        else:
            c_rad = 0.0
            a_rad = np.arctan2(R[0, 1], R[1, 1]) if sb > 0 else -np.arctan2(R[0, 1], R[1, 1])

        return cls(x=x, y=y, z=z,
                   a=float(np.degrees(a_rad)),
                   b=float(np.degrees(b_rad)),
                   c=float(np.degrees(c_rad)))

    def __matmul__(self, other: "KrlFrame") -> "KrlFrame":
        r"""KRL Geometric Operator ':' equivalent (F1 : F2 = T1 @ T2)."""
        T1 = self.to_matrix()
        T2 = other.to_matrix()
        return KrlFrame.from_matrix(T1 @ T2)


class KrlVariableParser:
    """Parses KRL DAT file declarations and literals."""

    FRAME_REGEX = re.compile(
        r"DECL\s+(?:GLOBAL\s+)?(FRAME|POS|E6POS)\s+([A-Za-z0-9_]+)\s*=\s*\{([^}]+)\}",
        re.IGNORECASE
    )

    @classmethod
    def parse_frame_literal(cls, literal_str: str) -> Dict[str, float]:
        """Extract key-value parameters like {X 100.0, Y 50.0, Z 300.0, A 0.0, B 90.0, C 0.0}."""
        pairs = re.findall(r"([XYZABCST])\s+([-\d.]+)", literal_str)
        return {key.upper(): float(val) for key, val in pairs}

    @classmethod
    def parse_line(cls, line: str) -> Optional[Tuple[str, str, KrlFrame]]:
        """Parse a DECL FRAME/POS line into (type, var_name, KrlFrame)."""
        match = cls.FRAME_REGEX.search(line)
        if not match:
            return None
        vtype, name, content = match.groups()
        data = cls.parse_frame_literal(content)
        frame = KrlFrame(
            x=data.get("X", 0.0),
            y=data.get("Y", 0.0),
            z=data.get("Z", 0.0),
            a=data.get("A", 0.0),
            b=data.get("B", 0.0),
            c=data.get("C", 0.0),
        )
        return vtype.upper(), name, frame


def main():
    print("=" * 65)
    print("Lesson 15: KRL Syntax, Variables & Geometric Operator ':'")
    print("=" * 65)

    base = KrlFrame(x=100.0, y=0.0, z=0.0, a=0.0, b=0.0, c=0.0)
    point = KrlFrame(x=200.0, y=50.0, z=150.0, a=90.0, b=0.0, c=0.0)
    tool = KrlFrame(x=0.0, y=0.0, z=80.0, a=0.0, b=0.0, c=0.0)

    # KRL Geometric chaining: P_target = BASE : P_POINT : TOOL
    res = base @ point @ tool
    print(f"\nBASE:  X={base.x}, Y={base.y}, Z={base.z}")
    print(f"POINT: X={point.x}, Y={point.y}, Z={point.z}, A={point.a}")
    print(f"TOOL:  Z={tool.z}")
    print(f"\nResult of (BASE : POINT : TOOL):")
    print(f"  Pos: [{res.x:.2f}, {res.y:.2f}, {res.z:.2f}] mm")
    print(f"  Ori: A={res.a:.2f}°, B={res.b:.2f}°, C={res.c:.2f}°")


if __name__ == "__main__":
    main()

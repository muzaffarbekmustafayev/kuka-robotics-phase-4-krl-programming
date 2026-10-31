# Advanced Motion Commands & Approximation
## Harakat buyruqlari va trayektoriyani silliqlash | Команды движения и сглаживание траектории

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
PTP, LIN, CIRC buyruqlari, trayektoriyani silliqlash (C_PTP, C_DIS, C_ORI), $ADVANCE ko'rsatkichi va zamonaviy Spline bloklari.

#### 🇷🇺 Русский:
Команды PTP, LIN, CIRC, сглаживание траектории (C_PTP, C_DIS, C_ORI), указатель $ADVANCE и современный Spline.

#### 🇬🇧 English:
PTP, LIN, CIRC, path approximation parameters (C_PTP, C_DIS, C_ORI), $ADVANCE pointer, and modern Splines (SLIN, SCIRC).

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
16-advanced-motion-commands/
├── src/
│   ├── krl/            # Production KRL code (.src, .dat) [All code & comments in English]
│   └── scripts/        # Python verification scripts (.py) [All code & comments in English]
├── sim/                # KUKA.Sim Pro layouts (.vcmx), URDF and CAD models
├── docs/               # Theoretical diagrams, figures, and proofs
├── CLAUDE.md           # AI developer instructions
└── README.md           # Trilingual guide (Uzbek, Russian, English)
```

---

### 🧮 Mathematical Foundations & Verification
All formulas, derivations, and theorems for this lesson are detailed in [**docs/derivations.md**](./docs/derivations.md).
Runnable Python verification scripts are provided in `src/scripts/verify_theorem.py`.

To run the verification test:
```bash
uv run --with numpy python src/scripts/verify_theorem.py
```

---
🔗 **[Return to Master Syllabus / Bosh Mundarija](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

# Logic Operators, Control Flow & INTERRUPT Routines
## Mantiqiy operatorlar, sikllar va INTERRUPT mexanizmlari | Логические операторы, циклы и механизм прерываний INTERRUPT

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
Mantiqiy shartlar, sikllar (LOOP, WHILE, FOR) hamda asinxron uzilishlar (INTERRUPT) orqali avariya to'xtashlari va chekinish.

#### 🇷🇺 Русский:
Условия, циклы (LOOP, WHILE, FOR), асинхронные прерывания INTERRUPT для экстренной остановки (BRAKE) и отката.

#### 🇬🇧 English:
Conditional branches, loops (LOOP, WHILE, FOR), asynchronous INTERRUPT handling, BRAKE commands, and emergency retract routines.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
17-logic-and-interrupts/
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

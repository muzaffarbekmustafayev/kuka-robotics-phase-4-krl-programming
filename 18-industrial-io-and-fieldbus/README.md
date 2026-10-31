# Industrial Fieldbus Networks & Digital I/O Interfacing
## Sanoat tarmoqlari (Fieldbus) va raqamli I/O integratsiyasi | Промышленные сети (Fieldbus) и интеграция цифрового ввода/вывода

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
ProfiNet, EtherCAT protokollari, WorkVisual orqali signallarni xaritalash, $IN va $OUT signallari orqali tutqichlarni boshqarish.

#### 🇷🇺 Русский:
Протоколы ProfiNet, EtherCAT, маппинг сигналов в WorkVisual, управление захватами через $IN и $OUT.

#### 🇬🇧 English:
ProfiNet and EtherCAT configuration in WorkVisual, digital I/O mapping ($IN, $OUT), pneumatic and electric gripper interfacing.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
18-industrial-io-and-fieldbus/
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

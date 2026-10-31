# 15-Dars: KRL sintaksisi, o'zgaruvchilar va geometrik operator ':'
## KRL Syntax, Data Types & The Geometric Operator ':'

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA Robot Language (KRL) dasturlash tilining leksik va grammatik qoidalarini, asosiy (`INT`, `REAL`, `BOOL`) hamda murakkab fazoviy turlarni (`FRAME`, `POS`, `E6POS`, `AXIS`) o'rganish, dastur kodi (`.src`) va ma'lumotlar ro'yxati (`.dat`) ajratilishini tahlil qilish hamda KRL geometrik operatori (`:`) semantikasini simulyatsiya qiluvchi parser yaratish.

---

### 📊 2. Natija (Result)
1. **Python KRL Turlari va Operator Simulyatori (`krl_types_parser.py`):**
   - KRL `FRAME` va `POS` ob'ektlarini $SE(3)$ bir jinsli transformatsiyalariga va ortga o'tkazish.
   - Geometrik operator `:` zanjirli matritsaviy ko'paytmasi ($F_1 : F_2 \equiv T_1 \cdot T_2$).
   - KRL `.dat` fayllaridan o'zgaruvchilarni ajratib oluvchi regex leksik analizatori.
2. **KRL Ishlab chiqarish dasturi (`TYPES_DEMO.src` va `TYPES_DEMO.dat`):**
   - Lokal va global deklaratsiyalar, dinamik asbob ofset harakati (`LIN P_BASE_TARGET : fOffset`).
3. **Pytest Unit Testlari (`test_krl_parser.py`):**
   - Frame konvertatsiyasi, `:` operatori kompozitsiyasi va `.dat` parslanishi (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$F_{out} = F_1 : F_2 \iff T(F_{out}) = T(F_1) \cdot T(F_2)$$
$$T(F) = \begin{bmatrix} R_z(A) R_y(B) R_x(C) & \mathbf{p}(X,Y,Z) \\ \mathbf{0}^T & 1 \end{bmatrix}$$

Nazariy tahlillar [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python tahlilchisining chiqishi:
```bash
uv run --with numpy python src/scripts/krl_types_parser.py
```

Konsol chiqishi:
```
=================================================================
Lesson 15: KRL Syntax, Variables & Geometric Operator ':'
=================================================================

BASE:  X=100.0, Y=0.0, Z=0.0
POINT: X=200.0, Y=50.0, Z=150.0, A=90.0
TOOL:  Z=80.0

Result of (BASE : POINT : TOOL):
  Pos: [300.00, 50.00, 230.00] mm
  Ori: A=90.00°, B=0.00°, C=0.00°
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_krl_parser.py
```
Natija: `3 passed in 0.13s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

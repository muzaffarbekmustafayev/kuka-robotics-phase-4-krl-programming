# 16-Dars: Ilg'or harakat komandalari (PTP, LIN, CIRC va Splaynlar)
## Advanced Motion Commands: PTP, LIN, CIRC & Continuous Approximation

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA sanoat robotlarida harakat turlarini (PTP, LIN, CIRC), bo'g'inlararo sinxronlashtirish qoidalarini, 3 ta nuqta orqali fazoviy aylanma interpolyatsiyani, tezlik va zarba cheklangan (jerk-limited) profillarni hamda uzluksiz aproksimatsiya (`C_DIS`, `C_PTP`) parametrlarini dasturlash.

---

### 📊 2. Natija (Result)
1. **Python Trayektoriya Profillovchisi (`trajectory_profiler.py`):**
   - Chiziqli harakat uchun trapetsiodal tezlik va tezlanish generatori.
   - 3D fazoda ixtiyoriy 3 ta nuqta bo'yicha CIRC yoyini aniq hisoblash.
2. **KRL Ishlab chiqarish dasturi (`MOTION_MODES.src` va `MOTION_MODES.dat`):**
   - `PTP XHOME C_PTP`, `LIN P1 C_DIS`, `CIRC P_AUX, P2 C_DIS` kombinatsiyalari.
3. **Pytest Unit Testlari (`test_profiler.py`):**
   - Trayektoriya masofasi, chekka nuqtalar va kollinearlik xatoliklari nazorati (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$T_{exec} = \max_{i=1..6} \left(\frac{|\Delta q_i|}{v_{max, i}}\right), \quad \mathbf{p}(\theta) = \mathbf{C} + R(\cos\theta \mathbf{u} + \sin\theta \mathbf{v})$$

Isbotlar va splayn parametrlari [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python profillovchisini ishga tushirish:
```bash
uv run --with numpy python src/scripts/trajectory_profiler.py
```

Konsol chiqishi:
```
=================================================================
Lesson 16: Motion Commands (PTP, LIN, CIRC) & Velocity Profiles
=================================================================

Linear Profile (500 mm move):
  Duration: 2.25 s
  Peak Velocity: 250.00 mm/s

CIRC 3-Point Interpolation (5 Waypoints):
  Point #1: [400.00, 0.00, 300.00] mm
  Point #2: [435.36, 14.64, 300.00] mm
  Point #3: [450.00, 50.00, 300.00] mm
  Point #4: [435.36, 85.36, 300.00] mm
  Point #5: [400.00, 100.00, 300.00] mm
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_profiler.py
```
Natija: `3 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

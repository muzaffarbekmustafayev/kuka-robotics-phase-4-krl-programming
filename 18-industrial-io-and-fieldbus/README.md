# 18-Dars: Sanoat I/O tizimlari va Fieldbus (PROFINET / PLC Handshake)
## Industrial I/O & Fieldbus Integration (PROFINET, EtherCAT & PLC Handshaking)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KRC4/KRC5 boshqaruvchisining sanoat aloqa protokollari (PROFINET, EtherCAT) orqali raqamli kirish/chiqish signallari bilan ishlashini, KRL `SIGNAL` guruhlash deklaratsiyalarini va avtomobilsozlik hamda og'ir sanoatda qo'llaniladigan 4-fazali deterministik PLC Handshake sinxronizatsiya algoritmini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Fieldbus va I/O Menejeri (`fieldbus_io_controller.py`):**
   - KRL `$IN[1..128]` va `$OUT[1..128]` signallarini emulyatsiya qilish.
   - Ko'p bitli `SIGNAL` so'zlarini binar dekompozitsiya va konvertatsiya qilish.
   - Deterministik 4 fazali PLC Handshake simulyatsiyasi.
2. **KRL Ishlab chiqarish dasturi (`PLC_HANDSHAKE.src` va `PLC_HANDSHAKE.dat`):**
   - Retseptlar bo'yicha dinamik tarmoqlanish (`SWITCH diJobID`), ishchi statuslar (`doRobotReady`, `doRobotBusy`, `doJobDone`).
3. **Pytest Unit Testlari (`test_fieldbus.py`):**
   - Bit darajasidagi aniqlik va PLC xavfsiz sinxronlashuvi (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$\text{JobID} = \sum_{k=0}^{N-1} b_k \cdot 2^k, \quad T_{cycle} = T_{PLC} + T_{bus} + T_{KRC}$$

Nazariy tahlillar [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python simulyatsiyasini ishga tushirish:
```bash
uv run --with numpy python src/scripts/fieldbus_io_controller.py
```

Konsol chiqishi:
```
=================================================================
Lesson 18: Industrial I/O & Fieldbus (PROFINET / PLC Handshake)
=================================================================

Handshake Simulation:
  Sent Job ID:       42
  Robot Read Job ID: 42
  Handshake Success: True
  Job Done Signal:   True
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_fieldbus.py
```
Natija: `2 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

# 17-Dars: Mantiq, interruptlar va hodisalarga asoslangan boshqaruv
## Logic, Interrupts & Event-Driven Motion Control in KRL

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KRC boshqaruvchisida asinxron voqealarga asoslangan boshqaruv mexanizmlari: `INTERRUPT DECL`, `INTERRUPT ON/OFF`, `BRAKE`, `RESUME` va Advance Run Pointer ($ADVANCE$) ishlash qoidalarini o'rganish hamda tezkor datchiklar signali bo'yicha harakatdagi robotni to'xtatib obyektni aniqlash (Touch-Sensing / Part Search) dasturini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Interrupt Simulyatori (`interrupt_simulator.py`):**
   - Chiziqli qidiruv harakati davomida datchik signali tutilishi.
   - Favqulodda dinamik tormozlanish ($s_{brake} = v^2 / 2a$) va inersiya bo'yicha siljish (overshoot) hisobi.
   - Interrupt yoqilgan/o'chirilgan holatlarini to'liq emulyatsiya qilish.
2. **KRL Ishlab chiqarish dasturi (`TOUCH_SENSE.src` va `TOUCH_SENSE.dat`):**
   - `$IN[5]` orqali mahsulotni aniqlash, `$POS_INT` koordinatasini yozib olish va pnevmatik qisqichni boshqarish.
3. **Pytest Unit Testlari (`test_interrupts.py`):**
   - Tormozlanish masofasi va interruptni boshqarish testlari (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$s_{brake} = \frac{v(t_{event})^2}{2 \cdot a_{max}}, \quad T_{plan} = n_{adv} \cdot T_{ipol}$$

Tizimli tahlillar va KRC arxitekturasi [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python simulyatorini sinash:
```bash
uv run --with numpy python src/scripts/interrupt_simulator.py
```

Konsol chiqishi:
```
=================================================================
Lesson 17: Logic, Interrupts & Event-Driven Control (KRL)
=================================================================

Search motion from 0.0 mm to 500.0 mm at 250 mm/s:
  Sensor Trip Position: 250.00 mm
  Braking Stop Position: 254.14 mm
  Braking Overshoot:     4.14 mm
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_interrupts.py
```
Natija: `2 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

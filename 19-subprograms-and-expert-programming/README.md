# 19-Dars: Subprogrammalar, Funksiyalar va Parametrik Palletayzer
## Subprograms, Functions (DEFFCT) & Parametric 3D Palletizing

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-4-krl-programming-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KRL tilida modulli arxitektura qurish: protseduralar (`DEF`), qiymat qaytaruvchi funksiyalar (`DEFFCT`), parametr uzatish turlari (`:IN`, `:OUT`) hamda sanoat logistikasida keng qo'llaniladigan 3D parametrik palletizatsiya (matritsali taxlash) algoritmini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Parametrik Palletayzer Engine (`parametric_palletizer.py`):**
   - 1D tartib raqamini 3D fazoviy to'rga o'girish ($n \to (i_x, i_y, i_z)$).
   - Pallet burchagi burilishi ($R_{pallet}(\psi)$) va xavfsiz yaqinlashish (approach) traektoriyasi.
2. **KRL Ishlab chiqarish dasturi (`PALLET_EXPERT.src` va `PALLET_EXPERT.dat`):**
   - `DEFFCT POS CALC_PALLET_POS(nIdx: IN)` funksiyasi orqali har bir detal uchun koordinatani dinamik generatsiya qilish.
3. **Pytest Unit Testlari (`test_palletizer.py`):**
   - Sig'im hisobi, to'r indeksatsiyasi va chegaradan chiqish xatosi (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$i_z = \lfloor n / (N_x N_y) \rfloor, \quad i_y = \lfloor (n \bmod N_x N_y) / N_x \rfloor, \quad i_x = (n \bmod N_x N_y) \bmod N_x$$
$$\mathbf{P}(n) = \mathbf{P}_{origin} + R_{pallet} [i_x \Delta x, i_y \Delta y, i_z \Delta z]^T$$

To'liq nazariya va matematik isbotlar [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python dvigatelini ishga tushirish:
```bash
uv run --with numpy python src/scripts/parametric_palletizer.py
```

Konsol chiqishi:
```
=================================================================
Lesson 19: Parametric Palletizer & KRL Expert Subprograms
=================================================================

Pallet Configuration: 3x2x2 (Total: 12 parts)
  Part # 0 (Grid (0, 0, 0)): Place=[400.0, -150.0, 100.0] mm, Approach=[400.0, -150.0, 150.0] mm
  Part # 5 (Grid (2, 1, 0)): Place=[495.19, -41.67, 100.0] mm, Approach=[495.19, -41.67, 150.0] mm
  Part #11 (Grid (2, 1, 1)): Place=[495.19, -41.67, 140.0] mm, Approach=[495.19, -41.67, 190.0] mm
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_palletizer.py
```
Natija: `3 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

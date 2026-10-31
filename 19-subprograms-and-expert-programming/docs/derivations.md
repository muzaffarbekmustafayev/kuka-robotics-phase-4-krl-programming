# KRL Ekspert Dasturlash va Parametrik 3D Palletizatsiya

## 1. Subprogrammala va Funksiyalar Arxitekturasi
KRL da dastur strukturalashning ikkita asosiy mexanizmi mavjud:
1. `DEF SubName(param: IN, param2: OUT) ... END` — qiymat qaytarmaydigan protsedura.
2. `DEFFCT ReturnType FctName(param: IN) ... RETURN val ... ENDFCT` — hisoblangan qiymatni qaytaruvchi funksiya.

Parametr uzatish usullari:
- `:IN` (Call by Value) — argument nusxalanadi, tashqi o'zgaruvchi o'zgarmaydi;
- `:OUT` (Call by Reference) — argument xotira manzili bo'yicha uzatiladi, funksiya ichidagi o'zgarishlar tashqariga ta'sir qiladi.

---

## 2. 3D Fazoviy To'r (Palletizing Grid) Matematik Modeli
Palletdagi har bir detalning fazoviy joylashuvi 3 o'lchamli qatlamlar matritsasi sifatida ifodalanadi:

$$N_{total} = N_x \cdot N_y \cdot N_z$$

Ketma-ket tartib raqami $n \in [0, N_{total} - 1]$ dan 3D to'r indekslari $(i_x, i_y, i_z)$ ni ajratib olish (Euclidean division / Modulo arifmetikasi):

$$i_z = \left\lfloor \frac{n}{N_x \cdot N_y} \right\rfloor$$
$$r = n \pmod{N_x \cdot N_y}$$
$$i_y = \left\lfloor \frac{r}{N_x} \right\rfloor$$
$$i_x = r \pmod{N_x}$$

Fazoviy koordinata vektori:
$$\mathbf{P}(n) = \mathbf{P}_{origin} + R_{pallet} \begin{bmatrix} i_x \cdot \Delta x \\ i_y \cdot \Delta y \\ i_z \cdot \Delta z \end{bmatrix}$$

Xavfsiz yaqinlashish nuqtasi:
$$\mathbf{P}_{approach}(n) = \mathbf{P}(n) + [0, 0, \Delta Z_{safe}]^T$$
Bu formulalar qolip yuzasini yoki taglikni to'ldirishda minglab nuqtalarni qo'lda o'rgatish (teaching) zaruratini butunlay yo'qotadi.

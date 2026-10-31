# KUKA Harakat Rejimlari va Tezlik Profillari Matematikasi

## 1. PTP (Point-to-Point) Sinxron Harakati
PTP harakatida robot bo'g'inlari bir vaqtda boshlanib, bir vaqtda tugashi uchun yetakchi o'q (leading axis) aniqlanadi:
$$T_{exec} = \max_{i=1..6} \left( \frac{|\Delta q_i|}{v_{max, i}} \right)$$

Har bir o'qning tezligi sinxronlashtiriladi:
$$v_i = \frac{\Delta q_i}{T_{exec}} \le v_{max, i}$$

---

## 2. LIN va CIRC Kartesian Trayektoriyalari
1. **LIN (To'g'ri chiziqli harakat):**
   $$\mathbf{p}(t) = \mathbf{p}_1 + s(t) \cdot \frac{\mathbf{p}_2 - \mathbf{p}_1}{\|\mathbf{p}_2 - \mathbf{p}_1\|}$$
   bu yerda $s(t)$ — trapetsiodal yoki S-curve skalyar masofa profili.

2. **CIRC (Doiraviy harakat):**
   Fazodagi 3 ta nuqta ($P_1, P_{aux}, P_2$) orqali yagona aylana radiusi $R$ va markazi $\mathbf{C}$ hisoblanadi:
   $$\mathbf{n} = \frac{(P_{aux} - P_1) \times (P_2 - P_1)}{\|(P_{aux} - P_1) \times (P_2 - P_1)\|}$$
   $$\mathbf{p}(\theta) = \mathbf{C} + R (\cos\theta \mathbf{u} + \sin\theta \mathbf{v})$$

---

## 3. Uzluksiz Trayektoriya Aproksimatsiyasi (`C_DIS`, `C_PTP`)
Robot maqsadli nuqtada to'xtamasdan o'tishi uchun silliqlash radiusi $r_{approx}$ ishlatiladi.
Oraliq o'tish zonasida Bezier yoki Kubik splaynlar orqali tezlikning uzilishisiz silliq ulanish amalga oshiriladi:

$$\mathbf{p}(t) = (1 - \lambda(t)) \mathbf{p}_1(t) + \lambda(t) \mathbf{p}_2(t), \quad \lambda(t) \in [0, 1]$$
Bu tebranishlarni yo'qotadi va sikl vaqtini (cycle time) 20-35% gacha qisqartiradi.

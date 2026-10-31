# KRL Sintaksisi, Ma'lumotlar Turlari va Geometrik Operator ':'

## 1. KRL Ma'lumotlar Turlari Ierarxiyasi

1. **Primitiv turlar:**
   - `INT` (32-bit butun son: $-2^{31} \dots 2^{31}-1$)
   - `REAL` (32-bit suzuvchi nuqtali son IEEE 754)
   - `BOOL` (`TRUE` yoki `FALSE`)
   - `CHAR` (8-bit ASCII belgisi)

2. **Strukturali turlar (Structures):**
   - `FRAME`: `{X, Y, Z, A, B, C}` — 6-DOF kartesian koordinatalari (mm va gradus).
   - `POS`: `FRAME` + `S` (Status bitmask) + `T` (Turn bitmask).
   - `E6POS`: `POS` + `E1` .. `E6` (qo'shimcha tashqi o'qlar: linear track, rotary positioner).
   - `AXIS`: `{A1, A2, A3, A4, A5, A6}` — robotning 6 ta bo'g'in burchagi (gradusda).
   - `E6AXIS`: `AXIS` + `E1` .. `E6`.

---

## 2. KRL Geometrik Operatori `:` (Colon Operator)
KRL dasturlash tilidagi ikki nuqta `:` operatori maxsus $SE(3)$ bir jinsli transformatsiyalar ko'paytmasini (koordinata sistemalari kompozitsiyasini) bildiradi:

$$F_{out} = F_1 : F_2 \iff T(F_{out}) = T(F_1) \cdot T(F_2)$$

bu yerda $T(F) \in SE(3)$ matritsasi:
$$T(F) = \begin{bmatrix} R(A, B, C) & \mathbf{p}(X, Y, Z) \\ \mathbf{0}^T & 1 \end{bmatrix}$$

### Assotsiativlik qoidasi:
$$(F_1 : F_2) : F_3 = F_1 : (F_2 : F_3)$$
Lekin kommutativ EMAS:
$$F_1 : F_2 \neq F_2 : F_1$$
Bu xossa dinamik asbob siljishlarini hisoblashda ishlatiladi:
`P_OFFSET = P_TARGET : {X 0.0, Y 0.0, Z 50.0, A 0.0, B 0.0, C 0.0}`.

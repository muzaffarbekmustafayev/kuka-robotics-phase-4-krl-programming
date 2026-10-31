# KRL Interruptlar, BRAKE/RESUME va Advance Run Pointer

## 1. Advance Run Pointer ($ADVANCE$)
KRL arxitekturasi ikkita mustaqil oqimdan iborat:
1. **Asosiy hisoblash oqimi (Advance Run / Hauptlauf):** Harakat komandalarini oldindan hisoblaydi ($ADVANCE = 0 \dots 5$ qadam oldinda).
2. **Haqiqiy harakat oqimi (Main Run / Roboterlauf):** Robot aktuatorlarining real jismoniy harakati.

Agar kod ichida mantiqiy I/O signali kutilsa (`WAIT FOR $IN[1]`), Advance run to'xtaydi (Advance Run Stop). Silliq uzluksiz harakat uchun `CONTINUE` komandasi ishlatiladi:
```krl
CONTINUE
IF $IN[1] THEN
  ...
```

---

## 2. Interrupt Mexanikasi va Braking Dinamikasi
Tezkor datchik (masalan, optik yoki taktil sensor `$IN[5]`) aktivlashganda, robot kontrolleri quyidagi zanjirni bajaradi:

1. Asosiy dastur konteksti saqlanadi va interrupt servisi ishga tushadi.
2. `BRAKE` komandasi orqali robot joriy trayektoriyada maksimal sekinlanish bilan to'xtatiladi:
   $$s_{brake} = \frac{v^2}{2 \cdot a_{max}}$$
3. `RESUME` komandasi orqali joriy chaqirilgan harakat funksiyasi butunlay bekor qilinadi (bufer tozalanadi) va nazorat to'g'ridan-to'g'ri asosiy chaqiruvchi dastur pog'onasiga qaytadi.

Bu mexanizm palletda detallar balandligi noma'lum bo'lganda, ularni taktil usulda qidirib topish va avariya holatlarining oldini olish uchun sanoatda yagona standart yechimdir.

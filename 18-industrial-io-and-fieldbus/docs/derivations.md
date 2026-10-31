# Sanoat I/O Tizimi, Fieldbus va PLC Sinxronizatsiyasi

## 1. KRL Signal Bitmapping Matematikasi
KRL da raqamli kirish va chiqish portlarini butun sonli o'zgaruvchilarga birlashtirish ikkilik sanoq sistemasi pozitsion og'irliklari asosida ishlaydi:

$$\text{JobID} = \sum_{k=0}^{N-1} b_k \cdot 2^k$$
bu yerda $b_k \in \{0, 1\}$ — $k$-raqamli kirish pini (`$IN[start + k]$`).
$N=8$ bit bo'lganda: $\text{JobID} \in [0, 2^8 - 1] = [0, 255]$.

---

## 2. 4-Fazali PLC Handshake Protokoli
Robot va zavod Master PLC (Siemens S7-1500 / Beckhoff TwinCAT) orasidagi ma'lumotlar almashinuvi deterministik 4 fazali algoritm bo'yicha kechadi:

1. **Talab fazasi (Request):** PLC yangi retsept raqamini uzatadi (`diJobID = N`) va ishga tushirish signalini beradi (`diStartRequest = TRUE`).
2. **Qabul va Tasdiq (Ack & Echo):** Robot yangi retseptni o'qiydi, o'zining bandligini bildiradi (`doRobotBusy = TRUE`), va xatoliklarni tekshirish uchun o'qilgan raqamni ortga qaytaradi (`doJobEcho = N`).
3. **Talabni tozalash (Clear Request):** PLC robot tomonidan aks-sado berilgan raqam to'g'riligini tasdiqlab, `diStartRequest = FALSE` qiladi.
4. **Bajarish va Yakun (Execution & Done):** Robot mexanik ishni bajaradi, `doJobDone = TRUE` signalini ko'taradi va `doRobotBusy = FALSE` qiladi.

Bu protokol signal uzilishlari, tarmoq kechikishlari va paketlar yo'qolishida ikkala tomonning bir vaqtda to'xtab qolishi yoki noto'g'ri operatsiyani bajarishining 100% oldini oladi.

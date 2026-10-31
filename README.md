# Phase 4: KUKA Robot Language (KRL) Programming
## 4-Bob: KUKA Robot Language (KRL) Dasturlash
### Глава 4: Программирование на KUKA Robot Language (KRL)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 🌐 Phase Description (Trilingual)

#### 🇺🇿 O'zbekcha:
Sanoat KRL sintaksisi, harakat buyruqlari (PTP, LIN, CIRC, Splines), asinxron INTERRUPT, ProfiNet/EtherCAT I/O va modulli arxitektura.

#### 🇷🇺 Русский:
Синтаксис KRL, команды движения (PTP, LIN, CIRC, Splines), асинхронные прерывания INTERRUPT, промышленный I/O ProfiNet/EtherCAT.

#### 🇬🇧 English:
Industrial KRL syntax, motion commands (PTP, LIN, CIRC, Splines), asynchronous INTERRUPTs, ProfiNet/EtherCAT fieldbus I/O.

---

### 📑 Lessons Curriculum / Darslar Mundarijasi / Содержание уроков

* [**15-krl-syntax-and-variables**: KRL Syntax, Variables & Data Architecture](./15-krl-syntax-and-variables)
  * 🇺🇿 KRL tili sintaksisi, .src va .dat fayllar tuzilishi, FRAME, POS, E6POS, AXIS, E6AXIS maxsus tiplari.
  * 🇷🇺 Синтаксис языка KRL, структура файлов .src и .dat, типы данных FRAME, POS, E6POS, AXIS, E6AXIS.
  * 🇬🇧 KRL syntax, .src and .dat module pairing, FRAME, POS, E6POS, AXIS, and E6AXIS data types.

* [**16-advanced-motion-commands**: Advanced Motion Commands & Approximation](./16-advanced-motion-commands)
  * 🇺🇿 PTP, LIN, CIRC buyruqlari, trayektoriyani silliqlash (C_PTP, C_DIS, C_ORI), $ADVANCE ko'rsatkichi va zamonaviy Spline bloklari.
  * 🇷🇺 Команды PTP, LIN, CIRC, сглаживание траектории (C_PTP, C_DIS, C_ORI), указатель $ADVANCE и современный Spline.
  * 🇬🇧 PTP, LIN, CIRC, path approximation parameters (C_PTP, C_DIS, C_ORI), $ADVANCE pointer, and modern Splines (SLIN, SCIRC).

* [**17-logic-and-interrupts**: Logic Operators, Control Flow & INTERRUPT Routines](./17-logic-and-interrupts)
  * 🇺🇿 Mantiqiy shartlar, sikllar (LOOP, WHILE, FOR) hamda asinxron uzilishlar (INTERRUPT) orqali avariya to'xtashlari va chekinish.
  * 🇷🇺 Условия, циклы (LOOP, WHILE, FOR), асинхронные прерывания INTERRUPT для экстренной остановки (BRAKE) и отката.
  * 🇬🇧 Conditional branches, loops (LOOP, WHILE, FOR), asynchronous INTERRUPT handling, BRAKE commands, and emergency retract routines.

* [**18-industrial-io-and-fieldbus**: Industrial Fieldbus Networks & Digital I/O Interfacing](./18-industrial-io-and-fieldbus)
  * 🇺🇿 ProfiNet, EtherCAT protokollari, WorkVisual orqali signallarni xaritalash, $IN va $OUT signallari orqali tutqichlarni boshqarish.
  * 🇷🇺 Протоколы ProfiNet, EtherCAT, маппинг сигналов в WorkVisual, управление захватами через $IN и $OUT.
  * 🇬🇧 ProfiNet and EtherCAT configuration in WorkVisual, digital I/O mapping ($IN, $OUT), pneumatic and electric gripper interfacing.

* [**19-subprograms-and-expert-programming**: Subprograms, Functions & Expert KRL Architecture](./19-subprograms-and-expert-programming)
  * 🇺🇿 Global va lokal qism-dasturlar, funksiyalar (DEFFCT), argument uzatish va modulli parametrik zavod avtomatizatsiyasi karkasini qurish.
  * 🇷🇺 Глобальные и локальные подпрограммы, функции (DEFFCT), передача аргументов и создание модульного фреймворка автоматизации.
  * 🇬🇧 Global/local subroutines, functions (DEFFCT), call-by-value/call-by-reference argument passing, and modular automation frameworks.

---

### 🏛️ Repository Internal Structure
```
kuka-robotics-phase-4-krl-programming/
├── 15-krl-syntax-and-variables/
├── 16-advanced-motion-commands/
├── 17-logic-and-interrupts/
├── 18-industrial-io-and-fieldbus/
├── 19-subprograms-and-expert-programming/
```

---

### 👥 Academic Alliance & Authorship
* **Author / Muallif:** Muzaffarbek Mustafayev
* **Academic Partners:** Samarkand State University (SamDU) & Tomsk State University (TSU)
* 🔗 **[Master Syllabus Navigator](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**

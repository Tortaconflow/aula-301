# Aula 301 · Anexo Técnico y Calidad de Procesos Educativos

**Unidad Curricular:** Estadística Aplicada a las Ciencias Sociales (`DI-EAC-03`) · Grupo 301  
**Institución:** Instituto de Investigaciones Sociológicas (IISUABJO) — UABJO, Oaxaca  
**Orientación de Calidad (Ingeniería Industrial Aplicada):** Dra. Maldonado  
**Documento Rector Pedagógico:** [MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md](MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md)  
**Repositorio Oficial:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)  
**Sitio en Producción (PWA):** [https://aula-301.vercel.app](https://aula-301.vercel.app)

---

## 1. Resumen Técnico-Pedagógico

Este anexo traduce los lineamientos de **calidad de procesos, ergonomía y prevención de errores** de la **Dra. Maldonado** al servicio de una **adecuación curricular no significativa** en el IISUABJO. En un contexto donde 46.7 % del alumnado del caso modelo estudia únicamente con celular, 30 % comparte equipo y las computadoras escolares operan con hardware limitado e internet intermitente, se diseñó una plataforma web ligera (*Local-First*, `sw.js v6`) que traslada la captura y el resguardo de evidencias al dispositivo del estudiante, eliminando los desperdicios por espera y retrabajo.

---

## 2. Principios de Ingeniería Industrial al Servicio del Aula

### 2.1 Reducción de Desperdicios (*Lean Education / Muda*)
* **Espera y saturación (*Waiting*):** Al eliminar recursos tipográficos externos pesados y operar con estrategia *Stale-While-Revalidate* en `sw.js v6`, las vistas abren instantáneamente desde memoria local tras la primera visita (o directo desde archivo `index.html` en memoria USB).
* **Reprocesos (*Rework*):** El autoguardado automático en tiempo real (cada 400 ms en `localStorage`) impide que cortes eléctricos o caídas de señal borren las conclusiones redactadas.

### 2.2 Ergonomía Táctil (ISO 9241-110) y Hardware Modesto
* **Objetivos táctiles $\ge 44\text{ px}$:** Botones de navegación, tarjetas, selectores de autoevaluación y botones de tablas cumplen altura mínima de 44 px para uso cómodo en teléfonos de pantalla pequeña.
* **Rendimiento sin GPU pesada:** Se reemplazaron gradientes multicapa fijos y desenfoques agresivos (`backdrop-filter`) por superficies limpias de alto contraste y hoja `@media print` dedicada para quienes trabajan en papel.

### 2.3 Teoría de Colas Desacopladas
Frente a sistemas centralizados propensos a congestión cuando $\rho = \lambda / (c\mu) \ge 1$ en fechas límite de entrega, Aula 301 opera con nodos cliente desacoplados ($c_{local} = 1$, $\lambda_{central} = 0$ en captura) y consolida al cierre mediante recepción por lotes en el navegador del docente.

### 2.4 *Poka-Yoke* Formativo y Verificación de Constancias
* **Prevención de omisiones en origen:** El sistema exige completar los 4 criterios de la rúbrica de autoevaluación y una redacción mínima antes de registrar la entrega final.
* **Huella de integridad en transporte:** Cada constancia `.json` exportada incorpora una huella criptográfica **SHA-256** calculada sobre `matricula | estudiante | actividad_id | actividad | estado_entrega | fecha_generacion | conclusiones | autoevaluación ordenada` (usando Web Crypto API o respaldo síncrono en JavaScript puro cuando se ejecuta en `file://`). Esto detecta de inmediato si un archivo fue alterado accidentalmente al enviarse por WhatsApp o USB (aclarando con honestidad técnica que la verificación sin servidor comprueba integridad del archivo de transporte y no sustituye una firma institucional centralizada).

---

## 3. Flujo Operativo Resumido

1. **Estudiante:** Ingresa con **matrícula + nombre** (con opción de limpieza para equipos compartidos), resuelve cualquiera de los **3 Mini Casos oficiales** (`aula301_minicaso1_acceso_tecnologico.csv`, etc., con BOM UTF-8 compatible con Excel/Calc antiguo), realiza su autoevaluación obligatoria y comparte su constancia como archivo `.json` único por matrícula, texto copiado por **WhatsApp**, o en **papel/libreta** mediante la hoja imprimible.
2. **Docente (clave de aula `3010`):** Recibe entregas en la **Bandeja de Recepción** (arrastrando archivos `.json`/`.txt`, pegando texto de WhatsApp o capturando entregas en libreta), verifica automáticamente la integridad, asienta calificación oficial (`0–10`) y retroalimentación persistente con deduplicación por matrícula/actividad, y descarga `aula301_concentrado_entregas.csv`.

---

## 4. Auditoría Multi-Agente Goldfish

El sistema fue sometido a dos rondas de inspección independiente (*Ola 1*: 3 agentes; *Ola 2*: 5 agentes `egm-codebase-details`, `egm-design`, `egm-comprehension`, `egm-zoom-out` y `egm-structural`), descritas con detalle en [METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md](METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md). Entre las correcciones verificadas con Chrome/Node destacan: reparación del total en la descarga CSV (`totalCasos` en lugar de `undefined`/`NaN`), respaldo SHA-256 para `file://`, limpieza de jerga técnica en la interfaz, alineación estadística de los Minicasos 1 y 2 y regeneración de las 7 capturas y la presentación en PowerPoint/PDF.

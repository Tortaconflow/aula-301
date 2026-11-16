# AGENTS.md — Protocolo de Continuidad para Agentes de Inteligencia Artificial

> **REGLA DE ORO PARA CUALQUIER AGENTE QUE INTERVENGA ESTE PROYECTO:**  
> Este proyecto **NO es un desarrollo comercial de programación por programación**. Pertenece al área de **CIENCIAS DE LA EDUCACIÓN Y ADECUACIÓN CURRICULAR** en el **IISUABJO (UABJO)**, Oaxaca.  
> Todo código, cambio visual, diapositiva o texto dirigido al estudiante y al docente **debe aprobar una lectura comprensible para alguien de Ciencias Sociales/Humanidades sin formación en sistemas**. La tecnología está estrictamente subordinada al **Diseño Universal para el Aprendizaje (DUA)** y a la eliminación de **Barreras para el Aprendizaje y la Participación (BAP)**.

---

## 1. Identidad Institucional y Curricular

* **Plataforma:** Aula 301 (Mediación educativa sin conexión / PWA ligera)
* **Institución:** Instituto de Investigaciones Sociológicas de la Universidad Autónoma "Benito Juárez" de Oaxaca (**IISUABJO — UABJO**), Oaxaca, México.
* **Licenciatura:** Ciencias Sociales y Estudios Políticos (Tercer Semestre · Grupo 301).
* **Unidad Curricular de Aprendizaje (UCA):** *Estadística Aplicada a las Ciencias Sociales* (`DI-EAC-03`, 9 créditos, 144 horas semestrales: 4 docentes y 4 independientes por semana).
* **Orientación de Calidad de Procesos:** Dra. Maldonado (enfoque preventivo de errores / *Poka-Yoke* pedagógico).
* **Repositorio Oficial en GitHub:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)
* **Sitio en Producción:** [https://aula-301.vercel.app](https://aula-301.vercel.app)

---

## 2. Diagnóstico Situado de Oaxaca y del Grupo 301

* **Contexto Sociodemográfico Estatal (INEGI / CONEVAL 2024–2026):**
  * Pobreza multidimensional: **51.6 %** (vs. 29.6 % nacional).
  * Rezago educativo: **30.5 %** (vs. 18.6 % nacional).
  * Informalidad laboral: **79.9 %** (1er Trimestre 2026).
  * Diversidad lingüística: **31.2 %** de la población de 3 años y más habla lengua originaria (Censo 2020).
* **Diagnóstico del Aula (datos modelados a partir del diagnóstico exploratorio del grupo, `n = 30`):**
  * **46.7 %** estudia únicamente con teléfono celular; **30.0 %** comparte equipo; solo **23.3 %** cuenta con computadora propia.
  * Las computadoras escolares del aula *"a duras penas arrancan"* y la conectividad es nula o intermitente.
  * Presencia de BAP afectivas (timidez o temor al participar en voz alta) que exigen reflexión escrita previa y rúbricas transparentes.

---

## 3. Marco Teórico y Curricular Obligatorio

1. **Adecuación Curricular No Significativa:** Conserva los 9 créditos, 144 horas y 8 bloques temáticos. Ajusta acceso, tiempos, materiales y evaluación.
2. **DUA (Montoya et al., 2024; UNESCO):** Múltiple representación (tabla, gráfica, glosario, CSV, impresión en papel), múltiple acción/expresión (celular sin red, PC, WhatsApp, USB o libreta física) y múltiple implicación situada en Oaxaca.
3. **Aprendizaje Situado y Locus de Enunciación (López Ocampo et al., 2021; Plan IISUABJO):** Evita ejemplos abstractos y juicios estigmatizantes.
4. **Las 6 Tablas Curriculares (`js/data.js` — Única Fuente de Verdad):**
   * *Tabla 1:* Continuidad (`DI-EAC-03`, 9 créditos, 144 h).
   * *Tabla 2:* Matriz BAP (Excel + LibreOffice + app sin red + práctica en papel).
   * *Tabla 3:* Contenidos originales en 8 bloques adaptados.
   * *Tabla 4:* Saberes de la UCA (**Científico y disciplinario**, **Cultural y comunitario**, **Empírico y de sentido común**).
   * *Tabla 5:* Tres Mini Casos oficiales:
     1. *Minicaso 1:* Acceso tecnológico y participación educativa (`n = 30` + variable cuantitativa horas semanales).
     2. *Minicaso 2:* Escolaridad y empleo juvenil (matriz de contingencia 3 × 2, `n = 40`).
     3. *Minicaso 3:* Acceso a servicios básicos (`n = 50`).
   * *Tabla 6:* Secuencia didáctica de 8 semanas.

---

## 4. Restricciones Mínimas de Compatibilidad para Equipos Antiguos

* **Cero dependencias pesadas:** HTML5, CSS3 y JavaScript ES5/ES6 nativos sin librerías ni fuentes externas (`fonts.googleapis.com` prohibido para no bloquear la carga sin red).
* **Funcionamiento garantizado en `file://` y offline:** Debe abrir haciendo doble clic en `index.html`. La verificación de constancias usa Web Crypto API con respaldo síncrono en JS puro (`sha256Pure`) para funcionar incluso en `file://`. Service Worker `sw.js` en versión **`aula301-cache-v6`** con estrategia *Stale-While-Revalidate* e `{ ignoreSearch: true }`.
* **Privacidad y flujo real Docente-Alumno:**
  * Ingreso por **matrícula + nombre completo** (con opción de equipo compartido).
  * Modo Docente protegido por clave demostrativa (`3010`), con carga por archivo (`.json`/`.txt`), arrastrar y soltar, texto copiado de WhatsApp y registro manual de libretas en papel (`@media print` habilitado).
  * Todos los controles táctiles cumplen altura mínima **44 px**.

---

## 5. Estructura Real del Repositorio

```text
aula-301/
├── AGENTS.md
├── README.md
├── .gitignore
├── index.html
├── manifest.json
├── sw.js                                          # Caché v6 (Stale-While-Revalidate)
├── generate_deck.py                               # Generador portable PPTX (13 láminas)
├── css/styles.css
├── js/
│   ├── data.js                                    # Fuente Única de Verdad (Tablas 1-6, 3 Minicasos, Glosario)
│   └── app.js
├── icons/
│   ├── icon-192.png
│   └── icon-512.png
└── docs/
    ├── MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md # Documento rector de Ciencias de la Educación
    ├── MANUAL_USUARIO_DOCENTE_ALUMNO.md
    ├── DOCUMENTACION_TECNICA_INDUSTRIAL.md
    ├── JUSTIFICACION_FORMAL_REA_GOLDFISH_UNIVERSIDAD.md
    ├── METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md
    └── presentacion/
        ├── Aula_301_Adecuacion_Curricular_Oaxaca.pptx # Presentación oficial (2594.3 KB)
        ├── Aula_301_Adecuacion_Curricular_Oaxaca.pdf  # Respaldo PDF universal (2046.9 KB)
        ├── BANCO_100_PREGUNTAS_AULA301.md
        ├── PROTOCOLO_PRESENTACION_Y_SIMULACION.md
        └── capturas/                               # 01 a 07 PNG verificadas
```

---

## 6. Instrucciones para Nuevas Modificaciones

1. Edita los contenidos curriculares únicamente en `js/data.js` (nunca dupliques datos fijos en `index.html`).
2. Verifica cualquier texto nuevo frente a un lector de Ciencias Sociales (cero jerga informática innecesaria en pantalla o banco de preguntas).
3. Si cambias `index.html`, `css/styles.css`, `js/data.js` o `js/app.js`, actualiza el número de versión en `sw.js` (siguiente a `v6`), regenera las capturas/presentación si cambia la interfaz, ejecuta pruebas reales y sincroniza con `origin main`.

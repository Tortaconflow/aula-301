# AGENTS.md — Protocolo de Continuidad para Agentes de Inteligencia Artificial

> **IMPORTANTE PARA CUALQUIER AGENTE QUE INTERVENGA ESTE PROYECTO:**
> Este proyecto **NO es un ejercicio de programación de software tradicional ni de ingeniería de sistemas**. Es un proyecto del área de **CIENCIAS DE LA EDUCACIÓN Y ADECUACIÓN CURRICULAR**. 
> La tecnología (código HTML/JS/CSS, Service Workers, PWA) es únicamente un **recurso didáctico y de mediación pedagógica** subordinado a los principios de inclusión, equidad y justicia educativa en el estado de Oaxaca.
> **REGLA FUNDAMENTAL:** Nunca desvíes las explicaciones o propuestas hacia jerga técnica vacía o "vibe coding". Todo desarrollo, ajuste o documentación debe estar fundamentado en las Ciencias de la Educación, el Diseño Universal para el Aprendizaje (DUA) y la eliminación de Barreras para el Aprendizaje y la Participación (BAP).

---

## 1. Identidad Institucional y Curricular del Proyecto

* **Nombre de la Plataforma:** Aula 301 (PWA Local-First)
* **Institución:** Instituto de Investigaciones Sociológicas de la Universidad Autónoma "Benito Juárez" de Oaxaca (IISUABJO - UABJO), Ciudad Universitaria, Oaxaca, México.
* **Licenciatura:** Ciencias Sociales y Estudios Políticos (Tercer Semestre, Grupo 301).
* **Unidad Curricular de Aprendizaje (UCA):** *Estadística Aplicada a las Ciencias Sociales* (Clave: `DI-EAC-03`, 9 créditos, 144 horas semestrales: 4 docentes + 4 independientes por semana).
* **Asesoría y Lineamientos:** Dra. Maldonado (Ingeniería Industrial aplicada a procesos formativos / Poka-Yoke pedagógico).
* **Repositorio Oficial en GitHub:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)
* **Despliegue Web en Producción:** [https://aula-301.vercel.app](https://aula-301.vercel.app)

---

## 2. Diagnóstico Situado y Realidad del Aula en Oaxaca

El agente entrante debe comprender que la plataforma fue diseñada para responder a la realidad material de Oaxaca:
* **Contexto Socioeconómico (INEGI / CONEVAL 2024-2026):**
  * Pobreza multidimensional: **51.6%** (vs. 29.6% nacional).
  * Rezago educativo: **30.5%** (vs. 18.6% nacional).
  * Tasa de informalidad laboral: **79.9%** (1er Trimestre 2026).
  * Diversidad lingüística: **31.2%** de hablantes de lenguas originarias.
* **Diagnóstico del Aula 301 (Cuestionario aplicado a estudiantes):**
  * **46.7%** estudia y entrega tareas **únicamente con teléfono celular**.
  * **30.0%** usa celular y computadora compartida familiar o de cibercafé.
  * Solo **23.3%** cuenta con computadora propia.
  * **Infraestructura escolar crítica:** Las computadoras del aula escolar *"a duras penas arrancan"* y la conectividad en Ciudad Universitaria es nula o inestable.
  * **BAP afectivas:** Inseguridad y timidez para participar en voz alta frente al grupo por temor al error.

---

## 3. Marco Teórico y Pedagógico Obligatorio

1. **Adecuación Curricular No Significativa:**
   * No reduce contenidos ni baja el estándar académico: se preservan los 9 créditos, 144 horas y 8 bloques temáticos de Estadística.
   * Modifica el **acceso**, los **tiempos**, la **mediación didáctica** y los **materiales** para eliminar las BAP.
2. **Diseño Universal para el Aprendizaje (DUA) (Montoya et al., 2024; UNESCO):**
   * *Múltiples formas de representación:* Datos presentados en tabla de frecuencias, gráfica de barras visual, texto reflexivo y archivo CSV descargable.
   * *Múltiples formas de acción y expresión:* El alumno redacta en celular, en PC o en libreta; entrega por PWA offline, WhatsApp, USB o Bluetooth.
   * *Múltiples formas de implicación:* Temáticas sociales de Oaxaca (acceso tecnológico, empleo juvenil y servicios básicos).
3. **Aprendizaje Situado y Locus de Enunciación (Díaz Barriga; López Ocampo et al., 2021; Plan IISUABJO):**
   * Superación de ejemplos abstractos (dados, ruletas) hacia problemáticas concretas del entorno comunitario.
   * El estudiante explicita desde dónde lee los datos sin estigmatizar a los grupos sociales.
4. **Metodología de Mini Casos Didácticos (Wassermann, 1999; Stake; Yin):**
   * Los 3 mini casos oficiales estructurados en la **Tabla 5** del proyecto curricular.
5. **Evaluación Formativa y Poka-Yoke Pedagógico (Shigeo Shingo / ISO 9241-110):**
   * Rúbrica transparente disponible desde el inicio de la actividad.
   * Autoevaluación previa obligatoria (metacognición y autorregulación).
   * La interfaz bloquea el envío si la autoevaluación está incompleta (Poka-Yoke preventivo, no punitivo).
   * Autoguardado reactivo local cada 400 ms para evitar la pérdida accidental de datos.

---

## 4. Las 6 Tablas Curriculares Oficiales (Fuente Única de Verdad)

Cualquier cambio o extensión debe mantener congruencia con las 6 tablas del documento de adecuación curricular (disponibles en `js/data.js`):
* **Tabla 1:** Continuidad curricular (Clave DI-EAC-03, 9 créditos, 144 horas, articulación con Estadística Inferencial).
* **Tabla 2:** Matriz BAP (Ajustes de acceso, mediación, recursos y evaluación formativa).
* **Tabla 3:** Ajuste de 8 bloques de contenido original hacia aplicaciones contextuales en Oaxaca.
* **Tabla 4:** Saberes formativos: Científico/Disciplinar, Cultural/Comunitario y Ético/Sentido común.
* **Tabla 5:** Matriz de 3 Mini Casos Didácticos:
  1. *Mini caso 1:* Acceso tecnológico y participación educativa (frecuencias, porcentajes, tendencia central, dispersión).
  2. *Mini caso 2:* Escolaridad y empleo juvenil (tablas de contingencia y correlación con informalidad).
  3. *Mini caso 3:* Acceso a servicios básicos (proporciones, frecuencias relativas y reporte metodológico).
* **Tabla 6:** Secuencia de 8 semanas de trabajo docente y evidencia independiente.

---

## 5. Arquitectura Técnica y Restricciones de Implementación

* **Tecnología Base:** Vanilla HTML5, CSS3 puro (variables CSS, glassmorphism ergonómico) y JavaScript nativo modular (ES5/ES6 compatible).
* **PROHIBICIÓN ESTRICTA:** No agregar frameworks pesados (React, Angular, Vue, Next.js), ni librerías de gráficos pesadas (Chart.js, D3) ni preprocesadores que requieran entornos Node.js complejos para correr. El proyecto debe poder abrirse haciendo doble clic en `index.html` en un navegador de hace 10 años.
* **Arquitectura Local-First (Offline 100%):**
  * `sw.js`: Service Worker con estrategia Cache-First (`aula301-cache-v4`).
  * `localStorage`: Persistencia local de borradores, entregas y autoevaluaciones.
  * `Web Crypto API`: Generación de firmas SHA-256 locales en comprobantes `.json` exportables.
* **Bandeja de Ingesta Docente:** El docente puede arrastrar o cargar los comprobantes `.json` que los alumnos le envíen por WhatsApp, correo o Bluetooth para consolidar calificaciones sin requerir base de datos remota activa.
* **Optimización para Máquinas de Bajos Recursos:** La aplicación pesa menos de 1 MB y la presentación en PowerPoint está diseñada sin animaciones complejas ni tipografías externas para proyectores VGA y procesadores lentos.

---

## 6. Estructura del Repositorio

```text
aula-301/
├── AGENTS.md                                # Este documento de instrucciones para agentes
├── index.html                               # Aplicación PWA con vistas: Inicio, Actividades, Calificaciones, Recursos
├── manifest.json                            # Manifiesto Web PWA
├── sw.js                                    # Service Worker offline (v4)
├── generate_deck.py                         # Generador en Python (python-pptx) de la presentación
├── css/
│   └── styles.css                           # Estilos accesibles, contraste ISO 9241-110, responsive móvil
├── js/
│   ├── data.js                              # Fuente única de verdad (Tablas 1 a 6, diagnóstico Oaxaca, 3 mini casos)
│   └── app.js                               # Controlador de interfaz, autoguardado, SHA-256, visor de tablas
├── icons/
│   ├── icon-192.png                         # Ícono PWA 192px
│   └── icon-512.png                         # Ícono PWA 512px
└── docs/
    ├── DOCUMENTACION_TECNICA_INDUSTRIAL.md   # Dossier técnico industrial para la Dra. Maldonado
    ├── JUSTIFICACION_FORMAL_REA_GOLDFISH_UNIVERSIDAD.md # Justificación formal universitaria
    ├── MANUAL_USUARIO_DOCENTE_ALUMNO.md     # Manual operativo para profesores y alumnos
    ├── METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md # Bitácora de auditoría REA y Goldfish
    └── presentacion/
        ├── Aula_301_Adecuacion_Curricular_Oaxaca.pptx # Presentación oficial para PC escolar (992 KB)
        ├── BANCO_100_PREGUNTAS_AULA301.md    # 100 preguntas reflexivas para dinámicas con el grupo
        ├── PROTOCOLO_PRESENTACION_Y_SIMULACION.md # Plan de contingencia y guión paso a paso
        └── capturas/                        # 6 capturas estáticas de alta resolución (800x600)
            ├── 01_login_view.png
            ├── 02_inicio_home.png
            ├── 03_actividades_cards.png
            ├── 04_workspace_minicaso.png
            ├── 05_calificaciones_resumen.png
            └── 06_docente_ingesta.png
```

---

## 7. Instrucciones Clave para Nuevas Tareas

1. **Si el usuario te pide crear o modificar actividades:**
   * Alinéalas siempre con la **Tabla 5** y la **Tabla 6**. No inventes casos descontextualizados; deben tocar temas de Oaxaca (pobreza, informalidad, lenguas, servicios básicos, educación).
2. **Si el usuario te pide mejorar el diseño o código:**
   * Garantiza que el tamaño del paquete no suba de peso innecesariamente.
   * Mantén los botones táctiles con un tamaño mínimo de **44 × 44 px** (ergonomía móvil para estudiantes que viajan en transporte público o usan pantallas estrelladas).
   * Mantén el autoguardado debounced en `localStorage` y la validación Poka-Yoke antes de cualquier envío.
3. **Si el usuario te pide preparar presentaciones o materiales impresos:**
   * Considera siempre que la computadora del salón *"a duras penas arranca"*. Utiliza materiales estáticos (capturas de pantalla, archivos `.pptx` o guías descargables) que no requieran conexión a internet durante la exposición.
4. **Al finalizar cualquier modificación:**
   * Incrementa la versión de caché en `sw.js` (ejemplo: `aula301-cache-v5`) si modificas `index.html`, `js/data.js` o `js/app.js`.
   * Verifica la integridad de los archivos y realiza commit y push a `main` en [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301).

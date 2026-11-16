# Aula 301 — Adecuación Curricular y Mediación Inclusiva (IISUABJO, UABJO)

Plataforma educativa abierta, ultraligera y funcional **sin conexión a internet**, construida como recurso de mediación pedagógica desde las **Ciencias de la Educación** y el **Diseño Universal para el Aprendizaje (DUA)** para la Unidad Curricular de Aprendizaje (UCA) **Estadística Aplicada a las Ciencias Sociales** (`DI-EAC-03`, tercer semestre, Grupo 301) en el Instituto de Investigaciones Sociológicas de la UABJO (**IISUABJO**), Oaxaca, bajo orientación de calidad de procesos de la **Dra. Maldonado**.

* **Plataforma en línea (PWA):** [https://aula-301.vercel.app](https://aula-301.vercel.app)
* **Repositorio público en GitHub:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)
* **Protocolo para agentes e IA:** [AGENTS.md](AGENTS.md)
* **Documento rector en Ciencias de la Educación:** [docs/MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md](docs/MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md)
* **Manual Docente y Estudiante:** [docs/MANUAL_USUARIO_DOCENTE_ALUMNO.md](docs/MANUAL_USUARIO_DOCENTE_ALUMNO.md)
* **Presentación lista para PC escolar (.pptx y .pdf):** [docs/presentacion/Aula_301_Adecuacion_Curricular_Oaxaca.pptx](docs/presentacion/Aula_301_Adecuacion_Curricular_Oaxaca.pptx) · [PDF de respaldo](docs/presentacion/Aula_301_Adecuacion_Curricular_Oaxaca.pdf)
* **Protocolo de exposición y Banco de 100 preguntas:** [PROTOCOLO_PRESENTACION_Y_SIMULACION.md](docs/presentacion/PROTOCOLO_PRESENTACION_Y_SIMULACION.md) · [BANCO_100_PREGUNTAS_AULA301.md](docs/presentacion/BANCO_100_PREGUNTAS_AULA301.md)

---

## Características Pedagógicas y de Accesibilidad (Oaxaca)

1. **Acceso sin contraseñas bloqueantes y seguro en equipos compartidos:** Ingreso por matrícula y nombre completo, con limpieza opcional de sesión tras descargar constancias (pensado para el 30 % que comparte equipo o usa PCs escolares).
2. **Los 3 Mini Casos oficiales de la Adecuación Curricular (Tabla 5):**
   * *Minicaso 1:* Acceso tecnológico y participación educativa ($n = 30$, con variable cuantitativa complementaria de horas semanales para tendencia central y dispersión).
   * *Minicaso 2:* Escolaridad y empleo juvenil (matriz de contingencia 3 × 2, $n = 40$).
   * *Minicaso 3:* Acceso a servicios básicos (proporciones y cierre metodológico, $n = 50$).
3. **Evaluación Formativa y Andamiaje Preventivo:** Rúbrica abierta desde el inicio, autoevaluación previa obligatoria (*Poka-Yoke* formativo), estimación orientativa en *Mis calificaciones* (`0 de 3 minicasos`) y hoja imprimible para práctica en papel/libreta (DUA).
4. **Entrega sin internet y Bandeja Docente Unificada:** Descarga de datos CSV con codificación UTF-8 BOM para Excel/LibreOffice, constancia verificable o copiable para **WhatsApp**, más recepción docente (clave de demostración: `3010`) por archivo, texto pegado o registro de entregas en papel físico.
5. **Visor Curricular y Glosario:** Consulta interactiva de las **6 Tablas de la Adecuación Curricular** y glosario breve en la pestaña *Recursos y Tablas*, sin depender de internet ni de tipografías externas.

---

## Estructura Real del Repositorio

```text
aula-301/
├── AGENTS.md                                      # Reglas pedagógicas y técnicas para agentes
├── README.md                                      # Guía general del proyecto
├── .gitignore
├── index.html                                     # Aplicación PWA ligera compatible con file://
├── manifest.json                                  # Manifiesto PWA instalable
├── sw.js                                          # Service Worker offline (aula301-cache-v6)
├── generate_deck.py                               # Generador reproducible de la presentación PPTX
├── css/styles.css                                 # Estilos ligeros, >=44px ISO 9241-110 e impresión DUA
├── js/
│   ├── data.js                                    # Fuente Única de Verdad (Tablas 1-6, 3 Minicasos, Glosario)
│   └── app.js                                     # Controlador ES5/ES6 sin dependencias externas
├── icons/                                         # Íconos PWA (192px y 512px)
└── docs/
    ├── MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md # Documento rector de Ciencias de la Educación
    ├── MANUAL_USUARIO_DOCENTE_ALUMNO.md           # Guía de uso para alumnos y docentes
    ├── DOCUMENTACION_TECNICA_INDUSTRIAL.md        # Anexo de calidad de procesos (Dra. Maldonado)
    ├── JUSTIFICACION_FORMAL_REA_GOLDFISH_UNIVERSIDAD.md # Anexo formal REA y Goldfish
    ├── METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md # Bitácora de Olas 1 y 2 Goldfish
    └── presentacion/
        ├── Aula_301_Adecuacion_Curricular_Oaxaca.pptx # Diapositivas ligeras con capturas (2.5 MB)
        ├── Aula_301_Adecuacion_Curricular_Oaxaca.pdf  # Respaldo universal para aulas sin Office (2.0 MB)
        ├── BANCO_100_PREGUNTAS_AULA301.md          # 100 preguntas de Ciencias Sociales, DUA y Estadística
        ├── PROTOCOLO_PRESENTACION_Y_SIMULACION.md  # Estrategia anti-fallos para PCs modestas
        └── capturas/                               # 7 capturas reales actualizadas (01 a 07)
```

---

## Licencia y Uso Universitario
Material abierto y gratuito para la comunidad estudiantil y docente de la **Universidad Autónoma "Benito Juárez" de Oaxaca (UABJO)**.

/**
 * Aula 301 — Fuente única de verdad pedagógica y curricular
 * Basado en el "Proyecto de Adecuación Curricular" para la UCA:
 * "Estadística Aplicada a las Ciencias Sociales" (Clave DI-EAC-03, 3er Semestre)
 * Licenciatura en Ciencias Sociales y Estudios Políticos — IISUABJO, UABJO, Oaxaca.
 *
 * Enfoque rector: Ciencias de la Educación, Adecuación Curricular No Significativa,
 * Diseño Universal para el Aprendizaje (DUA), Atención a las BAP y Aprendizaje Situado.
 */
window.AULA301_DATA = {
  metadata: {
    institucion: "Instituto de Investigaciones Sociológicas (IISUABJO) — UABJO",
    licenciatura: "Licenciatura en Ciencias Sociales y Estudios Políticos",
    uca: "Estadística Aplicada a las Ciencias Sociales",
    clave: "DI-EAC-03",
    semestre: "Tercer Semestre · Grupo 301",
    creditos: 9,
    horasSemestrales: 144,
    horasDocentesSemana: 4,
    horasIndependientesSemana: 4,
    enfoquePedagogico: "Ciencias de la Educación · Adecuación Curricular No Significativa · DUA y Aprendizaje Situado",
    asesoriaCalidad: "Dra. Maldonado (Enfoque de calidad formativa y prevención de errores)",
    estatusDatos: "Datos modelados con fines didácticos a partir del diagnóstico exploratorio del Grupo 301",
    githubRepo: "https://github.com/Tortaconflow/aula-301",
    sitioWeb: "https://aula-301.vercel.app"
  },

  diagnosticoOaxaca: {
    pobrezaMultidimensional: "51.6 % en Oaxaca (vs. 29.6 % nacional — INEGI / CONEVAL)",
    rezagoEducativo: "30.5 % en Oaxaca (vs. 18.6 % nacional — INEGI 2024)",
    informalidadLaboral: "79.9 % de la población ocupada (1er Trimestre 2026 — INEGI)",
    diversidadLinguistica: "31.2 % de la población de 3 años y más habla lengua originaria (Censo 2020)",
    brechaDigitalAula: "46.7 % depende solo del teléfono celular; 30.0 % comparte equipo; 23.3 % tiene computadora propia",
    barrerasIdentificadas: [
      "Conectividad intermitente o inexistente y paquetes de datos móviles limitados.",
      "Equipos escolares antiguos con baja capacidad y predominio de pantallas pequeñas de celular.",
      "Inseguridad o timidez para participar oralmente en clase; necesidad de práctica situada en problemas de Oaxaca."
    ]
  },

  // Roles funcionales reales de la plataforma
  roles: {
    estudiante: { label: "Estudiante", name: "Carlos Arturo" },
    docente: { label: "Docente", name: "Docente del Grupo 301" }
  },

  // Escala orientativa transparente para estimación de autoevaluación formativa
  escalaAutoevaluacion: {
    "Logrado": 10.0,
    "En proceso": 7.2,
    "Inicial": 4.0
  },

  // TABLA 5 + TABLA 3 + TABLA 6: Matriz Oficial de los 3 Mini Casos Didácticos
  miniCasos: [
    {
      id: 1,
      badge: "Actividad 1 · Semanas 1 a 5",
      titulo: "Minicaso 1: Acceso tecnológico y participación educativa",
      meta: "Estadística Descriptiva · n = 30 casos didácticos · DUA",
      estadoDefault: "Pendiente",
      disponible: true,
      aplicacionEstadistica: "Organización de frecuencias y porcentajes, categoría modal, gráficas y cálculo de media, mediana y dispersión sobre horas semanales de conectividad.",
      descripcion: "Analiza cómo se distribuye el acceso a dispositivos en 30 estudiantes de Oaxaca (variable cualitativa nominal) y revisa en la base descargable las horas semanales de conexión estable (variable cuantitativa) para reflexionar sobre formatos escolares inclusivos.",
      totalCasos: 30,
      tipoVisualizacion: "barras",
      csvFilename: "aula301_minicaso1_acceso_tecnologico.csv",
      csvNote: "Nota: Datos modelados con fines didacticos (Grupo 301, IISUABJO). La categoria de dispositivo es cualitativa nominal (frecuencias, % y moda); la segunda tabla del archivo incluye horas semanales de conexion estable (n=30) para calcular media, mediana, rango y desviacion estandar.",
      categorias: [
        { categoria: "Solo celular", casos: 14, porcentajeTexto: "46.7 %", porcentajeAncho: 46.7 },
        { categoria: "Celular y computadora compartida", casos: 9, porcentajeTexto: "30.0 %", porcentajeAncho: 30.0 },
        { categoria: "Computadora propia", casos: 7, porcentajeTexto: "23.3 %", porcentajeAncho: 23.3 }
      ],
      variableCuantitativa: {
        nombre: "Horas semanales de acceso estable para estudio (n = 30 casos didácticos)",
        resumen: "Media: 6.20 h · Mediana: 5.5 h · Rango: 14 h (Mín. 1 h, Máx. 15 h) · Desviación estándar muestral: 4.11 h",
        valores: [2, 3, 2, 4, 3, 5, 2, 1, 3, 4, 2, 3, 3, 2, 6, 8, 5, 7, 6, 8, 7, 5, 6, 12, 14, 10, 15, 11, 13, 14]
      },
      consigna: "1) Identifica la categoría modal (dispositivo predominante) en la tabla de frecuencias; 2) Si trabajas en Semana 4 o 5, descarga los datos para calcular tendencia central y dispersión sobre las horas de conexión; 3) Escribe dos conclusiones sobre qué debe cuidar un docente al solicitar tareas en Oaxaca.",
      glosaLocus: "El locus de enunciación es el lugar social, cultural y experiencial desde el que lees la realidad. Responde considerando tus propias condiciones de estudio y las de tu grupo:",
      preguntaReflexiva: "Si casi la mitad de tus compañeros estudia únicamente con celular, ¿qué formatos de entrega y mediación pedagógica resultan verdaderamente equitativos?"
    },
    {
      id: 2,
      badge: "Actividad 2 · Semana 7",
      titulo: "Minicaso 2: Escolaridad y empleo juvenil",
      meta: "Tabla de Contingencia 3 × 2 · n = 40 casos didácticos · Oaxaca",
      estadoDefault: "Disponible",
      disponible: true,
      aplicacionEstadistica: "Construcción de tablas de contingencia (3 × 2), cálculo de porcentajes condicionales por fila e interpretación de asociaciones entre variables.",
      descripcion: "Examina una tabla cruzada entre nivel de escolaridad y condición de empleo juvenil (informal o formal), contextualizada al 79.9 % de informalidad laboral en Oaxaca.",
      totalCasos: 40,
      tipoVisualizacion: "contingencia",
      csvFilename: "aula301_minicaso2_escolaridad_empleo.csv",
      csvNote: "Nota: Matriz de contingencia 3x2 modelada con fines didacticos sobre escolaridad y empleo juvenil en Oaxaca (Grupo 301, IISUABJO).",
      matrizContingencia: {
        columnas: ["Escolaridad alcanzada", "Empleo informal", "Empleo formal", "Total fila", "% Informalidad"],
        filas: [
          { categoria: "Secundaria o menos", informal: 14, formal: 2, total: 16, pctTexto: "87.5 %" },
          { categoria: "Bachillerato", informal: 11, formal: 4, total: 15, pctTexto: "73.3 %" },
          { categoria: "Superior o técnica", informal: 5, formal: 4, total: 9, pctTexto: "55.6 %" }
        ],
        totales: { informal: 30, formal: 10, total: 40, pctTexto: "75.0 %" }
      },
      categorias: [
        { categoria: "Secundaria o menos (14 de 16 en informalidad)", casos: 14, porcentajeTexto: "87.5 % informal", porcentajeAncho: 87.5 },
        { categoria: "Bachillerato (11 de 15 en informalidad)", casos: 11, porcentajeTexto: "73.3 % informal", porcentajeAncho: 73.3 },
        { categoria: "Superior o técnica (5 de 9 en informalidad)", casos: 5, porcentajeTexto: "55.6 % informal", porcentajeAncho: 55.6 }
      ],
      consigna: "Compara los porcentajes condicionales de empleo informal por nivel educativo en la tabla de contingencia y redacta dos conclusiones explicando la asociación observada y sus límites sociales.",
      glosaLocus: "Desde los saberes ético-comunitarios (Tabla 4), leer cifras de informalidad implica analizar condiciones estructurales de Oaxaca sin estigmatizar a las juventudes:",
      preguntaReflexiva: "¿Por qué una proporción importante de jóvenes con bachillerato o estudios superiores continúa insertándose en empleos informales?"
    },
    {
      id: 3,
      badge: "Actividad 3 · Semana 8",
      titulo: "Minicaso 3: Acceso a servicios básicos",
      meta: "Proporciones y Cobertura · n = 50 viviendas didácticas · Cierre",
      estadoDefault: "Disponible",
      disponible: true,
      aplicacionEstadistica: "Cálculo de proporciones, comparación de frecuencias absolutas y relativas, e interpretación de diferencias de cobertura para el apartado metodológico final.",
      descripcion: "Compara la cobertura de agua entubada, energía eléctrica y drenaje en 50 viviendas simuladas para redactar conclusiones y alcances en el informe cuantitativo de cierre.",
      totalCasos: 50,
      tipoVisualizacion: "barras",
      csvFilename: "aula301_minicaso3_servicios_basicos.csv",
      csvNote: "Nota: Datos modelados con fines didacticos para el cierre del apartado metodologico (Semana 8, Grupo 301, IISUABJO).",
      categorias: [
        { categoria: "Cobertura completa (agua, luz y drenaje)", casos: 16, porcentajeTexto: "32.0 %", porcentajeAncho: 32.0 },
        { categoria: "Cobertura parcial (1 o 2 servicios)", casos: 22, porcentajeTexto: "44.0 %", porcentajeAncho: 44.0 },
        { categoria: "Carencia de servicios básicos", casos: 12, porcentajeTexto: "24.0 %", porcentajeAncho: 24.0 }
      ],
      consigna: "Compara las frecuencias absolutas y las proporciones relativas de cobertura de servicios básicos y redacta dos conclusiones precisando los alcances metodológicos de estos resultados.",
      glosaLocus: "El aporte transversal de la UCA (Tabla 4) pide proponer acciones proporcionales a los datos respetando la dignidad de las localidades:",
      preguntaReflexiva: "¿Cómo comunicarías estas desigualdades de cobertura en un informe académico cuidando de no generalizar ni estigmatizar a ninguna comunidad?"
    }
  ],

  // Rúbrica formativa y auténtica basada en el DUA y en la Tabla 4 del documento oficial
  rubricaEjemplo: {
    niveles: ["Logrado", "En proceso", "Inicial"],
    criterios: [
      {
        criterio: "Planteamiento y Locus de Enunciación",
        ayuda: "Delimita la pregunta social y reconoce desde dónde lees los datos.",
        logrado: "Formula una pregunta social delimitada y reflexiona sobre su posición al interpretar el fenómeno.",
        enProceso: "La pregunta es comprensible, pero amplia o poco situada en el contexto.",
        inicial: "No se distingue la pregunta ni la intención analítica."
      },
      {
        criterio: "Organización y Cálculo Estadístico",
        ayuda: "Ordena frecuencias, porcentajes o medidas con claridad.",
        logrado: "Tabla ordenada, con totales y porcentajes exactos y justificación del procedimiento.",
        enProceso: "Tabla completa pero con errores menores de cálculo o formato.",
        inicial: "Datos sueltos, sin ordenamiento ni procedimientos visibles."
      },
      {
        criterio: "Interpretación Social Situada",
        ayuda: "Concluye con respaldo en los datos, sin prejuicios ni exageraciones.",
        logrado: "Conclusiones fundamentadas en los datos, explicitando alcances y límites éticos sin estigmatizar.",
        enProceso: "Describe superficialmente los números sin profundizar en el significado social.",
        inicial: "Opina desde el sentido común sin apoyarse en la evidencia estadística."
      },
      {
        criterio: "Comunicación y Accesibilidad",
        ayuda: "Usa gráficas legibles y redacción breve comprensible para el grupo.",
        logrado: "Representación clara y texto breve, respetuoso y accesible para compañeros.",
        enProceso: "Gráfica o redacción cumplen parcialmente con criterios de legibilidad.",
        inicial: "Presentación confusa, ilegible o sin estructura."
      }
    ]
  },

  // LAS 6 TABLAS OFICIALES DE LA ADECUACIÓN CURRICULAR (Definición declarativa unificada)
  tablasAdecuacionCurricular: [
    {
      numero: 1,
      titulo: "Continuidad en la propuesta curricular",
      descripcion: "Elementos estructurales de la UCA que se conservan íntegros para mantener el rigor universitario.",
      columnas: ["Elemento original", "Continuidad en la propuesta"],
      campos: ["elemento", "detalle"],
      filas: [
        { elemento: "Identificación", detalle: "Clave DI-EAC-03; tercer semestre; nueve créditos." },
        { elemento: "Carga académica", detalle: "Cuatro horas docentes y cuatro independientes por semana; 144 horas semestrales." },
        { elemento: "Propósito formativo", detalle: "Comprender conceptos estadísticos y aplicarlos al estudio de fenómenos sociales." },
        { elemento: "Trayectoria", detalle: "Recupera saberes previos y aporta bases para Estadística Inferencial y Sistematización y Análisis de Datos Cualitativos." }
      ]
    },
    {
      numero: 2,
      titulo: "Matriz de adecuación curricular (Acceso y mediación BAP)",
      descripcion: "Ajustes de acceso, materiales y evaluación para eliminar Barreras para el Aprendizaje y la Participación sin bajar la exigencia.",
      columnas: ["Componente", "Base curricular original", "Ajuste de acceso y mediación"],
      campos: ["componente", "original", "ajuste"],
      filas: [
        { componente: "Saberes y desempeños", original: "Sistematización de información, lectura del contexto y alternativas éticas.", ajuste: "Guías de análisis y evidencias individuales para hacer visibles esos mismos saberes." },
        { componente: "Metodología", original: "Aprendizaje situado, diálogo, ejercicios y estudio de casos.", ajuste: "Mini casos didácticos delimitados y aplicados a la realidad social." },
        { componente: "Recursos", original: "Excel, laptop, proyector, pizarrón y hojas.", ajuste: "Se conserva el trabajo en Excel; se añaden archivos compatibles, alternativas gratuitas, aplicación ligera sin red y práctica en papel." },
        { componente: "Evaluación", original: "Productos diversos, escalas estimativas, rúbricas e interrogación.", ajuste: "Avances con retroalimentación y revisión; formatos equivalentes de respuesta con criterios comunes." }
      ]
    },
    {
      numero: 3,
      titulo: "Ajuste de contenidos originales a la aplicación contextual",
      descripcion: "Vinculación de los ocho bloques de Estadística Aplicada con preguntas concretas de la realidad social.",
      columnas: ["Contenidos originales", "Aplicación propuesta"],
      campos: ["bloques", "aplicacion"],
      filas: [
        { bloques: "1. Conceptos generales / 2. Métodos estadísticos", aplicacion: "Distinguir estadística descriptiva e inferencial, ramas y tipos de análisis. Elegir un procedimiento coherente con una pregunta social." },
        { bloques: "3. Excel y presentaciones gráficas / 4. Medidas de tendencia central", aplicacion: "Construir tablas de frecuencia, histogramas, polígonos y otras gráficas pertinentes. Calcular e interpretar media, mediana y moda." },
        { bloques: "5. Medidas de dispersión / 6. Curva normal", aplicacion: "Calcular rango, varianza, desviación estándar y coeficiente de variación. Explicar propiedades de la curva normal sin asumir que todo dato se distribuye así." },
        { bloques: "7. Muestreo y encuestas / 8. Apartado metodológico cuantitativo", aplicacion: "Diseñar cuestionarios, distinguir técnicas de muestreo y calcular tamaños de muestra con supuestos explícitos. Integrar diseño, población, instrumentos y análisis." }
      ]
    },
    {
      numero: 4,
      titulo: "Saberes establecidos en la UCA y evidencias de aprendizaje",
      descripcion: "Articulación de los saberes científico, cultural-comunitario y empírico-ético del perfil de egreso (IISUABJO).",
      columnas: ["Saber establecido en la UCA", "Definición curricular", "Aporte y evidencia de aprendizaje"],
      campos: ["saber", "definicion", "evidencia"],
      filas: [
        { saber: "Científico y disciplinario", definicion: "Sistematiza y analiza información de su entorno mediante herramientas tecnológicas para construir acciones de transformación social.", evidencia: "Investigación social: identifica variables, construye una base ordenada, justifica los procedimientos y presenta resultados reproducibles." },
        { saber: "Cultural y comunitario", definicion: "Reconoce su locus de enunciación para interpretar realidades complejas interactuando con distintas identidades culturales.", evidencia: "Análisis crítico situado: contrasta interpretaciones con pares de forma respetuosa y registra cómo su propia posición influye en la lectura de datos." },
        { saber: "Empírico y de sentido común", definicion: "Propone alternativas al entorno social bajo principios éticos encaminados al bien común.", evidencia: "Aporte transversal: propone una acción proporcional a los resultados y explicita sus límites, sin divulgar identidades ni estigmatizar grupos." }
      ]
    },
    {
      numero: 5,
      titulo: "Mini casos y aplicaciones estadísticas propuestas",
      descripcion: "Tres problemas didácticos delimitados que evitan ejercicios descontextualizados.",
      columnas: ["Mini caso", "Aplicación de los contenidos estadísticos"],
      campos: ["minicaso", "aplicacion"],
      filas: [
        { minicaso: "Acceso tecnológico y participación educativa", aplicacion: "Organización de frecuencias y porcentajes, cálculo de medidas de tendencia central y dispersión, y elaboración de gráficas." },
        { minicaso: "Escolaridad y empleo juvenil", aplicacion: "Construcción de tablas de contingencia, cálculo de porcentajes e interpretación de asociaciones entre variables." },
        { minicaso: "Acceso a servicios básicos", aplicacion: "Cálculo de proporciones, comparación de frecuencias absolutas y relativas, e interpretación de diferencias en la cobertura de servicios." }
      ]
    },
    {
      numero: 6,
      titulo: "Secuencia del proyecto de ocho semanas",
      descripcion: "Organización gradual (64 horas de proyecto dentro de las 144 horas de la UCA) articulando trabajo docente guiado y evidencia independiente.",
      columnas: ["Semana y contenidos", "Trabajo docente y actividad", "Evidencia independiente"],
      campos: ["semana", "docente", "evidencia"],
      filas: [
        { semana: "1. Conceptos generales", docente: "Inicio: diagnóstico breve, acuerdos de diálogo y pregunta del proyecto. Mini caso 1 como situación de entrada.", evidencia: "Glosario con ejemplos y delimitación inicial de la pregunta." },
        { semana: "2. Métodos estadísticos", docente: "Contrastar tipos de análisis y formular variables. Precisar qué permite responder un diseño descriptivo.", evidencia: "Ficha de pregunta, variables y fuentes posibles." },
        { semana: "3. Excel y gráficas", docente: "Demostración guiada y práctica con tablas, histograma y polígono. Comparar representaciones.", evidencia: "Archivo de datos, diccionario de variables y gráficas." },
        { semana: "4. Tendencia central", docente: "Resolver análisis del mini caso 1. Justificar la elección de media, mediana o moda.", evidencia: "Cálculos revisados y explicación individual." },
        { semana: "5. Dispersión", docente: "Calcular rango, varianza, desviación estándar y coeficiente de variación. Explicitar convención poblacional o muestral.", evidencia: "Comentario sobre heterogeneidad y efecto del valor extremo." },
        { semana: "6. Curva normal", docente: "Explicar propiedades con ejemplos preparados. Contrastar simetría ideal con datos del caso y evitar supuestos automáticos.", evidencia: "Comparación gráfica y nota sobre alcance del modelo." },
        { semana: "7. Muestreo y encuestas", docente: "Trabajar mini caso 2, diseñar preguntas y distinguir técnicas. Ejercitar tamaño de muestra con supuestos explícitos.", evidencia: "Instrumento breve y justificación de población, muestra y selección." },
        { semana: "8. Apartado metodológico", docente: "Cierre: mini caso 3, integración del informe, revisión entre pares y comunicación de hallazgos.", evidencia: "Informe corregido y reflexión individual sobre el aprendizaje." }
      ]
    }
  ],

  // Glosario accesible de Ciencias de la Educación y Estadística Aplicada
  glosarioEducativo: [
    {
      termino: "Adecuación Curricular No Significativa",
      definicion: "Ajuste en tiempos, materiales, formatos y mediación docente para garantizar la inclusión sin recortar contenidos ni disminuir el rigor académico de la asignatura."
    },
    {
      termino: "BAP (Barreras para el Aprendizaje y la Participación)",
      definicion: "Obstáculos que no provienen de la capacidad del estudiante, sino de entornos, recursos o metodologías rígidas (por ejemplo, exigir computadora propia o conexión continua en Oaxaca)."
    },
    {
      termino: "DUA (Diseño Universal para el Aprendizaje)",
      definicion: "Marco pedagógico que ofrece múltiples formas de presentar la información (tablas, gráficas, texto, papel), de participar/entregar y de motivar a través de casos reales cercanos."
    },
    {
      termino: "Locus de enunciación",
      definicion: "El lugar social, cultural, económico y geográfico desde el que cada persona observa e interpreta los fenómenos sociales."
    },
    {
      termino: "Evaluación Formativa y Metacognición",
      definicion: "Uso de la rúbrica y la autoevaluación antes de entregar para que el propio estudiante identifique qué comprendió y qué debe fortalecer, más allá de una calificación numérica final."
    },
    {
      termino: "Categoría Modal vs. Media aritmética",
      definicion: "En datos nominales (como tipo de dispositivo: celular o computadora) solo se calcula frecuencia, porcentaje y categoría modal (la más repetida). La media y desviación estándar se calculan únicamente sobre variables numéricas continuas o discretas (como horas semanales)."
    }
  ]
};

// Compatibilidad segura para llamadas legadas
window.AULA301_DATA.minicasoEjemplo = window.AULA301_DATA.miniCasos[0];

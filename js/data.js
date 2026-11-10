/**
 * Aula 301 — Fuente única de verdad de datos pedagógicos y curriculares
 * Basado en el "Proyecto de Adecuación Curricular" para la UCA:
 * "Estadística Aplicada a las Ciencias Sociales" (Clave DI-EAC-03, 3er Semestre)
 * Licenciatura en Ciencias Sociales y Estudios Políticos — IISUABJO, UABJO, Oaxaca.
 * 
 * Enfoque pedagógico: Ciencias de la Educación, DUA (Diseño Universal para el Aprendizaje),
 * Aprendizaje Situado y Atención a las BAP (Barreras para el Aprendizaje y la Participación).
 */
window.AULA301_DATA = {
  // Metadatos institucionales y curriculares oficiales
  metadata: {
    institucion: "Instituto de Investigaciones Sociológicas (IISUABJO) - UABJO",
    licenciatura: "Licenciatura en Ciencias Sociales y Estudios Políticos",
    uca: "Estadística Aplicada a las Ciencias Sociales",
    clave: "DI-EAC-03",
    semestre: "Tercer Semestre",
    creditos: 9,
    horasSemestrales: 144,
    horasDocentesSemana: 4,
    horasIndependientesSemana: 4,
    enfoquePedagogico: "Adecuación Curricular No Significativa, Aprendizaje Situado y DUA",
    asesoriaIndustrial: "Dra. Maldonado",
    githubRepo: "https://github.com/Tortaconflow/aula-301"
  },

  // Diagnóstico del contexto de Oaxaca y BAP del grupo (Datos oficiales INEGI / Cuestionario Grupo 301)
  diagnosticoOaxaca: {
    pobrezaMultidimensional: "51.6 % en Oaxaca (vs. 29.6 % nacional)",
    rezagoEducativo: "30.5 % en Oaxaca (vs. 18.6 % nacional - INEGI 2024)",
    informalidadLaboral: "79.9 % de la población ocupada (INEGI 2026)",
    diversidadLinguistica: "31.2 % de la población habla lengua indígena (Censo 2020)",
    brechaDigitalAula: "46.7 % de estudiantes solo cuenta con celular; 30 % celular y PC compartida; 23.3 % PC propia",
    barrerasIdentificadas: [
      "Brecha de conectividad e infraestructura digital en Ciudad Universitaria y hogares.",
      "Inseguridad y timidez para participar en intervenciones orales espontáneas.",
      "Necesidad de vincular la teoría estadística con problemáticas sociales reales de Oaxaca."
    ]
  },

  // Roles de usuario en la plataforma
  roles: {
    estudiante: { label: "Estudiante", name: "Carlos Arturo" },
    docente: { label: "Docente", name: "Docente Titular (IISUABJO)" },
    administrador: { label: "Administrador", name: "Reily" }
  },

  // TABLA 5: Matriz Oficial de Mini Casos Didácticos
  miniCasos: [
    {
      id: 1,
      titulo: "Minicaso 1: Acceso tecnológico y participación educativa",
      semana: "Semanas 1 a 4",
      aplicacionEstadistica: "Organización de frecuencias y porcentajes, cálculo de medidas de tendencia central y dispersión, y elaboración de gráficas.",
      descripcion: "Analiza la distribución del acceso a dispositivos tecnológicos en un grupo de 30 estudiantes y reflexiona sobre el diseño de estrategias pedagógicas inclusivas en Oaxaca.",
      totalCasos: 30,
      csvFilename: "aula301_minicaso1_acceso_tecnologico.csv",
      csvNote: "Datos didácticos simulados del Minicaso 1 - Aula 301 / IISUABJO",
      categorias: [
        { categoria: "Solo celular", casos: 14, porcentajeTexto: "46.7 %", porcentajeAncho: 46.7 },
        { categoria: "Celular y computadora compartida", casos: 9, porcentajeTexto: "30.0 %", porcentajeAncho: 30.0 },
        { categoria: "Computadora propia", casos: 7, porcentajeTexto: "23.3 %", porcentajeAncho: 23.3 }
      ],
      preguntaReflexiva: "Si casi la mitad de tus compañeros estudia únicamente con teléfono celular, ¿qué formatos de entrega y mediación pedagógica resultan verdaderamente equitativos?"
    },
    {
      id: 2,
      titulo: "Minicaso 2: Escolaridad y empleo juvenil",
      semana: "Semanas 5 a 7",
      aplicacionEstadistica: "Construcción de tablas de contingencia, cálculo de porcentajes e interpretación de asociaciones entre variables.",
      descripcion: "Explora la relación entre niveles de escolaridad alcanzados y la inserción en empleo formal o informal en jóvenes de las ocho regiones de Oaxaca.",
      totalCasos: 40,
      csvFilename: "aula301_minicaso2_escolaridad_empleo.csv",
      csvNote: "Datos didácticos simulados del Minicaso 2 - Aula 301 / IISUABJO",
      categorias: [
        { categoria: "Secundaria o menos / Empleo informal", casos: 18, porcentajeTexto: "45.0 %", porcentajeAncho: 45.0 },
        { categoria: "Bachillerato / Empleo informal", casos: 12, porcentajeTexto: "30.0 %", porcentajeAncho: 30.0 },
        { categoria: "Superior o técnico / Empleo formal", casos: 10, porcentajeTexto: "25.0 %", porcentajeAncho: 25.0 }
      ],
      preguntaReflexiva: "¿Qué límites tienen los datos estadísticos para explicar las trayectorias laborales sin considerar el contexto comunitario y económico?"
    },
    {
      id: 3,
      titulo: "Minicaso 3: Acceso a servicios básicos",
      semana: "Semana 8 (Cierre del Proyecto)",
      aplicacionEstadistica: "Cálculo de proporciones, comparación de frecuencias absolutas y relativas, e interpretación de diferencias en la cobertura de servicios.",
      descripcion: "Compara el acceso a agua potable, energía eléctrica y drenaje entre municipios urbanos y rurales de Oaxaca para integrar el apartado metodológico final.",
      totalCasos: 50,
      csvFilename: "aula301_minicaso3_servicios_basicos.csv",
      csvNote: "Datos didácticos simulados del Minicaso 3 - Aula 301 / IISUABJO",
      categorias: [
        { categoria: "Cobertura completa (Agua, luz, drenaje)", casos: 16, porcentajeTexto: "32.0 %", porcentajeAncho: 32.0 },
        { categoria: "Cobertura parcial (1 o 2 servicios)", casos: 22, porcentajeTexto: "44.0 %", porcentajeAncho: 44.0 },
        { categoria: "Carencia de servicios básicos", casos: 12, porcentajeTexto: "24.0 %", porcentajeAncho: 24.0 }
      ],
      preguntaReflexiva: "¿Cómo formular propuestas de política social sustentadas en datos sin revictimizar ni estigmatizar a las comunidades?"
    }
  ],

  // Rúbrica formativa y auténtica basada en el DUA y en la Tabla 4 del documento
  rubricaEjemplo: {
    niveles: ["Logrado", "En proceso", "Inicial"],
    criterios: [
      {
        criterio: "Planteamiento y Locus de Enunciación",
        logrado: "Formula una pregunta social delimitada y reflexiona sobre su posición al interpretar el fenómeno.",
        enProceso: "La pregunta es comprensible, pero amplia o desvinculada del contexto.",
        inicial: "No se distingue la pregunta ni la intención pedagógica."
      },
      {
        criterio: "Organización y Cálculo Estadístico",
        logrado: "Tabla de frecuencias ordenada, con totales y porcentajes exactos y justificación del procedimiento.",
        enProceso: "Tabla completa pero con errores menores de cálculo o formato.",
        inicial: "Datos sueltos, sin ordenamiento ni procedimientos visibles."
      },
      {
        criterio: "Interpretación Social Situada",
        logrado: "Conclusiones fundamentadas en los datos, explicitando alcances y limitaciones éticas sin prejuicios.",
        enProceso: "Describe superficialmente los números sin profundizar en el significado social.",
        inicial: "Opina desde el sentido común sin apoyarse en la evidencia estadística."
      },
      {
        criterio: "Comunicación y Accesibilidad",
        logrado: "Representación gráfica clara, lenguaje respetuoso, sintético y accesible para el grupo.",
        enProceso: "Gráfica o redacción cumplen parcialmente con criterios de legibilidad.",
        inicial: "Presentación confusa, ilegible o sin estructura."
      }
    ]
  },

  // LAS 6 TABLAS OFICIALES DE LA ADECUACIÓN CURRICULAR (Documento Drive)
  tablasAdecuacionCurricular: [
    {
      numero: 1,
      titulo: "Continuidad en la propuesta curricular",
      descripcion: "Elementos estructurales de la UCA que se mantienen para garantizar el rigor y la validez institucional.",
      filas: [
        { elemento: "Identificación", detalle: "Clave DI-EAC-03; tercer semestre; nueve créditos." },
        { elemento: "Carga académica", detalle: "Cuatro horas docentes y cuatro independientes por semana; 144 horas semestrales." },
        { elemento: "Propósito formativo", detalle: "Comprender conceptos estadísticos y aplicarlos al estudio de fenómenos sociales." },
        { elemento: "Trayectoria", detalle: "Recupera saberes previos y aporta bases para Estadística Inferencial y Análisis Cualitativo." }
      ]
    },
    {
      numero: 2,
      titulo: "Matriz de adecuación curricular (Atención a las BAP)",
      descripcion: "Ajustes de acceso y mediación pedagógica sin reducir la exigencia formativa.",
      filas: [
        { componente: "Saberes y desempeños", original: "Sistematización de información, lectura del contexto y alternativas éticas.", ajuste: "Guías de análisis y evidencias individuales para hacer visibles esos mismos saberes." },
        { componente: "Metodología", original: "Aprendizaje situado, diálogo, ejercicios y estudio de casos.", ajuste: "Mini casos didácticos delimitados y aplicados a la realidad social de Oaxaca." },
        { componente: "Recursos", original: "Excel, laptop, proyector, pizarrón y hojas.", ajuste: "Se conserva Excel; se añaden archivos compatibles, alternativas gratuitas, PWA offline y práctica en papel." },
        { componente: "Evaluación", original: "Productos diversos, escalas estimativas, rúbricas e interrogación.", ajuste: "Avances con retroalimentación formativa y revisión; formatos equivalentes con criterios comunes." }
      ]
    },
    {
      numero: 3,
      titulo: "Ajuste de contenidos originales a la aplicación contextual",
      descripcion: "Traducción de los 8 bloques temáticos de la UCA hacia problemas del entorno oaxaqueño.",
      filas: [
        { bloques: "1. Conceptos generales / 2. Métodos estadísticos", aplicacion: "Distinguir estadística descriptiva e inferencial. Elegir procedimientos coherentes con una pregunta social." },
        { bloques: "3. Excel y gráficas / 4. Medidas de tendencia central", aplicacion: "Construir tablas de frecuencia, histogramas y polígonos. Calcular e interpretar media, mediana y moda." },
        { bloques: "5. Medidas de dispersión / 6. Curva normal", aplicacion: "Calcular rango, varianza, desviación estándar y coeficiente de variación. Analizar alcances de la curva normal sin supuestos automáticos." },
        { bloques: "7. Muestreo y encuestas / 8. Apartado metodológico", aplicacion: "Diseñar cuestionarios situados, distinguir técnicas de muestreo y estructurar el informe cuantitativo integrado." }
      ]
    },
    {
      numero: 4,
      titulo: "Saberes de la UCA y evidencias de aprendizaje",
      descripcion: "Articulación entre saberes disciplinares, comunitarios y éticos (Perfil de egreso IISUABJO).",
      filas: [
        { saber: "Científico y disciplinario", definicion: "Sistematiza y analiza información de su entorno con herramientas tecnológicas para la transformación social.", evidencia: "Investigación social: base ordenada, procedimientos justificados y resultados reproducibles." },
        { saber: "Cultural y comunitario", definicion: "Reconoce su locus de enunciación para interpretar realidades complejas en diálogo intercultural.", evidencia: "Análisis crítico situado: contrasta interpretaciones con pares y explicita su propia posición." },
        { saber: "Empírico y de sentido común", definicion: "Propone alternativas sociales bajo principios éticos hacia el bien común.", evidencia: "Aporte transversal: propuesta proporcional a los datos, protegiendo identidades y sin estigmatizar." }
      ]
    },
    {
      numero: 5,
      titulo: "Mini casos didácticos y aplicaciones estadísticas",
      descripcion: "Problemas situados que articulan la teoría con la realidad empírica de Oaxaca.",
      filas: [
        { minicaso: "Acceso tecnológico y participación educativa", aplicacion: "Frecuencias, porcentajes, medidas de tendencia central, dispersión y gráficas." },
        { minicaso: "Escolaridad y empleo juvenil", aplicacion: "Tablas de contingencia, porcentajes e interpretación de asociaciones entre variables." },
        { minicaso: "Acceso a servicios básicos", aplicacion: "Proporciones, frecuencias absolutas y relativas, y brechas de cobertura territorial." }
      ]
    },
    {
      numero: 6,
      titulo: "Secuencia didáctica del proyecto (8 Semanas)",
      descripcion: "Distribución del trabajo docente guiado y la evidencia independiente del estudiante.",
      filas: [
        { semana: "Semana 1: Conceptos generales", docente: "Diagnóstico inicial, acuerdos de diálogo. Mini caso 1 como situación de entrada.", evidencia: "Glosario con ejemplos contextuales y delimitación de la pregunta." },
        { semana: "Semana 2: Métodos estadísticos", docente: "Contrastar tipos de análisis y formular variables sociales.", evidencia: "Ficha de pregunta, variables y fuentes posibles." },
        { semana: "Semana 3: Excel y gráficas", docente: "Demostración guiada y práctica con tablas e histogramas.", evidencia: "Archivo de datos, diccionario de variables y gráficas." },
        { semana: "Semana 4: Tendencia central", docente: "Resolución del Mini caso 1. Justificar elección de media, mediana o moda.", evidencia: "Cálculos revisados y explicación individual fundamentada." },
        { semana: "Semana 5: Dispersión", docente: "Calcular rango, varianza y desviación estándar. Efecto de valores atípicos.", evidencia: "Comentario sobre heterogeneidad y dispersión social." },
        { semana: "Semana 6: Curva normal", docente: "Contrastar simetría teórica con la realidad asimétrica de Oaxaca.", evidencia: "Comparación gráfica y nota sobre alcances del modelo." },
        { semana: "Semana 7: Muestreo y encuestas", docente: "Mini caso 2: diseño de preguntas, técnicas de muestreo y supuestos.", evidencia: "Instrumento breve y justificación de población y muestra." },
        { semana: "Semana 8: Apartado metodológico", docente: "Mini caso 3: cierre, integración del informe y coevaluación formativa.", evidencia: "Informe cuantitativo final corregido y reflexión individual metacognitiva." }
      ]
    }
  ]
};

// Compatibilidad hacia atrás con referencias del prototipo
window.AULA301_DATA.minicasoEjemplo = window.AULA301_DATA.miniCasos[0];

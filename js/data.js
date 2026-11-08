/**
 * Aula 301 — Fuente única de verdad de datos del modelo (MVP)
 * Los datos del minicaso de ejemplo, la rúbrica de ejemplo y los roles
 * viven únicamente aquí para evitar duplicados entre tabla, gráfica, CSV y autoevaluación.
 */
window.AULA301_DATA = {
  roles: {
    estudiante: { label: "Estudiante", name: "Carlos Arturo" },
    docente: { label: "Docente", name: "Docente del Grupo 301" },
    administrador: { label: "Administrador", name: "Reily" }
  },
  minicasoEjemplo: {
    total: 30,
    csvFilename: "aula301_minicaso_ejemplo.csv",
    csvNote: "Nota: datos ficticios de EJEMPLO para practica - Aula 301",
    categorias: [
      { categoria: "Solo celular", casos: 14, porcentajeTexto: "46,7 %", porcentajeAncho: 46.7 },
      { categoria: "Celular y computadora compartida", casos: 9, porcentajeTexto: "30 %", porcentajeAncho: 30 },
      { categoria: "Computadora propia", casos: 7, porcentajeTexto: "23,3 %", porcentajeAncho: 23.3 }
    ]
  },
  rubricaEjemplo: {
    niveles: ["Logrado", "En proceso", "Inicial"],
    criterios: [
      {
        criterio: "Planteamiento",
        logrado: "Formula una pregunta clara y delimitada.",
        enProceso: "La pregunta es comprensible, pero amplia.",
        inicial: "No se distingue la pregunta."
      },
      {
        criterio: "Organización de datos",
        logrado: "Tabla ordenada, con totales y porcentajes correctos.",
        enProceso: "Tabla completa con errores menores.",
        inicial: "Datos sueltos, sin tabla."
      },
      {
        criterio: "Interpretación",
        logrado: "Conclusiones ligadas a los datos, sin exagerar.",
        enProceso: "Describe los datos, pero concluye poco.",
        inicial: "Opina sin apoyarse en los datos."
      },
      {
        criterio: "Comunicación",
        logrado: "Gráfico legible y texto breve y claro.",
        enProceso: "Gráfico o texto cumplen a medias.",
        inicial: "No se entiende el resultado."
      }
    ]
  }
};

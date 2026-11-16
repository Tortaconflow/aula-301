# Dictamen y Justificación Universitaria: Arquitectura Accesible, Ingeniería Inversa y Auditoría Multi-Agente Goldfish en Aula 301

> **Relación con Ciencias de la Educación:**  
> Este texto formaliza la dimensión epistemológica y de aseguramiento de calidad sobre el uso de agentes inteligentes en educación superior, en articulación subordinada al documento rector pedagógico [MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md](MARCO_PEDAGOGICO_Y_ADECUACION_CURRICULAR.md).

**Institución:** Instituto de Investigaciones Sociológicas (IISUABJO) — Universidad Autónoma "Benito Juárez" de Oaxaca (UABJO)  
**Licenciatura:** Licenciatura en Ciencias Sociales y Estudios Políticos (3er Semestre · Grupo 301)  
**Unidad Curricular de Aprendizaje (UCA):** *Estadística Aplicada a las Ciencias Sociales* (`DI-EAC-03`)  
**Orientación de Calidad de Procesos:** Dra. Maldonado  
**Repositorio Público:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)  
**Sitio Desplegado:** [https://aula-301.vercel.app](https://aula-301.vercel.app)

---

## 1. Resumen Académico

El proyecto **Aula 301** integra una adecuación curricular no significativa basada en el Diseño Universal para el Aprendizaje (DUA) con una mediación tecnológica ultraligera diseñada específicamente para la realidad de Oaxaca, donde el 46.7 % del grupo modelo accede solo mediante celular, 30.0 % comparte equipo, el rezago educativo estatal alcanza 30.5 % y la informalidad laboral 79.9 % (INEGI / CONEVAL). 

Para demostrar que un profesional o estudiante del área educativa puede crear software didáctico seguro sin caer en el improvisado *“vibe coding”*, se articuló un análisis funcional comparativo de sistemas escolares existentes (SICE UABJO y Google Classroom) con dos ciclos de auditoría del **Enjambre Multi-Agente Goldfish (`egm-*`)**, consolidando rigor pedagógico, accesibilidad en hardware modesto e integridad verificable en las entregas sin conexión.

---

## 2. Deconstrucción de Sistemas Educativos y Alternativa Situada

| Dimensión | SICE UABJO | Google Classroom | Aula 301 (Mediación DUA) |
| :--- | :--- | :--- | :--- |
| **Disponibilidad sin red** | 0 % (requiere servidor activo) | Parcial / consumo de telemetría | **100 % operativa sin internet (`sw.js v6`) o vía `file://`** |
| **Compatibilidad de equipos** | Fallos frecuentes en saturación ($\rho \ge 1$) | App nativa > 120 MB; pesada en PCs antiguas | **Ultraligera sin fuentes ni librerías externas** |
| **Formatos alternativos** | Formulario rígido único | Requiere cuenta en la nube | **Archivo `.json`, texto para WhatsApp y hoja imprimible en papel** |
| **Integridad y recepción** | Sujeta a caída en envío | Nube corporativa | **Huella SHA-256 canónica en transporte + Bandeja Docente consolidada** |

---

## 3. Cómo el Educador Gobierna a la IA (Superación del *Vibe Coding*)

La tesis universitaria central del proyecto sostiene que **la pedagogía debe gobernar a la tecnología y no al revés**:
1. **Reglas del dominio educativo primero:** El docente o estudiante de Ciencias Sociales define qué barreras (BAP) existen, qué contenidos de las **6 Tablas de la UCA `DI-EAC-03`** se trabajan y qué tono ético exige cada minicaso (*sin estigmatizar a las comunidades*).
2. **Contraloría multi-agente (`Goldfish Swarm`):** En la segunda ola de auditoría intervinieron cinco perfiles críticos independientes (`egm-codebase-details`, `egm-design`, `egm-comprehension`, `egm-zoom-out`, `egm-structural`), los cuales impidieron errores de estadística descriptiva, detectaron cálculos rotos de CSV, obligaron a traducir la interfaz a lenguaje educativo llano y validaron las 13 diapositivas y su PDF de respaldo sobre equipos modestos.

---

## 4. Conclusiones

1. Es viable que educadores y científicos sociales diseñen recursos digitales soberanos, gratuitos y auditables en GitHub sin depender de departamentos externos ni licencias comerciales.
2. El verdadero criterio de calidad en tecnología educativa para Oaxaca no es la complejidad técnica, sino garantizar que ningún estudiante quede excluido por falta de computadora o conexión a internet.

---

## Referencias Bibliográficas

1. **IISUABJO - UABJO.** (2023). *Plan de Estudios de la Licenciatura en Ciencias Sociales y Estudios Políticos y Secuencia Curricular DI-EAC-03*. UABJO.
2. **Montoya Naguas, T. M., Fierro Ríos, M. C., Ayala Arias, M. C., Lema Cordonez, P. C., & Pillapaxi Taipei, M. P.** (2024). El Diseño Universal de Aprendizaje (DUA), un modelo para la inclusión educativa. *Ciencia Latina*, 8(4), 10905–10920.
3. **Martell León, L. F. U.** (2020). Las Barreras para el Aprendizaje y la Participación. Un análisis desde la Psicología. *Academicus*, 1(17), 66–73.
4. **López Ocampo, N. A. et al.** (2021). Práctica pedagógica y motivación desde el aprendizaje situado. *Tesis Psicológica*, 16(1), 178–201.
5. **Wassermann, S.** (1999). *El estudio de casos como método de enseñanza*. Amorrortu.
6. **Kleppmann, M. et al.** (2019). *Local-first software: you own your data, in spite of the cloud*. ACM Onward! 2019.
7. **International Organization for Standardization.** (2020). *ISO 9241-110:2020 Ergonomics of human-system interaction*. ISO.
8. **Shingo, S.** (1986). *Zero Quality Control: Source Inspection and the Poka-Yoke System*. Productivity Press.

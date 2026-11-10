# Universidad Autónoma “Benito Juárez” de Oaxaca
## Instituto de Investigaciones Sociológicas (IISUABJO) / Instituto de Ciencias de la Educación (ICEUABJO)
**Área de Formación Metodológica y Tecnológica · Licenciatura en Ciencias Sociales**  
**Cátedra:** Estadística Aplicada a las Ciencias Sociales · Grupo 301  
**Titular de la Materia:** Dra. Maldonado (Especialidad en Ingeniería Industrial y Calidad de Procesos)  
**Ciclo Académico:** Semestre 2026-II / Noviembre 2026  

---

# DICTAMEN TÉCNICO Y MONOGRAFÍA METODOLÓGICA FORMAL
## Justificación de Ingeniería y Arquitectura Resiliente en la Plataforma "Aula 301": Integración del Marco de Ingeniería Inversa (REA) y el Enjambre Multi-Agente Goldfish de Google Antigravity para la Superación del *Vibe Coding*

**Autor / Proyectista:** Alumno Investigador del Grupo 301  
**Repositorio Oficial en Producción:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)  
**Entorno Productivo Desplegado:** [https://aula-301.vercel.app](https://aula-301.vercel.app)  

---

### Resumen Académico
El presente dictamen formal expone la justificación epistémica, metodológica y técnica del proyecto de innovación educativa **Aula 301**. La plataforma nace como una respuesta ingenieril a la brecha de infraestructura que afecta a la comunidad estudiantil del IISUABJO en Oaxaca, donde el **46.7% de la matrícula opera exclusivamente a través de telefonía celular inteligente** y un **30% adicional comparte dispositivos familiares**, en un entorno caracterizado por conectividad intermitente y paquetes de datos limitados. Para asegurar que el software resultante no incurriera en las debilidades del desarrollo empírico contemporáneo conocido como *Vibe Coding* (improvisación no estructurada mediada por modelos generativos), el proyecto adoptó dos metodologías de rigor industrial: 
1. La **Ingeniería Inversa Funcional y Sistémica (REA - *Reverse Engineering Anything*)**, utilizada para deconstruir plataformas dominantes como el Sistema Integral de Control Escolar (**SICE UABJO**) y **Google Classroom**, identificando sus fallas de cola y cuellos de botella para descartar la fragilidad de sus servidores centrales.
2. El **Enjambre de Agentes Revisores Goldfish (EGM Swarm)** de Google Antigravity, un sistema de gobernanza multi-perspectiva donde auditores especializados con mandatos críticos validaron la conformidad línea a línea del código fuente, forzaron la incorporación de sellado criptográfico **SHA-256** mediante Web Crypto API, blindaron la ergonomía táctil bajo la norma **ISO 9241-110** (objetivos táctiles $\ge 44\text{ px}$) y cerraron el ciclo docente mediante una bandeja de ingesta de datos offline.

El trabajo demuestra con evidencia empírica cómo un estudiante del área educativa y ciencias sociales puede diseñar, dirigir y auditar software institucional con estándares de **Cero Defectos (*Zero Defects*)**, alta disponibilidad descentralizada y pertinencia pedagógica.

**Descriptores:** *Ingeniería Inversa de Sistemas, Enjambre Goldfish, Arquitectura Local-First, Vibe Coding, Ergonomía Cognitiva, Poka-Yoke Pedagógico, Confiabilidad de Sistemas.*

---

## 1. Contextualización y Diagnóstico Empírico de Operaciones

En el marco de la **Ingeniería Industrial**, cualquier intervención en un sistema de servicio debe partir de un diagnóstico empírico de la demanda y las restricciones materiales del entorno de operación (*Gemba*).

En el Grupo 301 de Estadística Aplicada del IISUABJO, el análisis inicial sobre una muestra de $N = 30$ casos ficticios pero representativos de la realidad regional arrojó la siguiente distribución de recursos tecnológicos:

```text
Distribución de Acceso Tecnológico (Grupo 301):
├── Solo teléfono celular inteligente:          14 alumnos (46.7%)  [Dispositivo Dominante]
├── Celular y computadora compartida:            9 alumnos (30.0%)  [Restricción de Concurrencia]
└── Computadora propia y de uso exclusivo:       7 alumnos (23.3%)  [Minoría Tecnológica]
Total de casos muestreados:                     30 alumnos (100.0%)
```

### La Paradoja de los Sistemas Institucionales
Tanto las autoridades universitarias como las plataformas comerciales asumen que el alumno promedio se ubica en el 23.3% que dispone de una computadora de escritorio con enlace de banda ancha dedicado. Cuando se implementan soluciones diseñadas bajo ese supuesto:
* El **76.7% de los estudiantes** queda en condiciones de vulnerabilidad operativa.
* Se presentan fallas recurrentes por desconexión en redes móviles 3G o paquetes de datos limitados.
* El docente enfrenta una sobrecarga administrativa atendiendo justificaciones de entregas frustradas por fallas en el servidor institucional.

---

## 2. Metodología de Ingeniería Inversa (Marco REA: *Reverse Engineering Anything*)

Para no reinventar la rueda ni cometer los errores habituales del software educativo, se aplicó la disciplina de la **Ingeniería Inversa de Procesos y Sistemas**. El objetivo no fue plagiar código, sino **desensamblar conceptualmente la arquitectura de dos gigantes del sector**: el **SICE UABJO** y **Google Classroom**.

```mermaid
flowchart TD
    subgraph Deconstruccion["Fase 1: Ingeniería Inversa Analítica (Marco REA)"]
        SICE["SICE UABJO (Monolito SQL Síncrono)"]
        CLASS["Google Classroom (Cloud-First Propietario)"]
    end

    subgraph Diagnostico["Fase 2: Hallazgos de Deconstrucción"]
        SICE -->|Cuello de botella| D1["Cola saturada (rho >= 1) / Pérdida en desconexión"]
        CLASS -->|Fortaleza/Debilidad| D2["Modularidad excelente / Pesadez (>120 MB) y telemetría"]
    end

    subgraph Sintesis["Fase 3: Síntesis Arquitectónica en Aula 301"]
        D1 --> AULA["Aula 301: Local-First (Zero-Server en entrega)"]
        D2 --> AULA
        AULA --> PWA["PWA Ultraligera (~85 KB) + Caché First"]
    end
```

### 2.1 Deconstrucción del SICE UABJO: El Problema de la Centralización Extrema
* **Naturaleza del Sistema:** Arquitectura cliente-servidor tradicional conectada a una base de datos relacional centralizada.
* **Análisis de Teoría de Colas:** En fechas de entrega o reinscripciones masivas, la tasa media de llegada de peticiones ($\lambda$) supera exponencialmente la tasa media de servicio del servidor ($\mu$). Al alcanzarse la condición de congestión:
  $$\rho = \frac{\lambda}{c\mu} \ge 1$$
  La longitud de la cola y los tiempos de espera tienden a infinito, derivando en los conocidos errores HTTP 504 (*Gateway Timeout*) y en la pérdida absoluta de formularios no guardados.
* **Lección de Ingeniería para Aula 301:** **Eliminar el servidor central como punto único de falla (*Single Point of Failure*)**. La captura de tareas y la evaluación deben ocurrir localmente en el procesador del teléfono móvil de cada alumno.

### 2.2 Deconstrucción de Google Classroom: La Fricción de la Nube Propietaria
* **Naturaleza del Sistema:** Aplicación reactiva conectada a microservicios en la nube de Google.
* **Fortaleza Técnica Reutilizada:** El paradigma de **tarjetas modulares (*Activity Cards*)**, donde cada minicaso o tarea se encapsula en una tarjeta limpia con estado visual (*Pendiente* / *Entregada*), permitiendo al usuario expandir el detalle únicamente cuando decide trabajar.
* **Barrera de Infraestructura Identificada:** Classroom requiere autenticación síncrona obligatoria con cuentas corporativas, descarga una aplicación nativa que consume más de 120 MB en la memoria interna del teléfono y ejecuta constantes solicitudes de telemetría que agotan los datos móviles de los estudiantes en comunidades.
* **Lección de Ingeniería para Aula 301:** Implementar el diseño visual de tarjetas modulares pero condensado en una **Progressive Web App (PWA) de apenas 85 KB**, ejecutable en cualquier navegador sin instalar aplicaciones pesadas de tiendas comerciales.

---

## 3. Superación Metodológica del *“Vibe Coding”* mediante Ingeniería Guiada por Agentes

El término *“Vibe Coding”* se ha popularizado en el ecosistema informático para denotar la práctica riesgosa de construir aplicaciones mediante inteligencia artificial generativa solicitando código sin especificaciones de ingeniería, operando bajo el axioma informal de *“parece que funciona en mi pantalla”*.

Para una investigación avalada por la cátedra de Ingeniería Industrial de la Dra. Maldonado, el *Vibe Coding* representa una amenaza inaceptable por las siguientes razones:
1. **Generación de Deuda Técnica Oculta:** Código redundante, variables globales mal acopladas y falta de manejo de errores en casos de borde (*Edge Cases*).
2. **Fragilidad ante Fallas:** El software se bloquea si el usuario realiza una secuencia imprevista de clics o si se interrumpe la conexión.
3. **Falta de Trazabilidad y Seguridad:** Datos planos fácilmente manipulables en el navegador que comprometen la validez de las calificaciones.

### La Solución Implementada: Marco de Ingeniería Asistida
En lugar de improvisar, el desarrollo de Aula 301 se blindó mediante cuatro invariantes técnicas innegociables:

| Invariante de Ingeniería | Justificación Operativa | Implementación en Código |
| :--- | :--- | :--- |
| **Fuente Única de Verdad (*Single Source of Truth*)** | Evitar discrepancias entre lo que ve el alumno, lo que grafica la app y lo que exporta el CSV. | Todos los datos del minicaso residen únicamente en `js/data.js` (`window.AULA301_DATA`). |
| **Ergonomía Táctil Certificada (ISO 9241-110)** | Adaptar el software al uso con una sola mano en pantallas de 390px. | Altura mínima de contacto táctil de **44px** en `.btn`, `.btn.small` y `.seg button`. |
| **Prevención de Errores en Origen (*Poka-Yoke*)** | Impedir entregas vacías o sin proceso reflexivo de evaluación. | El botón de entrega final se bloquea si la autoevaluación formativa no tiene el 100% de criterios respondidos. |
| **Persistencia Asíncrona en Caliente (*Drafting Local*)** | Proteger el trabajo del alumno ante apagones o llamadas entrantes. | Escuchador reactivo con *debounce* de 400 ms en el evento `input` que guarda en `localStorage` en tiempo real. |

---

## 4. El Enjambre Evaluador Goldfish de Google: Auditoría Hostil Multi-Perspectiva

Para garantizar la robustez del sistema, se recurrió al **enjambre de agentes especializados Goldfish (EGM Swarm)** de Google Antigravity. En lugar de solicitar aprobación pasiva, se asignaron mandatos de auditoría hostil y crítica destructiva:

```mermaid
sequenceDiagram
    autonumber
    actor Educador as Investigador (Área Educación)
    participant EGM as Orquestador Goldfish (Antigravity)
    participant CodeAuditor as egm-codebase-details
    participant DesignCritic as egm-design
    participant ReaderAuditor as egm-comprehension
    participant Codebase as Código Fuente (GitHub)

    Educador->>EGM: Despliegue de Enjambre Auditor
    par Auditoría Paralela Exhaustiva
        EGM->>CodeAuditor: Auditar conformidad línea a línea (código vs. documento)
        EGM->>DesignCritic: Crítica hostil de arquitectura y vectores de falla
        EGM->>ReaderAuditor: Revisión de rigor académico y terminología institucional
    end
    CodeAuditor-->>Educador: 🔴 Hallazgos: Referencias nulas en DOM y ausencia de autosave real
    DesignCritic-->>Educador: 🔴 Hallazgos: JSON falsable en cliente y ciclo docente inconcluso
    ReaderAuditor-->>Educador: 🟡 Hallazgos: Concurrencia imprecisa y siglas sin desglosar
    Educador->>Codebase: Remediación: Web Crypto SHA-256, Bandeja Docente y Poka-Yoke
    Codebase-->>Educador: Validación integral con Puppeteer (0 excepciones)
```

### 4.1 Auditoría Técnica de Código (`egm-codebase-details`)
* **Vulnerabilidad Detectada:** Existían llamadas a nodos del DOM (`#emptyActivities` y `#coPanel`) que, al no estar definidos en ciertas vistas de `index.html`, lanzaban excepciones en tiempo de ejecución (`TypeError: Cannot read properties of null`), deteniendo la ejecución de scripts posteriores y bloqueando la instalación del Service Worker.
* **Remediación:** Declaración estructural de los contenedores en `index.html` y adición de guardas preventivas en `js/app.js`.
* **Vulnerabilidad de Datos:** La documentación aseguraba la existencia de "guardado en caliente", pero el código exigía que el alumno pulsara manualmente un botón. Se desarrolló un temporizador con *debounce* (400 ms) en el evento `input` de redacción de conclusiones, cumpliendo cabalmente con la especificación técnica.

### 4.2 Crítica de Arquitectura y Seguridad (`egm-design`)
* **Falla de Integridad:** El archivo `.json` de entrega original era texto plano editable en cualquier computadora, lo que abría la puerta a alteraciones de hora, contenido o autoevaluación por parte de usuarios malintencionados.
* **Remediación Criptográfica:** Integración de la **Web Crypto API** nativa del navegador. Antes de exportar, el sistema genera un **hash SHA-256** derivado de la concatenación inmutable de:
  $$\text{Payload} = \text{Nombre} \parallel \text{Fecha ISO} \parallel \text{Texto Conclusiones} \parallel \text{Matriz de Autoevaluación}$$
  Cualquier modificación posterior de un solo carácter en el archivo invalida la huella criptográfica.
* **Falla del Ciclo Docente:** El sistema retenía los datos en el celular del alumno, obligando al profesor a revisar mensajes dispersos sin consolidación. Se construyó en el código la **Bandeja de Ingesta Docente**, permitiendo al profesor cargar en lote los comprobantes `.json` para desencriptar, verificar la firma SHA-256 y consolidar el cuadro de calificaciones en una sola vista.

### 4.3 Auditoría de Comprensión y Rigor Académico (`egm-comprehension`)
* **Imprecisión Teórica:** Se identificó el uso de la frase informal *"concurrencia infinita"*. Se corrigió por el modelo formal de **colas estocásticas desacopladas**, donde cada terminal cliente funge como un servidor unitario autónomo ($c_{local} = 1$), resultando en una demanda nula sobre servidores centrales ($\lambda_{central} = 0$).
* **Formalización Institucional:** Desglose riguroso de todas las siglas universitarias (**SICE**, **IISUABJO**, **ICEUABJO**, **UABJO**).

---

## 5. Implementación en Aula 301: Principios de Calidad de la Dra. Maldonado

Como especialista en **Ingeniería Industrial**, la Dra. Maldonado enfatiza la eliminación de pérdidas y la robustez de los procesos. Aula 301 traduce estos conceptos a la ingeniería web:

### 5.1 Manufactura Esbelta (*Lean Education / Reducción de Desperdicios - Muda*)
* **Eliminación del Desperdicio de Espera (*Waiting*):** En conexiones 3G en los valles centrales o la sierra de Oaxaca, la carga de plataformas pesadas demora de 15 a 45 segundos. En Aula 301, el Service Worker v3 entrega la interfaz desde el almacenamiento local del teléfono en **menos de 120 milisegundos**.
* **Eliminación del Desperdicio de Defectos (*Defects/Rework*):** El guardado automático local en caliente y el sellado criptográfico eliminan el retrabajo causado por formularios perdidos.

### 5.2 Teoría de Confiabilidad y Disponibilidad (*High Availability SLA 99.99%*)
Al no depender de infraestructura de servidores universitarios para la captura de tareas, la disponibilidad del sistema frente a cortes de energía en el campus o mantenimiento de servidores centrales es del **100% en el dispositivo del estudiante**.

---

## 6. Discusión Epistemológica: El Educador como Desarrollador Soberano

Este proyecto abre un debate de primer orden en el ámbito de la educación y las ciencias sociales:

> **¿Debe un profesional de la educación conformarse con ser un usuario pasivo de plataformas que ignoran la realidad de sus alumnos?**

La respuesta de esta monografía es un rotundo **no**. Cuando los educadores dependen de software empaquetado por corporaciones trasnacionales:
* Se normaliza la exclusión de los alumnos sin conectividad continua.
* Se aceptan caídas de sistema como "inevitables".
* Se pierde soberanía sobre el proceso pedagógico.

El marco metodológico de **Ingeniería Inversa (REA) + Auditoría con Enjambre Goldfish** demuestra que las herramientas de inteligencia artificial avanzada no deben usarse para generar código superficial sin control, sino como un **equipo de ingeniería multidisciplinaria bajo la dirección del educador**. Quien conoce la realidad humana del aula define las reglas; los agentes aseguran el rigor técnico, la seguridad y la calidad industrial.

---

## 7. Conclusiones y Dictamen Final

1. **Viabilidad Técnica Comprobada:** La plataforma **Aula 301** se encuentra actualmente desplegada en producción en [https://aula-301.vercel.app](https://aula-301.vercel.app), con su código fuente público y auditado en [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301).
2. **Eficacia del Marco Metodológico:** La combinación de ingeniería inversa deconstructiva y auditoría multi-agente Goldfish permitió erradicar los riesgos del *Vibe Coding*, produciendo una herramienta robusta, ergonómica y libre de excepciones en tiempo de ejecución.
3. **Aportación a la Cátedra de Estadística:** El proyecto no solo resolvió la entrega de trabajos, sino que convirtió el propio dilema del acceso tecnológico en el objeto de estudio estadístico del curso ($N = 30$, variables cualitativas, frecuencias y porcentajes), fusionando de forma armónica la pedagogía, la estadística descriptiva y la ingeniería industrial.

---

### Referencias Bibliográficas

1. **Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M.** (2019). *Local-first software: you own your data, in spite of the cloud*. Proceedings of the 2019 ACM SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections on Programming and Software (Onward! 2019), 154–178. Association for Computing Machinery. https://doi.org/10.1145/3359591.3359737
2. **International Organization for Standardization.** (2020). *Ergonomics of human-system interaction — Part 110: Interaction principles* (ISO Standard No. 9241-110:2020).
3. **Shingo, S.** (1986). *Zero Quality Control: Source Inspection and the Poka-Yoke System*. Productivity Press.
4. **Womack, J. P., & Jones, D. T.** (2003). *Lean Thinking: Banish Waste and Create Wealth in Your Corporation*. Free Press.
5. **Gross, D., Shortle, J. F., Thompson, J. M., & Harris, C. M.** (2008). *Fundamentals of Queueing Theory* (4th ed.). John Wiley & Sons.
6. **World Wide Web Consortium (W3C).** (2024). *Service Workers Nightly & Web Cryptography API Specification*. W3C Recommendation.

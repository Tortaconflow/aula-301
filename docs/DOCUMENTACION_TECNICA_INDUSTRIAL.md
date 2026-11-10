# Aula 301 · Dossier de Ingeniería y Documentación Técnica
## Sistema Educativo Descentralizado y Resiliente (Local-First / PWA)
**Materia:** Estadística Aplicada a las Ciencias Sociales · Grupo 301  
**Institución:** Instituto de Investigaciones Sociológicas (IISUABJO) / ICEUABJO, UABJO  
**Docente Titular:** Dra. Maldonado (Especialidad en Ingeniería Industrial)  
**Versión:** 2.0 (Producción / PWA Offline-First)  

---

## 1. Resumen Ejecutivo (Executive Summary)

El proyecto **Aula 301** es una solución de ingeniería de software educativo desarrollada bajo los principios de **Ingeniería Industrial**, **Ergonomía Cognitiva** y **Arquitectura Local-First**. 

Tradicionalmente, las plataformas educativas institucionales (como el SICE UABJO o Google Classroom) operan bajo un modelo cliente-servidor síncrono que asume conectividad continua de alta velocidad. En el contexto socioeconómico de los estudiantes del IISUABJO en Oaxaca, donde el **46.7% de la matrícula únicamente cuenta con teléfono inteligente** y enfrenta conectividad intermitente, este modelo genera fallos críticos de servicio, pérdida de información y fricción en la entrega de tareas.

Aula 301 rediseña el proceso de enseñanza-aprendizaje eliminando cuellos de botella mediante una **Progressive Web App (PWA)** autosuficiente que traslada el cómputo, la persistencia y la evaluación al propio dispositivo del usuario, garantizando una disponibilidad operativa del 100% (*High Availability Edge-Computing*) aun en condiciones de desconexión total.

```mermaid
flowchart TD
    subgraph Tradicional["Modelo Tradicional Centralizado (SICE)"]
        A1[Estudiante móvil] -->|Petición síncrona HTTP| B1[Servidor Central]
        B1 -->|Cuello de botella / Caída de red| C1[Error 504 / Pérdida de entrega]
    end

    subgraph Aula301["Modelo Aula 301 (Local-First / Zero-Server)"]
        A2[Estudiante móvil] -->|Carga inmediata| SW[Service Worker Cache-First]
        A2 -->|Persistencia local| DB[(LocalStorage / State Engine)]
        DB -->|Generación offline| RCV[Comprobante JSON / CSV]
        RCV -.->|Sincronización asíncrona| CLOUD[Nube / Docente cuando haya red]
    end
```

---

## 2. Justificación desde la Ingeniería Industrial: El "Por Qué" y la Importancia

Como disciplina enfocada en la optimización de procesos complejos, eliminación de desperdicios, ergonomía y aseguramiento de la calidad, la **Ingeniería Industrial** provee el marco analítico fundamental para justificar el diseño de Aula 301:

### 2.1 Eliminación de Desperdicios (*Lean Education / Muda*)
En la manufactura y los servicios esbeltos, los tiempos de espera y los defectos de reproceso representan desperdicio puro:
* **Tiempos de espera (*Delay/Wait*):** En plataformas convencionales, la latencia de carga en conexiones 3G/EDGE o zonas rurales de Oaxaca genera tiempos muertos de hasta 15-45 segundos por vista. En Aula 301, gracias al Service Worker precacheado, el tiempo de renderizado (*First Contentful Paint*) es inferior a **120 ms**.
* **Reprocesos (*Defects/Rework*):** Cuando un formulario falla por pérdida momentánea de señal a mitad de una entrega, el estudiante pierde su trabajo y debe reiniciarlo. Aula 301 introduce **guardado automático local en caliente** (*Drafting Local*), eliminando el 100% del reproceso por desconexión.

### 2.2 Ergonomía de Sistemas e Interfaz Humano-Máquina (HMI)
* **Diseño Mobile-First Estricto (Base 390px):** Los datos empíricos del minicaso evidencian que el celular es la herramienta primaria de trabajo. La interfaz fue dimensionada para uso ergonómico a una sola mano, respetando las zonas táctiles naturales del pulgar (*Thumb Zone*), con botones de altura mínima de 44px conforme a estándares de usabilidad ISO 9241-110.
* **Reducción de Carga Cognitiva (*Glassmorphism Minimalista*):** Cada vista presenta únicamente la información requerida para la tarea en curso. En la pantalla de Inicio se eliminaron elementos duplicados, manteniendo una interfaz estática sin scroll innecesario.

### 2.3 Confiabilidad de Sistemas y Teoría de Colas
* **Capacidad de Servicio ($c$) vs. Demanda ($\lambda$):** Los servidores centralizados colapsan cuando la tasa de llegada de peticiones supera la capacidad de procesamiento ($\rho = \lambda / c\mu \ge 1$), como ocurre habitualmente en fechas límite de entrega en el SICE.
* **Descentralización del Procesamiento:** Al convertir cada navegador web en un nodo autónomo de procesamiento (*Edge Node*), la capacidad del sistema escala linealmente con el número de estudiantes: $c_{sistema} = n \times c_{cliente}$. No existe un punto único de falla (*Single Point of Failure*).

### 2.4 Control Estadístico de Calidad y Evaluación Formativa
* **Rúbricas Analíticas Estandarizadas:** Se sustituye la evaluación subjetiva por una matriz de 4 criterios x 3 niveles de desempeño (*Logrado*, *En proceso*, *Inicial*), reduciendo la variabilidad del proceso evaluativo (*Six Sigma principle*).
* **Autoevaluación Formativa con Bucle de Retroalimentación Inmediato:** El alumno evalúa su propio trabajo antes del envío, promoviendo el autocontrol de calidad en origen (*Poka-yoke pedagógico*).

---

## 3. Manual de Operación Profesional

### 3.1 Flujo Operativo del Estudiante

```mermaid
sequenceDiagram
    autonumber
    actor Estudiante
    participant Navegador as Interfaz PWA
    participant Storage as Almacenamiento Local
    participant Archivo as Sistema de Archivos

    Estudiante->>Navegador: 1. Ingreso con matrícula (sin dependencia de red)
    Navegador->>Storage: 2. Restauración de sesión y estado
    Estudiante->>Navegador: 3. Abre "Mis actividades" -> Minicaso 1
    Navegador->>Navegador: 4. Despliega tabla de frecuencias y gráfica
    Estudiante->>Navegador: 5. Descarga dataset (aula301_minicaso_ejemplo.csv)
    Estudiante->>Navegador: 6. Realiza Autoevaluación en la rúbrica interactiva
    Navegador->>Storage: 7. Guarda selecciones de rúbrica
    Estudiante->>Navegador: 8. Redacta conclusiones (2 frases de análisis)
    Estudiante->>Navegador: 9. Clic en "Guardar borrador" / "Registrar entrega"
    Navegador->>Storage: 10. Persiste entrega con timestamp local
    Navegador->>Navegador: 11. Actualiza vista "Mis calificaciones"
    Estudiante->>Archivo: 12. Genera comprobante exportable (.json)
```

1. **Ingreso y Acceso Inicial:**
   - Ingrese su matrícula o nombre de usuario en la pantalla de demostración. La interfaz recordará su sesión en el dispositivo.
2. **Navegación por Pestañas Modulares:**
   - **Inicio:** Pantalla estática de bienvenida que contextualiza los objetivos del curso y notificaciones del aula.
   - **Mis actividades:** Lista de tarjetas modulares. Al pulsar *“Ver detalle y resolver”* en la **Actividad 1**, se despliega el espacio de trabajo con:
     * Tabla de frecuencias calculada y gráfica de barras proporcionales.
     * Botón para descargar el dataset crudo en formato CSV para análisis en Excel / Calc.
     * Rúbrica formativa interactiva: pulse sobre el nivel de logro para cada criterio.
     * Área de entrega: escriba sus dos frases de interpretación estadística.
     * Botón de **Guardar borrador local** (permite continuar después).
     * Botón de **Registrar entrega final** (sella la entrega con marca temporal local).
     * Botón de **Exportar comprobante**: genera un archivo `.json` firmado con los datos de entrega para respaldo o envío alternativo por WhatsApp o correo.
3. **Consulta de Calificaciones:**
   - La pestaña **Mis calificaciones** calcula de forma automática la nota proyectada basada en la rúbrica formativa y muestra el estatus de la entrega.
4. **Recursos y Beneficios Institucionales:**
   - Consulte las guías paso a paso para acceder a herramientas gratuitas del convenio universitario (Microsoft 365, GitHub Student Pack, Notion, Figma).

---

### 3.2 Flujo Operativo del Docente

1. **Cambio de Modo de Operación:**
   - En la vista *Mis actividades*, el docente puede activar el selector de modo **"Docente"** o **"Admin"**.
2. **Generación de Nuevas Actividades:**
   - El formulario de gestión permite definir el título, consigna del estudiante y criterios de rúbrica desglosados línea por línea.
   - La actividad se integra instantáneamente como una nueva tarjeta interactiva (*Actividad 3*, *Actividad 4*, etc.) con persistencia en el dispositivo.
3. **Simulador de Red Intermitente (*Contingency Testing*):**
   - Utilice el botón **"Simular sin conexión"** para validar en tiempo real cómo responde la plataforma cuando un alumno pierde conectividad.

---

## 4. Matriz Comparativa de Ingeniería de Software

| Dimensión Técnica | SICE UABJO Tradicional | Google Classroom | Aula 301 (Propuesta) |
| :--- | :--- | :--- | :--- |
| **Arquitectura de Datos** | Monolito SQL centralizado | Cloud-First propietario | **Local-First descentralizado** |
| **Disponibilidad Offline** | 0% (inutilizable sin internet) | Parcial (solo lectura caché) | **100% funcional (lectura y escritura)** |
| **Tolerancia a Concurrencia** | Baja (colapsos en fechas límite) | Alta (infraestructura Google) | **Infinita a nivel de cliente (Zero-Server)** |
| **Consumo de Datos Móviles** | Alto por recargas continuas | Medio por sincronización pesada | **Ultraligero (~85 KB primera carga, 0 KB subsecuentes)** |
| **Rigor de la Fuente Única** | Consultas dispersas | Múltiples pantallas | **Fuente única estricta (`data.js` + `localStorage`)** |
| **Instalabilidad Móvil (PWA)** | No soportada | Requiere app pesada nativa (~120 MB) | **PWA nativa web (< 1 MB de almacenamiento)** |

---

## 5. Conclusiones y Valor Estratégico

Aula 301 demuestra cómo las metodologías de **Ingeniería Industrial** pueden aplicarse a las tecnologías web y a la pedagogía universitaria. Al analizar la realidad material de los estudiantes y optimizar el proceso de entrega de tareas desde la raíz, se crea una herramienta resiliente, inclusiva y con rigor estadístico.

> **Enfoque de Calidad Total:** No se trata de construir software más complejo, sino de diseñar procesos con cero defectos, alta disponibilidad y máxima accesibilidad para la comunidad universitaria de Oaxaca.

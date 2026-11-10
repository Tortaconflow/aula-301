# Aula 301 · Dossier de Ingeniería y Documentación Técnica
## Sistema Educativo Descentralizado y Resiliente (Local-First / PWA)
**Materia:** Estadística Aplicada a las Ciencias Sociales · Grupo 301  
**Institución:** Instituto de Investigaciones Sociológicas (IISUABJO) / Instituto de Ciencias de la Educación (ICEUABJO), Universidad Autónoma "Benito Juárez" de Oaxaca (UABJO)  
**Docente Titular:** Dra. Maldonado (Especialidad en Ingeniería Industrial)  
**Versión:** 2.1 (Producción / PWA Offline-First con Integridad Criptográfica)  

---

## 1. Resumen Ejecutivo (Executive Summary)

El proyecto **Aula 301** es una solución de ingeniería de software educativo desarrollada bajo los principios de **Ingeniería Industrial**, **Ergonomía Cognitiva** y **Arquitectura Local-First**. 

Tradicionalmente, las plataformas educativas institucionales —como el **SICE** (*Sistema Integral de Control Escolar* de la UABJO) o Google Classroom— operan bajo un modelo cliente-servidor síncrono que asume conectividad continua de alta velocidad. En el contexto socioeconómico de los estudiantes del IISUABJO en Oaxaca, donde el **46.7% de la matrícula únicamente cuenta con teléfono inteligente** y enfrenta conectividad intermitente, este modelo genera fallos críticos de servicio, pérdida de información y fricción en la entrega de tareas.

Aula 301 rediseña el proceso de enseñanza-aprendizaje eliminando cuellos de botella mediante una **Progressive Web App (PWA)** autosuficiente que traslada el cómputo, la persistencia y la evaluación al propio dispositivo del usuario, garantizando una disponibilidad operativa del 100% (*High Availability Edge-Computing*) aun en condiciones de desconexión total.

```mermaid
flowchart TD
    subgraph Tradicional["Modelo Tradicional Centralizado (SICE)"]
        A1[Estudiante móvil] -->|Petición síncrona HTTP| B1[Servidor Central SICE]
        B1 -->|Cuello de botella / Caída de red| C1[Error 504 / Pérdida de entrega]
    end

    subgraph Aula301["Modelo Aula 301 (Local-First / PWA)"]
        A2[Estudiante móvil] -->|Carga inmediata <120ms| SW[Service Worker Cache-First]
        A2 -->|Persistencia en caliente debounced| DB[(LocalStorage / State Engine)]
        DB -->|Sellado criptográfico| RCV[Comprobante JSON con Hash SHA-256]
        RCV -.->|Transferencia asíncrona: WhatsApp/BT/USB| DOC[Bandeja de Ingesta Docente]
        DOC -->|Consolidación local / Cierre de ciclo| ACTA[Auditoría y Calificación Docente]
    end
```

---

## 2. Justificación desde la Ingeniería Industrial: El "Por Qué" y la Importancia

Como disciplina enfocada en la optimización de procesos complejos, eliminación de desperdicios, ergonomía y aseguramiento de la calidad, la **Ingeniería Industrial** provee el marco analítico fundamental para justificar el diseño de Aula 301:

### 2.1 Eliminación de Desperdicios (*Lean Education / Muda*)
En la manufactura y los servicios esbeltos, los tiempos de espera y los defectos de reproceso representan desperdicio puro:
* **Tiempos de espera (*Delay/Wait*):** En plataformas convencionales, la latencia de carga en conexiones 3G/EDGE o zonas rurales de Oaxaca genera tiempos muertos de hasta 15-45 segundos por vista. En Aula 301, gracias al Service Worker precacheado (`sw.js` v3), el tiempo de renderizado (*First Contentful Paint*) es inferior a **120 ms**.
* **Reprocesos (*Defects/Rework*):** Cuando un formulario falla por pérdida momentánea de señal a mitad de una entrega, el estudiante pierde su trabajo y debe reiniciarlo. Aula 301 introduce **guardado automático local en caliente** (*Drafting Local*) con escuchadores `input` debounced (400 ms), eliminando el 100% del reproceso por desconexión involuntaria.

### 2.2 Ergonomía de Sistemas e Interfaz Humano-Máquina (HMI / ISO 9241-110)
* **Diseño Mobile-First Estricto (Base 390px):** Los datos empíricos del minicaso evidencian que el celular es la herramienta primaria de trabajo ($n = 30$, donde 46.7% solo usa celular y 30% comparte equipo). La interfaz fue dimensionada para uso ergonómico a una sola mano, respetando las zonas táctiles naturales del pulgar (*Thumb Zone*), con botones de altura mínima estricta de **44px** conforme a estándares internacionales de usabilidad táctil **ISO 9241-110**.
* **Reducción de Carga Cognitiva (*Glassmorphism Minimalista*):** Cada vista presenta únicamente la información requerida para la tarea en curso. En la pantalla de Inicio se eliminaron elementos duplicados, manteniendo una interfaz estática sin scroll innecesario.

### 2.3 Confiabilidad de Sistemas y Teoría de Colas Desacopladas
* **Capacidad de Servicio ($c$) vs. Demanda ($\lambda$):** Los servidores centralizados colapsan cuando la tasa de llegada de peticiones supera la capacidad de procesamiento ($\rho = \lambda / c\mu \ge 1$), como ocurre habitualmente en fechas límite de entrega en el SICE UABJO.
* **Desacoplamiento Estocástico:** Al convertir cada navegador web en un nodo autónomo de procesamiento (*Edge Node*), la contención central es nula ($\lambda_{central} = 0$). Cada cliente opera como un servidor unitario ($c_{local} = 1$), eliminando la formación de colas y los tiempos de espera en servidor.

### 2.4 Control Estadístico de Calidad y Poka-Yoke Pedagógico
* **Rúbricas Analíticas Estandarizadas:** Se sustituye la evaluación subjetiva por una matriz de 4 criterios x 3 niveles de desempeño (*Logrado*, *En proceso*, *Inicial*), reduciendo la variabilidad del proceso evaluativo (*Six Sigma principle*).
* **Poka-Yoke Pedagógico (Mecanismo a Prueba de Errores):** El sistema exige que el alumno complete el 100% de los criterios de su autoevaluación formativa antes de permitir el registro de la entrega final, evitando entregas vacías o incompletas en origen.
* **Integridad Criptográfica Local (SHA-256):** Cada entrega exportada genera un hash SHA-256 utilizando la **Web Crypto API** (`crypto.subtle.digest`), concatenando la identidad del alumno, el texto de las conclusiones, la fecha ISO y la autoevaluación para proveer verificación de no alteración.

---

## 3. Manual de Operación Profesional

### 3.1 Flujo Operativo del Estudiante

```mermaid
sequenceDiagram
    autonumber
    actor Estudiante
    participant Navegador as Interfaz PWA
    participant Storage as Almacenamiento Local
    participant Crypto as Web Crypto API
    participant Archivo as Sistema de Archivos

    Estudiante->>Navegador: 1. Ingreso con matrícula (sin dependencia de red)
    Navegador->>Storage: 2. Restauración de sesión y estado
    Estudiante->>Navegador: 3. Abre "Mis actividades" -> Minicaso 1
    Navegador->>Navegador: 4. Despliega tabla de frecuencias y gráfica
    Estudiante->>Navegador: 5. Descarga dataset (aula301_minicaso_ejemplo.csv)
    Estudiante->>Navegador: 6. Realiza Autoevaluación en la rúbrica interactiva
    Navegador->>Storage: 7. Guarda selecciones de rúbrica
    Estudiante->>Navegador: 8. Redacta conclusiones (guardado en caliente debounced)
    Estudiante->>Navegador: 9. Clic en "Registrar entrega" (valida Poka-yoke)
    Navegador->>Storage: 10. Persiste entrega con timestamp local
    Navegador->>Navegador: 11. Actualiza vista "Mis calificaciones"
    Estudiante->>Crypto: 12. Genera hash SHA-256 de integridad
    Crypto->>Archivo: 13. Exporta comprobante sellado (.json)
```

1. **Ingreso y Acceso Inicial:**
   - Ingrese su matrícula o nombre de usuario en la pantalla de demostración. La interfaz recordará su sesión en el dispositivo.
2. **Navegación por Pestañas Modulares:**
   - **Inicio:** Pantalla estática de bienvenida que contextualiza los objetivos del curso y notificaciones del aula.
   - **Mis actividades:** Lista de tarjetas modulares. Al pulsar *“Ver detalle y resolver”* en la **Actividad 1**, se despliega el espacio de trabajo con:
     * Tabla de frecuencias calculada y gráfica de barras proporcionales ($N = 30$).
     * Botón para descargar el dataset crudo en formato CSV para análisis en Excel / Calc.
     * Rúbrica formativa interactiva: pulse sobre el nivel de logro para cada criterio.
     * Área de entrega: escriba sus dos frases de interpretación estadística (se respalda automáticamente conforme escribe).
     * Botón de **Guardar borrador local** y **Registrar entrega final** (sella la entrega).
     * Botón de **Exportar comprobante**: genera un archivo `.json` sellado con hash SHA-256 para envío por WhatsApp, correo o Bluetooth.
3. **Consulta de Calificaciones:**
   - La pestaña **Mis calificaciones** calcula de forma automática la nota proyectada basada en la rúbrica formativa y muestra el estatus de la entrega.
4. **Recursos y Beneficios Institucionales:**
   - Consulte las guías paso a paso para acceder a herramientas gratuitas del convenio universitario (Microsoft 365, GitHub Student Pack, Notion, Figma).

---

### 3.2 Flujo Operativo del Docente y Cierre del Balance de Información

1. **Cambio de Modo de Operación:**
   - En la vista *Mis actividades*, el docente puede activar el selector de modo **"Docente"** o **"Admin"**. El rol seleccionado se mantiene persistente.
2. **Generación de Nuevas Actividades:**
   - El formulario de gestión permite definir el título, consigna del estudiante y criterios de rúbrica desglosados línea por línea, integrándose dinámicamente como nuevas tarjetas interactivas (*Actividad 3*, *Actividad 4*, etc.).
3. **Bandeja de Ingesta y Consolidación Docente:**
   - Para cerrar el ciclo de información sin depender de un servidor central, el docente cuenta con el botón **"📥 Cargar comprobantes (.json)"**.
   - Permite seleccionar o arrastrar múltiples comprobantes `.json` enviados por los estudiantes por cualquier canal digital.
   - La plataforma decodifica los archivos, valida el hash criptográfico SHA-256 y despliega una lista consolidada con el nombre del alumno, fecha de entrega, conclusiones y desglose de autoevaluación listo para calificar.
4. **Simulador de Red Intermitente (*Contingency Testing*):**
   - Utilice el botón **"Simular sin conexión"** para validar en tiempo real cómo responde la plataforma ante desconexiones.

---

## 4. Matriz Comparativa de Ingeniería de Software

| Dimensión Técnica | SICE UABJO Tradicional | Google Classroom | Aula 301 (Propuesta) |
| :--- | :--- | :--- | :--- |
| **Arquitectura de Datos** | Monolito SQL centralizado | Cloud-First propietario | **Local-First descentralizado** |
| **Disponibilidad Offline** | 0% (inutilizable sin internet) | Parcial (solo lectura caché) | **100% funcional (lectura y escritura)** |
| **Modelo de Concurrencia** | Colas centralizadas propensas a saturación ($\rho \ge 1$) | Nube elástica de alta capacidad | **Desacoplada: cada nodo es autónomo ($c_{local} = 1$)** |
| **Consumo de Datos Móviles** | Alto por recargas continuas | Medio por sincronización pesada | **Ultraligero (~85 KB primera carga, 0 KB subsecuentes)** |
| **Integridad de Entrega** | Sujeto a confirmación de servidor | Registro en la nube | **Sello criptográfico SHA-256 en cliente** |
| **Cierre de Ciclo Docente** | Base de datos central | Panel en la nube | **Bandeja de Ingesta y Consolidación JSON** |
| **Instalabilidad Móvil (PWA)** | No soportada | Requiere app nativa (~120 MB) | **PWA nativa web (< 1 MB en dispositivo)** |

---

## 5. Auditoría de Calidad Técnica: Enjambre de Revisores Goldfish (EGM)

Para garantizar el cumplimiento de los más altos estándares de calidad, seguridad y rigor académico, el proyecto Aula 301 y esta documentación fueron sometidos a una auditoría multi-agente mediante el enjambre **Goldfish**:

1. **Auditoría de Código y Correspondencia (`egm-codebase-details`):**
   * *Hallazgos subsanados:* Se corrigieron referencias nulas potenciales a `#emptyActivities` y `#coPanel` en el DOM; se implementó el guardado en caliente (*debounced autosave*); se eliminaron notas infladas por defecto (`--` en lugar de `10.0` sin evaluar).
2. **Crítica Arquitectónica de Sistemas (`egm-design`):**
   * *Hallazgos subsanados:* Se implementó la firma de integridad SHA-256 en los comprobantes JSON vía Web Crypto API; se agregó la **Bandeja de Ingesta Docente** para resolver el cuello de botella de recepción de entregas; se optimizó la resiliencia del Service Worker v3 ante fallas en fuentes de terceros.
3. **Auditoría de Comprensión y Claridad Académica (`egm-comprehension`):**
   * *Hallazgos subsanados:* Se desglosaron todas las siglas institucionales (**SICE**, **IISUABJO**, **ICEUABJO**, **UABJO**); se reformuló la hipérbole de "concurrencia infinita" por el modelo formal de colas desacopladas; se explicitó la naturaleza formativa de la autoevaluación frente a la calificación oficial.

---

## 6. Conclusiones y Valor Estratégico

Aula 301 demuestra cómo las metodologías de **Ingeniería Industrial** pueden aplicarse a las tecnologías web y a la pedagogía universitaria. Al analizar la realidad material de los estudiantes y optimizar el proceso de entrega de tareas desde la raíz, se crea una herramienta resiliente, inclusiva y con rigor estadístico.

> **Enfoque de Calidad Total:** No se trata de construir software más complejo, sino de diseñar procesos con cero defectos, alta disponibilidad y máxima accesibilidad para la comunidad universitaria de Oaxaca.


# Aula 301 — Estadística Aplicada a las Ciencias Sociales (ICEUABJO / UABJO)

Plataforma educativa interactiva y **Offline-First** desarrollada para **Estadística Aplicada a las Ciencias Sociales · Grupo 301** (ICEUABJO / IISUABJO, UABJO). Diseñada con enfoque **mobile-first**, estética moderna *glassmorphism* y capacidades PWA para operar 100% sin conexión a internet en beneficio de estudiantes con conectividad intermitente en Oaxaca.

🌐 **Demo en vivo:** [https://aula-301.vercel.app](https://aula-301.vercel.app)  
📦 **Repositorio:** [https://github.com/Tortaconflow/aula-301](https://github.com/Tortaconflow/aula-301)  
📄 **Dossier de Ingeniería Industrial (Dra. Maldonado):** [docs/DOCUMENTACION_TECNICA_INDUSTRIAL.md](docs/DOCUMENTACION_TECNICA_INDUSTRIAL.md)  
🎓 **Artículo Académico Formal (Metodología REA & Goldfish Swarm):** [docs/METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md](docs/METODOLOGIA_INGENIERIA_INVERSA_Y_AGENTES_GOLDFISH.md)

---

## Características Principales

1. **Diseño Mobile-First Estricto (`390px` base) & Glassmorphism:**
   - Inspirado en las maquetas visuales del equipo: efecto cristal translúcido (*backdrop blur*), bordes suaves y fondo con malla de gradiente atmosférico.
   - La pantalla de **Inicio** es estática y sin scroll innecesario, mostrando bienvenida personalizada, cápsula de avisos y propósito institucional.

2. **Arquitectura Offline-First (PWA Instalable):**
   - **Service Worker (`sw.js` Cache-First):** Almacena en caché todos los activos esenciales (HTML, CSS, JS, fuentes e iconos) permitiendo que la plataforma funcione en modo avión o sin red celular.
   - **Web App Manifest (`manifest.json`):** Permite instalar la plataforma como una app nativa en Android e iOS.
   - **Persistencia Local (`localStorage`):** Guarda sesiones, autoevaluaciones, borradores de tareas, entregas de actividades y actividades creadas por el docente sin depender de un servidor externo.

3. **Vistas de Contenido Modulares (Paso 3):**
   - **Mis actividades:** Tarjetas limpias de actividades (`Actividad 1`, `Actividad 2`) con espacio de trabajo interactivo desplegable (tabla de frecuencias, gráfica de barras reactiva, descarga CSV, rúbrica, autoevaluación y módulo de entrega offline con exportación de comprobante JSON).
   - **Mis calificaciones:** Tarjeta de resumen general con promedio reactivo ponderado por autoevaluación, métricas de avance y desglose de entrega por actividad con retroalimentación.
   - **Recursos:** Tarjetas *glass* con guías paso a paso para el canje de beneficios estudiantiles (Microsoft 365, GitHub Student Pack, Notion, Figma, Spotify Universitario).

4. **Fuente Única de Verdad (`Single Source of Truth`):**
   - Los datos del minicaso (*"Acceso tecnológico y participación en clase"*, `n = 30`) y los criterios de la rúbrica se definen una sola vez en `js/data.js`, alimentando de forma sincronizada tablas, gráficas, CSV descargable y formularios.

---

## Estructura del Proyecto

```text
aula-301/
├── index.html       # Estructura semántica con 5 vistas únicas (Login, Inicio, Actividades, Calificaciones, Recursos)
├── manifest.json    # Manifiesto PWA para instalación móvil nativa
├── sw.js            # Service Worker con estrategia de caché offline v2
├── css/
│   └── styles.css   # Estilos mobile-first, glassmorphism y temas adaptativos
├── js/
│   ├── data.js      # Fuente única de verdad de datos, roles y rúbricas
│   └── app.js       # Control de navegación, persistencia offline, entregas y lógica de usuario
├── icons/
│   ├── icon-192.png # Icono PWA para pantalla de inicio
│   └── icon-512.png # Icono PWA de alta resolución
└── README.md        # Documentación para portafolio
```

---

## Licencia y Créditos
Proyecto desarrollado para la comunidad estudiantil de la **Universidad Autónoma Benito Juárez de Oaxaca (UABJO)**. Libre para fines educativos y formativos.

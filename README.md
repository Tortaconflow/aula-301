# Aula 301 — Estadística Aplicada a las Ciencias Sociales (ICEUABJO / UABJO)

Modelo funcional ligero (MVP) de plataforma educativa para **Estadística Aplicada a las Ciencias Sociales · Grupo 301** (ICEUABJO / IISUABJO, UABJO), diseñado con enfoque **mobile-first** para estudiantes que acceden principalmente desde teléfono móvil y con conexiones lentas o intermitentes en Oaxaca.

🌐 **Demo en vivo:** [https://aula-301.vercel.app](https://aula-301.vercel.app)

---

## Arquitectura del proyecto

El proyecto separa estructura, estilos y fuente única de datos sin depender de librerías pesadas externas para garantizar carga inmediata:

```text
aula-301/
├── index.html       # Punto de entrada con las 5 vistas únicas (Login, Inicio, Mis actividades, Mis calificaciones, Recursos)
├── css/
│   └── styles.css   # Diseño Mobile-First (base 390px -> tablet -> escritorio) con paleta institucional ICEUABJO
├── js/
│   ├── data.js      # Fuente única de verdad para el minicaso EJEMPLO, criterios de rúbrica y roles
│   └── app.js       # Navegación por vistas, renderizado dinámico, exportación CSV y controles por rol
└── README.md        # Documentación del repositorio
```

## Principios de diseño e invariantes

- **Mobile-First real (`390px` base):** La vista de **Inicio** cabe en una sola pantalla de celular sin scroll vertical ni horizontal, con áreas táctiles cómodas en menú y tarjetas.
- **Una sola fuente de verdad por vista y por dato:**
  - Los datos del minicaso de ejemplo (*"Acceso tecnológico y participación en clase"*, `n = 30`) se definen una sola vez en `js/data.js` y alimentan simultáneamente la tabla HTML, la gráfica de barras y el archivo descargable `.csv`.
  - Los criterios de la rúbrica de ejemplo se definen una sola vez en `js/data.js` y construyen tanto la tabla de rúbrica como el módulo de autoevaluación.
- **Cero dependencias pesadas:** HTML5 semántico, CSS moderno y JavaScript puro (Vanilla JS) pensado para condiciones de baja conectividad.

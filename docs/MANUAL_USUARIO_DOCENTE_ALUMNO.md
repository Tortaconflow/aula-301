# Aula 301 · Manual Integral de Usuario
## Guía Oficial de Operación para Estudiantes y Docentes
**Materia:** Estadística Aplicada a las Ciencias Sociales · Grupo 301  
**Institución:** Instituto de Investigaciones Sociológicas (IISUABJO) / ICEUABJO, UABJO  
**Docente Titular:** Dra. Maldonado  
**Versión de la Plataforma:** 2.1 (PWA Offline-First con Integridad Criptográfica)  

---

# PARTE I: MANUAL PARA EL ESTUDIANTE

## 1. Acceso a la Plataforma e Instalación Móvil (PWA)
1. **Acceso Web:** Abre tu navegador habitual (Chrome, Safari, Firefox o Edge) e ingresa a:  
   👉 [https://aula-301.vercel.app](https://aula-301.vercel.app)
2. **Instalación como App en tu Celular (Sin Play Store):**
   * En **Android (Chrome):** Toca los tres puntos arriba a la derecha y selecciona **"Agregar a la pantalla principal"** o **"Instalar aplicación"**.
   * En **iPhone (Safari):** Toca el botón de Compartir (icono con flecha hacia arriba) y elige **"Agregar al inicio"**.
3. **Inicio de Sesión:**
   * Escribe tu nombre o matrícula (ej. `Carlos Arturo`) y cualquier contraseña temporal (ej. `1234`).
   * Pulsa **"Iniciar sesión"**. Tu sesión se guardará en tu teléfono automáticamente.

---

## 2. Pantalla de Inicio (Navegación Limpia)
* Al ingresar verás tu saludo personalizado (*"Bienvenido/a, Carlos Arturo"*).
* **Barra de Avisos (Megáfono):** Muestra si hay comunicados urgentes del docente.
* **Leyenda Institucional:** Recuerda que Aula 301 es una herramienta creada para garantizar la entrega de tareas y el acceso a beneficios sin consumir datos innecesarios.

---

## 3. Resolución de Actividades y Minicasos de Estadística
1. En la barra superior, pulsa la pestaña **"Mis actividades"**.
2. Verás las tarjetas modulares. En la **Actividad 1 (Minicaso: Acceso tecnológico y participación en clase)**, pulsa **"Ver detalle y resolver"**.
3. Se desplegará tu espacio de trabajo interactivo:
   * **Tabla de frecuencias:** Muestra el número de casos y el porcentaje de alumnos según su dispositivo ($n = 30$).
   * **Gráfica de barras:** Representa visualmente la proporción de cada categoría.
   * **Descargar datos (CSV):** Pulsa este botón si deseas abrir la base de datos en Excel o LibreOffice Calc.

---

## 4. Autoevaluación con Rúbrica y Entrega Offline
1. **Autoevaluación Formativa (*Poka-Yoke*):**
   * Lee la rúbrica de 4 criterios (*Planteamiento, Organización de datos, Interpretación, Comunicación*).
   * En el bloque de autoevaluación, pulsa el nivel de logro que consideras que tiene tu trabajo (*Logrado*, *En proceso*, o *Inicial*).
   * ⚠️ **Importante:** El sistema no te permitirá entregar si dejas criterios sin evaluar.
2. **Redacción de Conclusiones:**
   * Escribe tus dos frases de interpretación estadística sobre el dispositivo dominante.
   * **Guardado en caliente automático:** No te preocupes si se te apaga el celular; la plataforma guarda automáticamente cada letra que escribes en la memoria interna de tu dispositivo.
3. **Registrar Entrega:**
   * Pulsa **"Registrar entrega final"**. El badge de tu tarjeta cambiará inmediatamente a color verde (**Entregada**).
4. **Exportar Comprobante con Huella Digital:**
   * Pulsa **"Exportar comprobante"**. Se descargará un archivo llamado `comprobante_entrega_actividad_1.json`.
   * Este archivo incluye tu nombre, fecha, autoevaluación y un sello de seguridad criptográfico (**Hash SHA-256**) que garantiza que tu tarea no fue alterada.
   * Puedes enviar este archivo pequeño a tu docente por **WhatsApp, correo o Bluetooth** sin necesidad de entrar a ningún sistema pesado.

---

## 5. Consulta de Calificaciones y Recursos
* **Pestaña "Mis calificaciones":** Podrás ver tu promedio formativo proyectado (ej. **10.0**), tus métricas de avance y la retroalimentación de lo que escribiste.
* **Pestaña "Recursos":** Consulta cómo canjear herramientas gratuitas con tu correo universitario (Office 365, GitHub Student Pack, Notion, Figma y Spotify).

---

# PARTE II: MANUAL PARA EL DOCENTE (DRA. MALDONADO)

## 1. Conmutación a Modo Docente / Administrador
1. En la barra superior, dirígete a **"Mis actividades"**.
2. En la barra de selector de rol (*"Modo:"*), pulsa **"Docente"** o **"Admin"**.
3. La interfaz se adaptará para mostrar los paneles exclusivos de gestión académica y recepción de tareas.

---

## 2. Creación de Nuevas Actividades y Tareas
1. En el panel **"+ Crear nueva actividad (Docente)"**:
   * **Título:** Escribe el nombre del minicaso (ej. *Minicaso 3: Distribución del ingreso en hogares*).
   * **Instrucciones:** Redacta qué debe entregar el estudiante y para cuándo.
   * **Rúbrica:** Define los criterios y niveles (un criterio por línea).
2. Pulsa **"+ Publicar actividad"**. La actividad se integrará de inmediato como una nueva tarjeta (*Actividad 3*, etc.) con persistencia local en el dispositivo.
3. **Controles adicionales:** Puedes activar o desactivar la autoevaluación obligatoria y la coevaluación entre pares con los conmutadores táctiles.

---

## 3. Bandeja de Ingesta y Consolidación de Entregas (Recepción JSON)
Dado que los alumnos en comunidades pueden entregar sin conexión a internet enviando su comprobante por WhatsApp o memoria USB:
1. En la vista de actividades como Docente, baja hasta la sección **"Bandeja de Entregas (Consolidación de Comprobantes JSON)"**.
2. Pulsa el botón **"📥 Cargar comprobantes (.json)"**.
3. Selecciona uno o varios archivos `.json` que te hayan compartido los alumnos.
4. **Procesamiento automático:** La plataforma decodificará cada archivo en pantalla mostrando:
   * Nombre completo del estudiante.
   * Fecha y hora exacta de generación.
   * Conclusiones redactadas por el estudiante.
   * Desglose de la autoevaluación por rúbrica.
   * **Verificación de Integridad SHA-256:** Sello criptográfico que comprueba que el archivo no fue manipulado tras su emisión.

---

## 4. Auditoría de Red y Simulación de Contingencias (*Contingency Testing*)
* Pulsa el botón **"Simular sin conexión"** en cualquier momento para comprobar que la interfaz responde con cero latencia y mantiene todas sus capacidades operativas aún con la red desconectada.

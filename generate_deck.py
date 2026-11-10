import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Paleta cromática educativa institucional
    BG_DARK = RGBColor(26, 27, 65)         # Indigo oscuro profundo
    BG_CARD = RGBColor(255, 255, 255)      # Blanco tarjeta
    BG_LIGHT = RGBColor(248, 250, 252)     # Gris slate ultra suave
    TEXT_MAIN = RGBColor(15, 23, 42)       # Texto principal oscuro
    TEXT_MUTED = RGBColor(71, 85, 105)     # Texto secundario / gris
    TEXT_WHITE = RGBColor(255, 255, 255)   # Blanco puro
    TEXT_LILAC = RGBColor(199, 210, 254)   # Lilac suave
    ACCENT_PURPLE = RGBColor(79, 70, 229)  # Púrpura educativo
    ACCENT_GOLD = RGBColor(217, 119, 6)    # Ámbar Oaxaca
    ACCENT_GREEN = RGBColor(16, 185, 129)  # Verde logro DUA
    BORDER_LIGHT = RGBColor(226, 232, 240) # Borde sutil

    CAPTURES_DIR = r"C:\Users\reily\.gemini\antigravity\scratch\aula-301\docs\presentacion\capturas"
    REPO_URL = "https://github.com/Tortaconflow/aula-301"

    def set_slide_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num, total_slides=13):
        # Franja superior o encabezado limpio
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10.5), Inches(0.95))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Categoría / Supertítulo
        p_cat = tf.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.name = "Calibri"
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_PURPLE
        p_cat.space_after = Pt(2)

        # Título principal
        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN

        # Contador de diapositiva
        num_box = slide.shapes.add_textbox(Inches(11.5), Inches(0.4), Inches(1.0), Inches(0.4))
        ntf = num_box.text_frame
        ntf.margin_right = ntf.margin_top = 0
        np = ntf.paragraphs[0]
        np.alignment = PP_ALIGN.RIGHT
        np.text = f"{slide_num:02d} / {total_slides:02d}"
        np.font.name = "Calibri"
        np.font.size = Pt(12)
        np.font.bold = True
        np.font.color.rgb = TEXT_MUTED

    def add_footer(slide):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_bottom = tf.margin_right = 0
        p = tf.paragraphs[0]
        p.text = f"Aula 301 · Adecuación Curricular UCA Estadística Aplicada (IISUABJO) · Repositorio: {REPO_URL}"
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_LIGHT):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: PORTADA
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, BG_DARK)

    # Franja decorativa Oaxaca
    decoline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.1), Inches(11.733), Inches(0.06))
    decoline.fill.solid()
    decoline.fill.fore_color.rgb = ACCENT_GOLD
    decoline.line.fill.background()

    # Caja de Título
    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "CIENCIAS DE LA EDUCACIÓN & DISEÑO UNIVERSAL PARA EL APRENDIZAJE (DUA)"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(12)

    p = tf1.add_paragraph()
    p.text = "Adecuación Curricular Inclusiva y\nMediación Didáctica Situada en Oaxaca"
    p.font.name = "Calibri"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "UCA: Estadística Aplicada a las Ciencias Sociales (Clave DI-EAC-03 · 3er Semestre)\nLicenciatura en Ciencias Sociales y Estudios Políticos — IISUABJO, UABJO"
    p.font.name = "Calibri"
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(224, 231, 255)
    p.space_after = Pt(20)

    # Tarjeta inferior con datos clave
    add_card(s1, Inches(0.8), Inches(5.6), Inches(11.733), Inches(1.3), RGBColor(38, 41, 92), None)
    tb_meta = s1.shapes.add_textbox(Inches(1.0), Inches(5.7), Inches(11.333), Inches(1.1))
    tf_meta = tb_meta.text_frame
    tf_meta.word_wrap = True
    
    p = tf_meta.paragraphs[0]
    p.text = "Docente / Asesoría: Dra. Maldonado  |  Grupo 301 (IISUABJO)  |  Estudiante: Carlos Arturo"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)

    p = tf_meta.add_paragraph()
    p.text = f"Repositorio de Código Abierto y Documentación: {REPO_URL}\nDespliegue Web Gratuito (PWA): https://aula-301.vercel.app  ·  100% Funcional sin Internet"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(199, 210, 254)

    # ==========================================
    # SLIDE 2: DIAGNÓSTICO EN OAXACA & BAP
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2, BG_LIGHT)
    add_header(s2, "Diagnóstico Situado: Las Barreras de Aprendizaje en Oaxaca", "1. Diagnóstico Contextual", 2)
    add_footer(s2)

    # Columna izquierda: Realidad Sociodemográfica Oaxaca (Datos del Drive)
    add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    tb_oax = s2.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf_oax = tb_oax.text_frame
    tf_oax.word_wrap = True

    p = tf_oax.paragraphs[0]
    p.text = "Realidad Sociodemográfica de Oaxaca (INEGI 2024-2026)"
    p.font.name = "Calibri"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    points_oax = [
        ("Pobreza Multidimensional:", " 51.6% en Oaxaca vs. 29.6% nacional (INEGI / CONEVAL)."),
        ("Rezago Educativo:", " 30.5% en Oaxaca frente a 18.6% a escala nacional."),
        ("Informalidad Laboral:", " 79.9% de la población ocupada (1er Trimestre 2026)."),
        ("Diversidad Lingüística:", " 31.2% de la población de 3+ años habla lengua originaria."),
        ("Limitación Tecnológica:", " Estudiantes combinan estudio con trabajo informal y largos trayectos.")
    ]
    for bold_txt, norm_txt in points_oax:
        p = tf_oax.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "• " + bold_txt
        run_b.font.bold = True
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = norm_txt
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = TEXT_MUTED

    # Columna derecha: Cuestionario Grupo 301 & BAP
    add_card(s2, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    tb_bap = s2.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.333), Inches(4.8))
    tf_bap = tb_bap.text_frame
    tf_bap.word_wrap = True

    p = tf_bap.paragraphs[0]
    p.text = "Diagnóstico del Aula 301: BAP Identificadas"
    p.font.name = "Calibri"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    points_bap = [
        ("Brecha de Dispositivos:", " 46.7% solo cuenta con teléfono celular para entregar tareas. Solo 23.3% tiene computadora propia."),
        ("Infraestructura Crítica:", " Las computadoras del aula 'a duras penas arrancan' y la red de CU es intermitente o inexistente."),
        ("BAP Pedagógica:", " Inseguridad y timidez para participar verbalmente; temor al juicio por error."),
        ("Premisa de Educación Inclusiva:", " Las BAP NO están en el estudiante ni en su capacidad; están en la rigidez de los medios y en el entorno didáctico.")
    ]
    for bold_txt, norm_txt in points_bap:
        p = tf_bap.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "• " + bold_txt
        run_b.font.bold = True
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = norm_txt
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 3: FUNDAMENTACIÓN PEDAGÓGICA (DUA & CASOS)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3, BG_LIGHT)
    add_header(s3, "Marco Pedagógico: DUA, Aprendizaje Situado y Estudio de Casos", "2. Fundamentación Educativa", 3)
    add_footer(s3)

    pillars = [
        ("Adecuación No Significativa", "Conserva el rigor curricular", 
         "No recorta contenidos ni disminuye la exigencia académica. Se mantienen los 9 créditos, 144 horas y propósitos formativos, adaptando tiempos, medios y formatos de acceso."),
        ("Diseño Universal (DUA)", "Montoya et al., 2024 / UNESCO",
         "1. Múltiples formas de representación (tabla, gráfica, texto).\n2. Múltiples formas de acción/expresión (móvil, papel, CSV).\n3. Múltiples formas de implicación (casos reales de Oaxaca)."),
        ("Aprendizaje Situado", "Díaz Barriga / López Ocampo (2021)",
         "El conocimiento se construye en interacción con la realidad comunitaria. La estadística deja de ser abstracta (dados y canicas) y aborda el empleo, tecnología y servicios de Oaxaca."),
        ("Estudio de Casos", "Wassermann (1999) / Stake / Yin",
         "Mini casos didácticos delimitados con preguntas críticas. Fomenta el análisis individual, la discusión respetuosa entre pares y el reconocimiento del locus de enunciación.")
    ]

    for i, (title, author, desc) in enumerate(pillars):
        left_pos = Inches(0.8 + i * 2.98)
        add_card(s3, left_pos, Inches(1.5), Inches(2.8), Inches(5.2))
        tb_p = s3.shapes.add_textbox(left_pos + Inches(0.15), Inches(1.65), Inches(2.5), Inches(4.9))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True

        p = tf_p.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(2)

        p = tf_p.add_paragraph()
        p.text = author
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(10)

        p = tf_p.add_paragraph()
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 4: LAS 6 TABLAS CURRICULARES (DEL DRIVE)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4, BG_LIGHT)
    add_header(s4, "Estructura Curricular: Las 6 Tablas de la Propuesta", "3. Diseño Curricular", 4)
    add_footer(s4)

    tables_info = [
        ("Tabla 1: Continuidad", "Clave DI-EAC-03; 3er Semestre; 9 créditos; 144 horas semestrales (4 docentes + 4 independientes semanales). Bases firmes para Estadística Inferencial."),
        ("Tabla 2: Matriz BAP", "Ajustes de acceso y mediación: De solo Excel en aula a alternativas gratuitas offline y papel. De examen punitivo a evaluación formativa."),
        ("Tabla 3: Contenidos Situados", "8 bloques articulados: Conceptos, Métodos, Excel, Tendencia Central, Dispersión, Curva Normal (asimetría oaxaqueña), Muestreo y Apartado Metodológico."),
        ("Tabla 4: Saberes y Evidencias", "Articulación de saberes: Científico/Disciplinar (base ordenada), Cultural/Comunitario (locus de enunciación) y Ético (sin estigmatizar comunidades)."),
        ("Tabla 5: Tres Mini Casos", "1. Acceso tecnológico y participación educativa.\n2. Escolaridad y empleo juvenil (contingencia).\n3. Acceso a servicios básicos (cobertura)."),
        ("Tabla 6: 8 Semanas de Proyecto", "Secuencia gradual: Diagnóstico inicial, formulación de variables, prácticas de tendencia central, dispersión, contraste con curva normal y reporte final.")
    ]

    for idx, (t_title, t_desc) in enumerate(tables_info):
        col = idx % 3
        row = idx // 3
        left_pos = Inches(0.8 + col * 4.0)
        top_pos = Inches(1.5 + row * 2.65)
        
        add_card(s4, left_pos, top_pos, Inches(3.75), Inches(2.4))
        tb_t = s4.shapes.add_textbox(left_pos + Inches(0.18), top_pos + Inches(0.15), Inches(3.4), Inches(2.1))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True

        p = tf_t.paragraphs[0]
        p.text = t_title
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(6)

        p = tf_t.add_paragraph()
        p.text = t_desc
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 5: LA TECNOLOGÍA COMO MEDIACIÓN PEDAGÓGICA
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5, BG_LIGHT)
    add_header(s5, "La Tecnología como Mediación Didáctica (No como Protagonista)", "4. Mediación Tecnológica", 5)
    add_footer(s5)

    # Izquierda: El problema de las plataformas tradicionales
    add_card(s5, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    tb_trad = s5.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf_trad = tb_trad.text_frame
    tf_trad.word_wrap = True

    p = tf_trad.paragraphs[0]
    p.text = "¿Por qué fallan Classroom y SICE en Oaxaca?"
    p.font.name = "Calibri"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38) # Rojo advertencia
    p.space_after = Pt(10)

    points_trad = [
        ("Dependencia de Conectividad Continua:", " Si se cae el internet a mitad de un formulario, se pierde la respuesta y genera frustración."),
        ("Alto Consumo de Datos Móviles:", " Plataformas pesadas con scripts comerciales gastan las recargas de celular de los alumnos."),
        ("Exclusión en Máquinas Lentas:", " Exigen navegadores modernos y alta memoria RAM. En las computadoras del aula que 'a duras penas arrancan', el sistema se congela."),
        ("Opacidad Evaluativa:", " La retroalimentación llega tarde, como una calificación sumativa sin proceso reflexivo.")
    ]
    for bold_txt, norm_txt in points_trad:
        p = tf_trad.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "✗ " + bold_txt
        run_b.font.bold = True
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = norm_txt
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = TEXT_MUTED

    # Derecha: La respuesta pedagógica de Aula 301
    add_card(s5, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    tb_a301 = s5.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.333), Inches(4.8))
    tf_a301 = tb_a301.text_frame
    tf_a301.word_wrap = True

    p = tf_a301.paragraphs[0]
    p.text = "La Respuesta de Aula 301: Mediación DUA Situada"
    p.font.name = "Calibri"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(10)

    points_a301 = [
        ("Arquitectura Local-First:", " Funciona 100% sin internet. El alumno puede redactar, autoevaluarse y consultar rúbricas en modo avión."),
        ("Cero Peso Computacional:", " Construida en HTML5/CSS3 limpio sin librerías pesadas. Carga instantánea incluso en computadoras escolares de 2010."),
        ("Autoguardado Local Reactivo:", " Cada letra pulsada se respalda en el navegador. Si la computadora se apaga de golpe, no se pierde el trabajo."),
        ("Emancipación Tecnológica:", " Código libre en GitHub (Tortaconflow/aula-301) para que cualquier escuela oaxaqueña pueda replicarla gratis.")
    ]
    for bold_txt, norm_txt in points_a301:
        p = tf_a301.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "✓ " + bold_txt
        run_b.font.bold = True
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = norm_txt
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 6: CAPTURAS 1 & 2 - ACCESO ERGONÓMICO
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6, BG_LIGHT)
    add_header(s6, "Evidencia Visual 1: Acceso Ergonómico y Reducción de la Ansiedad", "5. Entorno de Aprendizaje", 6)
    add_footer(s6)

    # Imagen 1: Login
    img1_path = os.path.join(CAPTURES_DIR, "01_login_view.png")
    if os.path.exists(img1_path):
        s6.shapes.add_picture(img1_path, Inches(0.8), Inches(1.5), width=Inches(3.8))
    
    # Imagen 2: Home
    img2_path = os.path.join(CAPTURES_DIR, "02_inicio_home.png")
    if os.path.exists(img2_path):
        s6.shapes.add_picture(img2_path, Inches(4.8), Inches(1.5), width=Inches(3.8))

    # Explicación Pedagógica Derecha
    add_card(s6, Inches(8.8), Inches(1.5), Inches(3.733), Inches(5.2))
    tb_s6 = s6.shapes.add_textbox(Inches(9.0), Inches(1.7), Inches(3.333), Inches(4.8))
    tf_s6 = tb_s6.text_frame
    tf_s6.word_wrap = True

    p = tf_s6.paragraphs[0]
    p.text = "Principios Pedagógicos Visibles"
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    p_items6 = [
        ("Bienvenida Personalizada:", " Saludo cálido 'Que sea un gran semestre', reduciendo la barrera afectiva inicial."),
        ("Navegación sin Sobrecarga:", " Menú claro de 4 opciones: Inicio, Actividades, Calificaciones y Recursos."),
        ("Diseño sin Scroll en Inicio:", " Pensado para pantallas pequeñas de celular y monitores escolares de baja resolución."),
        ("Barra de Avisos Asíncrona:", " La información esencial llega sin necesidad de recargar la página.")
    ]
    for b_t, n_t in p_items6:
        p = tf_s6.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "• " + b_t
        run_b.font.bold = True
        run_b.font.size = Pt(11)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = n_t
        run_n.font.size = Pt(11)
        run_n.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 7: CAPTURAS 3 & 4 - MINI CASOS & WORKSPACE
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7, BG_LIGHT)
    add_header(s7, "Evidencia Visual 2: Metodología de Mini Casos Didácticos", "6. Mediación en el Aula", 7)
    add_footer(s7)

    img3_path = os.path.join(CAPTURES_DIR, "03_actividades_cards.png")
    if os.path.exists(img3_path):
        s7.shapes.add_picture(img3_path, Inches(0.8), Inches(1.5), width=Inches(3.8))

    img4_path = os.path.join(CAPTURES_DIR, "04_workspace_minicaso.png")
    if os.path.exists(img4_path):
        s7.shapes.add_picture(img4_path, Inches(4.8), Inches(1.5), width=Inches(3.8))

    add_card(s7, Inches(8.8), Inches(1.5), Inches(3.733), Inches(5.2))
    tb_s7 = s7.shapes.add_textbox(Inches(9.0), Inches(1.7), Inches(3.333), Inches(4.8))
    tf_s7 = tb_s7.text_frame
    tf_s7.word_wrap = True

    p = tf_s7.paragraphs[0]
    p.text = "Andamiaje del Mini Caso 1"
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    p_items7 = [
        ("Problema Situado (Tabla 5):", " Acceso tecnológico de 30 compañeros del grupo (46.7% solo celular)."),
        ("Múltiple Representación (DUA):", " 1) Tabla numérica de frecuencias y porcentajes.\n2) Gráfica de barras visual.\n3) Archivo descargable en CSV para Excel o libreta."),
        ("Locus de Enunciación:", " Pregunta reflexiva: ¿Qué formato debe solicitar el docente para no excluir a quien solo tiene celular?"),
        ("Despliegue Modular:", " Las tareas no abruman al estudiante; se revelan por semanas.")
    ]
    for b_t, n_t in p_items7:
        p = tf_s7.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "• " + b_t
        run_b.font.bold = True
        run_b.font.size = Pt(11)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = n_t
        run_n.font.size = Pt(11)
        run_n.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 8: EVALUACIÓN FORMATIVA & POKA-YOKE
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8, BG_LIGHT)
    add_header(s8, "Evaluación Formativa, Metacognición y Andamiaje Preventivo", "7. Evaluación Auténtica", 8)
    add_footer(s8)

    ev_cards = [
        ("Rúbrica Transparente desde el Inicio", "Eliminación de la ambigüedad",
         "El estudiante conoce con precisión los criterios de calidad antes de escribir una sola línea. Cuatro criterios clave: Planteamiento, Organización de datos, Interpretación social situada y Comunicación."),
        ("Autoevaluación Obligatoria (Metacognición)", "El estudiante como evaluador de su propio aprendizaje",
         "Antes de entregar, el alumno valora su propio trabajo (Logrado / En proceso / Inicial). Esto fomenta la autorregulación y la conciencia sobre sus propios saberes (Tabla 4)."),
        ("Poka-Yoke Pedagógico (Diseño sin Errores)", "Shigeo Shingo / Ingeniería Industrial al servicio del aula",
         "La plataforma no permite enviar una tarea incompleta o sin autoevaluación. No es un castigo, es un andamiaje preventivo que evita que el alumno repruebe por descuidos mecánicos."),
        ("Respaldo y Seguridad Emocional", "Protección contra imprevistos técnicos",
         "Autoguardado cada 400ms en el navegador. La entrega genera un comprobante descargable con firma de integridad local, dando certeza al alumno de que su esfuerzo está respaldado.")
    ]

    for idx, (c_title, c_sub, c_body) in enumerate(ev_cards):
        col = idx % 2
        row = idx // 2
        left_pos = Inches(0.8 + col * 5.95)
        top_pos = Inches(1.5 + row * 2.65)

        add_card(s8, left_pos, top_pos, Inches(5.75), Inches(2.4))
        tb_e = s8.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(0.15), Inches(5.35), Inches(2.1))
        tf_e = tb_e.text_frame
        tf_e.word_wrap = True

        p = tf_e.paragraphs[0]
        p.text = c_title
        p.font.name = "Calibri"
        p.font.size = Pt(13.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(2)

        p = tf_e.add_paragraph()
        p.text = c_sub
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(6)

        p = tf_e.add_paragraph()
        p.text = c_body
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 9: CAPTURAS 5 & 6 - CALIFICACIONES & DOCENTE
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9, BG_LIGHT)
    add_header(s9, "Evidencia Visual 3: Acompañamiento Docente y Cierre de Ciclo", "8. Evaluación en Acción", 9)
    add_footer(s9)

    img5_path = os.path.join(CAPTURES_DIR, "05_calificaciones_resumen.png")
    if os.path.exists(img5_path):
        s9.shapes.add_picture(img5_path, Inches(0.8), Inches(1.5), width=Inches(3.8))

    img6_path = os.path.join(CAPTURES_DIR, "06_docente_ingesta.png")
    if os.path.exists(img6_path):
        s9.shapes.add_picture(img6_path, Inches(4.8), Inches(1.5), width=Inches(3.8))

    add_card(s9, Inches(8.8), Inches(1.5), Inches(3.733), Inches(5.2))
    tb_s9 = s9.shapes.add_textbox(Inches(9.0), Inches(1.7), Inches(3.333), Inches(4.8))
    tf_s9 = tb_s9.text_frame
    tf_s9.word_wrap = True

    p = tf_s9.paragraphs[0]
    p.text = "El Rol Docente en Aula 301"
    p.font.name = "Calibri"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    p_items9 = [
        ("Consulta Formativa:", " El estudiante monitorea su promedio y avances sin esperar semanas al reporte final."),
        ("Bandeja de Ingesta Docente:", " El profesor recibe comprobantes por WhatsApp, correo o memoria USB y los arrastra al panel."),
        ("Consolidación sin Servidor Central:", " La plataforma lee y verifica automáticamente los comprobantes locales."),
        ("Cierre de Ciclo de Información:", " Garantiza que ningún alumno se quede atrás por falta de internet en su hogar.")
    ]
    for b_t, n_t in p_items9:
        p = tf_s9.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "• " + b_t
        run_b.font.bold = True
        run_b.font.size = Pt(11)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = n_t
        run_n.font.size = Pt(11)
        run_n.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 10: ¿CÓMO SE ATREVE UN EDUCADOR A CREAR SOFTWARE?
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10, BG_LIGHT)
    add_header(s10, "¿Cómo un Educador se Atreve a Crear Software? La IA como Taller", "9. Democratización Tecnológica", 10)
    add_footer(s10)

    # Izquierda: El riesgo del Vibe Coding
    add_card(s10, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))
    tb_vibe = s10.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf_vibe = tb_vibe.text_frame
    tf_vibe.word_wrap = True

    p = tf_vibe.paragraphs[0]
    p.text = "El Riesgo del 'Vibe Coding' en Educación"
    p.font.name = "Calibri"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)
    p.space_after = Pt(10)

    points_v = [
        ("¿Qué es?", " Programar a tientas pidiendo cosas a un chat sin diseño pedagógico ni control de arquitectura."),
        ("Consecuencias:", " Código pesado, plagado de librerías innecesarias que saturan los celulares."),
        ("Inestabilidad:", " Funciona bien en la computadora nueva del docente, pero en el aula de Oaxaca con computadoras lentas simplemente colapsa."),
        ("Falsa Ilusión:", " Pareciera que 'ya hay app', pero pedagógicamente es inaccesible y excluyente.")
    ]
    for b_t, n_t in points_v:
        p = tf_vibe.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "✗ " + b_t
        run_b.font.bold = True
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = n_t
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = TEXT_MUTED

    # Derecha: La solución con Enjambre Goldfish
    add_card(s10, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.2))
    tb_gold = s10.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.333), Inches(4.8))
    tf_gold = tb_gold.text_frame
    tf_gold.word_wrap = True

    p = tf_gold.paragraphs[0]
    p.text = "Ingeniería Pedagógica Asistida (Goldfish Swarm)"
    p.font.name = "Calibri"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    points_g = [
        ("La Pedagogía Mandó sobre el Código:", " El educador definió las BAP, el DUA y las 6 tablas curriculares; la IA se subordinó a esas reglas."),
        ("Enjambre de 7 Agentes Especialistas:", " Críticos hostiles que auditaron simplicidad, ergonomía táctil (44px) y cero librerías innecesarias."),
        ("Ingeniería Inversa con REA:", " Se tomó la interfaz original soñada por Carlos Arturo y se limpiaron todos los vicios técnicos."),
        ("Resultado Emancipador:", " Un estudiante o docente de educación puede materializar software sostenible y seguro sin depender de un departamento de TI.")
    ]
    for b_t, n_t in points_g:
        p = tf_gold.add_paragraph()
        p.space_after = Pt(8)
        run_b = p.add_run()
        run_b.text = "✓ " + b_t
        run_b.font.bold = True
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = TEXT_MAIN
        run_n = p.add_run()
        run_n.text = n_t
        run_n.font.size = Pt(12)
        run_n.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 11: ¿POR QUÉ CAPTURAS Y NO DEMO EN VIVO?
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11, BG_LIGHT)
    add_header(s11, "Estrategia Didáctica: ¿Por qué Usar Capturas y no Demo en Vivo?", "10. Protocolo de Aula", 11)
    add_footer(s11)

    cards_strat = [
        ("La Realidad del Aula en Oaxaca", "Hardware limitado y fallas de red",
         "En el salón de clases las computadoras 'a duras penas arrancan'. Abrir múltiples pestañas de navegador o depender del Wi-Fi de la escuela es la causa #1 por la que fallan las presentaciones académicas de tecnología."),
        ("El Principio de Certeza Pedagógica", "El contenido debe fluir sin estrés",
         "El objetivo de la sesión no es presumir una conexión a internet, sino presentar y discutir la adecuación curricular. Las capturas garantizan que los 30 compañeros aprecien cada detalle sin interrupciones técnicas."),
        ("El Respaldo Triple de Aula 301", "Cero improvisación frente al grupo",
         "1. Presentación visual autosuficiente (este PowerPoint).\n2. Código auditable y público en GitHub para quien desee revisarlo.\n3. Aplicación PWA instalada localmente como respaldo optativo."),
        ("Lección de Ciencias de la Educación", "La didáctica anticipa contingencias",
         "Un buen diseño educativo prevé los fallos del contexto. Presentar con material estático de alta fidelidad es una decisión pedagógica profesional, no una limitación.")
    ]

    for idx, (c_t, c_s, c_b) in enumerate(cards_strat):
        col = idx % 2
        row = idx // 2
        left_pos = Inches(0.8 + col * 5.95)
        top_pos = Inches(1.5 + row * 2.65)

        add_card(s11, left_pos, top_pos, Inches(5.75), Inches(2.4))
        tb_st = s11.shapes.add_textbox(left_pos + Inches(0.2), top_pos + Inches(0.15), Inches(5.35), Inches(2.1))
        tf_st = tb_st.text_frame
        tf_st.word_wrap = True

        p = tf_st.paragraphs[0]
        p.text = c_t
        p.font.name = "Calibri"
        p.font.size = Pt(13.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(2)

        p = tf_st.add_paragraph()
        p.text = c_s
        p.font.name = "Calibri"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(6)

        p = tf_st.add_paragraph()
        p.text = c_b
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 12: DINÁMICA DE PREGUNTAS CON EL GRUPO
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12, BG_LIGHT)
    add_header(s12, "Dinámica con el Aula: Banco de Preguntas Reflexivas", "11. Interacción Pedagógica", 12)
    add_footer(s12)

    questions = [
        ("Pregunta 1 (Inclusión & DUA):", 
         "Si casi la mitad de nosotros solo tiene celular para estudiar, ¿por qué insistir en formatos cerrados como PDF o plataformas que consumen saldo en vez de herramientas offline?"),
        ("Pregunta 2 (Evaluación Formativa):", 
         "¿En qué te beneficia conocer la rúbrica y autoevaluarte antes de enviar la tarea en lugar de recibir una calificación fría dos semanas después?"),
        ("Pregunta 3 (Locus de Enunciación):", 
         "Al analizar que el 79.9% de Oaxaca labora en la informalidad, ¿podemos juzgar los datos estadísticos sin considerar nuestra propia realidad comunitaria?"),
        ("Pregunta 4 (Democratización):", 
         "¿Cómo cambia nuestra perspectiva al saber que como estudiantes de Ciencias Sociales y Educación podemos diseñar herramientas a la medida de nuestras escuelas?")
    ]

    for idx, (q_num, q_text) in enumerate(questions):
        top_pos = Inches(1.5 + idx * 1.3)
        add_card(s12, Inches(0.8), top_pos, Inches(11.733), Inches(1.15))
        tb_q = s12.shapes.add_textbox(Inches(1.0), top_pos + Inches(0.1), Inches(11.333), Inches(0.95))
        tf_q = tb_q.text_frame
        tf_q.word_wrap = True

        p = tf_q.paragraphs[0]
        p.text = q_num
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(2)

        p = tf_q.add_paragraph()
        p.text = q_text
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # ==========================================
    # SLIDE 13: CONCLUSIONES Y COMPROMISO CON OAXACA
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13, BG_DARK)

    decoline13 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.1), Inches(11.733), Inches(0.06))
    decoline13.fill.solid()
    decoline13.fill.fore_color.rgb = ACCENT_GOLD
    decoline13.line.fill.background()

    tb13 = s13.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(4.2))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    p = tf13.paragraphs[0]
    p.text = "CONCLUSIONES Y COMPROMISO SOCIAL DESDE OAXACA"
    p.font.name = "Calibri"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(10)

    p = tf13.add_paragraph()
    p.text = "La Educación no debe adaptarse al Software;\nel Software debe subordinarse a la Justicia Educativa."
    p.font.name = "Calibri"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(14)

    concl_points = [
        "1. La adecuación curricular no significativa demostró que se puede mantener la máxima exigencia universitaria cuidando la dignidad y las condiciones materiales del alumno.",
        "2. El Diseño Universal para el Aprendizaje (DUA) no es un ideal teórico; en el Aula 301 es una realidad técnica accesible.",
        "3. La Inteligencia Artificial asistida permitió a un estudiante del área educativa crear un entorno seguro, eliminando las barreras del 'vibe coding'.",
        "4. El conocimiento es comunitario: todo el código y la documentación quedan abiertos para la UABJO y para Oaxaca."
    ]
    for cp in concl_points:
        p = tf13.add_paragraph()
        p.text = cp
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.color.rgb = RGBColor(224, 231, 255)
        p.space_after = Pt(6)

    # Tarjeta de cierre
    add_card(s13, Inches(0.8), Inches(5.8), Inches(11.733), Inches(1.1), RGBColor(38, 41, 92), None)
    tb_cierre = s13.shapes.add_textbox(Inches(1.0), Inches(5.9), Inches(11.333), Inches(0.9))
    tf_c = tb_cierre.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.text = f"Repositorio Oficial en GitHub: {REPO_URL}  |  Despliegue: https://aula-301.vercel.app"
    p.font.name = "Calibri"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(4)

    p = tf_c.add_paragraph()
    p.text = "Agradecimiento especial a la Dra. Maldonado y al Instituto de Investigaciones Sociológicas (IISUABJO - UABJO)."
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(199, 210, 254)

    output_path = r"C:\Users\reily\.gemini\antigravity\scratch\aula-301\docs\presentacion\Aula_301_Adecuacion_Curricular_Oaxaca.pptx"
    prs.save(output_path)
    print(f"Presentación generada exitosamente en: {output_path}")

if __name__ == "__main__":
    create_deck()

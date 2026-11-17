import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


def create_student_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    BG_DARK = RGBColor(26, 27, 65)
    BG_CARD = RGBColor(255, 255, 255)
    BG_LIGHT = RGBColor(244, 246, 251)
    TEXT_MAIN = RGBColor(15, 23, 42)
    TEXT_MUTED = RGBColor(51, 65, 85)
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_LILAC = RGBColor(214, 222, 255)
    ACCENT_PURPLE = RGBColor(75, 46, 131)
    ACCENT_GOLD = RGBColor(180, 83, 9)
    ACCENT_GREEN = RGBColor(21, 128, 61)
    BORDER_LIGHT = RGBColor(203, 213, 225)

    FONT_UI = "Arial"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CAPTURES_DIR = os.path.join(BASE_DIR, "docs", "presentacion", "capturas")
    REPO_URL = "https://github.com/Tortaconflow/aula-301"
    WEB_URL = "https://aula-301.vercel.app"
    TOTAL_SLIDES = 9

    def set_slide_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category, slide_num):
        header_box = slide.shapes.add_textbox(Inches(0.65), Inches(0.32), Inches(10.8), Inches(0.95))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.name = FONT_UI
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_PURPLE
        p_cat.space_after = Pt(2)

        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.name = FONT_UI
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN

        num_box = slide.shapes.add_textbox(Inches(11.6), Inches(0.35), Inches(1.08), Inches(0.4))
        ntf = num_box.text_frame
        ntf.margin_right = ntf.margin_top = 0
        np = ntf.paragraphs[0]
        np.alignment = PP_ALIGN.RIGHT
        np.text = f"{slide_num:02d} / {TOTAL_SLIDES:02d}"
        np.font.name = FONT_UI
        np.font.size = Pt(12)
        np.font.bold = True
        np.font.color.rgb = TEXT_MUTED

    def add_footer(slide):
        footer_box = slide.shapes.add_textbox(Inches(0.65), Inches(7.02), Inches(12.03), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_bottom = tf.margin_right = 0
        p = tf.paragraphs[0]
        p.text = f"Aula 301 · IISUABJO, UABJO (Oaxaca) · App: {WEB_URL} · GitHub: {REPO_URL}"
        p.font.name = FONT_UI
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_LIGHT):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.adjustments[0] = 0.04
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()
        return card

    def add_bullets(tf, items, font_size=13, space_after=10):
        for bold_txt, norm_txt in items:
            p = tf.add_paragraph()
            p.space_after = Pt(space_after)
            rb = p.add_run()
            rb.text = bold_txt
            rb.font.name = FONT_UI
            rb.font.bold = True
            rb.font.size = Pt(font_size)
            rb.font.color.rgb = TEXT_MAIN
            rn = p.add_run()
            rn.text = norm_txt
            rn.font.name = FONT_UI
            rn.font.size = Pt(font_size)
            rn.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # LÁMINA 1: PORTADA PARA COMPAÑEROS
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, BG_DARK)

    decoline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.95), Inches(11.73), Inches(0.07))
    decoline.fill.solid()
    decoline.fill.fore_color.rgb = RGBColor(245, 158, 11)
    decoline.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.73), Inches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "PARA EL GRUPO 301 · IISUABJO, UABJO (OAXACA)"
    p.font.name = FONT_UI
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "¿Qué hicimos en Aula 301\ny cómo lo construimos?"
    p.font.name = FONT_UI
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.text = "Una herramienta hecha para nuestra realidad en Estadística Aplicada,\nsin necesitar computadora cara ni gastar saldo de internet."
    p.font.name = FONT_UI
    p.font.size = Pt(17)
    p.font.color.rgb = RGBColor(224, 231, 255)

    add_card(s1, Inches(0.8), Inches(5.5), Inches(11.73), Inches(1.35), RGBColor(38, 41, 92), None)
    tb_m = s1.shapes.add_textbox(Inches(1.05), Inches(5.68), Inches(11.23), Inches(1.0))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    p = tf_m.paragraphs[0]
    p.text = f"Pruébala aquí: {WEB_URL}   |   Código abierto: {REPO_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)
    p = tf_m.add_paragraph()
    p.text = "Estadística Aplicada a las Ciencias Sociales (DI-EAC-03) · Orientación: Dra. Maldonado"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LILAC

    # =========================================================================
    # LÁMINA 2: ¿POR QUÉ LO HICIMOS? (NUESTRA REALIDAD EN OAXACA)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2, BG_LIGHT)
    add_header(s2, "¿Por qué lo hicimos? El problema que todos vivimos en el salón", "1. El punto de partida", 2)
    add_footer(s2)

    add_card(s2, Inches(0.65), Inches(1.4), Inches(5.85), Inches(5.3))
    tb_l2 = s2.shapes.add_textbox(Inches(0.9), Inches(1.6), Inches(5.35), Inches(4.9))
    tf_l2 = tb_l2.text_frame
    tf_l2.word_wrap = True
    p = tf_l2.paragraphs[0]
    p.text = "Lo que pasa en nuestro grupo y en Oaxaca"
    p.font.name = FONT_UI
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(12)

    add_bullets(tf_l2, [
        ("- Casi la mitad solo usa celular (46.7 %): ", "No todos tenemos laptop propia para hacer tareas."),
        ("- El internet falla o cuesta caro: ", "Si se corta la señal en el camión o en CU, se pierde lo que estabas escribiendo."),
        ("- Compus lentas en el aula: ", "Las máquinas de la escuela a duras penas arrancan y se traban con páginas pesadas."),
        ("- Pena al hablar en clase: ", "A veces no participamos por miedo a equivocarnos frente a todos.")
    ], font_size=13, space_after=11)

    add_card(s2, Inches(6.83), Inches(1.4), Inches(5.85), Inches(5.3))
    tb_r2 = s2.shapes.add_textbox(Inches(7.08), Inches(1.6), Inches(5.35), Inches(4.9))
    tf_r2 = tb_r2.text_frame
    tf_r2.word_wrap = True
    p = tf_r2.paragraphs[0]
    p.text = "La idea central de la adecuación"
    p.font.name = FONT_UI
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(12)

    add_bullets(tf_r2, [
        ("- No es bajar el nivel: ", "Seguimos viendo los mismos 8 temas de Estadística y los 9 créditos de la materia."),
        ("- Es quitar estorbos injustos: ", "Que nadie repruebe o se atrase solo por no tener computadora o saldo."),
        ("- Aprender con casos de Oaxaca: ", "En vez de ejercicios aburridos, analizamos nuestro acceso tecnológico, empleo juvenil y servicios básicos.")
    ], font_size=13, space_after=12)

    # =========================================================================
    # LÁMINA 3: ¿QUÉ SE HIZO? (LOS 4 LOGROS PRINCIPALES)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3, BG_LIGHT)
    add_header(s3, "¿Qué se hizo exactamente en el proyecto Aula 301?", "2. Lo que construimos", 3)
    add_footer(s3)

    cards_3 = [
        ("1. Una página ligera sin internet", "Funciona en modo avión o desde USB",
         "La abres una vez y se guarda en tu celular. Puedes leer, analizar datos y escribir tus respuestas sin gastar tus megas."),
        ("2. Los 3 Mini Casos de Oaxaca", "Alineados a las 6 tablas de la materia",
         "1) Acceso tecnológico (n=30 + horas semanales).\n2) Escolaridad y empleo juvenil (tabla 3x2).\n3) Acceso a servicios básicos."),
        ("3. Varias formas de entregar", "Diseño Universal (DUA)",
         "Puedes descargar tu constancia, copiar el texto directo para mandarlo por WhatsApp, o imprimir la hoja para entregarla en libreta."),
        ("4. Guía clara antes de entregar", "Rúbrica y autoevaluación",
         "Ves desde el inicio qué te van a calificar y marcas cómo sientes tu avance antes de enviar, para no olvidar ningún punto.")
    ]

    for idx, (ct, cs, cb) in enumerate(cards_3):
        col = idx % 2
        row = idx // 2
        lx = Inches(0.65 + col * 6.1)
        ty = Inches(1.4 + row * 2.7)
        add_card(s3, lx, ty, Inches(5.9), Inches(2.48))
        tb = s3.shapes.add_textbox(lx + Inches(0.22), ty + Inches(0.18), Inches(5.46), Inches(2.15))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = ct
        p.font.name = FONT_UI
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(3)
        p = tf.add_paragraph()
        p.text = cs
        p.font.name = FONT_UI
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(8)
        p = tf.add_paragraph()
        p.text = cb
        p.font.name = FONT_UI
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 4: ¿CÓMO SE HIZO? (PASO A PASO SIN SER PROGRAMADORES)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4, BG_LIGHT)
    add_header(s4, "¿Cómo se hizo? Paso a paso desde Educación, no desde sistemas", "3. El proceso", 4)
    add_footer(s4)

    steps = [
        ("Paso 1: Partir del salón", "Diagnóstico y 6 Tablas",
         "Primero organizamos las 6 tablas de la adecuación curricular y los datos reales de nuestro grupo en Oaxaca."),
        ("Paso 2: Aprender de lo que ya existe", "Quitar lo que estorba",
         "Vimos qué sirve de Classroom (tarjetas ordenadas) y quitamos lo que falla del SICE (depender de un servidor lento)."),
        ("Paso 3: Mandar sobre la IA", "La pedagogía pone las reglas",
         "Usamos inteligencia artificial como herramienta de apoyo, pero nosotros decidimos qué debía tener: cero peso, sin contraseñas y opción en papel."),
        ("Paso 4: Revisión crítica (Goldfish)", "5 auditores revisaron todo",
         "Un equipo de 5 revisores virtuales buscó fallos: encontraron errores de cálculo en CSV, palabras muy técnicas y capturas viejas, y todo se corrigió.")
    ]

    for i, (st, ss, sb) in enumerate(steps):
        lx = Inches(0.65 + i * 3.08)
        add_card(s4, lx, Inches(1.4), Inches(2.9), Inches(5.3))
        tb = s4.shapes.add_textbox(lx + Inches(0.18), Inches(1.6), Inches(2.54), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st
        p.font.name = FONT_UI
        p.font.size = Pt(14.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(4)
        p = tf.add_paragraph()
        p.text = ss
        p.font.name = FONT_UI
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(10)
        p = tf.add_paragraph()
        p.text = sb
        p.font.name = FONT_UI
        p.font.size = Pt(12.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 5: ASÍ SE ENTRA Y ASÍ SE VEN LOS 3 MINI CASOS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5, BG_LIGHT)
    add_header(s5, "Así se usa: Entras con tu matrícula y eliges tu Minicaso", "4. Recorrido rápido", 5)
    add_footer(s5)

    p1 = os.path.join(CAPTURES_DIR, "01_login_view.png")
    p3 = os.path.join(CAPTURES_DIR, "03_actividades_cards.png")
    if os.path.exists(p1):
        add_card(s5, Inches(0.65), Inches(1.38), Inches(5.7), Inches(4.25))
        s5.shapes.add_picture(p1, Inches(0.75), Inches(1.45), height=Inches(4.1))
    if os.path.exists(p3):
        add_card(s5, Inches(6.98), Inches(1.38), Inches(5.7), Inches(4.25))
        s5.shapes.add_picture(p3, Inches(7.08), Inches(1.45), height=Inches(4.1))

    add_card(s5, Inches(0.65), Inches(5.78), Inches(12.03), Inches(1.1))
    tb5 = s5.shapes.add_textbox(Inches(0.85), Inches(5.88), Inches(11.63), Inches(0.9))
    tf5 = tb5.text_frame
    tf5.word_wrap = True
    p = tf5.paragraphs[0]
    p.text = "• Izquierda: Sin contraseñas difíciles. Pones tu matrícula y nombre; si estás en compu prestada, marcas la casilla para borrar tus datos al salir.\n• Derecha: Ves los 3 Mini Casos de la materia listos para abrir y resolver."
    p.font.name = FONT_UI
    p.font.size = Pt(12.5)
    p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 6: ASÍ TRABAJAS UN MINICASO (TABLA, GRÁFICA Y EXCEL/PAPEL)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6, BG_LIGHT)
    add_header(s6, "Dentro del Minicaso: Datos claros, gráfica y opción en papel", "5. Espacio de trabajo", 6)
    add_footer(s6)

    p4 = os.path.join(CAPTURES_DIR, "04_workspace_minicaso.png")
    if os.path.exists(p4):
        add_card(s6, Inches(0.65), Inches(1.38), Inches(7.15), Inches(5.4))
        s6.shapes.add_picture(p4, Inches(0.75), Inches(1.46), height=Inches(5.22))

    add_card(s6, Inches(8.05), Inches(1.38), Inches(4.63), Inches(5.4))
    tb6 = s6.shapes.add_textbox(Inches(8.25), Inches(1.6), Inches(4.23), Inches(5.0))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    p = tf6.paragraphs[0]
    p.text = "¿Qué puedes hacer aquí?"
    p.font.name = FONT_UI
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(12)

    add_bullets(tf6, [
        ("1. Ver tabla y gráfica: ", "Ya vienen ordenadas para entender rápido el caso."),
        ("2. Bajar para Excel/Calc: ", "Descarga los datos con un clic para tus prácticas de clase."),
        ("3. Imprimir si prefieres papel: ", "Saca una hoja limpia para contestar en tu libreta."),
        ("4. Pensar desde Oaxaca: ", "Una pregunta guía te ayuda a reflexionar desde tu propia realidad.")
    ], font_size=12.5, space_after=10)

    # =========================================================================
    # LÁMINA 7: TU AUTOEVALUACIÓN Y TU ENTREGA SEGURA
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7, BG_LIGHT)
    add_header(s7, "Autoevaluación y entrega: sin miedo a perder tu tarea", "6. Evaluación y entrega", 7)
    add_footer(s7)

    p5 = os.path.join(CAPTURES_DIR, "05_calificaciones_resumen.png")
    if os.path.exists(p5):
        add_card(s7, Inches(0.65), Inches(1.38), Inches(7.15), Inches(5.4))
        s7.shapes.add_picture(p5, Inches(0.75), Inches(1.46), height=Inches(5.22))

    add_card(s7, Inches(8.05), Inches(1.38), Inches(4.63), Inches(5.4))
    tb7 = s7.shapes.add_textbox(Inches(8.25), Inches(1.6), Inches(4.23), Inches(5.0))
    tf7 = tb7.text_frame
    tf7.word_wrap = True
    p = tf7.paragraphs[0]
    p.text = "Ventajas para ti"
    p.font.name = FONT_UI
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(12)

    add_bullets(tf7, [
        ("Se guarda solo: ", "Cada palabra que escribes se respalda al instante en tu cel."),
        ("Revisión previa: ", "Te recuerda valorar los 4 criterios de la rúbrica antes de entregar."),
        ("Manda por WhatsApp o USB: ", "Copia tu constancia con un botón o descarga el archivo con tu matrícula."),
        ("Estimación clara: ", "Te da una idea orientativa, pero la calificación final siempre es de tu docente.")
    ], font_size=12.5, space_after=10)

    # =========================================================================
    # LÁMINA 8: CÓMO RECIBE EL DOCENTE TODO (DIGITAL Y LIBRETA)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8, BG_LIGHT)
    add_header(s8, "Y el docente, ¿cómo recibe las tareas sin internet?", "7. Cierre con el docente", 8)
    add_footer(s8)

    p6 = os.path.join(CAPTURES_DIR, "06_docente_ingesta.png")
    if os.path.exists(p6):
        add_card(s8, Inches(0.65), Inches(1.38), Inches(7.15), Inches(5.4))
        s8.shapes.add_picture(p6, Inches(0.75), Inches(1.46), height=Inches(5.22))

    add_card(s8, Inches(8.05), Inches(1.38), Inches(4.63), Inches(5.4))
    tb8 = s8.shapes.add_textbox(Inches(8.25), Inches(1.6), Inches(4.23), Inches(5.0))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    p = tf8.paragraphs[0]
    p.text = "Nadie se queda fuera"
    p.font.name = FONT_UI
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(12)

    add_bullets(tf8, [
        ("Junta todo en un lugar: ", "Archivos de USB/correo, mensajes de WhatsApp y trabajos hechos en libreta."),
        ("Revisa que esté completo: ", "Confirma automáticamente que tu constancia no se alteró en el camino."),
        ("Pone tu nota y comentarios: ", "Y al final descarga toda la lista del grupo lista para Excel.")
    ], font_size=12.5, space_after=12)

    # =========================================================================
    # LÁMINA 9: CIERRE Y PREGUNTAS PARA EL GRUPO
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9, BG_DARK)

    decoline9 = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.65), Inches(0.85), Inches(12.03), Inches(0.06))
    decoline9.fill.solid()
    decoline9.fill.fore_color.rgb = RGBColor(245, 158, 11)
    decoline9.line.fill.background()

    tb9_t = s9.shapes.add_textbox(Inches(0.65), Inches(1.08), Inches(12.03), Inches(1.2))
    tf9_t = tb9_t.text_frame
    tf9_t.word_wrap = True
    p = tf9_t.paragraphs[0]
    p.text = "PARA PLATICAR EN EL SALÓN"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(4)
    p = tf9_t.add_paragraph()
    p.text = "La tecnología debe adaptarse a nosotros en Oaxaca, no al revés."
    p.font.name = FONT_UI
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    add_card(s9, Inches(0.65), Inches(2.4), Inches(12.03), Inches(2.9), RGBColor(38, 41, 92), None)
    tb9_q = s9.shapes.add_textbox(Inches(0.95), Inches(2.58), Inches(11.43), Inches(2.55))
    tf9_q = tb9_q.text_frame
    tf9_q.word_wrap = True
    p = tf9_q.paragraphs[0]
    p.text = "Preguntas rápidas para ustedes:"
    p.font.name = FONT_UI
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = RGBColor(251, 191, 36)
    p.space_after = Pt(10)

    for q in [
        "1. ¿Qué les parece poder mandar su tarea por WhatsApp o en libreta cuando falla el internet?",
        "2. ¿Les ayuda ver la rúbrica y autoevaluarse antes de entregar?",
        "3. ¿En qué otra materia del IISUABJO nos serviría una herramienta así de ligera?"
    ]:
        p = tf9_q.add_paragraph()
        p.text = q
        p.font.name = FONT_UI
        p.font.size = Pt(14)
        p.font.color.rgb = RGBColor(224, 231, 255)
        p.space_after = Pt(8)

    add_card(s9, Inches(0.65), Inches(5.6), Inches(12.03), Inches(1.25), RGBColor(30, 32, 74), None)
    tb9_f = s9.shapes.add_textbox(Inches(0.95), Inches(5.78), Inches(11.43), Inches(0.9))
    tf9_f = tb9_f.text_frame
    tf9_f.word_wrap = True
    p = tf9_f.paragraphs[0]
    p.text = f"Úsala gratis: {WEB_URL}   |   Código en GitHub: {REPO_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(4)
    p = tf9_f.add_paragraph()
    p.text = "¡Gracias, Grupo 301! (IISUABJO - UABJO, Oaxaca)"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LILAC

    out_path = os.path.join(BASE_DIR, "docs", "presentacion", "Aula_301_Para_Companeros_Que_Se_Hizo_y_Como.pptx")
    prs.save(out_path)
    print(f"Presentación para compañeros generada en: {out_path}")


if __name__ == "__main__":
    create_student_deck()

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

    # Paleta cromática de alto contraste para proyectores VGA y equipos modestos
    BG_DARK = RGBColor(26, 27, 65)          # Índigo oscuro profundo
    BG_CARD = RGBColor(255, 255, 255)       # Blanco limpio
    BG_LIGHT = RGBColor(244, 246, 251)      # Fondo claro descanso visual
    TEXT_MAIN = RGBColor(15, 23, 42)        # Negro pizarra legible
    TEXT_MUTED = RGBColor(51, 65, 85)       # Gris pizarra alto contraste
    TEXT_WHITE = RGBColor(255, 255, 255)    # Blanco
    TEXT_LILAC = RGBColor(214, 222, 255)    # Lila claro sobre fondo oscuro
    ACCENT_PURPLE = RGBColor(75, 46, 131)   # Morado IISUABJO
    ACCENT_GOLD = RGBColor(180, 83, 9)      # Ámbar Oaxaca legible
    ACCENT_GREEN = RGBColor(21, 128, 61)    # Verde logro DUA
    ACCENT_RED = RGBColor(185, 28, 28)      # Rojo alerta contrastado
    BORDER_LIGHT = RGBColor(203, 213, 225)  # Borde visible en proyector

    FONT_UI = "Arial"  # Tipografía universal compatible con Windows antiguo y LibreOffice
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CAPTURES_DIR = os.path.join(BASE_DIR, "docs", "presentacion", "capturas")
    REPO_URL = "https://github.com/Tortaconflow/aula-301"
    WEB_URL = "https://aula-301.vercel.app"
    TOTAL_SLIDES = 13

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
        p_title.font.size = Pt(20)
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
        p.text = f"Aula 301 · Adecuación Curricular Estadística Aplicada (IISUABJO - UABJO) · GitHub: {REPO_URL}"
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

    def add_bullet_list(tf, items, font_size=12.5, space_after=8):
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
    # LÁMINA 1: PORTADA INSTITUCIONAL Y PEDAGÓGICA
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, BG_DARK)

    decoline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.95), Inches(11.73), Inches(0.07))
    decoline.fill.solid()
    decoline.fill.fore_color.rgb = RGBColor(245, 158, 11)
    decoline.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.25), Inches(11.73), Inches(4.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_top = tf1.margin_bottom = 0

    p = tf1.paragraphs[0]
    p.text = "CIENCIAS DE LA EDUCACIÓN · ADECUACIÓN CURRICULAR Y DISEÑO UNIVERSAL (DUA)"
    p.font.name = FONT_UI
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Adecuación Curricular Inclusiva y\nMediación Didáctica Situada en Oaxaca"
    p.font.name = FONT_UI
    p.font.size = Pt(34)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.text = "UCA: Estadística Aplicada a las Ciencias Sociales (Clave DI-EAC-03 · 3er Semestre · 9 créditos)\nLicenciatura en Ciencias Sociales y Estudios Políticos — IISUABJO, UABJO"
    p.font.name = FONT_UI
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(224, 231, 255)

    add_card(s1, Inches(0.8), Inches(5.45), Inches(11.73), Inches(1.45), RGBColor(38, 41, 92), None)
    tb_meta = s1.shapes.add_textbox(Inches(1.05), Inches(5.6), Inches(11.23), Inches(1.15))
    tf_meta = tb_meta.text_frame
    tf_meta.word_wrap = True

    p = tf_meta.paragraphs[0]
    p.text = "Grupo 301 (IISUABJO)  |  Enfoque de calidad formativa: Dra. Maldonado  |  Estudiante modelo: Carlos Arturo"
    p.font.name = FONT_UI
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(8)

    p = tf_meta.add_paragraph()
    p.text = f"Repositorio público en GitHub: {REPO_URL}\nRecurso educativo abierto y gratuito (funciona sin internet): {WEB_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LILAC

    # =========================================================================
    # LÁMINA 2: DIAGNÓSTICO CONTEXTUAL DE OAXACA Y BAP DEL AULA 301
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2, BG_LIGHT)
    add_header(s2, "Diagnóstico Situado: Realidad de Oaxaca y Barreras de Aprendizaje (BAP)", "1. Diagnóstico Contextual", 2)
    add_footer(s2)

    add_card(s2, Inches(0.65), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_oax = s2.shapes.add_textbox(Inches(0.9), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_oax = tb_oax.text_frame
    tf_oax.word_wrap = True

    p = tf_oax.paragraphs[0]
    p.text = "Contexto Sociodemográfico de Oaxaca (INEGI 2024-2026)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    add_bullet_list(tf_oax, [
        ("- Pobreza multidimensional: ", "51.6 % en Oaxaca frente a 29.6 % nacional (INEGI / CONEVAL)."),
        ("- Rezago educativo: ", "30.5 % en la entidad frente a 18.6 % en el promedio del país."),
        ("- Informalidad laboral: ", "79.9 % de la población ocupada (1er Trimestre 2026); muchos alumnos trabajan."),
        ("- Diversidad lingüística: ", "31.2 % de la población de 3 años y más habla una lengua originaria."),
        ("- Movilidad y conectividad: ", "Traslados largos y señal intermitente en Ciudad Universitaria y comunidades.")
    ], font_size=12.5, space_after=9)

    add_card(s2, Inches(6.83), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_bap = s2.shapes.add_textbox(Inches(7.08), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_bap = tb_bap.text_frame
    tf_bap.word_wrap = True

    p = tf_bap.paragraphs[0]
    p.text = "BAP Identificadas en el Grupo 301 (Cuestionario a 13 alumnos)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    add_bullet_list(tf_bap, [
        ("- Brecha de acceso (caso modelo n=30): ", "46.7 % solo cuenta con teléfono celular; 30.0 % comparte equipo familiar; solo 23.3 % tiene PC propia."),
        ("- Equipos escolares modestos: ", "Las computadoras del aula apenas arrancan y la red de internet falla con frecuencia."),
        ("- Barrera afectiva y comunicativa: ", "Timidez o inseguridad para participar en voz alta por temor a equivocarse."),
        ("- Principio de Educación Inclusiva: ", "Las BAP NO residen en el alumno, sino en medios y didácticas rígidas.")
    ], font_size=12.5, space_after=9)

    # =========================================================================
    # LÁMINA 3: FUNDAMENTACIÓN PEDAGÓGICA EN CIENCIAS DE LA EDUCACIÓN
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3, BG_LIGHT)
    add_header(s3, "Marco Pedagógico: Adecuación Curricular, DUA y Aprendizaje Situado", "2. Ciencias de la Educación", 3)
    add_footer(s3)

    pillars = [
        ("Adecuación No Significativa", "Rigor e inclusión (UCA DI-EAC-03)",
         "No recorta contenidos ni baja estándares académicos: conserva intactos los 9 créditos, 144 horas y 8 bloques de Estadística. Ajusta acceso, tiempos, formatos y mediación docente."),
        ("Diseño Universal (DUA)", "Montoya et al. (2024) / UNESCO",
         "1) Múltiples representaciones (tablas, gráficas, glosario y libreta).\n2) Múltiples formas de expresión (celular, PC o entrega en papel).\n3) Implicación genuina mediante problemas reales de Oaxaca."),
        ("Aprendizaje Situado", "Díaz Barriga / López Ocampo (2021)",
         "Abandona ejercicios descontextualizados (dados o canicas). Conecta las variables estadísticas con el acceso educativo, empleo juvenil y servicios comunitarios de Oaxaca."),
        ("Estudio de Casos", "Wassermann (1999) / Stake / Yin",
         "Tres mini casos delimitados con preguntas críticas y trabajo en pares. Favorece la reflexión individual previa para que el alumno participe con seguridad y sin presión oral espontánea.")
    ]

    for idx, (p_title, p_ref, p_desc) in enumerate(pillars):
        col = idx % 2
        row = idx // 2
        lx = Inches(0.65 + col * 6.1)
        ty = Inches(1.38 + row * 2.72)

        add_card(s3, lx, ty, Inches(5.9), Inches(2.5))
        tb = s3.shapes.add_textbox(lx + Inches(0.22), ty + Inches(0.16), Inches(5.46), Inches(2.18))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = p_title
        p.font.name = FONT_UI
        p.font.size = Pt(14.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(2)

        p = tf.add_paragraph()
        p.text = p_ref
        p.font.name = FONT_UI
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = p_desc
        p.font.name = FONT_UI
        p.font.size = Pt(12.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 4: LAS 6 TABLAS CURRICULARES DEL DOCUMENTO OFICIAL
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4, BG_LIGHT)
    add_header(s4, "Matriz Curricular Completa: Las 6 Tablas de la Propuesta", "3. Diseño Curricular", 4)
    add_footer(s4)

    tables_summary = [
        ("Tabla 1: Continuidad", "Conserva Clave DI-EAC-03, 3er semestre, 9 créditos y 144 horas (4 docentes y 4 independientes semanales), dando base a Estadística Inferencial."),
        ("Tabla 2: Matriz BAP y Mediación", "Mantiene el trabajo en Excel y añade alternativas gratuitas, formatos compatibles offline y práctica equivalente en papel o libreta."),
        ("Tabla 3: Contenidos Situados", "Aplica los 8 bloques temáticos (conceptos, gráficas, tendencia central, dispersión, curva normal, muestreo e informe) a preguntas sociales."),
        ("Tabla 4: Saberes de la UCA", "Integra el saber científico-disciplinar, el saber cultural-comunitario (locus de enunciación) y el empírico-ético para el bien común."),
        ("Tabla 5: Tres Mini Casos", "1) Acceso tecnológico y participación educativa.\n2) Escolaridad y empleo juvenil.\n3) Acceso a servicios básicos."),
        ("Tabla 6: Secuencia de 8 Semanas", "Ruta gradual (64 horas de proyecto dentro de las 144 de la UCA): de diagnóstico y variables en Semanas 1-2 hasta informe final en Semana 8.")
    ]

    for idx, (t_head, t_body) in enumerate(tables_summary):
        col = idx % 3
        row = idx // 3
        lx = Inches(0.65 + col * 4.1)
        ty = Inches(1.38 + row * 2.72)

        add_card(s4, lx, ty, Inches(3.88), Inches(2.5))
        tb = s4.shapes.add_textbox(lx + Inches(0.2), ty + Inches(0.16), Inches(3.48), Inches(2.18))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = t_head
        p.font.name = FONT_UI
        p.font.size = Pt(13.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = t_body
        p.font.name = FONT_UI
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 5: TRES SABERES, TRES MINI CASOS Y SECUENCIA DE 8 SEMANAS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5, BG_LIGHT)
    add_header(s5, "Articulación en el Aula: Saberes (T4), Mini Casos (T5) y 8 Semanas (T6)", "4. Concreción Didáctica", 5)
    add_footer(s5)

    # Columna izquierda: 3 Saberes (Tabla 4)
    add_card(s5, Inches(0.65), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_sab = s5.shapes.add_textbox(Inches(0.9), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_sab = tb_sab.text_frame
    tf_sab.word_wrap = True

    p = tf_sab.paragraphs[0]
    p.text = "Tres Saberes del Perfil IISUABJO (Tabla 4)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    add_bullet_list(tf_sab, [
        ("1. Científico y disciplinario: ", "Identifica variables, construye una base ordenada, justifica procedimientos y presenta resultados reproducibles."),
        ("2. Cultural y comunitario: ", "Reconoce su locus de enunciación y contrasta lecturas de los datos con compañeros de distintas identidades culturales."),
        ("3. Empírico y de sentido común: ", "Propone acciones proporcionales a los datos bajo principios éticos, sin divulgar identidades ni estigmatizar comunidades.")
    ], font_size=12.5, space_after=12)

    # Columna derecha: Secuencia 8 Semanas (Tabla 6) + 3 Mini casos (Tabla 5)
    add_card(s5, Inches(6.83), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_sem = s5.shapes.add_textbox(Inches(7.08), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_sem = tb_sem.text_frame
    tf_sem.word_wrap = True

    p = tf_sem.paragraphs[0]
    p.text = "Secuencia de 8 Semanas y Mini Casos (Tablas 5 y 6)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    add_bullet_list(tf_sem, [
        ("Semanas 1 a 3 (Entrada y gráficas): ", "Minicaso 1 (Acceso tecnológico), glosario, ficha de variables y tablas en Excel o LibreOffice."),
        ("Semanas 4 a 6 (Centro, dispersión y curva): ", "Categoría modal vs. media, desviación estándar en horas de conexión y crítica a la simetría ideal de la curva normal."),
        ("Semana 7 (Muestreo y contingencia): ", "Minicaso 2 (Escolaridad y empleo juvenil, tabla 3x2) más diseño breve de instrumento de encuesta."),
        ("Semana 8 (Cierre metodológico): ", "Minicaso 3 (Acceso a servicios básicos), revisión entre pares e informe cuantitativo corregido.")
    ], font_size=12.5, space_after=10)

    # =========================================================================
    # LÁMINA 6: LA TECNOLOGÍA COMO MEDIACIÓN DIDÁCTICA (NO COMO FIN)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6, BG_LIGHT)
    add_header(s6, "La Tecnología como Mediación Didáctica (Al Servicio de la Inclusión)", "5. Mediación Pedagógica", 6)
    add_footer(s6)

    add_card(s6, Inches(0.65), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_fail = s6.shapes.add_textbox(Inches(0.9), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_fail = tb_fail.text_frame
    tf_fail.word_wrap = True

    p = tf_fail.paragraphs[0]
    p.text = "¿Por qué excluyen Classroom y SICE en Oaxaca?"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p.space_after = Pt(10)

    add_bullet_list(tf_fail, [
        ("[X] Conexión obligatoria permanente: ", "Si la señal se corta en el trayecto o en clase, se borra lo escrito y el alumno abandona la entrega."),
        ("[X] Gasto de datos móviles: ", "Las aplicaciones comerciales consumen saldo y memoria que muchos estudiantes de Oaxaca no pueden costear."),
        ("[X] Incompatibilidad con PCs antiguas: ", "En computadoras escolares que apenas arrancan, los sitios pesados se bloquean o congelan la clase."),
        ("[X] Silo escolar sin papel: ", "Dejan fuera a quien necesita trabajar en libreta o con hojas impresas.")
    ], font_size=12.5, space_after=10)

    add_card(s6, Inches(6.83), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_med = s6.shapes.add_textbox(Inches(7.08), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_med = tb_med.text_frame
    tf_med.word_wrap = True

    p = tf_med.paragraphs[0]
    p.text = "Aula 301 como Mediación DUA (Equidad de Acceso)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(10)

    add_bullet_list(tf_med, [
        ("[OK] Trabaja 100 % sin internet: ", "Se abre una vez o directo desde memoria USB y permite estudiar, autoevaluarse y redactar sin red."),
        ("[OK] Cero consumo de datos al estudiar: ", "Resguarda automáticamente el avance en el teléfono o PC para no perder el esfuerzo ante cortes de luz."),
        ("[OK] Ultraligera para equipos modestos: ", "Sin elementos pesados ni dependencias externas; arranca de inmediato en celulares básicos y aulas de Oaxaca."),
        ("[OK] Puente con el papel y libreta: ", "Incluye hoja de trabajo imprimible y registro docente de tareas hechas en cuaderno.")
    ], font_size=12.5, space_after=10)

    # =========================================================================
    # LÁMINA 7: EVIDENCIA VISUAL 1 — ACCESO SIN BARRERAS E INICIO LIMPIO
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7, BG_LIGHT)
    add_header(s7, "Evidencia Visual 1: Acceso Simple y Ambiente Libre de Ansiedad", "6. Entorno de Aprendizaje", 7)
    add_footer(s7)

    p1 = os.path.join(CAPTURES_DIR, "01_login_view.png")
    p2 = os.path.join(CAPTURES_DIR, "02_inicio_home.png")
    if os.path.exists(p1):
        add_card(s7, Inches(0.65), Inches(1.38), Inches(5.7), Inches(4.25))
        s7.shapes.add_picture(p1, Inches(0.75), Inches(1.45), height=Inches(4.1))
    if os.path.exists(p2):
        add_card(s7, Inches(6.98), Inches(1.38), Inches(5.7), Inches(4.25))
        s7.shapes.add_picture(p2, Inches(7.08), Inches(1.45), height=Inches(4.1))

    add_card(s7, Inches(0.65), Inches(5.78), Inches(12.03), Inches(1.1))
    tb_s7 = s7.shapes.add_textbox(Inches(0.85), Inches(5.86), Inches(11.63), Inches(0.95))
    tf_s7 = tb_s7.text_frame
    tf_s7.word_wrap = True
    tf_s7.margin_top = tf_s7.margin_bottom = 0

    p = tf_s7.paragraphs[0]
    p.text = "Lectura Pedagógica de ambas pantallas:"
    p.font.name = FONT_UI
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(3)

    p = tf_s7.add_paragraph()
    p.text = "• Acceso con matrícula y nombre (sin contraseñas olvidadas) más casilla de equipo compartido (30 % del aula) para evitar mezclar borradores.\n• Inicio estático con bienvenida cálida, menú de 5 botones grandes y aviso interactivo del proyecto sin saturar la vista."
    p.font.name = FONT_UI
    p.font.size = Pt(11.8)
    p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 8: EVIDENCIA VISUAL 2 — LOS 3 MINI CASOS Y LAS 6 TABLAS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8, BG_LIGHT)
    add_header(s8, "Evidencia Visual 2: Los 3 Mini Casos y Visor Curricular en Recursos", "7. Estructura Curricular Viva", 8)
    add_footer(s8)

    p3 = os.path.join(CAPTURES_DIR, "03_actividades_cards.png")
    p7 = os.path.join(CAPTURES_DIR, "07_recursos_tablas.png")
    if os.path.exists(p3):
        add_card(s8, Inches(0.65), Inches(1.38), Inches(5.7), Inches(4.25))
        s8.shapes.add_picture(p3, Inches(0.75), Inches(1.45), height=Inches(4.1))
    if os.path.exists(p7):
        add_card(s8, Inches(6.98), Inches(1.38), Inches(5.7), Inches(4.25))
        s8.shapes.add_picture(p7, Inches(7.08), Inches(1.45), height=Inches(4.1))

    add_card(s8, Inches(0.65), Inches(5.78), Inches(12.03), Inches(1.1))
    tb_s8 = s8.shapes.add_textbox(Inches(0.85), Inches(5.86), Inches(11.63), Inches(0.95))
    tf_s8 = tb_s8.text_frame
    tf_s8.word_wrap = True
    tf_s8.margin_top = tf_s8.margin_bottom = 0

    p = tf_s8.paragraphs[0]
    p.text = "Alineación exacta con las Tablas 1 a 6 de la Adecuación Curricular:"
    p.font.name = FONT_UI
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(3)

    p = tf_s8.add_paragraph()
    p.text = "• Izquierda: Los 3 mini casos reales de Tabla 5 (Acceso tecnológico, Escolaridad y empleo juvenil, y Servicios básicos) accesibles en todo momento.\n• Derecha: Pestaña Recursos y Tablas con glosario pedagógico-estadístico, visor de las 6 tablas y enlaces gratuitos (INEGI, CONEVAL, LibreOffice, Redalyc)."
    p.font.name = FONT_UI
    p.font.size = Pt(11.8)
    p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 9: EVIDENCIA VISUAL 3 — ESPACIO DE TRABAJO DEL MINICASO 1 (DUA)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9, BG_LIGHT)
    add_header(s9, "Evidencia Visual 3: Múltiple Representación y Locus de Enunciación", "8. Estudio de Caso en Acción", 9)
    add_footer(s9)

    p4 = os.path.join(CAPTURES_DIR, "04_workspace_minicaso.png")
    if os.path.exists(p4):
        add_card(s9, Inches(0.65), Inches(1.38), Inches(7.15), Inches(5.4))
        s9.shapes.add_picture(p4, Inches(0.75), Inches(1.46), height=Inches(5.22))

    add_card(s9, Inches(8.05), Inches(1.38), Inches(4.63), Inches(5.4))
    tb_s9 = s9.shapes.add_textbox(Inches(8.25), Inches(1.55), Inches(4.23), Inches(5.05))
    tf_s9 = tb_s9.text_frame
    tf_s9.word_wrap = True

    p = tf_s9.paragraphs[0]
    p.text = "Principios DUA Aplicados"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    add_bullet_list(tf_s9, [
        ("1. Representación múltiple: ", "Tabla de frecuencias (46.7 % solo celular), gráfica de barras proporcionales y descarga para Excel o LibreOffice Calc."),
        ("2. Rigor estadístico real: ", "Distingue la variable cualitativa (categoría modal) de las horas de conexión semanales (media 6.20 h, mediana 5.5 h) para Semana 4 y 5."),
        ("3. Opción en papel: ", "Botón directo para imprimir hoja de trabajo legible en blanco y negro."),
        ("4. Locus de enunciación: ", "Glosa accesible que invita al alumno a interpretar los números desde su experiencia en Oaxaca.")
    ], font_size=12, space_after=8)

    # =========================================================================
    # LÁMINA 10: EVALUACIÓN FORMATIVA, METACOGNICIÓN Y PREVENCIÓN DE ERRORES
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10, BG_LIGHT)
    add_header(s10, "Evaluación Formativa, Autoevaluación y Prevención de Errores", "9. Evaluación Auténtica", 10)
    add_footer(s10)

    p5 = os.path.join(CAPTURES_DIR, "05_calificaciones_resumen.png")
    if os.path.exists(p5):
        add_card(s10, Inches(0.65), Inches(1.38), Inches(7.15), Inches(5.4))
        s10.shapes.add_picture(p5, Inches(0.75), Inches(1.46), height=Inches(5.22))

    add_card(s10, Inches(8.05), Inches(1.38), Inches(4.63), Inches(5.4))
    tb_s10 = s10.shapes.add_textbox(Inches(8.25), Inches(1.55), Inches(4.23), Inches(5.05))
    tf_s10 = tb_s10.text_frame
    tf_s10.word_wrap = True

    p = tf_s10.paragraphs[0]
    p.text = "Andamiaje Formativo (Dra. Maldonado)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    add_bullet_list(tf_s10, [
        ("Rúbrica abierta desde el inicio: ", "4 criterios claros (Planteamiento, Organización, Interpretación situada y Comunicación)."),
        ("Autoevaluación previa (Metacognición): ", "Siguiendo el principio preventivo (Poka-Yoke), guía al estudiante a revisar los 4 criterios antes de entregar, evitando olvidos."),
        ("Escala transparente: ", "Muestra estimación orientativa (4.0 / 7.2 / 10.0) aclarando que la nota oficial corresponde al docente."),
        ("Cero pérdidas por corte eléctrico: ", "Guarda el texto al instante y ofrece copia directa para WhatsApp.")
    ], font_size=12, space_after=8)

    # =========================================================================
    # LÁMINA 11: EVIDENCIA VISUAL 4 — RECEPCIÓN DOCENTE DIGITAL Y EN PAPEL
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11, BG_LIGHT)
    add_header(s11, "Evidencia Visual 4: Recepción Docente Integrada (Digital y Libreta DUA)", "10. Acompañamiento Docente", 11)
    add_footer(s11)

    p6 = os.path.join(CAPTURES_DIR, "06_docente_ingesta.png")
    if os.path.exists(p6):
        add_card(s11, Inches(0.65), Inches(1.38), Inches(7.15), Inches(5.4))
        s11.shapes.add_picture(p6, Inches(0.75), Inches(1.46), height=Inches(5.22))

    add_card(s11, Inches(8.05), Inches(1.38), Inches(4.63), Inches(5.4))
    tb_s11 = s11.shapes.add_textbox(Inches(8.25), Inches(1.55), Inches(4.23), Inches(5.05))
    tf_s11 = tb_s11.text_frame
    tf_s11.word_wrap = True

    p = tf_s11.paragraphs[0]
    p.text = "Cierre de Ciclo sin Internet"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    add_bullet_list(tf_s11, [
        ("Recepción flexible (DUA): ", "El docente reúne archivos enviados por WhatsApp o USB, mensajes copiados y trabajos entregados en libreta física."),
        ("Verificación automática amigable: ", "Valida que la constancia digital no haya sufrido alteraciones durante el envío, en lenguaje claro para el maestro."),
        ("Retroalimentación real: ", "Permite asentar calificación y observaciones formativas por alumno."),
        ("Concentrado listo para acta: ", "Exporta todo el grupo en un archivo compatible con Excel y LibreOffice.")
    ], font_size=12, space_after=8)

    # =========================================================================
    # LÁMINA 12: ¿CÓMO UN EDUCADOR DISEÑA HERRAMIENTAS CON IA SIN IMPROVISAR?
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12, BG_LIGHT)
    add_header(s12, "De Usuarios Pasivos a Creadores de Mediaciones Didácticas Situadas", "11. Soberanía Pedagógica", 12)
    add_footer(s12)

    add_card(s12, Inches(0.65), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_l12 = s12.shapes.add_textbox(Inches(0.9), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_l12 = tb_l12.text_frame
    tf_l12.word_wrap = True

    p = tf_l12.paragraphs[0]
    p.text = "El riesgo de usar tecnología sin criterio educativo"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p.space_after = Pt(10)

    add_bullet_list(tf_l12, [
        ("[X] Improvisación superficial ('Vibe Coding'): ", "Pedir una herramienta genérica a una inteligencia artificial sin diagnóstico del aula produce recursos pesados que fallan en Oaxaca."),
        ("[X] Dependencia de especialistas ajenos: ", "Un programador externo rara vez conoce qué es una BAP, el locus de enunciación o que 46.7 % estudia en celular."),
        ("[X] Soluciones frágiles: ", "Se ven bien en computadoras nuevas con internet rápido, pero colapsan en salones universitarios con equipo limitado.")
    ], font_size=12.5, space_after=11)

    add_card(s12, Inches(6.83), Inches(1.38), Inches(5.85), Inches(5.35))
    tb_r12 = s12.shapes.add_textbox(Inches(7.08), Inches(1.55), Inches(5.35), Inches(5.0))
    tf_r12 = tb_r12.text_frame
    tf_r12.word_wrap = True

    p = tf_r12.paragraphs[0]
    p.text = "La Pedagogía Gobierna a la Técnica (Enjambre Goldfish)"
    p.font.name = FONT_UI
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    add_bullet_list(tf_r12, [
        ("[+] El educador define las reglas: ", "Se establecieron primero las 6 tablas de la UCA, principios DUA, accesibilidad en papel y cero dependencias externas."),
        ("[+] Revisión crítica multi-perspectiva: ", "El equipo auditor Goldfish (5 miradas especializadas en código, diseño, claridad pedagógica, estructura y sencillez) corrigió errores estadísticos, tecnicismos y fallos visuales."),
        ("[+] Resultado sostenible: ", "Cualquier docente o estudiante de Ciencias Sociales puede adaptar y sostener la herramienta desde GitHub sin presupuesto costoso.")
    ], font_size=12.5, space_after=11)

    # =========================================================================
    # LÁMINA 13: PROTOCOLO DE AULA, PREGUNTAS AL GRUPO Y CIERRE EN OAXACA
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13, BG_DARK)

    decoline13 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.65), Inches(0.75), Inches(12.03), Inches(0.06))
    decoline13.fill.solid()
    decoline13.fill.fore_color.rgb = RGBColor(245, 158, 11)
    decoline13.line.fill.background()

    tb13_top = s13.shapes.add_textbox(Inches(0.65), Inches(0.92), Inches(12.03), Inches(1.3))
    tf13_top = tb13_top.text_frame
    tf13_top.word_wrap = True
    p = tf13_top.paragraphs[0]
    p.text = "12. ESTRATEGIA SEGURA EN EL AULA Y DIÁLOGO CON EL GRUPO 301"
    p.font.name = FONT_UI
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(4)

    p = tf13_top.add_paragraph()
    p.text = "La Educación no debe adaptarse al Software; el Software debe servir a la Justicia Educativa."
    p.font.name = FONT_UI
    p.font.size = Pt(21)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    # Izquierda: Por qué usamos capturas y no demo en vivo
    add_card(s13, Inches(0.65), Inches(2.25), Inches(5.85), Inches(3.25), RGBColor(38, 41, 92), None)
    tb13_l = s13.shapes.add_textbox(Inches(0.88), Inches(2.4), Inches(5.39), Inches(2.95))
    tf13_l = tb13_l.text_frame
    tf13_l.word_wrap = True
    p = tf13_l.paragraphs[0]
    p.text = "¿Por qué exponemos con capturas estáticas?"
    p.font.name = FONT_UI
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(251, 191, 36)
    p.space_after = Pt(8)

    for line_txt in [
        "• En salones donde la PC 'a duras penas arranca' o no hay red, depender de una demostración en vivo provoca pausas e interrupciones.",
        "• Las capturas reales garantizan fluidez pedagógica ante todo el grupo; la aplicación queda lista en USB o navegador como respaldo.",
        "• Una buena didáctica previene contingencias técnicas del entorno."
    ]:
        p = tf13_l.add_paragraph()
        p.text = line_txt
        p.font.name = FONT_UI
        p.font.size = Pt(12)
        p.font.color.rgb = RGBColor(224, 231, 255)
        p.space_after = Pt(6)

    # Derecha: Preguntas rápidas del Banco para el Grupo 301
    add_card(s13, Inches(6.83), Inches(2.25), Inches(5.85), Inches(3.25), RGBColor(38, 41, 92), None)
    tb13_r = s13.shapes.add_textbox(Inches(7.06), Inches(2.4), Inches(5.39), Inches(2.95))
    tf13_r = tb13_r.text_frame
    tf13_r.word_wrap = True
    p = tf13_r.paragraphs[0]
    p.text = "Preguntas de diálogo para el Grupo 301"
    p.font.name = FONT_UI
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(167, 243, 208)
    p.space_after = Pt(8)

    for q_txt in [
        "1. Si 46.7 % solo tiene celular, ¿es justo exigir tareas en programas pesados de computadora?",
        "2. ¿Qué ventaja tiene autoevaluarte con la rúbrica antes de entregar?",
        "3. Al leer datos de Oaxaca (79.9 % informalidad), ¿por qué evitar estigmatizar?",
        "4. ¿De qué otras materias del IISUABJO adaptarías actividades con este enfoque?"
    ]:
        p = tf13_r.add_paragraph()
        p.text = q_txt
        p.font.name = FONT_UI
        p.font.size = Pt(12)
        p.font.color.rgb = RGBColor(224, 231, 255)
        p.space_after = Pt(5)

    # Banda de cierre GitHub y agradecimientos
    add_card(s13, Inches(0.65), Inches(5.72), Inches(12.03), Inches(1.25), RGBColor(30, 32, 74), None)
    tb13_f = s13.shapes.add_textbox(Inches(0.88), Inches(5.84), Inches(11.57), Inches(1.0))
    tf13_f = tb13_f.text_frame
    tf13_f.word_wrap = True
    p = tf13_f.paragraphs[0]
    p.text = f"Repositorio público en GitHub: {REPO_URL}   |   Plataforma web: {WEB_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)

    p = tf13_f.add_paragraph()
    p.text = "Agradecimiento especial a la Dra. Maldonado, al Instituto de Investigaciones Sociológicas (IISUABJO - UABJO) y a las y los compañeros del Grupo 301 en Oaxaca."
    p.font.name = FONT_UI
    p.font.size = Pt(11.5)
    p.font.color.rgb = TEXT_LILAC

    output_path = os.path.join(BASE_DIR, "docs", "presentacion", "Aula_301_Adecuacion_Curricular_Oaxaca.pptx")
    prs.save(output_path)
    print(f"Presentación regenerada con éxito en: {output_path}")


if __name__ == "__main__":
    create_deck()

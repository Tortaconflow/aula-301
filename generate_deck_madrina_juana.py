import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


def create_madrina_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Paleta cálida y formal acorde al ámbito normalista y Educación Física
    BG_DARK = RGBColor(20, 46, 56)          # Azul petróleo / Costa profundo
    BG_CARD = RGBColor(255, 255, 255)
    BG_LIGHT = RGBColor(244, 248, 249)
    TEXT_MAIN = RGBColor(15, 23, 42)
    TEXT_MUTED = RGBColor(51, 65, 85)
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_SOFT = RGBColor(209, 238, 245)
    ACCENT_TEAL = RGBColor(15, 118, 110)    # Verde azulado normalista
    ACCENT_GOLD = RGBColor(180, 83, 9)      # Ámbar Costa de Oaxaca
    ACCENT_PURPLE = RGBColor(75, 46, 131)   # Referencia MVP Aula 301
    BORDER_LIGHT = RGBColor(203, 213, 225)

    FONT_UI = "Arial"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CAPTURES_DIR = os.path.join(BASE_DIR, "docs", "presentacion", "capturas")
    REPO_URL = "https://github.com/Tortaconflow/aula-301"
    WEB_URL = "https://aula-301.vercel.app"
    TOTAL_SLIDES = 8

    def set_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()

    def add_header(slide, title, cat, num):
        hb = slide.shapes.add_textbox(Inches(0.65), Inches(0.32), Inches(10.8), Inches(0.95))
        tf = hb.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = cat.upper()
        p0.font.name = FONT_UI
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT_TEAL
        p0.space_after = Pt(2)

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.name = FONT_UI
        p1.font.size = Pt(21)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN

        nb = slide.shapes.add_textbox(Inches(11.6), Inches(0.35), Inches(1.08), Inches(0.4))
        np = nb.text_frame.paragraphs[0]
        np.alignment = PP_ALIGN.RIGHT
        np.text = f"{num:02d} / {TOTAL_SLIDES:02d}"
        np.font.name = FONT_UI
        np.font.size = Pt(12)
        np.font.bold = True
        np.font.color.rgb = TEXT_MUTED

    def add_footer(slide):
        fb = slide.shapes.add_textbox(Inches(0.65), Inches(7.02), Inches(12.03), Inches(0.35))
        p = fb.text_frame.paragraphs[0]
        p.text = f"Propuesta Educativa Autónoma (MVP Aula 301) · Normal de Río Grande · GitHub: {REPO_URL}"
        p.font.name = FONT_UI
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MUTED

    def add_card(slide, l, t, w, h, bg=BG_CARD, border=BORDER_LIGHT):
        c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
        c.adjustments[0] = 0.04
        c.fill.solid()
        c.fill.fore_color.rgb = bg
        if border:
            c.line.color.rgb = border
            c.line.width = Pt(1.2)
        else:
            c.line.fill.background()
        return c

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
    # LÁMINA 1: PORTADA PARA LA DRA. JUANA
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, BG_DARK)

    line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.95), Inches(11.73), Inches(0.07))
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(245, 158, 11)
    line.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.73), Inches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "PRESENTACIÓN ESPECIAL · EDUCACIÓN FÍSICA, PRÁCTICA DOCENTE Y TESIS"
    p.font.name = FONT_UI
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_SOFT
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Herramientas Educativas sin Internet\npara el Patio, la Normal y la Titulación"
    p.font.name = FONT_UI
    p.font.size = Pt(34)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.text = "Cómo un proyecto nacido en Oaxaca se convierte en un aliado para la Educación Física,\nlas jornadas de práctica en la Costa y el acompañamiento de tesis."
    p.font.name = FONT_UI
    p.font.size = Pt(16.5)
    p.font.color.rgb = RGBColor(226, 244, 248)

    add_card(s1, Inches(0.8), Inches(5.45), Inches(11.73), Inches(1.4), RGBColor(29, 64, 77), None)
    tbm = s1.shapes.add_textbox(Inches(1.05), Inches(5.65), Inches(11.23), Inches(1.0))
    tfm = tbm.text_frame
    tfm.word_wrap = True
    p = tfm.paragraphs[0]
    p.text = "Dirigido con respeto a: Dra. Juana  |  Educación Física · Escuela Normal de Río Grande, Oaxaca"
    p.font.name = FONT_UI
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)
    p = tfm.add_paragraph()
    p.text = f"Sinodal y Asesora de Tesis  |  Modelo base (MVP): {WEB_URL}  |  GitHub: {REPO_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(11.5)
    p.font.color.rgb = TEXT_SOFT

    # =========================================================================
    # LÁMINA 2: EL PUENTE CON LA EDUCACIÓN FÍSICA EN LA COSTA
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, BG_LIGHT)
    add_header(s2, "Del salón universitario a la cancha de Educación Física en la Costa", "1. Realidad compartida", 2)
    add_footer(s2)

    add_card(s2, Inches(0.65), Inches(1.4), Inches(5.85), Inches(5.3))
    tbl2 = s2.shapes.add_textbox(Inches(0.9), Inches(1.6), Inches(5.35), Inches(4.9))
    tfl2 = tbl2.text_frame
    tfl2.word_wrap = True
    p = tfl2.paragraphs[0]
    p.text = "El problema que usted vive en cancha y escuelas rurales"
    p.font.name = FONT_UI
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(12)

    add_bullets(tfl2, [
        ("- En el patio no hay Wi-Fi ni laptop: ", "El docente y el normalista trabajan bajo el sol, con silbato, libreta y celular en mano."),
        ("- Escuelas de práctica sin señal: ", "En comunidades de Río Grande y la Costa, depender de plataformas en la nube es irreal."),
        ("- Papeles que se pierden o mojan: ", "Listas de cotejo y evaluaciones de desempeño motriz terminan difíciles de concentrar."),
        ("- Diversidad e inclusión (DUA): ", "Cada grupo tiene alumnos con distintos ritmos, lenguas y capacidades físicas.")
    ], font_size=12.5, space_after=10)

    add_card(s2, Inches(6.83), Inches(1.4), Inches(5.85), Inches(5.3))
    tbr2 = s2.shapes.add_textbox(Inches(7.08), Inches(1.6), Inches(5.35), Inches(4.9))
    tfr2 = tbr2.text_frame
    tfr2.word_wrap = True
    p = tfr2.paragraphs[0]
    p.text = "Lo que ya comprobamos con Aula 301"
    p.font.name = FONT_UI
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(12)

    add_bullets(tfr2, [
        ("- Funciona 100 % sin internet: ", "La herramienta vive en el propio celular (ocupa menos que una foto) y no gasta saldo."),
        ("- Hecha para equipos modestos: ", "Corre igual en un celular sencillo, en una compu vieja o impresa en hojas de papel."),
        ("- Modelo replicable (MVP): ", "Ya fue validado en la universidad y nos abrió camino para educación a distancia."),
        ("- La pedagogía manda: ", "No adaptamos la Educación Física al software; creamos el recurso desde la práctica docente.")
    ], font_size=12.5, space_after=10)

    # =========================================================================
    # LÁMINA 3: ¿QUÉ HICIMOS Y CÓMO SE ADAPTA A EDUCACIÓN FÍSICA?
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, BG_LIGHT)
    add_header(s3, "¿Qué es exactamente este proyecto traducido a su disciplina?", "2. Puente pedagógico", 3)
    add_footer(s3)

    translations = [
        ("En lugar de plataformas pesadas...", "Un cuaderno digital ligero de cancha",
         "Sustituye sistemas burocráticos por pantallas limpias con letras grandes y botones cómodos para usar con una sola mano en el patio."),
        ("En lugar de ejercicios abstractos...", "Situaciones reales de práctica docente",
         "Así como allá usamos casos de Oaxaca, en Educación Física se adapta a secuencias didácticas, corporeidad, motricidad y hábitos saludables."),
        ("En lugar de evaluar al final a ciegas...", "Rúbricas y listas de cotejo formativas",
         "El normalista o alumno conoce los criterios desde el inicio, registra su autoevaluación y exporta su evidencia sin red."),
        ("En lugar de perder evidencias...", "Concentrado inmediato por WhatsApp o papel",
         "Al regresar de práctica donde sí hay señal (o por USB/papel), el docente reúne todas las evaluaciones en una sola tabla de Excel.")
    ]

    for i, (t_old, t_new, t_desc) in enumerate(translations):
        col = i % 2
        row = i // 2
        lx = Inches(0.65 + col * 6.1)
        ty = Inches(1.4 + row * 2.7)
        add_card(s3, lx, ty, Inches(5.9), Inches(2.48))
        tb = s3.shapes.add_textbox(lx + Inches(0.22), ty + Inches(0.18), Inches(5.46), Inches(2.15))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = t_old
        p.font.name = FONT_UI
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(2)
        p = tf.add_paragraph()
        p.text = t_new
        p.font.name = FONT_UI
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = ACCENT_TEAL
        p.space_after = Pt(8)
        p = tf.add_paragraph()
        p.text = t_desc
        p.font.name = FONT_UI
        p.font.size = Pt(12.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 4: EJEMPLO VISUAL DEL MODELO ACTUAL (ADAPTABLE A SU ÁREA)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, BG_LIGHT)
    add_header(s4, "Así luce nuestro modelo actual (listo para adaptar a su Normal)", "3. Evidencia real", 4)
    add_footer(s4)

    p4 = os.path.join(CAPTURES_DIR, "04_workspace_minicaso.png")
    p6 = os.path.join(CAPTURES_DIR, "06_docente_ingesta.png")
    if os.path.exists(p4):
        add_card(s4, Inches(0.65), Inches(1.38), Inches(5.7), Inches(4.25))
        s4.shapes.add_picture(p4, Inches(0.75), Inches(1.45), height=Inches(4.1))
    if os.path.exists(p6):
        add_card(s4, Inches(6.98), Inches(1.38), Inches(5.7), Inches(4.25))
        s4.shapes.add_picture(p6, Inches(7.08), Inches(1.45), height=Inches(4.1))

    add_card(s4, Inches(0.65), Inches(5.78), Inches(12.03), Inches(1.1))
    tb4 = s4.shapes.add_textbox(Inches(0.85), Inches(5.88), Inches(11.63), Inches(0.9))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    p = tf4.paragraphs[0]
    p.text = "• Izquierda: Hoy muestra datos de un caso social; adaptado a Educación Física mostraría pruebas de desempeño motriz, secuencias o guías de observación.\n• Derecha: El docente reúne evidencias recibidas por WhatsApp, USB o registradas en libreta física sin necesitar internet en la escuela."
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 5: QUÉ IMPLICA PARA USTED COMO ASESORA DE TESIS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, BG_LIGHT)
    add_header(s5, "¿Qué implica este proyecto para usted como Asesora de Tesis?", "4. Valor para asesoría", 5)
    add_footer(s5)

    add_card(s5, Inches(0.65), Inches(1.4), Inches(12.03), Inches(5.3))
    tb5 = s5.shapes.add_textbox(Inches(0.95), Inches(1.65), Inches(11.43), Inches(4.8))
    tf5 = tb5.text_frame
    tf5.word_wrap = True
    p = tf5.paragraphs[0]
    p.text = "De tesis de puro escritorio a propuestas didácticas reales y verificables:"
    p.font.name = FONT_UI
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(14)

    add_bullets(tf5, [
        ("1. Sustento pedagógico y normativo sólido: ", "Alineado a la Nueva Escuela Mexicana, Diseño Universal para el Aprendizaje (DUA) y atención a Barreras (BAP) en contextos rurales."),
        ("2. Productos tangibles para tesis de intervención: ", "Sus asesorados de la Normal de Río Grande pueden presentar no solo un documento escrito, sino una herramienta ligera real probada en su escuela de práctica."),
        ("3. Evidencias ordenadas de campo: ", "Diarios reflexivos, listas de cotejo y gráficas comparativas de avance motriz listos para incluirse en el capítulo de resultados sin retrabajo."),
        ("4. Cero barrera técnica para el normalista: ", "El estudiante diseña la propuesta educativa desde su área sin tener que ser ingeniero en sistemas.")
    ], font_size=13.5, space_after=12)

    # =========================================================================
    # LÁMINA 6: QUÉ IMPLICA PARA USTED COMO SINODAL
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, BG_LIGHT)
    add_header(s6, "¿Qué implica como Sinodal al evaluar exámenes y documentos?", "5. Valor para evaluación", 6)
    add_footer(s6)

    sinodal_cards = [
        ("Rigor metodológico verificable", "Sin 'adornos' tecnológicos vacíos",
         "Usted puede distinguir de inmediato cuándo una propuesta digital resuelve una necesidad real de la Costa (baja conectividad, inclusión) frente a una app copiada que no sirve en primaria."),
        ("Criterios y rúbricas transparentes", "Evaluación formativa auténtica",
         "Cada instrumento muestra exactamente qué se observó, bajo qué criterios de logro y con qué límites éticos, evitando interpretaciones sin evidencia."),
        ("Trazabilidad y prevención de errores", "Principio de calidad sin improvisación",
         "Los registros de campo conservan fecha, autor y coherencia interna, evitando pérdida de datos o resultados inventados a última hora."),
        ("Pertinencia territorial (Costa / Oaxaca)", "Justicia educativa normalista",
         "Fomenta que los futuros licenciados en Educación Física creen recursos propios desde su contexto en lugar de depender de plataformas caras de ciudad.")
    ]

    for i, (st, ss, sb) in enumerate(sinodal_cards):
        col = i % 2
        row = i // 2
        lx = Inches(0.65 + col * 6.1)
        ty = Inches(1.4 + row * 2.7)
        add_card(s6, lx, ty, Inches(5.9), Inches(2.48))
        tb = s6.shapes.add_textbox(lx + Inches(0.22), ty + Inches(0.18), Inches(5.46), Inches(2.15))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st
        p.font.name = FONT_UI
        p.font.size = Pt(14.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_TEAL
        p.space_after = Pt(2)
        p = tf.add_paragraph()
        p.text = ss
        p.font.name = FONT_UI
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(8)
        p = tf.add_paragraph()
        p.text = sb
        p.font.name = FONT_UI
        p.font.size = Pt(12.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # LÁMINA 7: ¿CÓMO ME PUEDE AYUDAR MEDIANTE SUS NECESIDADES A CREAR COSAS?
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7, BG_LIGHT)
    add_header(s7, "Alianza Práctica: Sus necesidades guían lo que podemos construir", "6. Creación conjunta", 7)
    add_footer(s7)

    add_card(s7, Inches(0.65), Inches(1.4), Inches(4.5), Inches(5.3), RGBColor(236, 253, 245), ACCENT_TEAL)
    tbl7 = s7.shapes.add_textbox(Inches(0.88), Inches(1.6), Inches(4.04), Inches(4.9))
    tfl7 = tbl7.text_frame
    tfl7.word_wrap = True
    p = tfl7.paragraphs[0]
    p.text = "¿Cómo funcionamos en equipo?"
    p.font.name = FONT_UI
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p.space_after = Pt(12)

    add_bullets(tfl7, [
        ("1. Usted nos señala la necesidad real: ", "Qué les cuesta trabajo a sus alumnos normalistas o qué falta en el patio escolar."),
        ("2. Validamos el criterio pedagógico: ", "Con su experiencia como doctora, asesora y sinodal definimos rúbricas y formatos."),
        ("3. Nosotros creamos la herramienta: ", "Construimos la aplicación ligera sin internet para probarla y perfeccionarla con usted.")
    ], font_size=12.5, space_after=14)

    add_card(s7, Inches(5.4), Inches(1.4), Inches(7.28), Inches(5.3))
    tbr7 = s7.shapes.add_textbox(Inches(5.68), Inches(1.6), Inches(6.72), Inches(4.9))
    tfr7 = tbr7.text_frame
    tfr7.word_wrap = True
    p = tfr7.paragraphs[0]
    p.text = "3 cosas concretas que podríamos crear en equipo para la Normal:"
    p.font.name = FONT_UI
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(12)

    add_bullets(tfr7, [
        ("Idea A — Evaluador de Cancha sin Internet: ", "Listas de cotejo y rúbricas de desempeño motriz y aptitud física para usar en el patio con un solo clic y descargar los resultados en Excel."),
        ("Idea B — Bitácora de Prácticas Normalistas: ", "Registro offline de diarios de observación, incidentes y reflexión pedagógica para estudiantes enviados a comunidades sin señal."),
        ("Idea C — Banco de Juegos y Ajustes DUA: ", "Guía rápida offline de adaptaciones motrices para incluir en clase de Educación Física a niñas y niños con alguna barrera o discapacidad.")
    ], font_size=12.8, space_after=14)

    # =========================================================================
    # LÁMINA 8: CIERRE CON CARIÑO Y VISIÓN NORMALISTA
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8, BG_DARK)

    line8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.73), Inches(0.07))
    line8.fill.solid()
    line8.fill.fore_color.rgb = RGBColor(245, 158, 11)
    line8.line.fill.background()

    tb8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.55), Inches(11.73), Inches(3.3))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    p = tf8.paragraphs[0]
    p.text = "MENSAJE FINAL"
    p.font.name = FONT_UI
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_SOFT
    p.space_after = Pt(16)

    p = tf8.add_paragraph()
    p.text = "La mejor tecnología educativa de Oaxaca nace\ncuando la experiencia de una maestra normalista\nguía lo que se construye para sus escuelas."
    p.font.name = FONT_UI
    p.font.size = Pt(27)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    add_card(s8, Inches(0.8), Inches(5.45), Inches(11.73), Inches(1.35), RGBColor(29, 64, 77), None)
    tb8f = s8.shapes.add_textbox(Inches(1.05), Inches(5.65), Inches(11.23), Inches(0.95))
    tf8f = tb8f.text_frame
    tf8f.word_wrap = True
    p = tf8f.paragraphs[0]
    p.text = "Madrina Juana: ¿Qué problema de sus clases, prácticas o tesis le gustaría resolver primero?"
    p.font.name = FONT_UI
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(251, 191, 36)
    p.space_after = Pt(6)
    p = tf8f.add_paragraph()
    p.text = f"Modelo base (MVP): {WEB_URL}   |   Código abierto: {REPO_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_SOFT

    out_path = os.path.join(BASE_DIR, "docs", "presentacion", "Aula_301_Madrina_Juana_Normal_Rio_Grande.pptx")
    prs.save(out_path)
    print(f"Presentación para Madrina Juana generada en: {out_path}")


if __name__ == "__main__":
    create_madrina_deck()

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


def create_executive_deck():
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
    ACCENT_RED = RGBColor(185, 28, 28)
    BORDER_LIGHT = RGBColor(203, 213, 225)

    FONT_UI = "Arial"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    REPO_URL = "https://github.com/Tortaconflow/aula-301"
    WEB_URL = "https://aula-301.vercel.app"
    TOTAL_SLIDES = 6

    def set_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()

    def add_header(slide, title, cat, num):
        hb = slide.shapes.add_textbox(Inches(0.65), Inches(0.35), Inches(10.8), Inches(0.9))
        tf = hb.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = cat.upper()
        p0.font.name = FONT_UI
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT_PURPLE
        p0.space_after = Pt(2)

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.name = FONT_UI
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_MAIN

        nb = slide.shapes.add_textbox(Inches(11.6), Inches(0.38), Inches(1.08), Inches(0.4))
        ntf = nb.text_frame
        np = ntf.paragraphs[0]
        np.alignment = PP_ALIGN.RIGHT
        np.text = f"{num:02d} / {TOTAL_SLIDES:02d}"
        np.font.name = FONT_UI
        np.font.size = Pt(12)
        np.font.bold = True
        np.font.color.rgb = TEXT_MUTED

    def add_footer(slide):
        fb = slide.shapes.add_textbox(Inches(0.65), Inches(7.02), Inches(12.03), Inches(0.35))
        p = fb.text_frame.paragraphs[0]
        p.text = f"Aula 301 · Resumen Ejecutivo de Calidad · GitHub: {REPO_URL}"
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

    # =========================================================================
    # SLIDE 1: PORTADA EJECUTIVA
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, BG_DARK)

    line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.73), Inches(0.07))
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(245, 158, 11)
    line.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.73), Inches(3.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "RESUMEN EJECUTIVO · DIRECTO AL GRANO"
    p.font.name = FONT_UI
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Aula 301: Ingeniería Inversa (REA),\nAgentes de IA y Control de Calidad Goldfish"
    p.font.name = FONT_UI
    p.font.size = Pt(34)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.text = "Cómo evitamos improvisar con IA y garantizamos operación sin fallos en Oaxaca."
    p.font.name = FONT_UI
    p.font.size = Pt(18)
    p.font.color.rgb = RGBColor(224, 231, 255)

    add_card(s1, Inches(0.8), Inches(5.5), Inches(11.73), Inches(1.3), RGBColor(38, 41, 92), None)
    tbm = s1.shapes.add_textbox(Inches(1.05), Inches(5.7), Inches(11.23), Inches(0.95))
    tfm = tbm.text_frame
    tfm.word_wrap = True
    p = tfm.paragraphs[0]
    p.text = f"Presentación para: Dra. Maldonado (Ingeniería Industrial)  |  IISUABJO - UABJO"
    p.font.name = FONT_UI
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)
    p = tfm.add_paragraph()
    p.text = f"GitHub: {REPO_URL}   |   App: {WEB_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LILAC

    # =========================================================================
    # SLIDE 2: EL PROBLEMA OPERATIVO (DATOS DUROS)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, BG_LIGHT)
    add_header(s2, "1. El Problema: Cuellos de botella reales en Oaxaca", "Diagnóstico operativo", 2)
    add_footer(s2)

    probs = [
        ("46.7 % solo celular", "76.7 % sin equipo propio exclusivo (30 % compartido)."),
        ("Red inestable", "SICE y Classroom se caen o borran tareas al perder señal."),
        ("Hardware lento", "PCs escolares antiguas se congelan con apps pesadas."),
        ("Riesgo de 'Vibe Coding'", "Pedir código a ciegas a una IA genera fallos y retrabajo.")
    ]
    for i, (pt, pd) in enumerate(probs):
        col = i % 2
        row = i // 2
        lx = Inches(0.65 + col * 6.1)
        ty = Inches(1.45 + row * 2.65)
        add_card(s2, lx, ty, Inches(5.9), Inches(2.4))
        tb = s2.shapes.add_textbox(lx + Inches(0.25), ty + Inches(0.25), Inches(5.4), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = pt
        p.font.name = FONT_UI
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_RED
        p.space_after = Pt(10)
        p = tf.add_paragraph()
        p.text = pd
        p.font.name = FONT_UI
        p.font.size = Pt(14.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 3: LA SOLUCIÓN EN 3 PASOS (SIN RODEOS)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, BG_LIGHT)
    add_header(s3, "2. El Método: 3 pasos para cero improvisación", "Metodología aplicada", 3)
    add_footer(s3)

    steps = [
        ("1. REA (Ingeniería Inversa)", "Benchmark técnico",
         "• Analizamos SICE y Classroom.\n• Conservamos lo útil (tarjetas).\n• Eliminamos el cuello de botella (servidor central e internet)."),
        ("2. Agentes de IA con Reglas", "Especificación estricta",
         "• Fijamos restricciones antes de crear: 100 % offline, <1 MB, sin librerías pesadas.\n• Alineado a las 6 tablas de la materia y uso en papel."),
        ("3. Enjambre Goldfish", "Auditoría de calidad",
         "• 5 revisores críticos independientes auditaron código, diseño, claridad y datos.\n• Detectaron errores antes de entregar al grupo.")
    ]
    for i, (st, ss, sb) in enumerate(steps):
        lx = Inches(0.65 + i * 4.1)
        add_card(s3, lx, Inches(1.45), Inches(3.88), Inches(5.2))
        tb = s3.shapes.add_textbox(lx + Inches(0.22), Inches(1.65), Inches(3.44), Inches(4.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st
        p.font.name = FONT_UI
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_PURPLE
        p.space_after = Pt(4)
        p = tf.add_paragraph()
        p.text = ss
        p.font.name = FONT_UI
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        p.space_after = Pt(14)
        p = tf.add_paragraph()
        p.text = sb
        p.font.name = FONT_UI
        p.font.size = Pt(13.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 4: QUÉ DETECTÓ GOLDFISH Y QUÉ SE CORRIGIÓ
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, BG_LIGHT)
    add_header(s4, "3. Control de Calidad Goldfish: Fallos detectados y corregidos", "Inspección antes de entrega", 4)
    add_footer(s4)

    fixes = [
        ("CSV devolvía NaN", "Se corrigió lectura de totalCasos y se agregó BOM UTF-8 para Excel antiguo."),
        ("Falla sin internet / file://", "Se eliminaron fuentes externas y se agregó respaldo SHA-256 en JS puro."),
        ("Error estadístico en Minicaso 1", "Se añadió variable cuantitativa (horas) para validar media y desviación."),
        ("Exceso de jerga técnica", "Se tradujo toda la interfaz y el banco de preguntas a lenguaje educativo.")
    ]
    for i, (fx_bad, fx_ok) in enumerate(fixes):
        ty = Inches(1.42 + i * 1.35)
        add_card(s4, Inches(0.65), ty, Inches(12.03), Inches(1.18))
        tb = s4.shapes.add_textbox(Inches(0.9), ty + Inches(0.15), Inches(11.53), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        rb = p.add_run()
        rb.text = f"Hallazgo: {fx_bad}  ->  "
        rb.font.name = FONT_UI
        rb.font.size = Pt(14)
        rb.font.bold = True
        rb.font.color.rgb = ACCENT_RED
        rk = p.add_run()
        rk.text = fx_ok
        rk.font.name = FONT_UI
        rk.font.size = Pt(14)
        rk.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 5: RESULTADOS MEDIBLES (ROI PARA EL AULA)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, BG_LIGHT)
    add_header(s5, "4. Resultados Medibles: Menos retrabajo y cero bloqueos", "Impacto concreto", 5)
    add_footer(s5)

    metrics = [
        ("0 s de espera en servidor", "Cada dispositivo procesa y guarda localmente sin saturación."),
        ("100 % operativa sin red", "Funciona en modo avión, USB (file://), WhatsApp o papel."),
        ("Poka-Yoke en entregas", "Impide entregar sin completar los 4 criterios de rúbrica."),
        ("0 errores en pruebas", "Validada en Chrome headless con los 3 minicasos y 6 tablas.")
    ]
    for i, (mt, md) in enumerate(metrics):
        col = i % 2
        row = i // 2
        lx = Inches(0.65 + col * 6.1)
        ty = Inches(1.45 + row * 2.65)
        add_card(s5, lx, ty, Inches(5.9), Inches(2.4))
        tb = s5.shapes.add_textbox(lx + Inches(0.25), ty + Inches(0.25), Inches(5.4), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = mt
        p.font.name = FONT_UI
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(10)
        p = tf.add_paragraph()
        p.text = md
        p.font.name = FONT_UI
        p.font.size = Pt(14.5)
        p.font.color.rgb = TEXT_MAIN

    # =========================================================================
    # SLIDE 6: CIERRE EJECUTIVO
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, BG_DARK)

    line6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.73), Inches(0.07))
    line6.fill.solid()
    line6.fill.fore_color.rgb = RGBColor(245, 158, 11)
    line6.line.fill.background()

    tb6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.73), Inches(3.2))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    p = tf6.paragraphs[0]
    p.text = "CONCLUSIÓN EN UNA FRASE"
    p.font.name = FONT_UI
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_LILAC
    p.space_after = Pt(16)

    p = tf6.add_paragraph()
    p.text = "No programamos a ciegas:\nusamos REA + Agentes + Goldfish como control de calidad\npara entregar software que sí funciona en Oaxaca."
    p.font.name = FONT_UI
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    add_card(s6, Inches(0.8), Inches(5.45), Inches(11.73), Inches(1.3), RGBColor(38, 41, 92), None)
    tb6f = s6.shapes.add_textbox(Inches(1.05), Inches(5.68), Inches(11.23), Inches(0.9))
    tf6f = tb6f.text_frame
    tf6f.word_wrap = True
    p = tf6f.paragraphs[0]
    p.text = f"Repositorio auditable: {REPO_URL}   |   App: {WEB_URL}"
    p.font.name = FONT_UI
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)
    p = tf6f.add_paragraph()
    p.text = "Gracias por su tiempo, Dra. Maldonado. · Grupo 301, IISUABJO - UABJO"
    p.font.name = FONT_UI
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LILAC

    out_path = os.path.join(BASE_DIR, "docs", "presentacion", "Aula_301_Resumen_Ejecutivo_Ingeniera.pptx")
    prs.save(out_path)
    print(f"Presentación ejecutiva generada en: {out_path}")


if __name__ == "__main__":
    create_executive_deck()

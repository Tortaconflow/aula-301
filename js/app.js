/**
 * Aula 301 — Controlador pedagógico, accesibilidad DUA y persistencia sin red
 * Compatible con ES5/ES6 para navegadores modestos y apertura local file://.
 */
(function () {
  var data = window.AULA301_DATA;
  var activeWorkspaceId = null;
  var feedbackTimer = null;
  var teacherUnlockedInSession = false;

  var STORAGE_KEYS = {
    session: "aula301_session_v2",
    userLegacy: "aula301_session_user",
    activities: "aula301_teacher_activities",
    roster: "aula301_teacher_roster_v1"
  };

  function escapeHtml(str) {
    if (str === null || str === undefined) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function safeParse(raw, fallback) {
    try {
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) {
      return fallback;
    }
  }

  function getCurrentSession() {
    var s = safeParse(localStorage.getItem(STORAGE_KEYS.session), null);
    if (s && s.id && s.name) return s;
    var legacy = localStorage.getItem(STORAGE_KEYS.userLegacy);
    if (legacy) {
      return { id: normalizeSlug(legacy), name: legacy, shared: false };
    }
    return null;
  }

  function normalizeSlug(str) {
    var clean = String(str || "").trim().toLowerCase().replace(/[^a-z0-9_-]/g, "");
    return clean || "anonimo";
  }

  function studentActKey(base, actId) {
    var s = getCurrentSession() || { id: "demo", name: "Estudiante" };
    return base + "_" + normalizeSlug(s.id) + "_act" + actId;
  }

  function loadSubmission(actId) {
    return safeParse(localStorage.getItem(studentActKey("aula301_sub", actId)), null);
  }

  function saveSubmission(actId, sub) {
    try {
      localStorage.setItem(studentActKey("aula301_sub", actId), JSON.stringify(sub));
    } catch (e) {}
  }

  function loadSelfEval(actId) {
    return safeParse(localStorage.getItem(studentActKey("aula301_eval", actId)), {});
  }

  function saveSelfEval(actId, evalObj) {
    try {
      localStorage.setItem(studentActKey("aula301_eval", actId), JSON.stringify(evalObj));
    } catch (e) {}
  }

  function loadStoredActivities() {
    return safeParse(localStorage.getItem(STORAGE_KEYS.activities), []);
  }

  function saveStoredActivities(list) {
    try {
      localStorage.setItem(STORAGE_KEYS.activities, JSON.stringify(list));
    } catch (e) {}
  }

  function loadRoster() {
    return safeParse(localStorage.getItem(STORAGE_KEYS.roster), []);
  }

  function saveRoster(list) {
    try {
      localStorage.setItem(STORAGE_KEYS.roster, JSON.stringify(list));
    } catch (e) {}
  }

  // ========================================================================
  // SHA-256 puro en JS (garantiza funcionamiento exacto incluso en file://)
  // ========================================================================
  function sha256Pure(asciiOrUtf8) {
    var str = unescape(encodeURIComponent(String(asciiOrUtf8 || "")));
    function rightRotate(value, amount) {
      return (value >>> amount) | (value << (32 - amount));
    }
    var mathPow = Math.pow;
    var maxWord = mathPow(2, 32);
    var i, j, result = "";
    var words = [];
    var asciiBitLength = str.length * 8;

    var hash = sha256Pure.h = sha256Pure.h || [];
    var k = sha256Pure.k = sha256Pure.k || [];
    var primeCounter = k.length;
    var isComposite = {};
    for (var candidate = 2; primeCounter < 64; candidate++) {
      if (!isComposite[candidate]) {
        for (i = 0; i < 313; i += candidate) isComposite[i] = candidate;
        hash[primeCounter] = (mathPow(candidate, 0.5) * maxWord) | 0;
        k[primeCounter++] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
      }
    }

    str += "\x80";
    while ((str.length % 64) - 56) str += "\x00";
    for (i = 0; i < str.length; i++) {
      j = str.charCodeAt(i);
      if (j >> 8) return "";
      words[i >> 2] |= j << (((3 - i) % 4) * 8);
    }
    words[words.length] = (asciiBitLength / maxWord) | 0;
    words[words.length] = asciiBitLength;

    var H = hash.slice(0);
    for (j = 0; j < words.length;) {
      var w = words.slice(j, (j += 16));
      var oldHash = H.slice(0);
      for (i = 0; i < 64; i++) {
        var w15 = w[i - 15], w2 = w[i - 2];
        var a = H[0], e = H[4];
        var temp1 = H[7] +
          (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)) +
          ((e & H[5]) ^ (~e & H[6])) +
          k[i] +
          (w[i] = i < 16 ? w[i] : (
            w[i - 16] +
            (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15 >>> 3)) +
            w[i - 7] +
            (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2 >>> 10))
          ) | 0);
        var temp2 = (rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)) +
          ((a & H[1]) ^ (a & H[2]) ^ (H[1] & H[2]));
        H = [(temp1 + temp2) | 0].concat(H);
        H[4] = (H[4] + temp1) | 0;
        H.pop();
      }
      for (i = 0; i < 8; i++) H[i] = (H[i] + oldHash[i]) | 0;
    }
    for (i = 0; i < 8; i++) {
      for (j = 3; j + 1; j--) {
        var b = (H[i] >> (j * 8)) & 255;
        result += (b < 16 ? "0" : "") + b.toString(16);
      }
    }
    return result;
  }

  function canonicalSelfEvalString(evalObj) {
    var keys = Object.keys(evalObj || {}).sort();
    var out = {};
    keys.forEach(function (k) { out[k] = evalObj[k]; });
    return JSON.stringify(out);
  }

  function buildCanonicalPayload(obj) {
    return [
      String(obj.matricula || ""),
      String(obj.estudiante || ""),
      String(obj.actividad_id || ""),
      String(obj.actividad || ""),
      String(obj.estado_entrega || ""),
      String(obj.fecha_generacion || ""),
      String(obj.conclusiones_estudiante || ""),
      canonicalSelfEvalString(obj.autoevaluacion_rubrica || {})
    ].join("|");
  }

  function computeIntegrityHash(payload, callback) {
    if (window.crypto && window.crypto.subtle && typeof TextEncoder !== "undefined") {
      try {
        var encoder = new TextEncoder();
        window.crypto.subtle.digest("SHA-256", encoder.encode(payload))
          .then(function (buf) {
            var arr = Array.prototype.slice.call(new Uint8Array(buf));
            var hex = arr.map(function (b) {
              var s = b.toString(16);
              return s.length === 1 ? "0" + s : s;
            }).join("");
            callback(hex);
          })
          .catch(function () {
            callback(sha256Pure(payload));
          });
        return;
      } catch (e) {}
    }
    callback(sha256Pure(payload));
  }

  // ========================================================================
  // Navegación e Inicio (sin recargas de página)
  // ========================================================================
  function showView(name) {
    ["inicio", "actividades", "calificaciones", "recursos"].forEach(function (v) {
      var el = document.getElementById("view-" + v);
      if (!el) return;
      el.classList.toggle("hidden", v !== name);
      if (v === name) el.scrollTop = 0;
    });
    var navBtns = document.querySelectorAll("[data-nav]");
    for (var i = 0; i < navBtns.length; i++) {
      navBtns[i].setAttribute("aria-current", navBtns[i].getAttribute("data-nav") === name ? "true" : "false");
    }
    if (name === "calificaciones") renderGradesView();
  }

  function applySessionToUI(session) {
    var greet = document.getElementById("greetName");
    var headerMat = document.getElementById("headerMatricula");
    var logoutLabel = document.getElementById("logoutLabel");
    if (greet) greet.textContent = session ? session.name : "Estudiante";
    if (headerMat) headerMat.textContent = session ? session.id : "--";
    if (logoutLabel) logoutLabel.textContent = (session && session.shared) ? "Salir y limpiar" : "Salir";
  }

  function setupSessionAndNavigation() {
    var navBtns = document.querySelectorAll("[data-nav]");
    for (var i = 0; i < navBtns.length; i++) {
      (function (btn) {
        btn.addEventListener("click", function () {
          showView(btn.getAttribute("data-nav"));
        });
      })(navBtns[i]);
    }

    var avisosBtn = document.getElementById("avisosBtn");
    var avisosDetalle = document.getElementById("avisosDetalle");
    var avisosArrow = document.getElementById("avisosArrow");
    if (avisosBtn && avisosDetalle) {
      avisosBtn.addEventListener("click", function () {
        var isHidden = avisosDetalle.classList.toggle("hidden");
        avisosBtn.setAttribute("aria-expanded", isHidden ? "false" : "true");
        if (avisosArrow) avisosArrow.textContent = isHidden ? "▾" : "▴";
      });
    }

    var loginForm = document.getElementById("loginForm");
    if (loginForm) {
      loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var idVal = (document.getElementById("loginId").value || "").trim();
        var nameVal = (document.getElementById("loginUser").value || "").trim();
        var sharedEl = document.getElementById("sharedDeviceCheck");
        var isShared = sharedEl ? !!sharedEl.checked : false;
        if (!idVal || !nameVal) return;

        var sess = { id: idVal, name: nameVal, shared: isShared };
        try {
          localStorage.setItem(STORAGE_KEYS.session, JSON.stringify(sess));
        } catch (err) {}

        teacherUnlockedInSession = false;
        setRoleUI("estudiante");
        applySessionToUI(sess);
        renderActivitiesStack();
        renderGradesView();

        document.getElementById("loginView").classList.add("hidden");
        document.getElementById("appView").classList.remove("hidden");
        showView("inicio");
      });
    }

    var logoutBtn = document.getElementById("logoutBtn");
    if (logoutBtn) {
      logoutBtn.addEventListener("click", function () {
        var currentSess = getCurrentSession();
        if (currentSess && currentSess.shared) {
          // Limpiar datos personales de la sesión en equipo compartido tras haber exportado
          var slug = normalizeSlug(currentSess.id);
          data.miniCasos.forEach(function (mc) {
            try {
              localStorage.removeItem("aula301_sub_" + slug + "_act" + mc.id);
              localStorage.removeItem("aula301_eval_" + slug + "_act" + mc.id);
            } catch (e) {}
          });
        }
        try {
          localStorage.removeItem(STORAGE_KEYS.session);
          localStorage.removeItem(STORAGE_KEYS.userLegacy);
        } catch (err) {}

        teacherUnlockedInSession = false;
        setRoleUI("estudiante");
        activeWorkspaceId = null;
        if (loginForm) loginForm.reset();
        document.getElementById("appView").classList.add("hidden");
        document.getElementById("loginView").classList.remove("hidden");
      });
    }

    // Auto-restaurar si existe sesión previa
    var existing = getCurrentSession();
    if (existing) {
      setRoleUI("estudiante");
      applySessionToUI(existing);
      document.getElementById("loginView").classList.add("hidden");
      document.getElementById("appView").classList.remove("hidden");
      showView("inicio");
    }
  }

  // ========================================================================
  // Render dinámico unificado de los 3 Mini Casos (Fuente Única: data.js)
  // ========================================================================
  function csvEscapeCell(val) {
    var str = String(val === null || val === undefined ? "" : val).replace(/"/g, '""');
    return '"' + str + '"';
  }

  function downloadMiniCasoCsv(mc) {
    var lines = [];
    if (mc.tipoVisualizacion === "contingencia" && mc.matrizContingencia) {
      lines.push(mc.matrizContingencia.columnas.map(csvEscapeCell).join(","));
      mc.matrizContingencia.filas.forEach(function (row) {
        lines.push([
          csvEscapeCell(row.categoria),
          row.informal,
          row.formal,
          row.total,
          csvEscapeCell(row.pctTexto)
        ].join(","));
      });
      var tot = mc.matrizContingencia.totales;
      lines.push([
        csvEscapeCell("Total general"),
        tot.informal,
        tot.formal,
        tot.total,
        csvEscapeCell(tot.pctTexto)
      ].join(","));
    } else {
      var total = mc.totalCasos || mc.categorias.reduce(function (acc, item) { return acc + item.casos; }, 0);
      lines.push("categoria,casos,total_grupo,porcentaje");
      mc.categorias.forEach(function (r) {
        var pct = total > 0 ? Math.round((r.casos / total) * 1000) / 10 : 0;
        lines.push([csvEscapeCell(r.categoria), r.casos, total, pct].join(","));
      });
      if (mc.variableCuantitativa && mc.variableCuantitativa.valores) {
        lines.push("");
        lines.push(csvEscapeCell(mc.variableCuantitativa.nombre));
        lines.push("caso_num,horas_semanales");
        mc.variableCuantitativa.valores.forEach(function (v, idx) {
          lines.push((idx + 1) + "," + v);
        });
      }
    }
    lines.push("");
    lines.push(csvEscapeCell(mc.csvNote));

    var bom = "\uFEFF";
    var blob = new Blob([bom + lines.join("\n")], { type: "text/csv;charset=utf-8;" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = mc.csvFilename || ("aula301_minicaso_" + mc.id + ".csv");
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
      URL.revokeObjectURL(a.href);
      a.remove();
    }, 500);
  }

  function renderMiniCasoDataTableHtml(mc) {
    if (mc.tipoVisualizacion === "contingencia" && mc.matrizContingencia) {
      var cols = mc.matrizContingencia.columnas;
      var html = '<table aria-label="' + escapeHtml(mc.titulo) + '"><thead><tr>';
      cols.forEach(function (c, i) {
        html += '<th' + (i > 0 ? ' class="num"' : '') + '>' + escapeHtml(c) + '</th>';
      });
      html += '</tr></thead><tbody>';
      mc.matrizContingencia.filas.forEach(function (f) {
        html += '<tr>' +
          '<td>' + escapeHtml(f.categoria) + '</td>' +
          '<td class="num">' + f.informal + '</td>' +
          '<td class="num">' + f.formal + '</td>' +
          '<td class="num">' + f.total + '</td>' +
          '<td class="num">' + escapeHtml(f.pctTexto) + '</td>' +
        '</tr>';
      });
      var t = mc.matrizContingencia.totales;
      html += '<tr style="font-weight:800;background:var(--lilac-soft)">' +
        '<td>Total general</td><td class="num">' + t.informal + '</td><td class="num">' + t.formal + '</td><td class="num">' + t.total + '</td><td class="num">' + escapeHtml(t.pctTexto) + '</td>' +
      '</tr></tbody></table>';
      return html;
    }

    var rowsHtml = '<table aria-label="' + escapeHtml(mc.titulo) + '"><thead><tr><th>Categoría</th><th class="num">Casos</th><th class="num">%</th></tr></thead><tbody>';
    mc.categorias.forEach(function (item) {
      rowsHtml += '<tr><td>' + escapeHtml(item.categoria) + '</td><td class="num">' + item.casos + '</td><td class="num">' + escapeHtml(item.porcentajeTexto) + '</td></tr>';
    });
    rowsHtml += '<tr style="font-weight:800;background:var(--lilac-soft)"><td>Total</td><td class="num">' + mc.totalCasos + '</td><td class="num">100.0 %</td></tr></tbody></table>';
    return rowsHtml;
  }

  function buildWorkspaceNode(mc) {
    var panel = document.createElement("div");
    panel.className = "activity-workspace-panel";
    panel.id = "workspaceMinicaso" + mc.id;

    var quantHtml = "";
    if (mc.variableCuantitativa) {
      quantHtml = '<div class="quant-box">' +
        '<strong>Dato cuantitativo complementario (para Tendencia Central y Dispersión):</strong><br>' +
        '<span>' + escapeHtml(mc.variableCuantitativa.nombre) + '</span><br>' +
        '<span style="color:var(--purple);font-weight:700">' + escapeHtml(mc.variableCuantitativa.resumen) + '</span>' +
      '</div>';
    }

    var barsHtml = "";
    mc.categorias.forEach(function (item) {
      barsHtml += '<div class="bar-row">' +
        '<span>' + escapeHtml(item.categoria) + '</span>' +
        '<strong>' + escapeHtml(item.porcentajeTexto) + '</strong>' +
        '<div class="bar-track"><div class="bar-fill" style="width:' + Number(item.porcentajeAncho) + '%"></div></div>' +
      '</div>';
    });

    var rubricRows = "";
    data.rubricaEjemplo.criterios.forEach(function (c) {
      rubricRows += '<tr>' +
        '<td><strong>' + escapeHtml(c.criterio) + '</strong></td>' +
        '<td>' + escapeHtml(c.logrado) + '</td>' +
        '<td>' + escapeHtml(c.enProceso) + '</td>' +
        '<td>' + escapeHtml(c.inicial) + '</td>' +
      '</tr>';
    });

    panel.innerHTML =
      '<div class="workspace-header">' +
        '<span class="tag">Espacio de trabajo · Minicaso ' + mc.id + '</span>' +
        '<span class="example-badge">CASO DIDÁCTICO SITUADO</span>' +
      '</div>' +
      '<div class="case-detail">' +
        '<div class="panel">' +
          '<span class="tag">Datos didácticos · n = ' + mc.totalCasos + '</span>' +
          '<h3>' + escapeHtml(mc.titulo) + '</h3>' +
          renderMiniCasoDataTableHtml(mc) +
          quantHtml +
          '<div class="task"><strong>Consigna pedagógica:</strong> ' + escapeHtml(mc.consigna) + '</div>' +
          '<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px">' +
            '<button type="button" class="btn small" id="wsCsvBtn">Descargar datos para Excel / Calc (.csv)</button>' +
            '<button type="button" class="btn secondary small" id="wsPrintBtn">Imprimir hoja de trabajo (DUA)</button>' +
          '</div>' +
        '</div>' +
        '<div class="panel">' +
          '<h3>Representación gráfica</h3>' +
          '<div>' + barsHtml + '</div>' +
          '<hr class="divider">' +
          '<h3>Reflexión situada (Locus de enunciación)</h3>' +
          '<p style="font-size:0.86rem;color:var(--muted)">' + escapeHtml(mc.glosaLocus) + '</p>' +
          '<p style="font-weight:600">' + escapeHtml(mc.preguntaReflexiva) + '</p>' +
        '</div>' +
      '</div>' +
      '<div class="panel">' +
        '<h3>Rúbrica de evaluación formativa</h3>' +
        '<table class="rubric"><thead><tr><th>Criterio</th><th>Logrado (10)</th><th>En proceso (7.2)</th><th>Inicial (4.0)</th></tr></thead><tbody>' + rubricRows + '</tbody></table>' +
      '</div>' +
      '<div class="panel" id="wsSelfPanel">' +
        '<h3>Autoevaluación del estudiante (Metacognición)</h3>' +
        '<p style="color:var(--muted);font-size:0.9rem">Antes de registrar tu entrega, valora con honestidad tu propio avance en los 4 criterios.</p>' +
        '<div id="wsSelfCriteriaList"></div>' +
        '<p id="wsSelfSummary" style="margin-top:14px;font-weight:700"></p>' +
      '</div>' +
      '<div class="panel submission-panel">' +
        '<h3>Entrega de tu análisis (Modalidad accesible sin internet — DUA)</h3>' +
        '<p style="color:var(--muted);font-size:0.9rem">Todo lo que redactes se guarda automáticamente en este dispositivo sin gastar tus datos móviles. Al concluir, descarga tu constancia o copia el texto para enviarlo por WhatsApp o USB.</p>' +
        '<form id="wsSubmissionForm">' +
          '<label for="wsSubmissionText"><strong>Tu análisis y conclusiones situadas (mínimo 2 ideas claras):</strong></label>' +
          '<textarea id="wsSubmissionText" rows="4" placeholder="Escribe aquí tu interpretación basada en los datos del caso y su contexto en Oaxaca..." required></textarea>' +
          '<div class="submission-actions">' +
            '<button type="button" class="btn secondary" id="wsSaveDraftBtn">Guardar borrador en este dispositivo</button>' +
            '<button type="submit" class="btn" id="wsSubmitBtn">Registrar entrega final</button>' +
            '<button type="button" class="btn secondary small" id="wsExportBtn">Descargar constancia de entrega</button>' +
            '<button type="button" class="btn secondary small" id="wsCopyWaBtn">Copiar texto para WhatsApp</button>' +
          '</div>' +
          '<p id="wsFeedback" class="submission-feedback hidden" aria-live="polite"></p>' +
          '<div id="wsCopyFallbackBox" class="hidden" style="margin-top:8px"><label style="font-size:0.84rem;font-weight:700">Copia manual (mantén presionado el cuadro y selecciona Copiar):</label><textarea id="wsCopyFallbackText" rows="3" readonly style="margin-top:4px;font-size:0.82rem"></textarea></div>' +
        '</form>' +
      '</div>';

    wireWorkspaceEvents(panel, mc);
    return panel;
  }

  function wireWorkspaceEvents(panel, mc) {
    var csvBtn = panel.querySelector("#wsCsvBtn");
    if (csvBtn) {
      csvBtn.addEventListener("click", function () { downloadMiniCasoCsv(mc); });
    }

    var printBtn = panel.querySelector("#wsPrintBtn");
    if (printBtn) {
      printBtn.addEventListener("click", function () { window.print(); });
    }

    // Autoevaluación
    var selfList = panel.querySelector("#wsSelfCriteriaList");
    var selfSummary = panel.querySelector("#wsSelfSummary");
    var answers = loadSelfEval(mc.id);
    var totalCrit = data.rubricaEjemplo.criterios.length;

    function refreshSelfSummary() {
      var done = Object.keys(answers).length;
      if (done === 0) {
        selfSummary.textContent = "Aún no marcas ningún criterio.";
      } else if (done < totalCrit) {
        selfSummary.textContent = "Llevas " + done + " de " + totalCrit + " criterios guardados en este dispositivo.";
      } else {
        selfSummary.textContent = "Autoevaluación completa (" + totalCrit + " de " + totalCrit + " criterios valorados). Ya puedes registrar tu entrega.";
      }
    }

    data.rubricaEjemplo.criterios.forEach(function (item, idx) {
      var block = document.createElement("div");
      if (idx > 0) block.className = "crit-block";
      var title = document.createElement("strong");
      title.textContent = item.criterio;
      block.appendChild(title);

      var helper = document.createElement("div");
      helper.style.fontSize = "0.82rem";
      helper.style.color = "var(--muted)";
      helper.textContent = item.ayuda || "";
      block.appendChild(helper);

      var grid = document.createElement("div");
      grid.className = "eval-grid";
      data.rubricaEjemplo.niveles.forEach(function (nivel) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.textContent = nivel;
        var selected = answers[item.criterio] === nivel;
        btn.setAttribute("aria-pressed", selected ? "true" : "false");
        if (selected) btn.classList.add("sel");

        btn.addEventListener("click", function () {
          var siblings = grid.querySelectorAll("button");
          for (var s = 0; s < siblings.length; s++) {
            siblings[s].classList.remove("sel");
            siblings[s].setAttribute("aria-pressed", "false");
          }
          btn.classList.add("sel");
          btn.setAttribute("aria-pressed", "true");
          answers[item.criterio] = nivel;
          saveSelfEval(mc.id, answers);
          refreshSelfSummary();
        });
        grid.appendChild(btn);
      });
      block.appendChild(grid);
      selfList.appendChild(block);
    });
    refreshSelfSummary();

    // Redacción, Poka-Yoke y Entrega
    var textarea = panel.querySelector("#wsSubmissionText");
    var form = panel.querySelector("#wsSubmissionForm");
    var draftBtn = panel.querySelector("#wsSaveDraftBtn");
    var exportBtn = panel.querySelector("#wsExportBtn");
    var copyWaBtn = panel.querySelector("#wsCopyWaBtn");
    var feedbackEl = panel.querySelector("#wsFeedback");
    var copyBox = panel.querySelector("#wsCopyFallbackBox");
    var copyTxtArea = panel.querySelector("#wsCopyFallbackText");

    var savedSub = loadSubmission(mc.id);
    if (savedSub && savedSub.text) {
      textarea.value = savedSub.text;
    }

    function showFeedback(msg, isSuccess, persist) {
      if (feedbackTimer) clearTimeout(feedbackTimer);
      feedbackEl.textContent = msg;
      feedbackEl.classList.remove("hidden");
      feedbackEl.style.color = isSuccess ? "#166534" : "#92400e";
      feedbackEl.style.borderColor = isSuccess ? "#22c55e" : "#f59e0b";
      feedbackEl.style.background = isSuccess ? "#dcfce7" : "#fef3c7";
      if (!persist) {
        feedbackTimer = setTimeout(function () {
          feedbackEl.classList.add("hidden");
        }, 6000);
      }
    }

    // Guardado automático en caliente cada 400 ms manteniendo el estado coherente
    var debounceTimer = null;
    textarea.addEventListener("input", function () {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function () {
        var cur = loadSubmission(mc.id) || { status: "draft" };
        cur.text = textarea.value;
        cur.updatedAt = new Date().toISOString();
        saveSubmission(mc.id, cur);
      }, 400);
    });

    function updateCardBadge(status) {
      var badge = document.getElementById("badgeActividad" + mc.id);
      if (!badge) return;
      if (status === "delivered") {
        badge.textContent = "Entregada";
        badge.className = "status-pill delivered";
      } else {
        badge.textContent = "Borrador guardado";
        badge.className = "status-pill";
      }
    }

    draftBtn.addEventListener("click", function () {
      var cur = loadSubmission(mc.id) || {};
      var nextStatus = (cur.status === "delivered") ? "delivered" : "draft";
      saveSubmission(mc.id, {
        text: textarea.value.trim(),
        status: nextStatus,
        updatedAt: new Date().toISOString()
      });
      if (nextStatus === "delivered") {
        showFeedback("Cambios guardados en tu entrega registrada sin internet.", true, false);
      } else {
        updateCardBadge("draft");
        showFeedback("Borrador guardado en este dispositivo (no requiere internet).", true, false);
      }
      renderGradesView();
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var txt = textarea.value.trim();
      if (txt.length < 15) {
        showFeedback("Revisión previa: escribe al menos dos ideas claras basadas en los datos (mínimo 15 caracteres).", false, true);
        textarea.focus();
        return;
      }

      var curEval = loadSelfEval(mc.id);
      if (Object.keys(curEval).length < totalCrit) {
        showFeedback("Revisión previa pendiente: antes de registrar tu entrega, valora los " + totalCrit + " criterios de la rúbrica en la sección de Autoevaluación.", false, true);
        var selfPanelEl = panel.querySelector("#wsSelfPanel");
        if (selfPanelEl && selfPanelEl.scrollIntoView) {
          selfPanelEl.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        return;
      }

      saveSubmission(mc.id, {
        text: txt,
        status: "delivered",
        updatedAt: new Date().toISOString()
      });
      updateCardBadge("delivered");
      renderGradesView();
      showFeedback("¡Entrega registrada! Tu análisis y autoevaluación quedaron guardados en este dispositivo.", true, false);
    });

    function buildReceiptObject(callback) {
      var sess = getCurrentSession() || { id: "demo", name: "Carlos Arturo" };
      var txt = textarea.value.trim();
      var curSub = loadSubmission(mc.id) || {};
      var curEval = loadSelfEval(mc.id);
      var isoNow = new Date().toISOString();

      // Sincroniza texto vivo antes de exportar
      saveSubmission(mc.id, {
        text: txt,
        status: curSub.status === "delivered" ? "delivered" : "draft",
        updatedAt: isoNow
      });

      var obj = {
        plataforma: "Aula 301 — IISUABJO",
        actividad_id: mc.id,
        actividad: mc.titulo,
        matricula: sess.id,
        estudiante: sess.name,
        fecha_generacion: isoNow,
        fecha_local: new Date().toLocaleString("es-MX"),
        estado_entrega: curSub.status === "delivered" ? "ENTREGADA" : "BORRADOR",
        conclusiones_estudiante: txt,
        autoevaluacion_rubrica: curEval
      };
      var payload = buildCanonicalPayload(obj);
      computeIntegrityHash(payload, function (hex) {
        obj.firma_integridad_sha256 = hex;
        callback(obj);
      });
    }

    exportBtn.addEventListener("click", function () {
      var txt = textarea.value.trim();
      if (!txt) {
        showFeedback("Escribe primero tu análisis antes de descargar tu constancia.", false, true);
        return;
      }
      buildReceiptObject(function (receipt) {
        var jsonStr = JSON.stringify(receipt, null, 2);
        var blob = new Blob([jsonStr], { type: "application/json;charset=utf-8" });
        var dateTag = receipt.fecha_generacion.slice(0, 10).replace(/-/g, "");
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "aula301_minicaso" + mc.id + "_" + normalizeSlug(receipt.matricula) + "_" + dateTag + ".json";
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
          URL.revokeObjectURL(a.href);
          a.remove();
        }, 500);
        showFeedback("Constancia descargada (" + receipt.estado_entrega + "). Puedes enviarla a tu docente por WhatsApp, correo o USB.", true, false);
      });
    });

    copyWaBtn.addEventListener("click", function () {
      var txt = textarea.value.trim();
      if (!txt) {
        showFeedback("Escribe primero tu análisis para poder copiar tu constancia.", false, true);
        return;
      }
      buildReceiptObject(function (receipt) {
        var payloadCompact = JSON.stringify(receipt);
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(payloadCompact).then(function () {
            showFeedback("Constancia copiada al portapapeles. Pégala directo en tu mensaje de WhatsApp al docente.", true, false);
          }).catch(function () {
            copyTxtArea.value = payloadCompact;
            copyBox.classList.remove("hidden");
            copyTxtArea.select();
          });
        } else {
          copyTxtArea.value = payloadCompact;
          copyBox.classList.remove("hidden");
          copyTxtArea.select();
        }
      });
    });
  }

  function renderActivitiesStack() {
    var stack = document.getElementById("activitiesStack");
    if (!stack || !data.miniCasos) return;
    stack.innerHTML = "";

    data.miniCasos.forEach(function (mc) {
      var sub = loadSubmission(mc.id);
      var statusLabel = mc.estadoDefault || "Disponible";
      var statusClass = "status-pill";
      if (sub && sub.status === "delivered") {
        statusLabel = "Entregada";
        statusClass = "status-pill delivered";
      } else if (sub && sub.status === "draft") {
        statusLabel = "Borrador guardado";
      }

      var card = document.createElement("article");
      card.className = "activity-card-carlos";
      card.id = "cardActividad" + mc.id;
      var isOpen = activeWorkspaceId === mc.id;

      card.innerHTML =
        '<div class="activity-card-top">' +
          '<div class="activity-card-badge">' + escapeHtml(mc.badge) + '</div>' +
          '<span class="' + statusClass + '" id="badgeActividad' + mc.id + '">' + escapeHtml(statusLabel) + '</span>' +
        '</div>' +
        '<h3 class="activity-card-title">' + escapeHtml(mc.titulo) + '</h3>' +
        '<p class="activity-card-desc">' + escapeHtml(mc.descripcion) + '</p>' +
        '<div class="activity-card-footer">' +
          '<span class="activity-meta">' + escapeHtml(mc.meta) + '</span>' +
          '<button type="button" class="btn small" id="toggleActividad' + mc.id + 'Btn" aria-expanded="' + (isOpen ? "true" : "false") + '">' +
            (isOpen ? "Cerrar detalle" : "Ver detalle y resolver") +
          '</button>' +
        '</div>';

      stack.appendChild(card);

      var btn = card.querySelector("#toggleActividad" + mc.id + "Btn");
      btn.addEventListener("click", function () {
        activeWorkspaceId = (activeWorkspaceId === mc.id) ? null : mc.id;
        renderActivitiesStack();
        if (activeWorkspaceId === mc.id) {
          var wsEl = document.getElementById("workspaceMinicaso" + mc.id);
          if (wsEl && wsEl.scrollIntoView) wsEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
        }
      });

      if (isOpen) {
        stack.appendChild(buildWorkspaceNode(mc));
      }
    });
  }

  // ========================================================================
  // Vista Mis Calificaciones (Dinámica para los 3 Minicasos)
  // ========================================================================
  function computeEvalScore(evalObj) {
    var keys = Object.keys(evalObj || {});
    if (keys.length === 0) return null;
    var sum = 0;
    var scale = data.escalaAutoevaluacion || { "Logrado": 10.0, "En proceso": 7.2, "Inicial": 4.0 };
    keys.forEach(function (k) {
      sum += Number(scale[evalObj[k]] || 4.0);
    });
    return sum / keys.length;
  }

  function renderGradesView() {
    var sess = getCurrentSession() || { name: "Carlos Arturo" };
    var studentNameEl = document.getElementById("gradesStudentName");
    if (studentNameEl) studentNameEl.textContent = sess.name;

    var stack = document.getElementById("gradesCardsStack");
    var completedEl = document.getElementById("metricsCompleted");
    var statusEl = document.getElementById("metricsStatus");
    var overallEl = document.getElementById("overallGradeVal");
    if (!stack || !data.miniCasos) return;

    stack.innerHTML = "";
    var deliveredCount = 0;
    var sumGrades = 0;
    var gradedCount = 0;

    data.miniCasos.forEach(function (mc) {
      var sub = loadSubmission(mc.id);
      var evalObj = loadSelfEval(mc.id);
      var isDelivered = sub && sub.status === "delivered";
      if (isDelivered) {
        deliveredCount++;
        var sc = computeEvalScore(evalObj);
        if (sc !== null) {
          sumGrades += sc;
          gradedCount++;
        }
      }

      var card = document.createElement("article");
      card.className = "grade-card";

      var pillClass = isDelivered ? "status-pill delivered" : "status-pill";
      var pillText = isDelivered ? "Entregada" : (sub && sub.status === "draft" ? "En borrador" : "Sin entregar");

      var evalSummaryHtml = "";
      var critKeys = Object.keys(evalObj);
      if (critKeys.length > 0) {
        evalSummaryHtml = '<div style="background:var(--lilac-soft);border-radius:10px;padding:10px 12px;margin-top:8px;font-size:0.88rem"><strong>Autoevaluación:</strong> ' +
          critKeys.map(function (k) { return escapeHtml(k) + ": " + escapeHtml(evalObj[k]); }).join(" · ") +
          '</div>';
      }

      var bodyHtml = isDelivered
        ? '<p><strong>Estado:</strong> Entregada localmente (' + (sub.updatedAt ? escapeHtml(new Date(sub.updatedAt).toLocaleString("es-MX")) : "Hoy") + ').</p>' +
          '<p style="margin-top:6px"><strong>Tu análisis:</strong> "' + escapeHtml(sub.text) + '"</p>' +
          evalSummaryHtml +
          '<p style="color:#166534;margin-top:8px;font-weight:700">Trabajo listo para compartir con tu docente.</p>'
        : '<p style="color:var(--muted)">Aún no registras tu entrega final para este minicaso. Ve a <em>Mis actividades</em> para resolverlo.</p>';

      card.innerHTML =
        '<div class="grade-card-top">' +
          '<span class="tag">' + escapeHtml(mc.badge) + '</span>' +
          '<span class="' + pillClass + '">' + escapeHtml(pillText) + '</span>' +
        '</div>' +
        '<h3>' + escapeHtml(mc.titulo) + '</h3>' +
        '<div class="grade-card-body">' + bodyHtml + '</div>';

      stack.appendChild(card);
    });

    if (completedEl) completedEl.textContent = String(deliveredCount);
    if (statusEl) statusEl.textContent = deliveredCount > 0 ? (deliveredCount === data.miniCasos.length ? "Proyecto completo" : "En avance") : "En proceso";
    if (overallEl) overallEl.textContent = gradedCount > 0 ? (sumGrades / gradedCount).toFixed(1) : "--";
  }

  // ========================================================================
  // Controles Docentes: Rol con clave, Actividades locales y Bandeja Real
  // ========================================================================
  function setRoleUI(roleKey) {
    var safeRole = data.roles[roleKey] ? roleKey : "estudiante";
    document.body.setAttribute("data-role", safeRole);
    var statusEl = document.getElementById("roleStatus");
    if (statusEl) statusEl.textContent = data.roles[safeRole].label;

    var btns = document.querySelectorAll("[data-role-btn]");
    for (var i = 0; i < btns.length; i++) {
      btns[i].setAttribute("aria-pressed", btns[i].getAttribute("data-role-btn") === safeRole ? "true" : "false");
    }
  }

  function renderAddedActivities() {
    var container = document.getElementById("addedList");
    if (!container) return;
    container.innerHTML = "";
    var list = loadStoredActivities();

    list.forEach(function (act) {
      var card = document.createElement("article");
      card.className = "activity-card-carlos";
      card.innerHTML =
        '<div class="activity-card-top">' +
          '<div class="activity-card-badge">Actividad adicional</div>' +
          '<span class="status-pill scheduled">Creada en este equipo</span>' +
        '</div>' +
        '<h3 class="activity-card-title">' + escapeHtml(act.title) + '</h3>' +
        '<p class="activity-card-desc">' + escapeHtml(act.desc) + '</p>' +
        '<div class="hidden" id="extraDetail_' + act.id + '" style="background:var(--lilac-soft);border-radius:10px;padding:10px 12px;font-size:0.88rem">' +
          (act.rubric ? '<strong>Criterios:</strong><br>' + escapeHtml(act.rubric).replace(/\n/g, "<br>") : '<em>Sin rúbrica adicional especificada.</em>') +
        '</div>' +
        '<div class="activity-card-footer">' +
          '<span class="activity-meta">Guardada localmente</span>' +
          '<div style="display:flex;gap:8px;flex-wrap:wrap">' +
            '<button type="button" class="btn secondary small" data-toggle-extra="' + act.id + '">Ver criterios</button>' +
            '<button type="button" class="btn secondary small" data-del-extra="' + act.id + '">Quitar</button>' +
          '</div>' +
        '</div>';

      card.querySelector("[data-toggle-extra]").addEventListener("click", function () {
        var box = card.querySelector("#extraDetail_" + act.id);
        var isHidden = box.classList.toggle("hidden");
        this.textContent = isHidden ? "Ver criterios" : "Ocultar criterios";
      });
      card.querySelector("[data-del-extra]").addEventListener("click", function () {
        var next = loadStoredActivities().filter(function (x) { return x.id !== act.id; });
        saveStoredActivities(next);
        renderAddedActivities();
      });
      container.appendChild(card);
    });
  }

  function renderTeacherRoster() {
    var listEl = document.getElementById("importedReceiptsList");
    var countEl = document.getElementById("rosterCountLabel");
    if (!listEl) return;

    var roster = loadRoster();
    listEl.innerHTML = "";
    if (countEl) countEl.textContent = roster.length + " entrega(s) consolidada(s)";

    roster.forEach(function (entry, idx) {
      var card = document.createElement("article");
      card.className = "grade-card";

      var badgeClass = entry.integrity === "ok" ? "status-pill delivered" : (entry.integrity === "paper" ? "status-pill scheduled" : "status-pill warn");
      var badgeLabel = entry.integrity === "ok" ? "Archivo íntegro" : (entry.integrity === "paper" ? "Libreta / Papel (DUA)" : "Archivo alterado o sin sello");

      var evalChips = "";
      var ev = entry.autoevaluacion || {};
      var evKeys = Object.keys(ev);
      if (evKeys.length > 0) {
        evalChips = '<div style="background:var(--lilac-soft);border-radius:10px;padding:8px 12px;margin-top:6px;font-size:0.84rem"><strong>Autoevaluación del alumno:</strong><br>' +
          evKeys.map(function (k) { return "• " + escapeHtml(k) + ": <b>" + escapeHtml(ev[k]) + "</b>"; }).join("<br>") +
        '</div>';
      }

      card.innerHTML =
        '<div class="grade-card-top">' +
          '<span class="tag">' + escapeHtml(entry.actividad || ("Minicaso " + entry.actividad_id)) + ' · ' + escapeHtml(entry.estado_entrega || "ENTREGADA") + '</span>' +
          '<span class="' + badgeClass + '">' + escapeHtml(badgeLabel) + '</span>' +
        '</div>' +
        '<h3>' + escapeHtml(entry.estudiante) + ' <small style="font-weight:600;color:var(--muted)">(' + escapeHtml(entry.matricula) + ')</small></h3>' +
        '<p style="font-size:0.84rem;color:var(--muted)">Fecha registrada: ' + escapeHtml(entry.fecha_local || entry.fecha_generacion || "Hoy") + ' · Modalidad: ' + escapeHtml(entry.modalidad || "Digital offline") + '</p>' +
        '<p style="margin-top:4px"><strong>Análisis entregado:</strong> "' + escapeHtml(entry.conclusiones) + '"</p>' +
        evalChips +
        (entry.hash ? '<details style="margin-top:6px;font-size:0.78rem;color:var(--muted)"><summary style="cursor:pointer;min-height:36px">Detalles técnicos de verificación</summary><p style="word-break:break-all;margin:4px 0">Huella digital local: ' + escapeHtml(entry.hash) + '</p></details>' : '') +
        '<div class="teacher-eval-row">' +
          '<input type="number" min="0" max="10" step="0.5" placeholder="Nota (0-10)" aria-label="Calificación docente" value="' + escapeHtml(entry.notaDocente || "") + '" data-grade-idx="' + idx + '">' +
          '<input type="text" placeholder="Retroalimentación formativa del docente..." aria-label="Retroalimentación docente" value="' + escapeHtml(entry.obsDocente || "") + '" data-obs-idx="' + idx + '">' +
        '</div>';

      var gInput = card.querySelector("[data-grade-idx]");
      var oInput = card.querySelector("[data-obs-idx]");
      gInput.addEventListener("change", function () {
        var r = loadRoster();
        if (r[idx]) { r[idx].notaDocente = gInput.value; saveRoster(r); }
      });
      oInput.addEventListener("change", function () {
        var r = loadRoster();
        if (r[idx]) { r[idx].obsDocente = oInput.value; saveRoster(r); }
      });

      listEl.appendChild(card);
    });
  }

  function upsertRosterEntry(entry) {
    var roster = loadRoster();
    var matNorm = normalizeSlug(entry.matricula || entry.estudiante);
    var actKey = String(entry.actividad_id || "1");
    var foundIdx = -1;
    for (var i = 0; i < roster.length; i++) {
      if (normalizeSlug(roster[i].matricula) === matNorm && String(roster[i].actividad_id) === actKey) {
        foundIdx = i;
        break;
      }
    }
    if (foundIdx >= 0) {
      // Conservar nota y observaciones previas del docente si existían
      entry.notaDocente = roster[foundIdx].notaDocente || "";
      entry.obsDocente = roster[foundIdx].obsDocente || "";
      roster[foundIdx] = entry;
    } else {
      roster.unshift(entry);
    }
    saveRoster(roster);
    renderTeacherRoster();
  }

  function ingestReceiptJsonString(rawText, sourceLabel) {
    var receipt = safeParse(rawText, null);
    if (!receipt || (!receipt.estudiante && !receipt.conclusiones_estudiante)) {
      return false;
    }
    var canonicalObj = {
      matricula: receipt.matricula || normalizeSlug(receipt.estudiante),
      estudiante: receipt.estudiante || "Estudiante",
      actividad_id: receipt.actividad_id || 1,
      actividad: receipt.actividad || "Minicaso 1",
      estado_entrega: receipt.estado_entrega || "ENTREGADA",
      fecha_generacion: receipt.fecha_generacion || "",
      conclusiones_estudiante: receipt.conclusiones_estudiante || "",
      autoevaluacion_rubrica: receipt.autoevaluacion_rubrica || {}
    };

    var payload = buildCanonicalPayload(canonicalObj);
    computeIntegrityHash(payload, function (calculated) {
      var validFormat = /^[a-f0-9]{64}$/i.test(receipt.firma_integridad_sha256 || "");
      var integrityState = (validFormat && calculated === receipt.firma_integridad_sha256) ? "ok" : "bad";

      upsertRosterEntry({
        matricula: canonicalObj.matricula,
        estudiante: canonicalObj.estudiante,
        actividad_id: canonicalObj.actividad_id,
        actividad: canonicalObj.actividad,
        estado_entrega: canonicalObj.estado_entrega,
        fecha_generacion: canonicalObj.fecha_generacion,
        fecha_local: receipt.fecha_local || "Sin fecha",
        modalidad: sourceLabel || "Constancia digital offline",
        conclusiones: canonicalObj.conclusiones_estudiante,
        autoevaluacion: canonicalObj.autoevaluacion_rubrica,
        hash: receipt.firma_integridad_sha256 || "",
        integrity: integrityState
      });
    });
    return true;
  }

  function setupTeacherControls() {
    var offlineBtn = document.getElementById("offlineBtn");
    var offlinePanel = document.getElementById("offlineHelpPanel");
    if (offlineBtn && offlinePanel) {
      offlineBtn.addEventListener("click", function () {
        var hidden = offlinePanel.classList.toggle("hidden");
        offlineBtn.setAttribute("aria-expanded", hidden ? "false" : "true");
      });
    }

    var pinBox = document.getElementById("teacherPinPrompt");
    var pinInput = document.getElementById("teacherPinInput");
    var pinConfirm = document.getElementById("confirmTeacherPinBtn");
    var pinCancel = document.getElementById("cancelTeacherPinBtn");
    var pinErr = document.getElementById("teacherPinError");

    var roleBtns = document.querySelectorAll("[data-role-btn]");
    for (var i = 0; i < roleBtns.length; i++) {
      (function (btn) {
        btn.addEventListener("click", function () {
          var targetRole = btn.getAttribute("data-role-btn");
          if (targetRole === "docente" && !teacherUnlockedInSession) {
            if (pinBox) pinBox.classList.remove("hidden");
            if (pinErr) pinErr.classList.add("hidden");
            if (pinInput) { pinInput.value = ""; pinInput.focus(); }
            return;
          }
          setRoleUI(targetRole);
        });
      })(roleBtns[i]);
    }

    if (pinConfirm) {
      pinConfirm.addEventListener("click", function () {
        var val = (pinInput ? pinInput.value : "").trim();
        if (val === "3010") {
          teacherUnlockedInSession = true;
          if (pinBox) pinBox.classList.add("hidden");
          setRoleUI("docente");
          renderTeacherRoster();
        } else if (pinErr) {
          pinErr.textContent = "Clave incorrecta. Para demostración del Grupo 301 usa: 3010.";
          pinErr.classList.remove("hidden");
        }
      });
    }

    if (pinCancel) {
      pinCancel.addEventListener("click", function () {
        if (pinBox) pinBox.classList.add("hidden");
      });
    }

    // Selección de archivos + Drag & Drop
    var dropZone = document.getElementById("receiptDropZone");
    var fileInput = document.getElementById("importReceiptsInput");
    var triggerBtn = document.getElementById("triggerImportBtn");

    function handleFiles(fileList) {
      if (!fileList || !fileList.length) return;
      for (var j = 0; j < fileList.length; j++) {
        (function (file) {
          var reader = new FileReader();
          reader.onload = function (ev) {
            var ok = ingestReceiptJsonString(ev.target.result, "Archivo (" + file.name + ")");
            if (!ok) {
              alert("El archivo '" + file.name + "' no corresponde a una constancia válida de Aula 301.");
            }
          };
          reader.readAsText(file);
        })(fileList[j]);
      }
    }

    if (triggerBtn && fileInput) {
      triggerBtn.addEventListener("click", function () { fileInput.click(); });
      fileInput.addEventListener("change", function (e) {
        handleFiles(e.target.files);
        e.target.value = "";
      });
    }

    if (dropZone) {
      dropZone.addEventListener("dragover", function (e) {
        e.preventDefault();
        dropZone.classList.add("drag-over");
      });
      dropZone.addEventListener("dragleave", function () {
        dropZone.classList.remove("drag-over");
      });
      dropZone.addEventListener("drop", function (e) {
        e.preventDefault();
        dropZone.classList.remove("drag-over");
        if (e.dataTransfer && e.dataTransfer.files) {
          handleFiles(e.dataTransfer.files);
        }
      });
    }

    // Procesar texto pegado desde WhatsApp
    var pasteBtn = document.getElementById("processPastedBtn");
    var pasteArea = document.getElementById("pasteReceiptInput");
    if (pasteBtn && pasteArea) {
      pasteBtn.addEventListener("click", function () {
        var txt = pasteArea.value.trim();
        if (!txt) return;
        var ok = ingestReceiptJsonString(txt, "Mensaje pegado (WhatsApp)");
        if (ok) {
          pasteArea.value = "";
        } else {
          alert("El texto pegado no contiene una constancia válida.");
        }
      });
    }

    // Registro manual en papel / libreta (DUA)
    var paperForm = document.getElementById("paperRecordForm");
    if (paperForm) {
      paperForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var mat = document.getElementById("paperMat").value.trim();
        var name = document.getElementById("paperName").value.trim();
        var actId = document.getElementById("paperActId").value;
        var obs = document.getElementById("paperObs").value.trim();
        if (!mat || !name) return;

        var mc = data.miniCasos.filter(function (x) { return String(x.id) === String(actId); })[0];
        upsertRosterEntry({
          matricula: mat,
          estudiante: name,
          actividad_id: Number(actId),
          actividad: mc ? mc.titulo : ("Minicaso " + actId),
          estado_entrega: "ENTREGADA (PAPEL)",
          fecha_generacion: new Date().toISOString(),
          fecha_local: new Date().toLocaleString("es-MX"),
          modalidad: "Práctica en libreta / papel",
          conclusiones: obs || "(Trabajo revisado en formato impreso/libreta en clase)",
          autoevaluacion: {},
          hash: "",
          integrity: "paper"
        });
        paperForm.reset();
      });
    }

    // Exportar concentrado CSV docente con BOM UTF-8
    var exportRosterBtn = document.getElementById("exportRosterCsvBtn");
    if (exportRosterBtn) {
      exportRosterBtn.addEventListener("click", function () {
        var roster = loadRoster();
        var lines = ["matricula,estudiante,minicaso,modalidad,estado,integridad,calificacion_docente,observaciones_docente,conclusiones"];
        roster.forEach(function (r) {
          lines.push([
            csvEscapeCell(r.matricula),
            csvEscapeCell(r.estudiante),
            csvEscapeCell(r.actividad),
            csvEscapeCell(r.modalidad),
            csvEscapeCell(r.estado_entrega),
            csvEscapeCell(r.integrity === "ok" ? "Integro" : (r.integrity === "paper" ? "Papel/Libreta" : "Revisar")),
            csvEscapeCell(r.notaDocente || ""),
            csvEscapeCell(r.obsDocente || ""),
            csvEscapeCell(r.conclusiones)
          ].join(","));
        });
        var blob = new Blob(["\uFEFF" + lines.join("\n")], { type: "text/csv;charset=utf-8;" });
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "aula301_concentrado_entregas.csv";
        document.body.appendChild(a);
        a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
      });
    }

    var clearRosterBtn = document.getElementById("clearRosterBtn");
    if (clearRosterBtn) {
      clearRosterBtn.addEventListener("click", function () {
        if (confirm("¿Deseas vaciar la lista local de entregas en este equipo?")) {
          saveRoster([]);
          renderTeacherRoster();
        }
      });
    }

    var addForm = document.getElementById("addForm");
    if (addForm) {
      addForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var title = document.getElementById("addTitle").value.trim();
        var desc = document.getElementById("addDesc").value.trim();
        var rubric = document.getElementById("addRubric").value.trim();
        if (!title || !desc) return;
        var list = loadStoredActivities();
        list.push({ id: Date.now(), title: title, desc: desc, rubric: rubric });
        saveStoredActivities(list);
        renderAddedActivities();
        addForm.reset();
      });
    }

    renderAddedActivities();
    renderTeacherRoster();
  }

  // ========================================================================
  // Visor Declarativo de Tablas Curriculares (1 a 6) y Glosario Educativo
  // ========================================================================
  function setupResourcesAndTables() {
    var container = document.getElementById("curriculumTableContent");
    if (container && data.tablasAdecuacionCurricular) {
      var buttons = [1, 2, 3, 4, 5, 6].map(function (n) {
        return { id: "showTable" + n + "Btn", num: n };
      });

      function renderTable(tableNum) {
        var found = data.tablasAdecuacionCurricular.filter(function (t) { return t.numero === tableNum; })[0];
        if (!found) return;

        var html = '<h4 style="margin:0 0 6px 0;color:var(--purple-dark)">Tabla ' + found.numero + ': ' + escapeHtml(found.titulo) + '</h4>' +
          '<p style="font-size:0.88rem;color:var(--muted);margin-bottom:12px">' + escapeHtml(found.descripcion) + '</p>' +
          '<div style="overflow-x:auto"><table class="rubric" style="width:100%;font-size:0.86rem"><thead><tr>';

        found.columnas.forEach(function (col) {
          html += '<th>' + escapeHtml(col) + '</th>';
        });
        html += '</tr></thead><tbody>';

        found.filas.forEach(function (row) {
          html += '<tr>';
          found.campos.forEach(function (campo, idx) {
            var txt = escapeHtml(row[campo] || "");
            html += '<td>' + (idx === 0 ? '<strong>' + txt + '</strong>' : txt) + '</td>';
          });
          html += '</tr>';
        });
        html += '</tbody></table></div>';
        container.innerHTML = html;

        buttons.forEach(function (b) {
          var el = document.getElementById(b.id);
          if (el) el.className = (b.num === tableNum) ? "btn small" : "btn secondary small";
        });
      }

      buttons.forEach(function (b) {
        var el = document.getElementById(b.id);
        if (el) el.addEventListener("click", function () { renderTable(b.num); });
      });

      renderTable(5);
    }

    var glossaryEl = document.getElementById("glossaryContainer");
    if (glossaryEl && data.glosarioEducativo) {
      glossaryEl.innerHTML = "";
      data.glosarioEducativo.forEach(function (g) {
        var det = document.createElement("details");
        det.className = "glossary-item";
        det.innerHTML = '<summary>' + escapeHtml(g.termino) + '</summary>' +
          '<p style="margin:6px 0 4px 0;font-size:0.9rem;color:var(--ink)">' + escapeHtml(g.definicion) + '</p>';
        glossaryEl.appendChild(det);
      });
    }
  }

  function registerServiceWorker() {
    if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost" || location.hostname === "127.0.0.1")) {
      window.addEventListener("load", function () {
        navigator.serviceWorker.register("./sw.js").catch(function () {});
      });
    }
  }

  // Inicializar plataforma
  renderActivitiesStack();
  renderGradesView();
  setupTeacherControls();
  setupResourcesAndTables();
  setupSessionAndNavigation();
  registerServiceWorker();
})();

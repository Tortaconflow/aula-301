/**
 * Aula 301 — Lógica de interfaz, persistencia offline y navegación
 */
(function () {
  var data = window.AULA301_DATA;
  var answers = {};
  var editingRubric = false;

  // Claves de almacenamiento local (Offline Persistence)
  var STORAGE_KEYS = {
    user: "aula301_session_user",
    role: "aula301_session_role",
    activities: "aula301_teacher_activities",
    selfEval: "aula301_self_evaluation",
    submission1: "aula301_submission_act1",
    toggleAuto: "aula301_toggle_auto",
    toggleCo: "aula301_toggle_co"
  };

  // Cargar datos previos de localStorage de forma segura
  function loadStoredSubmission() {
    try {
      var raw = localStorage.getItem(STORAGE_KEYS.submission1);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  }

  function saveStoredSubmission(sub) {
    try {
      localStorage.setItem(STORAGE_KEYS.submission1, JSON.stringify(sub));
    } catch (e) {}
  }

  // Cargar datos previos de localStorage de forma segura
  function loadStoredActivities() {
    try {
      var raw = localStorage.getItem(STORAGE_KEYS.activities);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function saveStoredActivities(activities) {
    try {
      localStorage.setItem(STORAGE_KEYS.activities, JSON.stringify(activities));
    } catch (e) {}
  }

  function loadStoredSelfEval() {
    try {
      var raw = localStorage.getItem(STORAGE_KEYS.selfEval);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function saveStoredSelfEval(ans) {
    try {
      localStorage.setItem(STORAGE_KEYS.selfEval, JSON.stringify(ans));
    } catch (e) {}
  }

  // 1. Renderizar tabla y gráfica del minicaso desde la fuente única de verdad
  function renderMinicaso() {
    var tbody = document.getElementById("caseTableBody");
    var barsContainer = document.getElementById("caseBars");
    if (!tbody || !barsContainer) return;

    tbody.innerHTML = "";
    barsContainer.innerHTML = "";

    data.minicasoEjemplo.categorias.forEach(function (item) {
      var tr = document.createElement("tr");
      var tdCat = document.createElement("td");
      tdCat.textContent = item.categoria;
      var tdCasos = document.createElement("td");
      tdCasos.className = "num";
      tdCasos.textContent = String(item.casos);
      var tdPct = document.createElement("td");
      tdPct.className = "num";
      tdPct.textContent = item.porcentajeTexto;
      tr.appendChild(tdCat);
      tr.appendChild(tdCasos);
      tr.appendChild(tdPct);
      tbody.appendChild(tr);

      var row = document.createElement("div");
      row.className = "bar-row";
      var label = document.createElement("span");
      label.textContent = item.categoria;
      var strong = document.createElement("strong");
      strong.textContent = item.porcentajeTexto;
      var track = document.createElement("div");
      track.className = "bar-track";
      var fill = document.createElement("div");
      fill.className = "bar-fill";
      fill.style.width = item.porcentajeAncho + "%";
      track.appendChild(fill);
      row.appendChild(label);
      row.appendChild(strong);
      row.appendChild(track);
      barsContainer.appendChild(row);
    });
  }

  // 2. Renderizar rúbrica y formulario de autoevaluación con persistencia offline
  function renderRubricaYAutoevaluacion() {
    var rubricBody = document.getElementById("rubricTableBody");
    var selfCriteriaContainer = document.getElementById("selfCriteriaList");
    if (!rubricBody || !selfCriteriaContainer) return;

    rubricBody.innerHTML = "";
    selfCriteriaContainer.innerHTML = "";

    answers = loadStoredSelfEval();
    var totalCriterios = data.rubricaEjemplo.criterios.length;

    data.rubricaEjemplo.criterios.forEach(function (item, idx) {
      // Fila de la tabla de rúbrica
      var tr = document.createElement("tr");
      var tdCrit = document.createElement("td");
      var strongCrit = document.createElement("strong");
      strongCrit.textContent = item.criterio;
      tdCrit.appendChild(strongCrit);

      var tdLogrado = document.createElement("td");
      tdLogrado.textContent = item.logrado;
      var tdProceso = document.createElement("td");
      tdProceso.textContent = item.enProceso;
      var tdInicial = document.createElement("td");
      tdInicial.textContent = item.inicial;

      tr.appendChild(tdCrit);
      tr.appendChild(tdLogrado);
      tr.appendChild(tdProceso);
      tr.appendChild(tdInicial);
      rubricBody.appendChild(tr);

      // Bloque de autoevaluación correspondiente al mismo criterio
      var block = document.createElement("div");
      block.setAttribute("data-crit", item.criterio);
      if (idx > 0) {
        block.className = "crit-block";
      }
      var titleStrong = document.createElement("strong");
      titleStrong.textContent = item.criterio;
      block.appendChild(titleStrong);

      var grid = document.createElement("div");
      grid.className = "eval-grid";

      data.rubricaEjemplo.niveles.forEach(function (nivel) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.textContent = nivel;
        if (answers[item.criterio] === nivel) {
          btn.classList.add("sel");
        }

        btn.addEventListener("click", function () {
          grid.querySelectorAll("button").forEach(function (b) {
            b.classList.remove("sel");
          });
          btn.classList.add("sel");
          answers[item.criterio] = nivel;
          saveStoredSelfEval(answers);
          updateSelfSummary(totalCriterios);
        });
        grid.appendChild(btn);
      });

      block.appendChild(grid);
      selfCriteriaContainer.appendChild(block);
    });

    updateSelfSummary(totalCriterios);
  }

  function updateSelfSummary(totalCriterios) {
    var done = Object.keys(answers).length;
    var summaryEl = document.getElementById("selfSummary");
    if (!summaryEl) return;

    if (done === 0) {
      summaryEl.textContent = "Sin respuestas todavía.";
      return;
    }

    var txt =
      done === totalCriterios
        ? "Autoevaluación completa en este dispositivo: "
        : "Llevas " + done + " de " + totalCriterios + " criterios guardados localmente. ";
    if (done === totalCriterios) {
      txt +=
        Object.keys(answers)
          .map(function (k) {
            return k + ": " + answers[k];
          })
          .join(" · ") + ".";
    }
    summaryEl.textContent = txt;
  }

  // 3. Descarga de CSV usando la misma fuente de verdad del minicaso
  function setupCsvDownload() {
    var csvBtn = document.getElementById("csvBtn");
    if (!csvBtn) return;

    csvBtn.addEventListener("click", function () {
      var minicaso = data.minicasoEjemplo;
      var total = minicaso.total;
      var lines = ["categoria,casos,total,porcentaje"];
      minicaso.categorias.forEach(function (r) {
        var pct = Math.round((r.casos / total) * 1000) / 10;
        lines.push('"' + r.categoria + '",' + r.casos + "," + total + "," + pct);
      });
      lines.push("");
      lines.push(minicaso.csvNote);

      var blob = new Blob([lines.join("\n")], { type: "text/csv;charset=utf-8" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = minicaso.csvFilename;
      document.body.appendChild(a);
      a.click();
      setTimeout(function () {
        URL.revokeObjectURL(a.href);
        a.remove();
      }, 400);
    });
  }

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // 4. Navegación entre vistas únicas
  function showView(name) {
    ["inicio", "actividades", "calificaciones", "recursos"].forEach(function (v) {
      var el = document.getElementById("view-" + v);
      if (!el) return;
      el.classList.toggle("hidden", v !== name);
      if (v === name) el.scrollTop = 0;
    });
    document.querySelectorAll("[data-nav]").forEach(function (b) {
      b.setAttribute("aria-current", b.getAttribute("data-nav") === name ? "true" : "false");
    });
    if (name === "calificaciones") {
      renderGradesView();
    }
  }

  function setupNavigation() {
    document.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () {
        showView(b.getAttribute("data-nav"));
      });
    });
  }

  // 5. Login de demostración con memoria local
  function setupLogin() {
    var forgotBtn = document.getElementById("forgotBtn");
    var loginForm = document.getElementById("loginForm");
    var logoutBtn = document.getElementById("logoutBtn");

    if (forgotBtn) {
      forgotBtn.addEventListener("click", function () {
        document.getElementById("forgotMsg").classList.remove("hidden");
      });
    }

    if (loginForm) {
      loginForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var u = document.getElementById("loginUser").value.trim();
        var displayName = "Carlos Arturo";
        if (u && !/^\d+$/.test(u)) {
          var first = u.split(/\s+/)[0];
          displayName = first.charAt(0).toUpperCase() + first.slice(1);
        }
        document.getElementById("greetName").textContent = displayName;
        try {
          localStorage.setItem(STORAGE_KEYS.user, displayName);
        } catch (err) {}

        document.getElementById("loginView").classList.add("hidden");
        document.getElementById("appView").classList.remove("hidden");
        showView("inicio");
      });
    }

    if (logoutBtn) {
      logoutBtn.addEventListener("click", function () {
        document.getElementById("appView").classList.add("hidden");
        document.getElementById("loginView").classList.remove("hidden");
        document.getElementById("loginPass").value = "";
        try {
          localStorage.removeItem(STORAGE_KEYS.user);
        } catch (err) {}
      });
    }

    // Auto-restaurar sesión guardada localmente si ya había iniciado
    try {
      var savedUser = localStorage.getItem(STORAGE_KEYS.user);
      if (savedUser) {
        document.getElementById("greetName").textContent = savedUser;
        document.getElementById("loginView").classList.add("hidden");
        document.getElementById("appView").classList.remove("hidden");
        showView("inicio");
      }
    } catch (err) {}
  }

  // 6. Selector de rol, simulación offline y persistencia de actividades del docente
  function renderAddedCard(activity, idx) {
    var count = document.querySelectorAll(".activity-card-carlos").length;
    var num = count + 1;
    var card = document.createElement("article");
    card.className = "activity-card-carlos";
    card.innerHTML =
      '<div class="activity-card-top">' +
        '<div class="activity-card-badge">Actividad ' + num + '</div>' +
        '<span class="status-pill scheduled">Creada por docente</span>' +
      '</div>' +
      '<h3 class="activity-card-title">' + escapeHtml(activity.title) + '</h3>' +
      '<p class="activity-card-desc">' + escapeHtml(activity.desc) + '</p>' +
      (activity.rubric ? '<div style="font-size:0.86rem;background:var(--lilac-soft);border-radius:10px;padding:8px 12px;margin-top:6px;"><strong>Rúbrica:</strong> ' + escapeHtml(activity.rubric) + '</div>' : '') +
      '<div class="activity-card-footer">' +
        '<span class="activity-meta">Almacenada localmente</span>' +
        '<button type="button" class="btn secondary small">Ver detalles</button>' +
      '</div>';

    var container = document.getElementById("addedList");
    if (container) container.appendChild(card);
  }

  // 7. Espacio de trabajo de Actividad 1 y Entrega Offline-First
  function setupActivityWorkspaceAndSubmission() {
    var toggleBtn = document.getElementById("toggleActividad1Btn");
    var workspace = document.getElementById("workspaceActividad1");
    var badgeAct1 = document.getElementById("badgeActividad1");
    var submissionForm = document.getElementById("submissionForm");
    var submissionText = document.getElementById("submissionText");
    var saveDraftBtn = document.getElementById("saveDraftBtn");
    var exportBtn = document.getElementById("exportSubmissionBtn");
    var feedbackEl = document.getElementById("submissionFeedback");

    // Restaurar entrega previa si existe
    var savedSub = loadStoredSubmission();
    if (savedSub) {
      if (submissionText && savedSub.text) submissionText.value = savedSub.text;
      if (savedSub.status === "delivered") {
        if (badgeAct1) {
          badgeAct1.textContent = "Entregada";
          badgeAct1.className = "status-pill delivered";
        }
      }
    }

    if (toggleBtn && workspace) {
      toggleBtn.addEventListener("click", function () {
        var isOpen = workspace.classList.toggle("is-open");
        toggleBtn.textContent = isOpen ? "Cerrar detalle" : "Ver detalle y resolver";
      });
    }

    function showFeedback(msg, isSuccess) {
      if (!feedbackEl) return;
      feedbackEl.textContent = msg;
      feedbackEl.classList.remove("hidden");
      feedbackEl.style.color = isSuccess ? "#15803d" : "#b45309";
      feedbackEl.style.borderColor = isSuccess ? "rgba(22, 163, 74, 0.3)" : "rgba(235, 148, 12, 0.35)";
      feedbackEl.style.background = isSuccess ? "rgba(22, 163, 74, 0.12)" : "rgba(235, 148, 12, 0.12)";
      setTimeout(function () {
        feedbackEl.classList.add("hidden");
      }, 5000);
    }

    if (saveDraftBtn && submissionText) {
      saveDraftBtn.addEventListener("click", function () {
        var txt = submissionText.value.trim();
        saveStoredSubmission({
          text: txt,
          status: "draft",
          updatedAt: new Date().toISOString()
        });
        showFeedback("Borrador guardado localmente (Offline)", true);
      });
    }

    if (submissionForm && submissionText) {
      submissionForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var txt = submissionText.value.trim();
        if (!txt) return;

        saveStoredSubmission({
          text: txt,
          status: "delivered",
          updatedAt: new Date().toISOString()
        });

        if (badgeAct1) {
          badgeAct1.textContent = "Entregada";
          badgeAct1.className = "status-pill delivered";
        }

        showFeedback("¡Actividad 1 entregada con éxito! Registro persistido localmente.", true);
        renderGradesView();
      });
    }

    if (exportBtn && submissionText) {
      exportBtn.addEventListener("click", function () {
        var sub = loadStoredSubmission() || { text: submissionText.value.trim(), status: "draft" };
        var selfEval = loadStoredSelfEval();
        var student = document.getElementById("greetName") ? document.getElementById("greetName").textContent : "Carlos Arturo";
        var receipt = {
          plataforma: "Aula 301 — IISUABJO",
          actividad: "Actividad 1: Acceso tecnológico y participación en clase",
          estudiante: student,
          fecha_generacion: new Date().toLocaleString("es-MX"),
          estado_entrega: sub.status === "delivered" ? "ENTREGADA" : "BORRADOR",
          conclusiones_estudiante: sub.text || "(Sin texto)",
          autoevaluacion_rubrica: selfEval
        };

        var blob = new Blob([JSON.stringify(receipt, null, 2)], { type: "application/json;charset=utf-8" });
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "comprobante_entrega_actividad_1.json";
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
          URL.revokeObjectURL(a.href);
          a.remove();
        }, 400);
      });
    }
  }

  // 8. Renderizado dinámico de Mis calificaciones
  function renderGradesView() {
    var studentName = document.getElementById("greetName") ? document.getElementById("greetName").textContent : "Carlos Arturo";
    var gradesStudentEl = document.getElementById("gradesStudentName");
    if (gradesStudentEl) gradesStudentEl.textContent = studentName;

    var sub = loadStoredSubmission();
    var selfEval = loadStoredSelfEval();
    var isDelivered = sub && sub.status === "delivered";

    var completedEl = document.getElementById("metricsCompleted");
    var statusEl = document.getElementById("metricsStatus");
    var gradeCircleVal = document.getElementById("overallGradeVal");
    var gradeCardStatus1 = document.getElementById("gradeCardStatus1");
    var gradeCardBody1 = document.getElementById("gradeCardBody1");

    if (completedEl) completedEl.textContent = isDelivered ? "1" : "0";
    if (statusEl) statusEl.textContent = isDelivered ? "Al corriente" : "En proceso";

    // Calcular puntaje estimado basado en la autoevaluación
    var criterios = Object.keys(selfEval);
    if (isDelivered) {
      if (gradeCardStatus1) {
        gradeCardStatus1.textContent = "Entregada";
        gradeCardStatus1.className = "status-pill delivered";
      }

      var logradoCount = 0;
      criterios.forEach(function (k) {
        if (selfEval[k] === "Logrado") logradoCount += 2.5;
        else if (selfEval[k] === "En proceso") logradoCount += 1.8;
        else logradoCount += 1.0;
      });
      var estimatedGrade = criterios.length > 0 ? (logradoCount / (criterios.length * 2.5) * 10).toFixed(1) : "10";
      if (gradeCircleVal) gradeCircleVal.textContent = estimatedGrade;

      if (gradeCardBody1) {
        gradeCardBody1.innerHTML =
          '<p><strong>Estado:</strong> Entregada con registro local (' + (sub.updatedAt ? new Date(sub.updatedAt).toLocaleTimeString("es-MX") : "Hoy") + ').</p>' +
          '<p style="margin-top:6px"><strong>Tus conclusiones:</strong> "' + escapeHtml(sub.text) + '"</p>' +
          '<div style="background:var(--lilac-soft);border-radius:10px;padding:10px 12px;margin-top:8px;">' +
            '<strong>Autoevaluación:</strong> ' +
            (criterios.length > 0
              ? criterios.map(function(k){ return k + ": " + selfEval[k]; }).join(" · ")
              : "Pendiente de marcar criterios") +
          '</div>' +
          '<p style="color:#15803d;margin-top:8px;font-weight:700;">✓ Trabajo listo para revisión del docente.</p>';
      }
    } else {
      if (gradeCircleVal) gradeCircleVal.textContent = "--";
      if (gradeCardStatus1) {
        gradeCardStatus1.textContent = "Sin entregar";
        gradeCardStatus1.className = "status-pill";
      }
      if (gradeCardBody1) {
        gradeCardBody1.innerHTML = '<p style="color:var(--muted)">Aún no has registrado tu entrega o autoevaluación para esta actividad. Ve a "Mis actividades" para completarla.</p>';
      }
    }
  }

  function setupRoleAndTeacherControls() {
    var storedActivities = loadStoredActivities();
    if (storedActivities.length > 0) {
      storedActivities.forEach(renderAddedCard);
      document
        .getElementById("emptyActivities")
        .querySelector("p").textContent =
        "Hay " + storedActivities.length + " actividad(es) guardada(s) en este dispositivo.";
    }

    document.querySelectorAll("[data-role-btn]").forEach(function (b) {
      b.addEventListener("click", function () {
        var r = b.getAttribute("data-role-btn");
        var d = data.roles[r];
        if (!d) return;
        document.body.setAttribute("data-role", r);
        document.getElementById("roleStatus").textContent = d.label;
        document.getElementById("greetName").textContent = d.name;
        document.querySelectorAll("[data-role-btn]").forEach(function (x) {
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
      });
    });

    var offBtn = document.getElementById("offlineBtn");
    if (offBtn) {
      function updateOnlineState(simulated) {
        var isOnline = simulated !== undefined ? !simulated : navigator.onLine;
        offBtn.setAttribute("aria-pressed", isOnline ? "false" : "true");
        offBtn.textContent = isOnline ? "Simular sin conexión" : "Modo sin conexión: activo";
      }

      offBtn.addEventListener("click", function () {
        var currentlySimulated = offBtn.getAttribute("aria-pressed") === "true";
        updateOnlineState(!currentlySimulated);
      });

      window.addEventListener("online", function () { updateOnlineState(false); });
      window.addEventListener("offline", function () { updateOnlineState(true); });
    }

    var addForm = document.getElementById("addForm");
    if (addForm) {
      addForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var title = document.getElementById("addTitle").value.trim();
        var desc = document.getElementById("addDesc").value.trim();
        var rubric = document.getElementById("addRubric").value.trim();
        if (!title || !desc) return;

        var newActivity = { title: title, desc: desc, rubric: rubric, id: Date.now() };
        var list = loadStoredActivities();
        list.push(newActivity);
        saveStoredActivities(list);

        renderAddedCard(newActivity);
        document
          .getElementById("emptyActivities")
          .querySelector("p").textContent =
          "Hay " + list.length + " actividad(es) guardada(s) en este dispositivo.";
        e.target.reset();
      });
    }

    function bindToggle(id, storageKey, panelId) {
      var el = document.getElementById(id);
      if (!el) return;
      var saved = localStorage.getItem(storageKey) === "true";
      if (saved) {
        el.setAttribute("aria-pressed", "true");
        document.getElementById(panelId).classList.remove("hidden");
      }

      el.addEventListener("click", function () {
        var v = el.getAttribute("aria-pressed") === "true";
        var next = !v;
        el.setAttribute("aria-pressed", next ? "true" : "false");
        document.getElementById(panelId).classList.toggle("hidden", !next);
        try {
          localStorage.setItem(storageKey, String(next));
        } catch (err) {}
      });
    }

    bindToggle("toggleAuto", STORAGE_KEYS.toggleAuto, "selfPanel");
    bindToggle("toggleCo", STORAGE_KEYS.toggleCo, "coPanel");

    var editRubricBtn = document.getElementById("editRubricBtn");
    if (editRubricBtn) {
      editRubricBtn.addEventListener("click", function () {
        editingRubric = !editingRubric;
        this.textContent = editingRubric ? "Terminar edición" : "Editar rúbrica de ejemplo";
        document.querySelectorAll("#rubricTable tbody td").forEach(function (td) {
          td.contentEditable = editingRubric ? "true" : "false";
        });
      });
    }
  }

  // 7. Registro de Service Worker para funcionamiento 100% Offline
  function registerServiceWorker() {
    if ("serviceWorker" in navigator) {
      window.addEventListener("load", function () {
        navigator.serviceWorker.register("./sw.js").then(function (reg) {
          console.log("Service Worker registrado con éxito para Aula 301:", reg.scope);
        }).catch(function (err) {
          console.log("Fallo al registrar Service Worker:", err);
        });
      });
    }
  }

  // Inicializar todo
  renderMinicaso();
  renderRubricaYAutoevaluacion();
  setupCsvDownload();
  setupNavigation();
  setupLogin();
  setupActivityWorkspaceAndSubmission();
  renderGradesView();
  setupRoleAndTeacherControls();
  registerServiceWorker();
})();

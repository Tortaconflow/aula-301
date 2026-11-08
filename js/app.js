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
    toggleAuto: "aula301_toggle_auto",
    toggleCo: "aula301_toggle_co"
  };

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
  function renderAddedCard(activity) {
    var card = document.createElement("article");
    card.className = "added-card";
    var h = document.createElement("h3");
    h.textContent = activity.title;
    var p = document.createElement("p");
    p.textContent = activity.desc;
    card.appendChild(h);
    card.appendChild(p);

    if (activity.rubric) {
      var r = document.createElement("div");
      r.className = "rub";
      r.textContent = "Rúbrica:\n" + activity.rubric;
      card.appendChild(r);
    }

    var tag = document.createElement("p");
    tag.style.marginTop = "10px";
    var strongTag = document.createElement("strong");
    strongTag.textContent = "Agregada por el docente (Guardada localmente)";
    tag.appendChild(strongTag);
    card.appendChild(tag);

    document.getElementById("addedList").appendChild(card);
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
  setupRoleAndTeacherControls();
  registerServiceWorker();
})();

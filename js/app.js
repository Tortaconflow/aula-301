/**
 * Aula 301 — Lógica de interfaz y navegación por vistas
 */
(function () {
  var data = window.AULA301_DATA;
  var answers = {};
  var editingRubric = false;

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

  // 2. Renderizar rúbrica y formulario de autoevaluación desde la misma fuente de verdad
  function renderRubricaYAutoevaluacion() {
    var rubricBody = document.getElementById("rubricTableBody");
    var selfCriteriaContainer = document.getElementById("selfCriteriaList");
    if (!rubricBody || !selfCriteriaContainer) return;

    rubricBody.innerHTML = "";
    selfCriteriaContainer.innerHTML = "";

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
        btn.addEventListener("click", function () {
          grid.querySelectorAll("button").forEach(function (b) {
            b.classList.remove("sel");
          });
          btn.classList.add("sel");
          answers[item.criterio] = nivel;
          var done = Object.keys(answers).length;
          var txt =
            done === totalCriterios
              ? "Autoevaluación completa en esta sesión: "
              : "Llevas " + done + " de " + totalCriterios + " criterios. ";
          if (done === totalCriterios) {
            txt +=
              Object.keys(answers)
                .map(function (k) {
                  return k + ": " + answers[k];
                })
                .join(" · ") + ".";
          }
          document.getElementById("selfSummary").textContent = txt;
        });
        grid.appendChild(btn);
      });

      block.appendChild(grid);
      selfCriteriaContainer.appendChild(block);
    });
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
      if (b.classList.contains("portal-card")) return;
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

  // 5. Login de demostración y cierre de sesión
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
        if (u && !/^\d+$/.test(u)) {
          var first = u.split(/\s+/)[0];
          document.getElementById("greetName").textContent =
            first.charAt(0).toUpperCase() + first.slice(1);
        }
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
      });
    }
  }

  // 6. Selector de rol, simulación offline y herramientas del docente
  function bindToggle(id, onChange) {
    var el = document.getElementById(id);
    if (!el) return;
    el.addEventListener("click", function () {
      var v = el.getAttribute("aria-pressed") === "true";
      el.setAttribute("aria-pressed", v ? "false" : "true");
      onChange(!v);
    });
  }

  function setupRoleAndTeacherControls() {
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
      offBtn.addEventListener("click", function () {
        var on = offBtn.getAttribute("aria-pressed") === "true";
        offBtn.setAttribute("aria-pressed", on ? "false" : "true");
        offBtn.textContent = on ? "Simular sin conexión" : "Modo sin conexión: activo";
      });
    }

    var addForm = document.getElementById("addForm");
    if (addForm) {
      addForm.addEventListener("submit", function (e) {
        e.preventDefault();
        var title = document.getElementById("addTitle").value.trim();
        var desc = document.getElementById("addDesc").value.trim();
        var rub = document.getElementById("addRubric").value.trim();
        if (!title || !desc) return;

        var card = document.createElement("article");
        card.className = "added-card";
        var h = document.createElement("h3");
        h.textContent = title;
        var p = document.createElement("p");
        p.textContent = desc;
        card.appendChild(h);
        card.appendChild(p);

        if (rub) {
          var r = document.createElement("div");
          r.className = "rub";
          r.textContent = "Rúbrica:\n" + rub;
          card.appendChild(r);
        }

        var tag = document.createElement("p");
        tag.style.marginTop = "10px";
        var strongTag = document.createElement("strong");
        strongTag.textContent = "Agregada por el docente";
        tag.appendChild(strongTag);
        card.appendChild(tag);

        document.getElementById("addedList").appendChild(card);
        document
          .getElementById("emptyActivities")
          .querySelector("p").textContent =
          "Ya hay actividades agregadas por el docente en esta sesión.";
        e.target.reset();
        card.scrollIntoView({ behavior: "smooth", block: "center" });
      });
    }

    bindToggle("toggleAuto", function (enabled) {
      document.getElementById("selfPanel").classList.toggle("hidden", !enabled);
    });

    bindToggle("toggleCo", function (enabled) {
      document.getElementById("coPanel").classList.toggle("hidden", !enabled);
    });

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

  // Inicializar todo
  renderMinicaso();
  renderRubricaYAutoevaluacion();
  setupCsvDownload();
  setupNavigation();
  setupLogin();
  setupRoleAndTeacherControls();
})();

"use strict";

const pageTitles = {
  overview: "Regional Overview",
  sustain: "Sustain · Field Support",
  attract: "Attract · Digital Twin",
  bridge: "Bridge · Mentorship",
  analytics: "Evidence & Analytics",
};

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const money = (value, currency = "USD") =>
  new Intl.NumberFormat(undefined, {
    style: "currency",
    currency,
    maximumFractionDigits: 0,
  }).format(value);

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

let toastTimer;
function showToast(message) {
  const toast = $("#toast");
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("show"), 3200);
}

async function api(path, options = {}) {
  const response = await fetch(path, options);
  let payload;
  try {
    payload = await response.json();
  } catch {
    throw new Error(`Server returned ${response.status} without a JSON response.`);
  }
  if (!response.ok) {
    throw new Error(payload.detail || payload.message || `Request failed (${response.status}).`);
  }
  return payload;
}

function errorCard(error) {
  return `<div class="error-card"><b>Could not complete this check.</b><br>${escapeHtml(error.message)}</div>`;
}

function openPage(pageName) {
  if (!pageTitles[pageName]) return;
  $$(".page").forEach((page) => page.classList.toggle("active", page.id === pageName));
  $$(".nav-item").forEach((item) => item.classList.toggle("active", item.dataset.page === pageName));
  $("#pageTitle").textContent = pageTitles[pageName];
  $("#sidebar").classList.remove("open");
  window.scrollTo({ top: 0, behavior: "smooth" });
  if (pageName === "analytics") loadAnalytics();
}

$$('[data-page]').forEach((button) => button.addEventListener("click", () => openPage(button.dataset.page)));
$$('[data-go]').forEach((button) => button.addEventListener("click", () => openPage(button.dataset.go)));
$("#menuButton").addEventListener("click", () => $("#sidebar").classList.toggle("open"));

const moisture = $("#moisture");
moisture.addEventListener("input", () => {
  $("#moistureValue").textContent = `${moisture.value}%`;
});

$("#irrigationForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const output = $("#irrigationResult");
  output.innerHTML = '<div class="loading-card">Checking observation…</div>';
  try {
    const payload = await api("/api/v1/sustain/irrigation/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        soil_moisture_pct: Number(moisture.value),
        temp_c: Number($("#temperature").value),
        npk_nitrogen_ppm: Number($("#nitrogen").value),
        confirmed_cycles_this_week: Number($("#cycles").value),
        source_type: "manual",
      }),
    });
    const result = payload.data;
    const pumpOn = result.status === "PUMP_ON_RECOMMENDED";
    output.innerHTML = `
      <div class="recommendation-head">
        <div><p class="eyebrow green">GUARDED RESULT</p><h3 class="${pumpOn ? "status-on" : ""}">${pumpOn ? "Irrigation review suggested" : "No irrigation suggested"}</h3><p>${escapeHtml(payload.recommendation_context.summary)}</p></div>
        <span class="badge">${escapeHtml(payload.meta.data_status)}</span>
      </div>
      <div class="metric-strip">
        <div class="metric-box"><strong>${result.illustrative_volume_l} L</strong><span>Illustrative volume only</span></div>
        <div class="metric-box"><strong>${result.weekly_reclaimed_hours} h</strong><span>Estimated reclaimed time</span></div>
      </div>
      <div class="context-block"><b>Why</b><p>Moisture is ${result.soil_moisture_pct}% and the prototype threshold is ${result.threshold_pct}%.</p></div>
      <div class="context-block"><b>Important safeguard</b><p>${escapeHtml(payload.recommendation_context.safeguards[0])}</p></div>
      <div class="context-block"><b>Model limitation</b><p>${escapeHtml(result.limitations[0])}</p></div>`;
    showToast("Recommendation generated. Farmer review is still required.");
  } catch (error) {
    output.innerHTML = errorCard(error);
  }
});

const cropImage = $("#cropImage");
cropImage.addEventListener("change", () => {
  const file = cropImage.files[0];
  if (!file) return;
  $("#imagePreview").src = URL.createObjectURL(file);
  $("#dropZone").classList.add("has-image");
});

$("#cropForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const output = $("#cropResult");
  const file = cropImage.files[0];
  if (!file) {
    showToast("Choose a JPEG or PNG leaf image first.");
    return;
  }
  output.innerHTML = '<div class="loading-card">Analysing visible colour regions…</div>';
  try {
    const formData = new FormData();
    formData.append("image", file);
    const payload = await api("/api/v1/sustain/crop-screenings", { method: "POST", body: formData });
    const result = payload.data;
    const flagged = result.screening_label === "POSSIBLE_LEAF_STRESS_REVIEW";
    output.innerHTML = `
      <div class="recommendation-head">
        <div><p class="eyebrow green">PRELIMINARY SCREENING</p><h3>${flagged ? "Visible stress pattern needs review" : "No large visible lesion detected"}</h3><p>${escapeHtml(payload.recommendation_context.summary)}</p></div>
        <span class="badge">Low confidence</span>
      </div>
      <div class="screening-meter"><div class="meter-track"><div class="meter-fill" style="width:${Math.min(result.lesion_percent, 100)}%"></div></div><div class="meter-labels"><span>0%</span><b>${result.lesion_percent}% colour region</b><span>100%</span></div></div>
      <div class="context-block"><b>Prototype trigger</b><p>Review is suggested above ${result.threshold_percent}%. This is colour segmentation, not disease identification.</p></div>
      <div class="context-block"><b>Next safe action</b><p>${escapeHtml(payload.recommendation_context.safeguards[0])}</p></div>
      <div class="context-block"><b>Limitations</b><p>${escapeHtml(result.limitations.join(" "))}</p></div>`;
  } catch (error) {
    output.innerHTML = errorCard(error);
  }
});

$("#simulationForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const output = $("#simulationResult");
  output.innerHTML = '<div class="loading-card">Calculating three five-year scenarios…</div>';
  try {
    const payload = await api("/api/v1/attract/simulations", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        land_area_ha: Number($("#landArea").value),
        initial_capital: Number($("#capital").value),
        tech_level: $("#techLevel").value,
        climate_shock: $("#climateShock").checked,
        price_per_kg: Number($("#cropPrice").value),
        annual_operating_cost: Number($("#operatingCost").value),
        technology_investment: Number($("#techInvestment").value),
        currency: "USD",
      }),
    });
    const result = payload.data;
    const maxMagnitude = Math.max(...result.scenarios.flatMap((scenario) => scenario.years.map((year) => Math.abs(year.net_profit))), 1);
    const cards = result.scenarios.map((scenario) => {
      const bars = scenario.years.map((year) => `<i title="Year ${year.year}: ${money(year.net_profit, result.currency)}" style="height:${Math.max(4, Math.abs(year.net_profit) / maxMagnitude * 100)}%"></i>`).join("");
      return `<article class="scenario-card ${scenario.name === "central" ? "central" : ""}"><h4>${escapeHtml(scenario.name)}</h4><strong>${money(scenario.five_year_net_profit, result.currency)}</strong><small>5-year net profit</small><strong class="roi">${scenario.five_year_roi_pct}%</strong><small>Illustrative cumulative ROI</small><div class="mini-bars">${bars}</div></article>`;
    }).join("");
    const assumptions = result.assumptions;
    output.innerHTML = `
      <div class="panel-heading"><div><p class="eyebrow blue-text">SCENARIO COMPARISON</p><h3>Five-year illustrative outcomes</h3></div><span class="badge">Not a forecast</span></div>
      <div class="scenario-cards">${cards}</div>
      <div class="assumption-grid">
        <div><b>Base yield</b><span>${assumptions.base_yield_kg_ha} kg/ha</span></div>
        <div><b>Technology factor</b><span>${assumptions.technology_yield_factor}× yield</span></div>
        <div><b>Climate factor</b><span>${assumptions.climate_factor}× yield</span></div>
      </div>
      <div class="context-block"><b>Decision safeguard</b><p>${escapeHtml(payload.recommendation_context.safeguards[0])}</p></div>`;
  } catch (error) {
    output.innerHTML = errorCard(error);
  }
});

$("#findMatches").addEventListener("click", async () => {
  const output = $("#matchResults");
  output.innerHTML = '<article class="panel loading-card">Ranking consented profiles…</article>';
  const demoProfiles = {
    mentor: { display_name: "U Min Htet", lat: 16.8409, lon: 96.1735, crops: ["rice", "pulses"], offered_ha: 2, matching_consent: true },
    candidates: [
      { candidate_id: "learner-001", display_name: "Su Myat", approximate_area: "North Yangon", lat: 16.895, lon: 96.155, crops: ["rice", "vegetables"], preferred_ha: 2, matching_consent: true },
      { candidate_id: "learner-002", display_name: "Ko Lin", approximate_area: "Bago Region", lat: 17.336, lon: 96.481, crops: ["pulses", "rice"], preferred_ha: 3, matching_consent: true },
      { candidate_id: "learner-003", display_name: "May Thu", approximate_area: "Ayeyarwady Region", lat: 16.779, lon: 95.75, crops: ["horticulture", "rice"], preferred_ha: 1, matching_consent: true },
      { candidate_id: "learner-private", display_name: "Private profile", approximate_area: "Hidden", lat: 16.9, lon: 96.1, crops: ["rice"], preferred_ha: 2, matching_consent: false },
    ],
  };
  try {
    const payload = await api("/api/v1/bridge/matches/suggest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(demoProfiles),
    });
    output.innerHTML = payload.data.map((match) => {
      const initials = match.display_name.split(/\s+/).map((part) => part[0]).join("").slice(0, 2);
      return `<article class="panel match-card"><div class="candidate-avatar">${escapeHtml(initials)}</div><div class="candidate-info"><h3>${escapeHtml(match.display_name)}</h3><p>${escapeHtml(match.approximate_area)} · ${match.distance_km} km · Shared: ${escapeHtml(match.shared_crops.join(", ") || "none")}</p><div class="score-line"><i style="width:${match.score_percent}%"></i></div></div><div class="match-score"><strong>${match.score_percent}%</strong><small>explainable fit</small></div><div class="match-actions"><span>Contacts hidden · waiting for mutual acceptance</span><button class="accept-match" data-name="${escapeHtml(match.display_name)}">Request introduction</button></div></article>`;
    }).join("") || '<article class="panel empty-match"><h3>No eligible profiles</h3><p>Only profiles with active matching consent are considered.</p></article>';
    $$(".accept-match", output).forEach((button) => button.addEventListener("click", () => {
      button.disabled = true;
      button.textContent = "Request recorded";
      showToast(`Demo request recorded for ${button.dataset.name}. Contact details remain hidden.`);
    }));
  } catch (error) {
    output.innerHTML = `<article class="panel">${errorCard(error)}</article>`;
  }
});

let analyticsLoaded = false;
async function loadAnalytics() {
  if (analyticsLoaded) return;
  const grid = $("#chartGrid");
  try {
    const payload = await api("/api/v1/analytics/charts");
    grid.innerHTML = payload.data.map((chart, index) => `
      <article class="panel chart-card">
        <p class="eyebrow">CHART ${String(index + 1).padStart(2, "0")}</p><h3>${escapeHtml(chart.title)}</h3>
        <div class="chart-placeholder" aria-label="Placeholder only; no numerical values available"><i></i><i></i><i></i><i></i><i></i></div>
        <footer><span class="missing-badge">DATA MISSING</span><p>${escapeHtml(chart.message)}</p></footer>
      </article>`).join("");
    analyticsLoaded = true;
  } catch (error) {
    grid.innerHTML = errorCard(error);
  }
}

$("#countrySelect").addEventListener("change", (event) => {
  showToast(`Country context changed to ${event.target.selectedOptions[0].text}. Demo formulas remain unchanged.`);
});

api("/api/v1/health")
  .then(() => showToast("AgriVision demonstration system is ready."))
  .catch(() => showToast("Backend is not reachable. Start the FastAPI server first."));

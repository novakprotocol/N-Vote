const repo = "https://github.com/novakprotocol/N-Vote";
const json = path => fetch(path, { cache: "no-store" }).then(response => response.json());
const reactions = item => item.reactions || { "+1": 0, heart: 0, rocket: 0, eyes: 0 };
const link = item => item.url || `${repo}/issues/${item.issue_number}`;
const text = value => String(value ?? "");
const escapeHtml = value => text(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

function requestType(item) {
  return item.request_type || (item.area === "application-request" ? "application-request" : "request");
}

function renderAreas(areasData, requestsData, top5Data) {
  const container = document.getElementById("area-cards");
  container.innerHTML = "";
  (areasData.records || []).forEach(area => {
    const openCount = (requestsData.records || []).filter(item => item.area === area.slug && item.state !== "closed").length;
    const top = (top5Data.records || []).find(item => item.scope === "area" && item.area === area.slug);
    const kinds = (area.request_kinds || []).map(kind => `<span class="pill">${escapeHtml(kind)}</span>`).join("");
    container.innerHTML += `<article class="card">
      <div class="slug">${escapeHtml(area.slug)}</div>
      <h3>${escapeHtml(area.display_name)}</h3>
      <p>${escapeHtml(area.description)}</p>
      ${kinds ? `<div class="pills">${kinds}</div>` : ""}
      <p><b>${openCount}</b> open requests</p>
      <p><b>${top ? (top.top5 || []).length : 0}</b> top requests</p>
    </article>`;
  });
}

function renderApplicationRequests(data) {
  const container = document.getElementById("application-request-cards");
  const items = (data.records || []).filter(item => item.area === "application-request" || requestType(item) === "application-request");
  container.innerHTML = "";
  if (!items.length) {
    container.innerHTML = '<div class="item">No public application requests yet.</div>';
    return;
  }
  items.sort((a, b) => (b.score || 0) - (a.score || 0)).forEach(item => {
    const kinds = (item.request_kinds_supported || ["app", "web app", "game", "overlay", "docs", "other"])
      .map(kind => `<span class="pill">${escapeHtml(kind)}</span>`).join("");
    container.innerHTML += `<div class="item">
      <h3><a href="${escapeHtml(link(item))}">#${escapeHtml(item.issue_number)} ${escapeHtml(item.title)}</a></h3>
      <p>Public request type: ${escapeHtml(requestType(item))} · Status: ${escapeHtml(item.status || "status:submitted")} · Score: ${escapeHtml(item.score || 0)}</p>
      <div class="pills">${kinds}</div>
      <p class="muted">Public intake only. Owner approval is required before private implementation work.</p>
    </div>`;
  });
}

function renderRequests(data) {
  const body = document.getElementById("request-table");
  body.innerHTML = "";
  [...(data.records || [])].sort((a, b) => (b.score || 0) - (a.score || 0)).forEach((item, index) => {
    const vote = reactions(item);
    body.innerHTML += `<tr>
      <td>${index + 1}</td>
      <td>${escapeHtml(item.area || "other")}</td>
      <td>${escapeHtml(requestType(item))}</td>
      <td>${escapeHtml(item.title || "")}</td>
      <td>#${escapeHtml(item.issue_number || "")}</td>
      <td>${escapeHtml(item.status || "status:submitted")}</td>
      <td>${escapeHtml(item.score || 0)}</td>
      <td>${escapeHtml(vote["+1"] || 0)}</td>
      <td>${escapeHtml(vote.heart || 0)}</td>
      <td>${escapeHtml(vote.rocket || 0)}</td>
      <td>${escapeHtml(vote.eyes || 0)}</td>
      <td>${escapeHtml(item.opened_at || "")}</td>
      <td><a href="${escapeHtml(link(item))}">Open issue</a></td>
    </tr>`;
  });
}

function renderTop5(data) {
  const container = document.getElementById("top5");
  container.innerHTML = "";
  (data.records || []).forEach(group => {
    const title = group.scope === "overall" ? "Top 5 overall" : `Top 5 for ${group.area}`;
    const list = (group.top5 || []).map(item => `<li><a href="${escapeHtml(link(item))}">#${escapeHtml(item.issue_number)} ${escapeHtml(item.title)}</a> — score ${escapeHtml(item.score || 0)}</li>`).join("") || "<li>No public requests yet.</li>";
    container.innerHTML += `<div class="item"><h3>${escapeHtml(title)}</h3><ol>${list}</ol></div>`;
  });
}

function renderApproved(data) {
  const container = document.getElementById("approved-list");
  container.innerHTML = "";
  const items = data.records || [];
  if (!items.length) {
    container.innerHTML = '<div class="item">No approved-now public markers yet.</div>';
    return;
  }
  items.forEach(item => {
    container.innerHTML += `<div class="item">
      <h3><a href="${escapeHtml(link(item))}">#${escapeHtml(item.issue_number)} ${escapeHtml(item.title)}</a></h3>
      <p>Area: ${escapeHtml(item.area)} · Public status: ${escapeHtml(item.public_status || item.status || "approved-now")}</p>
      <p>Private work status: ${escapeHtml(item.private_work_status || "owner-approval-required")}</p>
    </div>`;
  });
}

Promise.all([
  json("data/areas.json"),
  json("data/requests.json"),
  json("data/friday-top5.json"),
  json("data/approved-now.json")
]).then(([areasData, requestsData, top5Data, approvedData]) => {
  renderAreas(areasData, requestsData, top5Data);
  renderApplicationRequests(requestsData);
  renderRequests(requestsData);
  renderTop5(top5Data);
  renderApproved(approvedData);
}).catch(error => {
  document.querySelector("main").innerHTML = `<section><h2>Data unavailable</h2><p>${escapeHtml(error.message)}</p></section>`;
});

// Handling full button linking in intake page
// To make it more user friendly
document.addEventListener("DOMContentLoaded", () => {
  const rows = document.querySelectorAll("tr[data-href]");
  rows.forEach((row) => {
    row.addEventListener("click", () => {
      window.location.assign(row.getAttribute("data-href"));
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const rows = document.querySelectorAll("tr[data-href]");
  console.log(rows);
  rows.forEach((row) => {
    row.addEventListener("click", () => {
      window.location.assign(row.getAttribute("data-href"));
    });
  });
});

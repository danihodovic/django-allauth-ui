document.addEventListener('DOMContentLoaded', function() {
  const theme = window.localStorage.getItem("allauth-theme") || "emerald";
  setTheme(theme);
  const select = document.getElementById("select-theme");
  select.value = theme;
}, false);

function onSelectChange() {
  const select = document.getElementById("select-theme");
  const theme = select.value;
  setTheme(theme);
}

function setTheme(theme) {
  const html = document.querySelector("html");
  html.dataset.theme = theme;
  window.localStorage.setItem("allauth-theme", theme);
}

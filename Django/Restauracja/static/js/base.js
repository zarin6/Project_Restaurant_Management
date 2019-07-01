document.getElementById("menu_button").addEventListener('mouseover', function() {
  document.getElementById("menu").style.display = "block";
});

document.getElementById("menu").addEventListener('mouseover', function() {
  document.getElementById("menu").style.display = "block";
});

document.getElementById("menu").addEventListener('mouseleave', function() {
  document.getElementById("menu").style.display = "none";
});

document.querySelector("header").addEventListener('mouseleave', function() {
  document.getElementById("menu").style.display = "none";
});
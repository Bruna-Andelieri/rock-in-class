document.addEventListener("DOMContentLoaded", function () {
  var urlParams = new URLSearchParams(window.location.search);
  var target = urlParams.get('scroll');

  if (target) {
    var targetElement = document.getElementById(target);

    if (targetElement) {
      targetElement.scrollIntoView({
        behavior: 'smooth'
      });
    }
  }
});


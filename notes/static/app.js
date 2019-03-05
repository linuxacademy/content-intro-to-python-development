document.addEventListener('DOMContentLoaded', function () {
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0),
    $deleteIcons = Array.prototype.slice.call(document.querySelectorAll('.delete'), 0);

  if ($navbarBurgers.length > 0) {
    $navbarBurgers.forEach(function($el) {
      $el.addEventListener('click', function() {
        var target = $el.dataset.target,
          $target = document.getElementById(target);
        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }

  if ($deleteIcons.length > 0) {
    $deleteIcons.forEach(function($el) {
      console.log("adding event listener", $el);
      $el.addEventListener('click', function() {
        var target = $el.dataset.target,
          $target = document.getElementById(target);
        $target.remove();
      });
    });
  }

  // Initialize syntax highlighting
  hljs.initHighlightingOnLoad();
});

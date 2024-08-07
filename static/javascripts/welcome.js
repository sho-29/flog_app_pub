
$(function() {
    $(window).scroll(function() {
      var scrollAnimationElm = document.querySelectorAll(".top-text",);
      var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
          var triggerMargin = 100;
          if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
            scrollAnimationElm[i].classList.add("on");
          }
        }
      }
      window.addEventListener("load", scrollAnimationFunc);
      window.addEventListener("scroll", scrollAnimationFunc);
    });
  });

  $(function() {
    $(window).scroll(function() {
      var scrollAnimationElm = document.querySelectorAll(".top-alert",);
      var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
          var triggerMargin = 100;
          if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
            scrollAnimationElm[i].classList.add("on");
          }
        }
      }
      window.addEventListener("load", scrollAnimationFunc);
      window.addEventListener("scroll", scrollAnimationFunc);
    });
  });

  $(function() {
    $(window).scroll(function() {
      var scrollAnimationElm = document.querySelectorAll(".top-alert",);
      var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
          var triggerMargin = 100;
          if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
            scrollAnimationElm[i].classList.add("on");
          }
        }
      }
      window.addEventListener("load", scrollAnimationFunc);
      window.addEventListener("scroll", scrollAnimationFunc);
    });
  });

  $(function() {
    $(window).scroll(function() {
      var scrollAnimationElm = document.querySelectorAll(".determine",);
      var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
          var triggerMargin = 100;
          if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
            scrollAnimationElm[i].classList.add("on");
          }
        }
      }
      window.addEventListener("load", scrollAnimationFunc);
      window.addEventListener("scroll", scrollAnimationFunc);
    });
  });


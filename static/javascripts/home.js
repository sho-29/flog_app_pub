document.addEventListener('DOMContentLoaded', function() {
  const container = document.querySelector('.card-container');
  const boxContainer = document.querySelector('.card-contents');
  const leftArrow = document.querySelector('.Arrow.left');
  const rightArrow = document.querySelector('.Arrow.right');
  const scrollAmount = 1100;

  leftArrow.addEventListener('click', () => {
    const containerWidth = container.offsetWidth;
    const maxScrollAmount = boxContainer.offsetWidth - containerWidth;
    const currentScrollAmount = Math.abs(parseInt(boxContainer.style.transform.split('(')[1])) || 0;
    const newScrollAmount = Math.max(currentScrollAmount - scrollAmount, 0);
    boxContainer.style.transform = `translateX(-${newScrollAmount}px)`;
    updateArrowVisibility(newScrollAmount, maxScrollAmount);
  });

  rightArrow.addEventListener('click', () => {
    const containerWidth = container.offsetWidth;
    const maxScrollAmount = boxContainer.offsetWidth - containerWidth;
    const currentScrollAmount = Math.abs(parseInt(boxContainer.style.transform.split('(')[1])) || 0;
    const newScrollAmount = Math.min(currentScrollAmount + scrollAmount, maxScrollAmount);
    boxContainer.style.transform = `translateX(-${newScrollAmount}px)`;
    updateArrowVisibility(newScrollAmount, maxScrollAmount);
  });

  function updateArrowVisibility(scrollAmount, maxScrollAmount) {
    if (scrollAmount === 0) {
      leftArrow.classList.add('Hide');
    } else {
      leftArrow.classList.remove('Hide');
    }

    if (scrollAmount === maxScrollAmount) {
      rightArrow.classList.add('Hide');
    } else {
      rightArrow.classList.remove('Hide');
    }
  }

  
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
      var scrollAnimationElm = document.querySelectorAll(".top-scenario",);
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
      var scrollAnimationElm = document.querySelectorAll(".post",);
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
});

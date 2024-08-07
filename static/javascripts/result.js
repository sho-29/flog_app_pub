// script.js
document.querySelectorAll('.quiz-toggle-button').forEach(function(button) {
    button.addEventListener('click', function() {
        var content = this.parentElement.nextElementSibling;
        if (content.style.display === 'block') {
            content.style.display = 'none';
            this.textContent = '解説を表示 ⬇️';
        } else {
            content.style.display = 'block';
            this.textContent = '解説を隠す ⬆️';
        }
    });
});

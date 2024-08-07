function showNextQuiz(current, total) {
    var currentQuiz = document.getElementById('quiz-' + current);
    var nextQuiz = document.getElementById('quiz-' + (current + 1));
    if (nextQuiz) {
        currentQuiz.style.display = 'none';
        nextQuiz.style.display = 'block';
    }
}

function showBeforeQuiz(current, total) {
    var currentQuiz = document.getElementById('quiz-' + current);
    var beforeQuiz = document.getElementById('quiz-' + (current -1));
    if (beforeQuiz) {
        currentQuiz.style.display = 'none';
        beforeQuiz.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    // ランダムにシャッフルする関数
    function shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }
    
    window.onload = function() {
        // すべてのクイズの選択肢を取得
        const boxes = document.querySelectorAll('.box');
    
        // 各クイズの選択肢をシャッフル
        boxes.forEach(box => {
            const options = Array.from(box.querySelectorAll('.option-label'));
            const shuffledOptions = shuffle(options);
            shuffledOptions.forEach(option => box.appendChild(option));
        });
    };
    //シャッフルここまで

});

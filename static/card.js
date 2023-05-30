// const questions = [
//     {
//         question: "Which of the following is NOT a primitive data type in Java?",
//         answers: [
//             { text: "int", correct: false },
//             { text: "boolean", correct: false },
//             { text: "string", correct: true },
//             { text: "char", correct: false }]

// const { json } = require("react-router-dom");

//     },
//     {
//         question: "Which of the following is used to create an object in Java?",
//         answers: [
//             { text: "new", correct: true },
//             { text: "create", correct: false },
//             { text: "object", correct: false },
//             { text: "init", correct: false }]
//     },
//     {
//         question: "What is the difference between "==" and .equals() in Java?",
//         answers: [
//             { text: "They are the same thing.", correct: false },
//             { text: " "==" is used to compare primitive data types, while equals() is used to compare objects.", correct: true },
//             { text: ".equals() is used to compare primitive data types, while == is used to compare objects.", correct: false },
//             { text: "None of the above.", correct: false }]

//     }
// ];
// window.location.href = "/gpt2";
var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 9000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}

// Retrieve the response from the cookie or local storage
var search = localStorage.getItem("search");
// Use the response for further processing and display
console.log(search);
$.ajax({
    type: 'POST',
    url: '/gpt',
    data: { search: search },
    success: function(response) {
        // Handle the response from the Flask route
        console.log(response);
        // var json = JSON.parse(response);
const questions = response
const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let score = 0;

function startQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHtml = "Next";
    showQuestion();
}


function showQuestion() {
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex + 1;
    questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

    currentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButtons.appendChild(button);
        if (answer.correct) {
            button.dataset.correct = answer.correct;
        }

        button.addEventListener("click", selectAnswer);
    });
}

function resetState() {
    nextButton.style.display = "none";
    while (answerButtons.firstChild) {
        answerButtons.removeChild(answerButtons.firstChild);
    }
}

function selectAnswer(e) {
    const selectedBtn = e.target;
    const isCorrect = selectedBtn.dataset.correct === "true";

    if (isCorrect) {
        selectedBtn.classList.add("correct");
        score++;
    }
    else {
        selectedBtn.classList.add("incorrect");
    }
    Array.from(answerButtons.children).forEach(button => {
        if (button.dataset.correct === "true") {
            button.classList.add("correct");
        }
        button.disabled = true;
    });
    nextButton.style.display = "block";
}


function showScore() {
    resetState();
    questionElement.innerHTML = `You scored ${score} out of ${questions.length}.`;
    nextButton.innerHTML = "Play Again";
    nextButton.style.display = "block";
}

function handleNextButton() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        showScore();
    }
}

nextButton.addEventListener("click", () => {
    if (currentQuestionIndex < questions.length) {
        handleNextButton();
    } else {
        startQuiz();
    }
});

startQuiz();

    },
    error: function(error) {
        console.error(error);
    }
});

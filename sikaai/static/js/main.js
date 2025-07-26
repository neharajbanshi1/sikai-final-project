document.addEventListener("DOMContentLoaded", () => {
    const mathCards = document.querySelectorAll(".math-card");
    let firstCard = null;
    let secondCard = null;
    let lock = false;

    mathCards.forEach(card => {
        card.addEventListener("click", () => {
            if (lock || card.classList.contains("matched") || card === firstCard) return;

            card.classList.add("flipped");

            if (!firstCard) {
                firstCard = card;
            } else {
                secondCard = card;
                lock = true;

                if (firstCard.dataset.match === secondCard.dataset.match) {
                    firstCard.classList.add("matched");
                    secondCard.classList.add("matched");
                    resetCards();
                } else {
                    setTimeout(() => {
                        firstCard.classList.remove("flipped");
                        secondCard.classList.remove("flipped");
                        resetCards();
                    }, 1000);
                }
            }
        });
    });

    function resetCards() {
        [firstCard, secondCard] = [null, null];
        lock = false;
    }
});
document.addEventListener("DOMContentLoaded", () => {
    const quizOptions = document.querySelectorAll(".quiz-option");

    quizOptions.forEach(option => {
        option.addEventListener("click", () => {
            // Reset all
            quizOptions.forEach(opt => {
                opt.style.backgroundColor = "#f3e8d3";
            });

            if (option.dataset.correct === "true") {
                option.style.backgroundColor = "#c6f6c6"; // green
            } else {
                option.style.backgroundColor = "#f6c6c6"; // red
            }
        });
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("chat-input");
    const button = document.getElementById("send-button");
    const chatBox = document.querySelector(".chat-messages");

    const responses = {
        "how do plants make food": "Plants make their food through photosynthesis! They use sunlight, water, and carbon dioxide to create glucose and oxygen.",
        "what is the capital of nepal": "The capital of Nepal is Kathmandu.",
        "hello": "Hi there! I'm happy you're here to learn!",
    };

    button.addEventListener("click", () => {
        const userMessage = input.value.trim();
        if (!userMessage) return;

        appendMessage("user", userMessage);
        const lower = userMessage.toLowerCase();
        const botReply = responses[lower] || "I'm not sure about that yet, but I'm still learning!";
        appendMessage("bot", botReply);
        input.value = "";
    });

    function appendMessage(sender, text) {
        const msg = document.createElement("div");
        msg.classList.add("message", sender === "bot" ? "bot-message" : "user-message");
        msg.textContent = text;
        chatBox.appendChild(msg);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});

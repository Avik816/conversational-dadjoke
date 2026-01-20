const chatSpace = document.querySelector(".chat-space");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");

/* Utility: scroll to bottom */
function scrollToBottom(smooth = true) {
    if (smooth) {
        chatSpace.scrollTo({
            top: chatSpace.scrollHeight,
            behavior: "smooth"
        });
    } else {
        chatSpace.scrollTop = chatSpace.scrollHeight;
    }
}

/* Create and add a message */
function addMessage(isAI, text) {
    const row = document.createElement("div");
    row.classList.add("message-row", isAI ? "ai-msg" : "user-msg");

    const avatar = document.createElement("img");
    avatar.classList.add("avatar");
    avatar.src = isAI ? "../elements/ai_icon.svg" : "../elements/user_icon.svg";
    avatar.alt = isAI ? "AI" : "User";

    const bubble = document.createElement("div");
    bubble.classList.add("message-bubble");
    bubble.textContent = text;

    if (isAI) {
        row.appendChild(avatar);
        row.appendChild(bubble);
    } else {
        row.appendChild(bubble);
        row.appendChild(avatar);
    }

    chatSpace.appendChild(row);
    scrollToBottom(true);
}

/* Fake AI response (placeholder) */
function getFakeAIResponse(userText) {
    const replies = [
        "😄 That's interesting!",
        "Tell me more!",
        "Haha, good one!",
        "I'm thinking about a joke for you...",
        "Nice! Want to hear something funny?"
    ];

    return replies[Math.floor(Math.random() * replies.length)];
}

/* Send message handler */
function sendMessage() {
    const text = userInput.value.trim();
    if (text === "") return;

    // Add user message
    addMessage(false, text);

    // Clear input
    userInput.value = "";

    // Simulate AI typing delay
    setTimeout(() => {
        const aiReply = getFakeAIResponse(text);
        addMessage(true, aiReply);
    }, 600); // 600ms delay (feels natural)
}

/* Click send button */
sendButton.addEventListener("click", sendMessage);

/* Press Enter to send */
userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});

const chatMessages = document.getElementById("chat-messages");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

// Auto-scroll chat to bottom
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

sendButton.addEventListener("click", () => {
    const userMessage  = messageInput.value.trim();
    if (message !== "") {
        // User message
        const userMessageElement = document.createElement("div");
        userMessageElement.textContent = "You: " + userMessage;
        chatMessages.appendChild(messageElement);

        // Response message
        const responseMessageElement = document.createElement("div");
        responseMessageElement.textContent = "Quanto: " + userMessage;
        chatMessages.appendChild(responseMessageElement);

        messageInput.value = "";
        scrollToBottom(); // Auto-scroll when new message added
    }
});

messageInput.addEventListener("keyup", (event) => {
    if (event.key === "Enter") {
        sendButton.click();
    }
});

// Initial auto-scroll to the bottom
scrollToBottom();

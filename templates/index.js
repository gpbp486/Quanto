const chatMessages = document.getElementById("chat-messages");
const messageInput = document.getElementById("message_input");
const sendButton = document.getElementById("send-button");
const quanto = document.getElementById("quanto-message");
const initialMessage = document.querySelector(".message"); // Find the message element in the DOM

// Auto-scroll chat to bottom
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Display the initial message
if (initialMessage) {
    const initialMessageText = initialMessage.textContent;
    const initialMessageElement = document.createElement("div");
    initialMessageElement.textContent = "Quanto: " + initialMessageText;
    chatMessages.appendChild(initialMessageElement);
}


messageInput.addEventListener("keyup", (event) => {
    if (event.key === "Enter") {
        sendButton.click();
    }
});


sendButton.addEventListener("click", async () => {
    const userMessage = messageInput.value.trim();
    if (userMessage !== "") {
        // User message
        const userMessageElement = document.createElement("div");
        userMessageElement.textContent = "You: " + userMessage;
        chatMessages.appendChild(userMessageElement);

        // Send the user's message to your server for processing by OpenAI
        const response = await sendMessageToServer(userMessage);

        // Response message
        const responseMessageElement = document.createElement("div");
        responseMessageElement.textContent = "Quanto: " + response;
        chatMessages.appendChild(responseMessageElement);

        messageInput.value = "";
        scrollToBottom(); // Auto-scroll when new message added
    }
});

// Define a function to send user's message to the server
async function sendMessageToServer(userMessage) {
    const response = await fetch('/' + userMessage);
    const data = await response.json();
    return data.answer;
}

// Initial auto-scroll to the bottom
scrollToBottom();

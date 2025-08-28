const API_URL = "http://127.0.0.1:8000"; // FastAPI backend URL

// Create a new chat session
export async function createSession() {
  const response = await fetch(`${API_URL}/session`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });

  if (!response.ok) {
    throw new Error("Failed to create session");
  }

  return await response.json();
}

// Send a message to the chatbot
export async function sendMessage(sessionId, message) {
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, message: message }),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  return await response.json();
}

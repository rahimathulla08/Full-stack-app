const API_URL = "http://127.0.0.1:8000"; // backend FastAPI URL

// Create a new session
export async function createSession() {
  const response = await fetch(`${API_URL}/session`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  if (!response.ok) throw new Error("Failed to create session");
  return response.json();
}

// Send a message to chatbot
export async function sendMessage(sessionId, message) {
  const response = await fetch("http://127.0.0.1:8000/api/Chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, message }),
  });
  if (!response.ok) throw new Error("Failed to send message");
  return response.json();
}

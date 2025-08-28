import React, { useState, useEffect } from "react";
import { createSession, sendMessage } from "../services/api";

function Chat() {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  // Create session when component loads
  useEffect(() => {
    async function init() {
      try {
        const session = await createSession();
        setSessionId(session.id);
      } catch (err) {
        console.error("Session creation failed:", err);
      }
    }
    init();
  }, []);

  // Handle sending a message
  async function handleSend() {
    if (!input.trim()) return;
    if (!sessionId) {
      alert("Session not ready yet. Please wait.");
      return;
    }

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await sendMessage(sessionId, input);
      const aiMessage = { role: "ai", content: response.reply };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (err) {
      console.error("Error sending message:", err);
    }

    setInput("");
  }

  return (
    <div style={{ maxWidth: "500px", margin: "0 auto" }}>
      <h2>Chatbot</h2>
      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          minHeight: "300px",
          overflowY: "auto",
        }}
      >
        {messages.map((m, i) => (
          <p key={i}>
            <b>{m.role === "user" ? "You" : "Bot"}:</b> {m.content}
          </p>
        ))}
      </div>
      <div style={{ marginTop: "10px" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ width: "80%", padding: "5px" }}
        />
        <button onClick={handleSend} style={{ width: "18%", marginLeft: "2%" }}>
          Send
        </button>
      </div>
    </div>
  );
}

export default Chat;

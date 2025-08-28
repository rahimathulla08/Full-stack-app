import React, { useState, useEffect, useRef } from "react";
import { createSession, sendMessage } from "../services/api";

function Chat() {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

  // Auto-scroll to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Create session on mount
  useEffect(() => {
    async function init() {
      try {
        const session = await createSession();
        setSessionId(session.session_id || session.id); // backend response key
      } catch (err) {
        console.error("❌ Session creation failed:", err);
      }
    }
    init();
  }, []);

  // Send message handler
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

      const aiMessage = {
        role: "ai",
        content:
          response.reply || response.answer || response.response || "🤖 No reply from server",
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (err) {
      console.error("❌ Error sending message:", err);
      setMessages((prev) => [
        ...prev,
        { role: "ai", content: "⚠️ Error contacting server" },
      ]);
    }

    setInput("");
  }

  // Handle Enter key press
  function handleKeyDown(e) {
    if (e.key === "Enter") {
      handleSend();
    }
  }

  return (
    <div style={{ maxWidth: "500px", margin: "0 auto" }}>
      <h2>💬 Chatbot</h2>
      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          minHeight: "300px",
          overflowY: "auto",
          borderRadius: "5px",
        }}
      >
        {messages.map((m, i) => (
          <p key={i}>
            <b>{m.role === "user" ? "You" : "Bot"}:</b> {m.content}
          </p>
        ))}
        <div ref={chatEndRef} />
      </div>
      <div style={{ marginTop: "10px", display: "flex", gap: "8px" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
          style={{ flex: 1, padding: "5px" }}
        />
        <button onClick={handleSend} style={{ padding: "5px 10px" }}>
          Send
        </button>
      </div>
    </div>
  );
}

export default Chat;

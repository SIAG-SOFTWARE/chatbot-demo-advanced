export default function ChatUI({ messages, onSend }) {
  return (
    <div style={{ width: "50%", margin: "auto", paddingTop: "40px" }}>
      <h2>🤖 SIAG Software – Advanced Chatbot</h2>

      <div style={{
        background: "#1f2833",
        padding: "20px",
        borderRadius: "10px",
        minHeight: "300px",
        color: "white"
      }}>
        {messages.map((m, i) => (
          <p key={i}><b>{m.role}:</b> {m.text}</p>
        ))}
      </div>

      <input
        id="msg"
        style={{ width: "80%", padding: "10px", marginTop: "15px" }}
        placeholder="Type a message..."
      />
      <button onClick={onSend} style={{ padding: "10px 15px" }}>
        Send
      </button>
    </div>
  );
}

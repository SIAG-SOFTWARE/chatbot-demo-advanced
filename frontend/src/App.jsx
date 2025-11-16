import { useState } from "react";
import ChatUI from "./ChatUI.jsx";
import { sendMessage } from "./api.js";

export default function App() {
  const [messages, setMessages] = useState([]);

  async function handleSend() {
    const input = document.getElementById("msg");
    const text = input.value;

    setMessages(prev => [...prev, { role: "You", text }]);

    const res = await sendMessage(text);

    setMessages(prev => [...prev, { role: "Bot", text: res.reply }]);
    input.value = "";
  }

  return <ChatUI messages={messages} onSend={handleSend} />;
}

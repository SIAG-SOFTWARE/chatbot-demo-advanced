export async function sendMessage(text) {
  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text })
  });

  return res.json();
}

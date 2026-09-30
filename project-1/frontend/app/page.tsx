"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`)
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("Backend unavailable"));
  }, []);

  return (
    <main>
      <h1>AI Project 1</h1>
      <p>Backend status: {status}</p>
    </main>
  );
}
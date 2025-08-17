import { useState } from "react";
import ReactJson from "react-json-view";
import "./index.css";

function App() {
  const [dataset, setDataset] = useState("patients");
  const [ids, setIds] = useState("");
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const API_BASE = "https://healthcare-data-apis.onrender.com"; // your Render URL

  async function handleSearch() {
    setError(null);
    setResults(null);

    try {
      const contexts = ids
        .split("\n")
        .map((id) => id.trim())
        .filter(Boolean);

      if (contexts.length === 0) {
        setError("Please enter at least one ID.");
        return;
      }

      const res = await fetch(`${API_BASE}/${dataset}/search_multiple`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contexts }),
      });

      if (!res.ok) throw new Error(`API error: ${res.status}`);
      const data = await res.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="panel">
      <h1>Healthcare Data Search</h1>

      <label>
        Choose dataset:{" "}
        <select value={dataset} onChange={(e) => setDataset(e.target.value)}>
          <option value="patients">Patients Data</option>
          <option value="finance">Finance Data</option>
          <option value="staff">Staff Data</option>
        </select>
      </label>

      <br /><br />

      <textarea
        rows="5"
        placeholder="Enter one or more IDs (newline separated)"
        value={ids}
        onChange={(e) => setIds(e.target.value)}
        style={{ width: "100%", padding: "8px" }}
      />

      <br /><br />
      <button onClick={handleSearch}>Search</button>

      {error && <p style={{ color: "red", marginTop: "1rem" }}>⚠️ {error}</p>}

      {results && (
        <div style={{ marginTop: "2rem" }}>
          <h2>Results</h2>
          <ReactJson src={results} theme="monokai" collapsed={2} />
        </div>
      )}
    </div>
  );
}

export default App;

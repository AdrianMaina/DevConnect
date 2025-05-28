import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Jobs from "./Jobs";
import Users from "./Users";

function App() {
  return (
    <Router>
      <div style={{ padding: 20 }}>
        <h1>DevConnect</h1>
        <nav>
          <Link to="/jobs" style={{ marginRight: 10 }}>Jobs</Link>
          <Link to="/users">Users</Link>
        </nav>

        <Routes>
          <Route path="/jobs" element={<Jobs />} />
          <Route path="/users" element={<Users />} />
          <Route path="/" element={<div>Welcome to DevConnect! Select a tab.</div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
import React from "react";

function JobCard({ job }) {
  return (
    <div style={{ border: "1px solid #ddd", padding: 10, marginBottom: 10, borderRadius: 5 }}>
      <h3>{job.title}</h3>
      <p><strong>Description:</strong> {job.description}</p>
      <p><strong>Tech Stack:</strong> {job.tech_stack}</p>
      <p><strong>Budget:</strong> ${job.budget}</p>
      <p><strong>Timeline:</strong> {job.timeline}</p>
    </div>
  );
}

export default JobCard;
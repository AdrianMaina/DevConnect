// src/components/ProposalForm.js
import React, { useState } from 'react';

const ProposalForm = ({ jobId }) => {
  const [proposal, setProposal] = useState({ rate: '', timeline: '', message: '' });
  const [status, setStatus] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('Submitting...');

    try {
      const response = await fetch('http://localhost:8000/proposals', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          job_id: jobId,
          rate: parseFloat(proposal.rate),
          timeline: proposal.timeline,
          message: proposal.message,
        }),
      });

      if (response.ok) {
        setStatus('Proposal submitted successfully!');
        setProposal({ rate: '', timeline: '', message: '' });
      } else {
        setStatus('Failed to submit proposal.');
      }
    } catch (error) {
      console.error('Error submitting proposal:', error);
      setStatus('Error occurred.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border rounded-lg bg-white shadow-md max-w-xl mx-auto mt-6">
      <h2 className="text-xl font-semibold mb-4">Submit Proposal</h2>
      <input
        type="number"
        placeholder="Hourly Rate"
        value={proposal.rate}
        onChange={(e) => setProposal({ ...proposal, rate: e.target.value })}
        className="border rounded p-2 mb-3 w-full"
        required
      />
      <input
        type="text"
        placeholder="Estimated Timeline"
        value={proposal.timeline}
        onChange={(e) => setProposal({ ...proposal, timeline: e.target.value })}
        className="border rounded p-2 mb-3 w-full"
        required
      />
      <textarea
        placeholder="Message"
        value={proposal.message}
        onChange={(e) => setProposal({ ...proposal, message: e.target.value })}
        className="border rounded p-2 mb-3 w-full"
        required
      />
      <button type="submit" className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">
        Submit
      </button>
      {status && <p className="mt-2 text-sm text-gray-700">{status}</p>}
    </form>
  );
};

export default ProposalForm;
# DevConnect — A Freelance Platform for Devs, by Devs
Tired of bloated gig platforms like Upwork or Fiverr? DevConnect is a minimal, developer-first alternative focused solely on tech freelancers and real software projects. No fluff — just clean UX, scoped tasks, and a job board tailored to coders.

# What It Does
Clients post well-defined dev jobs: title, description, stack, budget, and timeline.

Freelancers browse with smart filters (React, Python, Tailwind, etc.) and submit proposals (rate, ETA, message).

A client picks one proposal → both sides unlock basic chat.

Authentication is handled via Firebase, and messaging is stored via SQL (threaded, MVP-lite).

#  Stack
Frontend: We're using React for building a fast, component-based frontend and Tailwind CSS for rapid styling with utility classes. The UI will prioritize minimalism and developer comfort (dark mode, markdown-friendly chat, clean layout).

Backend: FastAPI with/ REST endpoints for users, jobs, proposals, and messages.

Database: PostgreSQL or SQLite.

Auth: Firebase.

# Core Components
JobBoard: paginated job listings + filters

JobCard: compact view of job info

ProposalForm: rate, timeline, message

Dashboard: for clients and freelancers to manage posts/applications

ChatBox: threaded chat between matched users



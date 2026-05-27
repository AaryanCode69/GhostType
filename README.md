# 👻 GhostType

GhostType is a real-time, multiplayer code execution and editing environment designed for synchronous collaboration between human developers and AI agents.

Bypassing standard stateless HTTP requests, GhostType utilizes persistent ASGI WebSockets and Conflict-free Replicated Data Types (CRDTs) to ensure millisecond-level synchronization across distributed clients without document locking. The AI is treated as a concurrent headless user, streaming keystrokes directly into the shared workspace.

## 🏗️ System Architecture & Tech Stack

**Current Status:** Phase 1 (Core ASGI Backend & Authentication)

| Component               | Technology                           | Primary Function                                                                                 |
| :---------------------- | :----------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Routing & State**     | FastAPI, Uvicorn, WebSockets         | Manages persistent client connections, room state, and bidirectional message broadcasting.       |
| **Database & ORM**      | PostgreSQL, SQLAlchemy 2.0 (asyncpg) | Asynchronous relational data storage for user accounts, workspaces, and auth states.             |
| **Conflict Resolution** | Yjs (y-py, y-websocket)              | _[Upcoming]_ Mathematical engine ensuring distributed state consistency across concurrent edits. |
| **The "Ghost" (AI)**    | Python, LangChain, LLM API           | _[Upcoming]_ A headless client connecting to the room to process intent and stream keystrokes.   |
| **Visual Interface**    | React, Monaco Editor                 | _[Upcoming]_ Frontend text engine, bound directly to the Yjs document state.                     |

## 🗺️ Execution Roadmap

- [x] **Phase 1: The ASGI Switchboard** - Establish the central asynchronous event loop.
  - Implement stateless JWT Authentication (HTTP setup + WebSocket handshake).
  - Build the in-memory Connection Manager to track users and prevent memory leaks.
- [ ] **Phase 2: The Headless Ghost** - Build the isolated Python agent client.
  - Implement regex pattern matching for triggers (`// prompt:`).
  - Wire LLM orchestration and simulate streaming keystrokes via WebSockets.
- [ ] **Phase 3: The Synchronization Engine** - Integrate `pycrdt` / `y-py` to manage state vectors.
  - Upgrade raw text broadcasting to binary CRDT update patches.
- [ ] **Phase 4: The Visual Client** - Spin up the React/Monaco environment.
  - Bind the editor instance to the Yjs document to translate physical keystrokes into network-ready operations.

## 📂 Project Structure

```text
ghosttype-backend/
├── app/
│   ├── api/
│   │   ├── dependencies.py       # JWT validation & dependency injection
│   │   ├── routes_auth.py        # HTTP /login and /register
│   │   └── routes_ws.py          # WebSocket endpoints & handshake logic
│   ├── core/
│   │   ├── config.py             # Environment variables (Pydantic settings)
│   │   └── security.py           # Password hashing and JWT encoding/decoding
│   ├── models/
│   │   └── user.py               # SQLAlchemy async database schemas
│   ├── services/
│   │   └── connection_manager.py # Stateful WebSocket tracking class
│   └── main.py                   # FastAPI application initialization
├── alembic/                      # Database migration scripts
├── requirements.txt
└── .env                          # Local secrets (ignored in version control)
```

## 🚀 Getting Started (Phase 1)

### Prerequisites

- **Python 3.10.12**
- **PostgreSQL** (Running locally or via Docker)

### 1. Clone & Setup Environment

Clone the repository and spin up a virtual environment:

```bash
git clone [https://github.com/yourusername/ghosttype.git](https://github.com/yourusername/ghosttype.git)
cd ghosttype-backend
python3.10 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

### 2. Install Dependencies

Install the required packages, including the ASGI server and async database drivers:

```bash
pip install -r requirements.txt

```

### 3. Environment Variables

Create a `.env` file in the root directory and populate it with your local configurations:

```env
# Database Configuration
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/ghosttype_db

# JWT Security
SECRET_KEY=generate_a_secure_random_string_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

```

### 4. Database Migrations

Initialize your database schema using Alembic:

```bash
alembic upgrade head

```

### 5. Run the Server

Boot up the Uvicorn server with the standard, high-performance `uvloop` (on Unix-like systems):

```bash
uvicorn app.main:app --reload

```

The REST API documentation will be available at `http://localhost:8000/docs`.

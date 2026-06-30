# AcadeMCP

AcadeMCP is a FastMCP server that gives AI assistants access to your class schedule, quizzes, absences, and Google Classroom in one place. It enables assistants like Claude and ChatGPT to understand your academic information and help you manage your academic life more effectively.

---

# ✨ Features

## 📅 Routine Management

- View today's schedule
- View classes for any day
- Find the next class
- Automatically resolve class schedules

---

## 📝 Quiz Management

- Add new quizzes
- Store quiz syllabus
- Store classroom information
- View all quizzes
- View upcoming quizzes
- Filter quizzes by course

---

## ❌ Absence Tracking

- Record absences
- View absences by course
- Count absences per course
- View absence statistics
- Delete absence records

---

## 🎓 Google Classroom Integration

- List all registered courses
- Retrieve announcements
- Retrieve assignments
- Access course information directly from Google Classroom

---

# 🏗 Project Structure

```text
AcadeMCP
│
├── database/
│   ├── init_db.py
│   ├── quiz_queries.py
│   └── absent_queries.py
│
├── tools/
│   ├── routine_tools.py
│   ├── quiz_tools.py
│   ├── absent_tools.py
│   └── classroom_tools.py
│
├── google/
│   ├── oauth.py
│   └── google_services.py
│
├── shared/
│   ├── config.py
│   └── db.py
│
├── main.py
├── pyproject.toml
└── README.md
```

---

# 🚀 Tech Stack

- FastMCP
- Python
- PostgreSQL
- Psycopg3
- Google Classroom API
- OAuth2
- Streamable HTTP

---

## Prerequisites

- Python 3.11+
- PostgreSQL
- uv

Install `uv` by following the official installation guide:

https://docs.astral.sh/uv/getting-started/installation/

Verify the installation:

```bash
uv --version
```

---

# 🚀 Getting Started

## Option 1: Run AcadeMCP Locally

The stable desktop version of AcadeMCP is available on the **`local-desktop-version`** branch.

Clone the repository:

```bash
git clone -b local-desktop-version https://github.com/Adnan-Shahriar-1190/AcadeMCP.git
cd AcadeMCP
```

Install all dependencies:

```bash
uv sync
```

All project dependencies are managed through **`pyproject.toml`**, so `uv sync` installs everything required.

---

## Configuration

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/academcp

GOOGLE_CLIENT_ID=your_google_client_id

GOOGLE_CLIENT_SECRET=your_google_client_secret

GOOGLE_REDIRECT_URI=http://localhost:8080
```

The database tables are automatically created when the server starts for the first time.

---

## Claude Desktop

Install AcadeMCP directly into Claude Desktop.

From the project directory, run:

```bash
uv run fastmcp install claude-desktop main.py
```

This automatically adds AcadeMCP to Claude Desktop.

---

## Other MCP Clients

If your MCP client uses a configuration file, add an entry similar to the following:

```json
{
  "mcpServers": {
    "academcp": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/path/to/AcadeMCP",
        "fastmcp",
        "run",
        "/path/to/AcadeMCP/main.py"
      ],
      "env": {}
    }
  }
}
```

Replace `/path/to/AcadeMCP` with the location where you cloned the repository.

---

## Option 2: Use the Hosted Server

If you don't want to run AcadeMCP locally, connect directly to the hosted MCP server using the following Streamable HTTP endpoint:

```text
https://helixion.fastmcp.app/mcp
```

Add this endpoint as an MCP connector in any compatible AI client that supports **Streamable HTTP**.

> **Note**
>
> The hosted server is intended for demonstration purposes and may change as development continues.

---

> **Note**
>
> The `main` branch contains the latest ongoing development.
>
> For the most stable local experience, use the `local-desktop-version` branch.

---

# 🛠 Available MCP Tools

## 📅 Routine Tools

- `get_current_datetime`
- `get_today_all_classes`
- `get_anyday_classes`
- `get_next_class_of_today`

---

## 📝 Quiz Tools

- `add_quiz_exam`
- `get_all_quizes`
- `get_upcoming_quizes`
- `get_quizes_for_course`

---

## ❌ Absence Tools

- `add_absent`
- `get_absences_for_course`
- `get_absence_count_for_course`
- `get_absence_count_all_courses`
- `delete_absent`

---

## 🎓 Classroom Tools

- `get_all_course_details`
- `get_course_announcements`
- `get_course_assignements`

---

# 🗄 Database

AcadeMCP stores academic information inside PostgreSQL.

Current database tables:

- quizzes
- absences

---

# 💬 Example Prompts

- "What classes do I have tomorrow?"
- "What is my next class?"
- "When is my next quiz?"
- "Show all Cloud Computing quizzes."
- "Record that I was absent today."
- "How many absences do I have in Data Analysis?"
- "Show recent announcements from Google Classroom."

---

# 🏛 Architecture

```text
                  AI Assistant
                        │
          Model Context Protocol (MCP)
                        │
               ┌─────────────────┐
               │    AcadeMCP     │
               └─────────────────┘
                  │          │
        ┌─────────┘          └─────────┐
        │                              │
 PostgreSQL                    Google Classroom
        │                           API
        │
 Quizzes & Absences
```

---

# 🚀 Future Improvements

- Assignment reminders
- Automatic deadline notifications
- Attendance percentage prediction
- AI study planner
- Calendar integration
- Email notifications
- Semester analytics
- Exam preparation assistant

---

# 📄 License

This project is licensed under the MIT License.

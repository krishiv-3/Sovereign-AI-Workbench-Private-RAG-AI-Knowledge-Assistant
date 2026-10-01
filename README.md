# Sovereign AI Workbench

> A private, document-grounded AI knowledge assistant built with Retrieval-Augmented Generation (RAG).

Sovereign AI Workbench is an AI-powered knowledge interface designed to let users query organization-specific documents using natural language. The system combines document retrieval, vector search, and an LLM workflow so responses can be grounded in a private knowledge base rather than relying only on a model's general knowledge.

## ✨ Features

- **Document-grounded Q&A** using a RAG workflow
- **Semantic vector search** with ChromaDB
- **LangChain integration** for retrieval and AI orchestration
- **Organization-specific knowledge base**
- **Python backend**
- **Custom web interface** for interacting with the AI system
- **Security layer** for application access
- Support for structured institutional documents and text-based knowledge sources
- Separate vector stores for different datasets/use cases

## 🧠 How It Works

```text
                    ┌─────────────────────┐
                    │   User Question     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Query Processing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Vector Retrieval   │
                    │      ChromaDB       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Relevant Documents  │
                    │     / Context       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    LLM + RAG        │
                    │    Generation       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Grounded Response   │
                    └─────────────────────┘
```

## 🏗️ Project Structure

```text
Sovereign_AI_Workbench_UI/
│
├── app.py
├── main.py
├── security.py
├── vector.py
├── vector2.py
├── requirements.txt
│
├── static/
│   ├── index.html
│   ├── app.js
│   └── styles.css
│
├── CGC_FINAL_DATA/
│   ├── CEC Audited Statements/
│   ├── CEC Mandatory Disclosure/
│   ├── Policies/
│   ├── University Committees 2026/
│   └── organization_profile.txt
│
├── cgc_chroma_db/
│   └── ChromaDB files
│
├── chrome_langchain_db/
│   └── ChromaDB files
│
└── realistic_restaurant_reviews.csv
```

## 🛠️ Tech Stack

### AI / Machine Learning
- Python
- Retrieval-Augmented Generation (RAG)
- LangChain
- Vector embeddings
- ChromaDB
- Large Language Model integration

### Backend
- Python
- Application/API layer
- Security/authentication logic

### Frontend
- HTML5
- CSS3
- JavaScript

### Data
- PDF documents
- Text documents
- CSV data
- Vector databases

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sovereign-ai-workbench.git
cd sovereign-ai-workbench
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file if your selected LLM/provider requires API credentials.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

Do **not** commit API keys or other secrets to GitHub.

### 5. Start the application

The exact entry point depends on the configured application flow. Commonly:

```bash
python main.py
```

or:

```bash
python app.py
```

If the project is configured as a web application, open the local URL shown in the terminal.

## 📚 Knowledge Base

The included development dataset contains organization-specific documents covering areas such as:

- Policies
- Mandatory disclosures
- Audited statements
- University regulations
- Committee documents
- Organization information

For a public GitHub repository, replace proprietary, confidential, copyrighted, or institution-restricted documents with public or synthetic sample data.

## 🔐 Security & Privacy

This project is designed around the idea of keeping an organization's knowledge within a controlled AI workflow.

Before publishing the repository:

- Remove API keys and passwords
- Remove `.env` files
- Do not commit private authentication data
- Do not publish database files containing sensitive information
- Review all uploaded documents for permission to redistribute them
- Add sensitive/generated databases to `.gitignore`
- Replace institutional documents with public/synthetic examples when necessary

### Recommended `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual environment
venv/
.venv/

# Environment variables
.env
.env.*

# Local databases / vector stores
*_chroma_db/
*_langchain_db/
chroma.sqlite3

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

## 🎯 Project Goals

The project explores how organizations can build domain-specific AI assistants that can:

1. Search internal knowledge semantically
2. Retrieve relevant information from documents
3. Provide context to an LLM
4. Generate answers grounded in retrieved information
5. Provide a user-friendly interface for interacting with organizational knowledge

## 🔮 Future Improvements

- Source citations for every generated answer
- Multi-document upload from the UI
- Automatic document ingestion and chunking
- Role-based access control
- Better authentication and session management
- Streaming AI responses
- Conversation history
- Document-level permissions
- Admin dashboard
- Improved hallucination detection
- Evaluation framework for retrieval quality and answer accuracy
- Cloud deployment
- Containerization with Docker
- Production-grade observability and logging

## 📌 Current Status

**Prototype / Development Project**

The current version demonstrates the core concept of a private RAG-based knowledge assistant and its supporting interface. Additional work is required for production deployment, security hardening, scalability, and systematic evaluation.

## 👨‍💻 Author

**Krishiv Sharma**

AI/ML • Python • RAG • Full Stack Development

---

⭐ If you find this project interesting, consider starring the repository.

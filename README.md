# Enterprise Document Intelligence System

An enterprise-grade AI system for intelligent document search, comparison, summarization, and compliance analysis using Hybrid Retrieval-Augmented Generation (RAG) and LangGraph.

## Features

- Hybrid Retrieval (Dense + BM25)
- Multi-Query Retrieval
- LangGraph Agent Workflow
- Structured LLM Routing
- Qdrant Vector Database
- Google Gemini Integration
- Enterprise Document Ingestion Pipeline
- Metadata-based Citations
- Document Comparison (Coming Soon)
- Document Summarization (Coming Soon)
- Conflict Detection (Coming Soon)

## Tech Stack

- Python 3.11
- LangChain
- LangGraph
- Google Gemini
- Qdrant
- HuggingFace Embeddings
- FastAPI (Upcoming)
- React (Upcoming)

## Project Structure

```text
src/
├── agents/
├── core/
├── ingestion/
├── prompts/
├── rag/
├── services/
└── tools/
```

## Setup

Clone the repository.

```bash
git clone <repository-url>
cd enterprise-document-intelligence
```

Create a virtual environment.

```bash
uv venv
source .venv/bin/activate
```

Install dependencies.

```bash
uv sync
```

Create your environment file.

```bash
cp .env.example .env
```

Add your Google Gemini API key to `.env`.

Index enterprise documents.

```bash
uv run python scripts/index_documents.py
```

Run tests.

```bash
uv run python scripts/test_graph.py
```

## Roadmap

- [x] Enterprise document ingestion
- [x] Hybrid retrieval
- [x] Multi-query retrieval
- [x] LangGraph routing
- [x] Search agent
- [ ] Compare agent
- [ ] Summarization agent
- [ ] Conflict detection
- [ ] FastAPI backend
- [ ] React frontend
- [ ] RAGAS evaluation

## License

MIT
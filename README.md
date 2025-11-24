# SDLC Agent — LangGraph + Pinecone (Minimal Framework)

This project provides a lightweight, extensible framework for building an SDLC (Software Development Life Cycle) automation agent. It uses **LangGraph** for orchestration, **Pinecone** for vector storage, and **FastAPI** as the service layer. The structure is intentionally minimal, allowing you to extend the agent with LLM-powered tasks such as requirement analysis, test-case creation, documentation generation, and model-driven code insights.

---

## What This Agent Can Do

The agent is designed as a flexible SDLC assistant that you can expand with LangGraph flows. Out of the box, the project supports:

### Core Abilities

* Accept tasks through an API (`/run`) and return structured outputs.
* Perform simple SDLC operations like generating test-case drafts.
* Store and retrieve vector embeddings using Pinecone.
* Integrate custom LLM chains for requirement analysis, refactoring suggestions, documentation generation, bug-pattern detection, or architecture summaries.
* Run scheduled workflows using Airflow (daily, hourly, CI-triggered, etc.).
* Deploy as a scalable microservice using Docker and Kubernetes.

### Extensible SDLC Tasks (you add the logic)

You can expand the agent to perform:

* Requirements parsing and refinement
* User story generation
* Test-case generation
* API spec generation
* Code review suggestions
* Risk analysis for features
* Architecture mapping and dependency extraction
* Knowledge-base retrieval using Pinecone
* Release-notes automation
* Lightweight CI-driven quality checks

The LangGraph structure makes it easy to plug in new nodes, state machines, and multi-step reasoning pipelines.

---

## Technology Behind This Project

### LangGraph

Used for defining agent workflows, branching logic, tool-calls, and multi-step reasoning. Ideal for building deterministic, inspectable agent behaviors.

### Pinecone

Handles vector storage. Useful for:

* Storing embeddings of requirements, documentation, code snippets
* Retrieval-augmented reasoning for SDLC tasks

### FastAPI

Provides the service layer and REST API.
Endpoints:

* `/health` – Status check
* `/run` – Trigger SDLC tasks

### Docker

Makes the entire project containerized and portable.
Used for local development, staging, and production.

### GitHub Actions (CI)

Runs linting and builds Docker images on every push to `main`.
You can extend it with tests, vulnerability scans, and auto-deploy steps.

### Kubernetes

Contains a minimal Deployment + Service manifest:

* Deploys the agent
* Exposes it over a LoadBalancer
* Injects API keys through Kubernetes Secrets

### Airflow

Includes a tiny DAG to trigger the agent on a schedule—ideal for running:

* Daily documentation sync
* Automated test-case generation
* SDLC pipeline routines

### Embedding Provider (stubbed)

The `embeddings.py` file provides a placeholder implementation.
Replace with:

* OpenAI embeddings
* Local models
* HuggingFace embedding models

---



---

## How to Run

### Local

```
make build
make run
```

### Docker

```
docker build -t sdlc-agent .
docker run -p 8000:8000 --env-file .env sdlc-agent
```

### Kubernetes

```
kubectl apply -f k8s/
```

### Airflow

Drop the DAG into your Airflow instance and enable it.

---



---



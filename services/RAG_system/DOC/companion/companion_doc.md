# Companion Assistant - Technical Documentation

## 1. Purpose

The `companion` module is intended to provide the conversational layer of the portfolio application.

It receives questions from the frontend, processes the user's request, and uses the `RAG_system` to retrieve information from the project's Markdown documentation.

## 2. Module Relationship

```text
Frontend
    ↓
Companion service
    ↓
RAG_system
    ↓
Chroma vector database
    ↓
Retrieved documents
    ↓
Companion response
```

The `companion` module is responsible for the interaction flow, while the `RAG_system` is responsible for document retrieval.

## 3. RAG System Integration

The RAG system contains two main operations:

### Document ingestion

The ingestion process:

1. reads Markdown files from the `DOC` directory
2. searches recursively through its subdirectories
3. divides documents into text chunks
4. generates embeddings
5. stores the embeddings in Chroma

The Markdown search pattern is:

```python
glob="**/*.md"
```

This allows documentation files to be loaded from nested project folders.

### Document consultation

The consultation process receives the user's message as a search query:

```python
results = db.similarity_search(user_message, k=3)
```

The system retrieves the three most similar document sections from the vector database.

## 4. Expected Request Flow

A typical request should follow this sequence:

1. The user submits a question through the frontend.
2. The frontend sends the question to the Companion backend.
3. The Companion module receives the user message.
4. The message is passed to the RAG consultation function.
5. The RAG system performs a similarity search.
6. Relevant documentation is returned.
7. The Companion uses that context to generate a response.
8. The response is returned to the frontend.

## 5. Example Query

User input:

```text
How does the warehouse module work?
```

Internal retrieval query:

```python
question = user_message
```

The RAG system searches the indexed documentation and returns relevant sections from the Warehouse Markdown files.

## 6. Documentation Source

The RAG system uses Markdown files stored under:

```text
services/RAG_system/DOC/
```

The documentation is organized by project. Each project can contain multiple Markdown files describing its functionality and technical implementation.

## 7. Current State

The Companion Assistant is currently under development. The intended architecture separates:

- conversation handling
- project knowledge retrieval
- document ingestion
- vector storage
- response generation

This separation allows the conversational layer and the retrieval layer to evolve independently.
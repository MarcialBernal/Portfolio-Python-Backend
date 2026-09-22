# Companion Assistant

## Overview

The Companion Assistant is a portfolio-oriented conversational assistant designed to guide visitors through the projects contained in the portfolio.

Its main purpose is to explain project functionality, architecture, technologies, and implementation details through natural-language interaction.

The assistant is intended to help recruiters and technical visitors understand the projects without requiring them to inspect every source file manually.

## Main Responsibilities

The assistant is designed to:

- answer questions about portfolio projects
- explain project functionality and architecture
- describe technologies and backend modules
- guide visitors through the portfolio
- provide context about implementation decisions
- retrieve relevant project information from the portfolio documentation

## RAG Integration

The Companion Assistant uses the `RAG_system` as its knowledge source.

The RAG system indexes Markdown documentation stored in the portfolio and retrieves relevant content when a user asks a question.

The expected interaction flow is:

```text
User question
    ↓
Companion Assistant
    ↓
RAG system
    ↓
Relevant project documentation
    ↓
Assistant response
```

For example, a user may ask:

```text
Can you explain the AutoML project?
```

The assistant can use the RAG system to retrieve the corresponding project documentation and generate a contextual explanation.

## Project Scope

The Companion Assistant provides conversational support for navigating and understanding the portfolio. It uses project documentation as a knowledge source and can assist visitors with:

- project explanations
- technical documentation retrieval
- architecture and technology descriptions
- guidance through the portfolio projects
- contextual answers based on the indexed documentation
- integration with the portfolio frontend
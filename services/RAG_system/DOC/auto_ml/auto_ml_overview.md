# AutoML Project Overview
// filepath: C:\Users\Marcial\Desktop\PORTFOLIO\portfolio\backend\services\RAG_system\DOC\auto_ml\auto_ml_overview.md

# AutoML Project

## Overview

The AutoML project is a backend service organized to manage a machine learning workflow for Bitcoin daily data. It includes data acquisition, preprocessing, model training, prediction, persisted model artifacts, and API routing.

The project is structured as a pipeline so that each stage of the machine learning workflow is separated into an independent module.

## Main Workflow

The project is organized around the following process:

1. Fetch raw Bitcoin data.
2. Preprocess the raw dataset.
3. Generate a processed dataset.
4. Train a machine learning model.
5. Persist the trained model and evaluation metrics.
6. Load the model to generate predictions.
7. Expose prediction functionality through backend routes.

## Project Components

- `data/raw/`: stores the original Bitcoin dataset.
- `data/processed/`: stores the transformed dataset used by the model.
- `pipeline/`: contains the data processing, training, and prediction stages.
- `model/`: contains the serialized trained model and metrics.
- `routers/`: contains the API routes.
- `schemas.py`: defines data schemas used by the service.
- `crud.py`: contains CRUD-related operations.
- `utils/`: contains reusable helper functions.

## Data Artifacts

The project currently contains:

- `btc_raw.csv`: raw Bitcoin data.
- `btc_daily.csv`: processed daily Bitcoin data.
- `model.pkl`: serialized trained model.
- `metrics.json`: model evaluation metrics.

## Execution Flow

The expected execution flow is:

```text
Raw data
   ↓
Data fetching
   ↓
Preprocessing
   ↓
Processed data
   ↓
Model training
   ↓
Persisted model
   ↓
Prediction service
   ↓
API route
```

## Purpose

The project provides a modular backend structure for executing a machine learning workflow and serving predictions through an API.
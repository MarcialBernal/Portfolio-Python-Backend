# AutoML Technical Documentation
// filepath: C:\Users\Marcial\Desktop\PORTFOLIO\portfolio\backend\services\RAG_system\DOC\auto_ml\auto_ml_technical_doc.md

# AutoML Technical Documentation

## 1. Module Structure

```text
auto_ml/
├── data/
│   ├── raw/
│   │   └── btc_raw.csv
│   └── processed/
│       └── btc_daily.csv
├── model/
│   ├── metrics.json
│   └── model.pkl
├── pipeline/
│   ├── fetch_data.py
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── __init__.py
├── routers/
│   ├── routes.py
│   └── __init__.py
├── utils/
│   └── helpers.py
├── crud.py
└── schemas.py
```

## 2. Data Layer

### `data/raw/`

Contains the original dataset used as input for the machine learning workflow.

Current file:

- `btc_raw.csv`

### `data/processed/`

Contains the dataset after the preprocessing stage.

Current file:

- `btc_daily.csv`

The processed dataset is used as input for model training and prediction.

## 3. Pipeline

### `fetch_data.py`

Responsible for obtaining or loading the source Bitcoin data used by the project.

### `preprocess.py`

Responsible for transforming the raw data into the processed dataset used by the training stage.

The output is stored in:

```text
data/processed/btc_daily.csv
```

### `train.py`

Responsible for training the machine learning model using the processed dataset.

The trained model is persisted as:

```text
model/model.pkl
```

The evaluation results are persisted as:

```text
model/metrics.json
```

### `predict.py`

Responsible for loading the persisted model and generating predictions from input data.

The prediction stage uses the model stored in:

```text
model/model.pkl
```

## 4. Model Artifacts

### `model.pkl`

Serialized representation of the trained machine learning model. It allows the prediction stage to reuse the trained model without retraining it for every request.

### `metrics.json`

Stores the metrics generated during model evaluation.

## 5. API Layer

### `routers/routes.py`

Contains the routes used to expose AutoML functionality through the backend API.

The routes act as the entry point for external requests and connect them with the prediction or service logic.

## 6. Schemas and CRUD

### `schemas.py`

Defines the data structures used to validate or transfer information through the AutoML service.

### `crud.py`

Contains operations related to data access or service-level CRUD functionality.

## 7. Utilities

### `utils/helpers.py`

Reserved for reusable helper functions shared by different components of the AutoML module.

## 8. Processing Flow

```text
btc_raw.csv
    ↓
fetch_data.py
    ↓
preprocess.py
    ↓
btc_daily.csv
    ↓
train.py
    ↓
model.pkl + metrics.json
    ↓
predict.py
    ↓
routers/routes.py
```

## 9. Separation of Responsibilities

The module separates responsibilities as follows:

- data storage: `data/`
- data acquisition: `fetch_data.py`
- preprocessing: `preprocess.py`
- training: `train.py`
- prediction: `predict.py`
- model persistence: `model/`
- API exposure: `routers/`
- input and output structures: `schemas.py`
- reusable helpers: `utils/`

## 10. Current Documentation Scope

This documentation describes the observable project structure and the responsibilities suggested by each module. The exact features, model type, input fields, prediction target, and evaluation metrics require reviewing the contents of the Python files.
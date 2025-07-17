# ML Feature Store Pipeline with Feast and Carbon Tracking

This project demonstrates how to design a Feature Store using [Feast](https://feast.dev/) and run end-to-end machine learning experiments with feature versioning, hyperparameter tuning, and carbon emission tracking.

---

## Project Structure
ml-feature-store-pipeline/
├── data/ # Raw and generated feature datasets
│ ├── athletes.csv # Original dataset
│ ├── athletes_clean.csv # Cleaned version
│ ├── feature_v1.csv # Feature version 1
│ ├── feature_v2.csv # Feature version 2
│ └── athletes_clean.parquet # Parquet version for Feast ingestion
│
├── feature/ # Feature store configuration
│ └── athlete_feature_store/
│ └── feature_repo/ # Feast repo (features.py, config, etc.)
│ ├── athlete_features.py
│ ├── feature_store.yaml
│ └── ...
│
├── pipeline/ # ML and data generation notebooks
│ ├── clean_data.ipynb
│ ├── generate_feature_v1.ipynb
│ ├── generate_feature_v2.ipynb
│ ├── ml_pipeline.ipynb
│ └── emissions_log/ # Emission logs from CodeCarbon
│
├── feast.png # Screenshot of feature registry
├── experiments.png # Screenshot of experiment results
├── carbon_emission.png # Screenshot of carbon tracking
└── README.md # Project documentation

---

## Goal

Build a reusable and auditable ML pipeline that:
- Uses **Feast** to version and serve features.
- Runs experiments across two feature versions and two hyperparameter sets.
- Tracks **model performance** and **carbon emissions** using [CodeCarbon](https://mlco2.github.io/codecarbon/).

---

## Tools & Frameworks

- **Feast**: Feature Store
- **Pandas & Scikit-learn**: ML pipeline
- **CodeCarbon**: Carbon footprint tracker
- **Parquet / CSV**: Offline data storage
- **Jupyter Notebooks**: Step-by-step development

---

## Pipeline Steps

### 1. Clean Raw Data
`clean_data.ipynb`  
- Reads `athletes.csv`, removes nulls and standardizes columns  
- Outputs `athletes_clean.csv` and `.parquet`

### 2. Generate Features
- `generate_feature_v1.ipynb`: Basic features like age, gender, region
- `generate_feature_v2.ipynb`: Engineered features (BMI, interaction terms, age groups)

Each version is saved as `feature_v1.csv` and `feature_v2.csv`.

### 3. Register Feature Store with Feast
- Feature views defined in `athlete_features.py`
- Run `feast apply` to register feature views and entities

### 4. Retrieve Training Data
- Use `get_historical_features()` from Feast
- Join with entity dataframe to get training set for V1 and V2

### 5. Train Models & Track Emissions
`ml_pipeline.ipynb`:
- Train 4 combinations:  
  - V1 + HP1, V1 + HP2, V2 + HP1, V2 + HP2
- Metrics logged: **RMSE**, **R²**, **Carbon emissions (kg CO₂eq)**
- Results saved to `emissions_log/`

---

## Results
_(See `experiments.png` and `carbon_emission.png` for full visual report)_

---

## Learnings

- Feature versioning helps evaluate the true impact of feature engineering.
- Carbon tracking adds sustainability visibility to ML development.
- Feast integrates well with scikit-learn pipelines for training and inference.

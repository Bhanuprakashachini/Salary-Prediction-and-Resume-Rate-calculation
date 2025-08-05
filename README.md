Great! Here's the updated **README.md** including your contact email:

---

# Salary Prediction & Resume Rate Calculation

## 🚀 Overview

This repository builds and evaluates machine learning models to:

* Predict individual salaries based on attributes like years of experience, education, industry, gender, job title, etc.
* Compute **Resume Rating Scores**—automated scoring of resumes (e.g. keyword matching, experience relevance, formatting quality).

It leverages Exploratory Data Analysis, feature engineering, and model evaluation to deliver actionable predictions and resume evaluations.

---

## 📁 Project Structure

```
├── data/
│   ├── raw/                  # Raw data files (e.g. Salary_Data.csv, Resumes.csv)
│   ├── processed/            # Cleaned and transformed datasets used for modeling
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_eda_and_visualization.ipynb
│   ├── 03_model_building.ipynb
│   ├── 04_resume_scoring.ipynb
├── src/
│   ├── preprocessing.py     # Data cleaning & feature engineering
│   ├── modeling.py          # Model training & evaluation logic
│   ├── scoring.py           # Resume scoring & rating logic
│   ├── utils.py             # Shared helper functions
├── models/
│   ├── best_model.pkl        # Serialized trained model
│   └── resume_score_model.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Dependencies

1. **Clone the repository**

   ```bash
   git clone https://github.com/Bhanuprakashachini/Salary-Prediction-and-Resume-Rate-calculation.git
   cd Salary-Prediction-and-Resume-Rate-calculation
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Explore in Jupyter Notebooks**

   * Run `notebooks/01_data_preprocessing.ipynb` through `03_model_building.ipynb` for salary prediction modeling.
   * Run `notebooks/04_resume_scoring.ipynb` to understand how resume ratings are computed.

---

## 📊 Data & Preprocessing

* **Salary dataset**: Contains features such as `age`, `gender`, `education`, `job_title`, `years_experience`, and salary target.
* **Resume dataset**: Includes candidate resumes parsed into features like relevant skills, keyword matches, years in role, etc.

Data processing includes:

* Handling missing/malformed entries
* Encoding categorical variables
* Normalizing continuous features
* Feature engineering (e.g. text vectorization, keyword scoring)

---

## 🧠 Modeling & Evaluation

We train and compare multiple regression models:

* **Linear Regression**
* **Decision Tree Regressor**
* **Random Forest Regressor**

Evaluation metrics:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE / RMSE)
* R‑squared (R²)

---

## 📈 Resume Rate Scoring

* Loads resumes and computes a **Resume Rating Score**, based on:

  * Matching job keywords
  * Education and experience alignment
  * Formatting markers and length

Customize the logic in `scoring.py` for your domain or job requirements.

---

## 🏃 Usage

```python
from modeling import load_model, predict_salary
from scoring import rate_resume

model = load_model('models/best_model.pkl')
salary_pred = predict_salary(model, new_candidate_dataframe)

resume_score = rate_resume('models/resume_score_model.pkl', resume_text)
```

---

## 🧪 Extensions

* Integrate NLP models for advanced resume parsing
* Add web UI (Streamlit/Flask)
* Deploy via API for job portals or HR systems

---

## 🤝 Contributing

Want to help improve this project? Here's how:

1. Fork the repo
2. Make your changes
3. Submit a pull request!

---

## 📜 License

This project is licensed under the MIT License.

---

## 📬 Contact

For queries, suggestions, or collaborations:

**Email**: [bhanuprakashachini08@gmail.com](mailto:bhanuprakashachini08@gmail.com)
**GitHub**: [@Bhanuprakashachini](https://github.com/Bhanuprakashachini)

---

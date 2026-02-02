
# Lead Conversion Prediction — End-to-End Machine Learning Deployment

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue" />
  <img src="https://img.shields.io/badge/Flask-API-black" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red" />
  <img src="https://img.shields.io/badge/Docker-Containerization-blue" />
  <img src="https://img.shields.io/badge/HuggingFace-Spaces-yellow" />
</p>

---

## Project Overview

This project implements a **production-oriented, end-to-end machine learning system** to predict whether a marketing lead will convert into a paying customer for an EdTech business.

The focus of this work is not limited to model accuracy, but on demonstrating **industry-grade ML deployment practices**, including:

- Model training and evaluation  
- Model serialization  
- REST API development  
- Containerization with Docker  
- Cloud deployment on Hugging Face Spaces  
- Frontend integration via Streamlit  

This mirrors how real-world ML systems are designed, deployed, and consumed by downstream applications.

---

## Business Problem

Marketing teams generate large volumes of leads from multiple acquisition channels.  
Only a subset of these leads convert, and manual prioritization is inefficient.

**Objective:**  
Predict lead conversion likelihood using historical behavioral and demographic data to improve:
- Lead prioritization
- Sales efficiency
- Conversion rates

---

## Dataset Summary

The dataset contains historical lead-level data with features such as:
- Website engagement metrics
- Interaction history
- Occupation and demographic attributes
- Lead activity indicators

**Target variable:**  
- `Converted` (binary classification: 1 = converted, 0 = not converted)

---

## Machine Learning Pipeline

### 1. Exploratory Data Analysis (EDA)
- Distribution analysis of numerical features
- Conversion rate comparison across categorical variables
- Missing value and imbalance assessment

### 2. Feature Engineering
- Encoding of categorical variables
- Feature selection based on business relevance
- Alignment of features with model requirements

### 3. Model Training
Multiple classification models were trained and evaluated:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting (final selection)

### 4. Model Evaluation
Models were compared using:
- Accuracy
- Precision
- Recall
- F1-score

The final model was selected based on balanced recall and precision, prioritizing correct identification of high-value leads.

---

## Model Serialization

The trained model was serialized using Python pickle to enable reuse in deployment.

python
import pickle

with open("final_lead_conversion_model.pkl", "wb") as f:
    pickle.dump(model, f)

The serialized model is loaded at inference time inside the deployed API.

⸻

## Backend API (Flask)

**API Description**

A Flask-based REST API exposes the trained model for inference.
	•	Endpoint: POST /predict
	•	Input: JSON payload
	•	Output: Conversion prediction

**Sample Request**

{
  "total_time_spent_on_website": 200,
  "page_views_per_visit": 3,
  "last_activity": "Email Opened"
}

**Sample Response**

{
  "lead_conversion_prediction": 1
}

**Important Note on Schema**

The trained model expects a feature schema aligned with the training data.
If partial or mismatched features are provided, the API returns a controlled fallback response and logs the mismatch.

This behavior is intentional and reflects real-world production challenges related to feature alignment.

---

## Containerization (Docker)

The backend service is fully containerized to ensure:
	•	Environment consistency
	•	Reproducible builds
	•	Cloud portability

The Docker image installs dependencies from requirements.txt, loads the serialized model, and exposes the Flask API.

---

## Cloud Deployment (Hugging Face Spaces)

**Backend Deployment**

The Flask API is deployed as a public Hugging Face Space.

**Backend URL:**
https://huggingface.co/spaces/SaiSadhasivam/lead-conversion-backend

---

## Frontend Deployment (Streamlit)

A Streamlit frontend provides a user-facing interface for interacting with the backend API.

**Frontend URL:**
https://huggingface.co/spaces/SaiSadhasivam/lead-conversion-frontend

The frontend allows users to:
	•	Enter lead attributes via a form
	•	Trigger API calls
	•	View predicted conversion outcomes

---

## API Testing

The backend API was tested using Hoppscotch to validate:
	•	Endpoint availability
	•	Request/response behavior
	•	Error handling for incomplete inputs

Due to the interactive and external nature of this testing, results are documented via logs and screenshots rather than embedded notebook outputs.

---

## Deployment Summary

The deployment demonstrates:
	•	End-to-end ML lifecycle completion
	•	Model serialization and loading
	•	REST API exposure
	•	Docker-based container execution
	•	Cloud deployment on Hugging Face Spaces
	•	Frontend-backend integration

Although full schema-aligned preprocessing was not implemented due to time constraints, the deployed system clearly highlights the importance of feature alignment in production ML systems.

---

## Limitations
	•	Input preprocessing and encoding are not yet handled inside the API layer
	•	The API assumes schema-aligned input
	•	Model monitoring and drift detection are not included

These limitations are explicitly acknowledged as realistic trade-offs under time constraints.

---

## Future Enhancements
	•	Automated input validation and schema enforcement
	•	Integrated feature preprocessing inside the API
	•	Probability-based predictions
	•	Model monitoring and logging
	•	Versioned model deployments

---

## Repository Structure

lead-conversion-ml-deployment/
│
├── ExtraaLearn_Lead_Conversion_Analysis.ipynb
├── app.py
├── Dockerfile
├── requirements.txt
├── final_lead_conversion_model.pkl
└── README.md


---

**Author:** Sai Sadasivam

This project was developed as part of a Postgraduate Program in Artificial Intelligence & Machine Learning,
in collaboration with The University of Texas at Austin.


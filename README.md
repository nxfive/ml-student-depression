# Student Depression Project

> ⚠️ This project is under active development.
> Architecture and features are evolving as new components are implemented.

## 🎯 Project Goal

This project aims to implement a **full end-to-end machine learning lifecycle**, from raw data ingestion to deployment, while following best practices in reproducibility, scalability, and maintainability.  

Key objectives include:

1️⃣ **Complete ML Lifecycle**  
   - Data loading, preprocessing, training, hyperparameter optimization, and retraining.  

2️⃣ **Robust Data Infrastructure**  
   - Storing and managing data in **AWS RDS**.  
   - Integration with **AWS S3** for storing datasets and model artifacts.  

3️⃣ **Efficient Model Training**  
   - Leveraging **multiprocessing** and **threading/async** for faster data processing and model training.  

4️⃣ **Task Queues & Scheduling**  
   - Using **Celery + Redis + Flower** for background jobs and monitoring.  
   - Orchestrating workflows with **Apache Airflow** for reproducible pipelines.  

5️⃣ **Deployment Strategy**  
   - Canary and shadow deployments for safe production rollout.  
   - Monitoring and logging integrated for continuous model evaluation.  
   - **Two main components**:  
     1. **Survey system** – collects anonymized survey responses.  
     2. **ML system** – handles data preprocessing, training, and predictions.  
   - Both components will be deployed on a **private VPS**, with future plans to move to **Kubernetes** for orchestration and scaling.

---

## 🗺️ Project Phases / Roadmap

1️⃣ **Initial Training [MVP]**  
   - Train a baseline model using the publicly available `student-depression` dataset from Kaggle.  

2️⃣ **Incremental Updates**  
   - Weekly retraining as new anonymized survey data becomes available.  
   - Continuous model improvement and evaluation.

3️⃣ **Task Queue & Async Processing**  
   - Integrate Celery, Redis, and Flower for background jobs.  
   - Enable asynchronous data processing and model training.  

4️⃣ **Pipeline Orchestration**  
   - Use Apache Airflow to orchestrate full ML workflow.  

5️⃣ **Monitoring & Observability**  
   - Implement Prometheus, Grafana, and ELK stack for metrics, logging, and alerts.  

6️⃣ **Production Deployment**  
   - Deploy components to private VPS initially.  
   - Future rollout using K3s with canary and shadow deployments.

---

## 🔍 Testing

The project includes a **multi-level testing strategy** to ensure reliability and maintainability:

1️⃣ **Unit Tests**  
   - Focus on the most critical and error-prone functions.

2️⃣ **Integration Tests**  
   - Test interactions between multiple components.

3️⃣ **External / Stage Tests**  
   - Run in a staging environment using snapshots of the database.  
   - Ensure the full system works correctly before deployment, including external dependencies like BentoML services and cloud storage (AWS S3/RDS).  

---

## 🛠️ Expected Tech Stack

- **Languages & Scripting:** Python, Bash  
- **Data Science & ML:** NumPy, Pandas, Scikit-learn, Optuna, MLflow, BentoML
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Database:** PostgreSQL, Alembic, SQLAlchemy
- **Configuration & Experiment Management:** Hydra, Omegaconf  
- **Task Queues & Background Jobs:** Celery, Redis, Flower  
- **Orchestration & Scheduling:** Airflow, K3s  
- **Deployment & Cloud:** AWS RDS, S3, CI/CD pipelines, Docker
- **Parallelism:** Multithreading, Multiprocessing  
- **Monitoring & Observability:** Prometheus, Grafana, Elasticsearch, Kibana, Filebeat

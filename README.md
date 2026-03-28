# 🚀 Customer Segmentation ML API

An end-to-end Machine Learning project that performs **customer segmentation using K-Means clustering** and exposes predictions via a **FastAPI REST API**.

---

## 📌 Project Overview

This project demonstrates how to:

* Train a machine learning model (K-Means clustering)
* Serve the model using FastAPI
* Build a client to send requests and receive predictions
* Structure a real-world ML + backend project

---

## 🧠 Problem Statement

Businesses need to group customers based on behavior (income, spending, etc.) to:

* Target marketing campaigns
* Improve customer experience
* Increase revenue

This project segments customers into clusters using **unsupervised learning (K-Means)**.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **FastAPI**
* **Uvicorn**
* **Joblib**

---

## 📁 Project Structure

```
customer_segmentation_kmeans/
│
├── app/
│   ├── main.py          # FastAPI routes
│   ├── schemas.py       # Request schema
│
├── src/
│   ├── train_model.py   # Model training script
│   └── predict.py       # Prediction logic
│
├── models/              # (Model files - ignored or optional)
│   └── .gitkeep
│
├── data/   
|    └── store_customers.csv   # Dataset (CSV)
│
├── client/
│   └── request.py       # Client script to call API
│
├── requirements.txt
└── README.md
└── run.py               # Server entry point
```

---

## ⚙️ How It Works

1. Train model using K-Means
2. Save model using `joblib`
3. FastAPI loads model
4. Client sends request → API
5. API returns predicted cluster

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
https://github.com/ICA-99/customer_segmentation_kmeans.git
cd customer_segmentation_kmeans
```

---

### 2. Create Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate   # Linux/Mac
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Train model 

```bash
python -m src.train_model
```

---

## ▶️ Run the Server

```bash
python run.py
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📡 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI available.

---

## 🧪 Test Using Client

```bash
python -m client.test_api
```

---

## 📥 Sample Request

```json
{
  "age": 25,
  "income": 50,
  "spending": 70
}
```

---

## 📤 Sample Response

```json
{
  "cluster": 2
}
```

---

## ⚠️ Important Note (Model Files)

Model files (`.joblib`) are **not included** in this repository.

To generate them, run:

```bash
python -m src.train_model
```

This will create files inside:

```
models/
```

---

## 📊 Features

* End-to-end ML pipeline
* FastAPI-based REST API
* Modular project structure
* Client-server architecture
* Ready for deployment

---

## 🧠 Key Learnings

* Understanding of IP, ports, and networking
* Converting ML models into APIs
* Handling request/response lifecycle
* Project structuring for scalability

---

## 🚀 Future Improvements

* Deploy on cloud (AWS / Render / Railway)
* Add Docker support
* Add authentication
* Improve model performance

---

## 🤝 Contributing

Pull requests are welcome. Feel free to open issues.

---

## 📎 Connect with Me

If you found this useful, feel free to connect on LinkedIn!

- 💼 [Anjan Pal - LinkedIn](https://www.linkedin.com/in/anjan-pal-ab5a5a247/)

---

## ⭐ Give a Star

If you like this project, please ⭐ the repo!

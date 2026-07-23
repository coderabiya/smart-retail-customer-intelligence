# 🛒 Shopper Spectrum  
## Customer Segmentation & Product Recommendation System

## 🚀 Live Demo

🔗 Streamlit App:

https://smart-retail-ai.streamlit.app


### 📌 Project Overview

Shopper Spectrum is a Machine Learning-based retail analytics application that helps businesses understand customer behavior and provide personalized product recommendations.

The project uses **RFM Analysis (Recency, Frequency, Monetary)** to segment customers into different groups using **K-Means Clustering** and recommends similar products using a product similarity-based recommendation system.

The complete solution is deployed as an interactive **Streamlit web application**.

---


## 🎯 Objectives

- Analyze customer purchasing behavior.
- Segment customers based on their buying patterns.
- Identify customer groups using machine learning.
- Recommend similar products to improve customer experience.
- Build an interactive web application for real-time predictions.

---

# 🧠 Machine Learning Approach

## 1. Customer Segmentation

Customer segmentation is performed using **K-Means Clustering**.

### Features Used:

- **Recency**  
  Number of days since the customer's last purchase.

- **Frequency**  
  Total number of purchases made by the customer.

- **Monetary**  
  Total amount spent by the customer.

### Workflow:
Customer Data
↓
RFM Feature Engineering
↓
Data Scaling
↓
K-Means Clustering
↓
Customer Segments


---

## 2. Product Recommendation System

A product recommendation system is developed using product similarity.

The system identifies similar products based on customer purchase patterns and recommends the top related products.

Workflow:
Product Data
↓
Similarity Calculation
↓
Product Similarity Matrix
↓
Top Recommended Products


---

# 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

### Deployment
- Streamlit Cloud

### Version Control
- GitHub

---

# 📂 Project Structure
Shopper-Spectrum
│
├── app.py
├── kmeans_model.pkl
├── scaler.pkl
├── product_similarity.pkl
├── requirements.txt
└── README.md


---

# 📊 Application Features

## 👥 Customer Segmentation

Users can enter:

- Recency
- Frequency
- Monetary value

The application predicts the customer cluster using the trained K-Means model.

---

## 🛍️ Product Recommendation

Users can enter a product name and receive:

- Similar products
- Top recommended items

📈 Model Details
Customer Segmentation Model

Algorithm:

K-Means Clustering

Input Features:

Recency
Frequency
Monetary

Output:

Customer Cluster

🔮 Future Improvements
Add customer purchase history visualization.
Improve recommendation accuracy using collaborative filtering.
Add real-time customer analytics dashboard.
Deploy using cloud platforms with database integration.


👩‍💻 Author- Rabiya Khanum

Machine Learning Project
Customer Segmentation & Recommendation System

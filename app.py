import streamlit as st
import pandas as pd
import joblib

# ===========================
# Load Files
# ===========================

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")
similarity_df = joblib.load("product_similarity.pkl")

# ===========================
# Page Title
# ===========================

st.set_page_config(page_title="Shopper Spectrum", page_icon="🛒")

st.title("🛒 Shopper Spectrum")
st.subheader("Customer Segmentation & Product Recommendation System")

st.write(
    "This application predicts customer segments using RFM values and recommends similar products using Machine Learning."
)

st.markdown("---")
# ===========================
# Customer Segmentation
# ===========================

st.header("👥 Customer Segmentation")

recency = st.number_input("Recency (Days)", min_value=0, value=30)
frequency = st.number_input("Frequency (Number of Purchases)", min_value=1, value=5)
monetary = st.number_input("Monetary (Total Spending)", min_value=1.0, value=500.0)

if st.button("Predict Customer Segment"):

    data = pd.DataFrame([[recency, frequency, monetary]],
                        columns=["Recency", "Frequency", "Monetary"])

    scaled_data = scaler.transform(data)

    cluster = kmeans.predict(scaled_data)[0]

    st.success(f"Predicted Cluster: {cluster}")

    if cluster == 0:
        st.info("This customer belongs to Cluster 0.")
    elif cluster == 1:
        st.info("This customer belongs to Cluster 1.")
    elif cluster == 2:
        st.info("This customer belongs to Cluster 2.")
    else:
        st.info("This customer belongs to Cluster 3.")

        # ===========================
# Product Recommendation
# ===========================

st.markdown("---")
st.header("🛍️ Product Recommendation")

product_name = st.text_input(
    "Enter Product Name",
    "WHITE HANGING HEART T-LIGHT HOLDER"
)

if st.button("Recommend Products"):

    if product_name in similarity_df.index:

        recommendations = similarity_df[product_name].sort_values(
            ascending=False
        )[1:6]

        st.success("Top 5 Recommended Products")

        for product in recommendations.index:
            st.write("✅", product)

    else:
        st.error("Product not found in the dataset.")
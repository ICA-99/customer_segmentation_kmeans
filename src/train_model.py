# 🔷 Import Libraries
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from core.config import DATASET_PATH, MODEL_PATH, SCALER_PATH, CLUSTER_NAMES


class CustomerSegmentation:

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = None
        self.X = None
        self.X_scaled = None
        self.scaler = None
        self.model = None
        self.labels = None
        self.centroids = None
        self.cluster_names = None   # 🔥 important


    # -------------------------------
    # 🔷 DATA LOADING
    # -------------------------------
    def load_data(self):
        self.df = pd.read_csv(self.dataset_path)


    # -------------------------------
    # 🔷 PREPROCESSING
    # -------------------------------
    def preprocess(self):
        if self.df is None:
            raise ValueError("Data not loaded.")

        self.df = self.df.drop(columns=["CustomerID", "Gender"], errors='ignore')

        self.df['Age'] = self.df['Age'].fillna(self.df['Age'].median())
        self.df['Annual Income (k$)'] = self.df['Annual Income (k$)'].fillna(self.df['Annual Income (k$)'].median())
        self.df['Spending Score (1-100)'] = self.df['Spending Score (1-100)'].fillna(self.df['Spending Score (1-100)'].median())

        self.X = self.df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].values


    # -------------------------------
    # 🔷 SCALING
    # -------------------------------
    def scale_data(self):
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)


    # -------------------------------
    # 🔷 TRAIN MODEL
    # -------------------------------
    def train_model(self, n_clusters=4):
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.labels = self.model.fit_predict(self.X_scaled)
        self.centroids = self.model.cluster_centers_

        # 🔥 After training → assign names
        self._assign_cluster_names()


    # -------------------------------
    # 🔷 AUTO LABELING (IMPORTANT)
    # -------------------------------
    def _assign_cluster_names(self):
        """
        Assign meaningful names based on Income & Spending
        """
        # Convert centroids back to original scale
        centroids_original = self.scaler.inverse_transform(self.centroids)

        df_centroids = pd.DataFrame(
            centroids_original,
            columns=['Age', 'Income', 'Spending']
        )

        # Sort by Income + Spending (business logic)
        df_centroids['score'] = df_centroids['Income'] + df_centroids['Spending']
        df_centroids = df_centroids.sort_values(by='score')

        labels = ["Budget", "Regular", "Premium", "VIP"]

        self.cluster_names = {}
        for i, idx in enumerate(df_centroids.index):
            self.cluster_names[idx] = labels[i]

        print("\nCluster Label Mapping:")
        print(self.cluster_names)


    # -------------------------------
    # 🔷 SAVE MODEL
    # -------------------------------
    def save_model(self,
                   model_path=MODEL_PATH,
                   scaler_path=SCALER_PATH,
                   cluster_path=CLUSTER_NAMES):

        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        joblib.dump(self.cluster_names, cluster_path)

        print("Model, scaler, and cluster mapping saved successfully")


    # -------------------------------
    # 🔷 LOAD MODEL
    # -------------------------------
    def load_model(self,
                   model_path="../models/model.pkl",
                   scaler_path="../models/scaler.pkl",
                   mapping_path="../models/cluster_names.pkl"):

        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.cluster_names = joblib.load(mapping_path)

        print("Model, scaler, and mapping loaded")


# -------------------------------
# 🔷 MAIN
# -------------------------------
if __name__ == "__main__":

    dataset_path = DATASET_PATH
    model = CustomerSegmentation(dataset_path)

    model.load_data()
    model.preprocess()
    model.scale_data()

    model.train_model(n_clusters=4)

    model.save_model()

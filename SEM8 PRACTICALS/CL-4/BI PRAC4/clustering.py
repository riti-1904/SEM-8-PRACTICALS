# assignment04_clustering.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
import warnings

warnings.filterwarnings("ignore")

# 1. Load Dataset
print("Loading the Iris dataset...")
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print("Dataset Loaded Successfully\n")

# 2. Data Preprocessing
print("Starting Data Preprocessing...")
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 3. Determine Optimal Clusters using Elbow Method
print("Finding optimal number of clusters using Elbow Method...")
wcss = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K, wcss, marker='o')
plt.title('Elbow Method For Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# From the elbow graph, assume optimal K = 3
optimal_k = 3
print(f"Using Optimal K = {optimal_k} for clustering...\n")

# 4. KMeans Clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)
df['Cluster'] = clusters

# 5. Evaluation Metrics
sil_score = silhouette_score(scaled_data, clusters)
db_score = davies_bouldin_score(scaled_data, clusters)
print(f"Silhouette Score: {sil_score:.3f}")
print(f"Davies-Bouldin Index: {db_score:.3f}\n")

# 6. PCA for Visualization
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)
df['PCA1'] = pca_data[:, 0]
df['PCA2'] = pca_data[:, 1]

# 7. Visualizing Clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='Set1', s=100)
plt.title('Clusters Visualization using PCA')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.grid(True)
plt.show()

# 8. Cluster Summary
print("Cluster Centers (in original scaled feature space):")
print(pd.DataFrame(kmeans.cluster_centers_, columns=iris.feature_names))

# 9. Heatmap of Cluster Means
print("\nPlotting heatmap of feature means per cluster...")
cluster_summary = df.groupby('Cluster')[iris.feature_names].mean()

plt.figure(figsize=(8, 5))
sns.heatmap(cluster_summary, annot=True, cmap='coolwarm')
plt.title('Feature Means per Cluster')
plt.show()

print("\n✅ Clustering Completed Successfully.")

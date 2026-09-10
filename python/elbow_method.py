import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


df = pd.read_csv("world_happiness_combined.csv")


features = ["Happiness_Score", "GDP", "Social_Support",
            "Life_Expectancy", "Freedom", "Generosity", "Corruption"]

X = df[features]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertias, marker='o', color='steelblue')
plt.title("Elbow Method - Optimal Number of Clusters")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.xticks(range(1, 11))
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_plot11.png")
plt.show()
print("Elbow plot saved.")


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)


score = silhouette_score(X_scaled, df["Cluster"])
print(f"Silhouette Score: {score:.4f}")


cluster_summary = df.groupby("Cluster")[features].mean().round(3)
print(cluster_summary)


df.to_csv("world_happiness_clustered11.csv", index=False)
print("Clustered file saved.")
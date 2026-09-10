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


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)


score = silhouette_score(X_scaled, df["Cluster"])
print(f"Silhouette Score: {score:.4f}")


cluster_summary = df.groupby("Cluster")[features].mean().round(3)
print(cluster_summary)


df.to_csv("world_happiness_clustered.csv", index=False)
print("Clustered file saved.")

colors = {0: "green", 1: "blue", 2: "orange", 3: "red"}
labels = {0: "Cluster 0", 1: "Cluster 1", 2: "Cluster 2", 3: "Cluster 3"}

plt.figure(figsize=(10, 6))
for cluster in [0, 1, 2, 3]:
    subset = df[df["Cluster"] == cluster]
    plt.scatter(subset["GDP"], subset["Happiness_Score"],
                c=colors[cluster], label=labels[cluster], alpha=0.6)

plt.title("K-Means Clustering (K=3): GDP vs Happiness Score")
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("cluster_scatter11.png")
plt.show()
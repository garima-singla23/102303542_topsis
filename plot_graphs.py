import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("text_classification_result.csv")

plt.figure()
plt.bar(df["MODELS"], df["Topsis Score"])
plt.xlabel("Pre-trained Models")
plt.ylabel("Topsis Score")
plt.title("TOPSIS Scores for Text Classification Models")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig("topsis_scores.png")
plt.show()
plt.figure()
plt.bar(df["MODELS"], df["Rank"])
plt.xlabel("Pre-trained Models")
plt.ylabel("Rank")
plt.title("Ranking of Text Classification Models (TOPSIS)")
plt.xticks(rotation=15)
plt.gca().invert_yaxis()   # Rank 1 at top
plt.tight_layout()

plt.savefig("topsis_ranking.png")
plt.show()

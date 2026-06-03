python
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load the dataset
data = pd.read_excel('2026_Sub_Awards_Nomination_Open_Data.xlsx')

# Data preprocessing
data['Actual to Planned Budget Ratio'] = data['Actual Budget'] / data['Planned Budget']
data['Actual to Planned Benefits Ratio'] = data['Actual Benefits'] / data['Planned Benefits']

# Visualization: Budget Analysis
plt.figure(figsize=(10, 6))
plt.bar(data['Initiative Name'], data['Actual to Planned Budget Ratio'], color='blue')
plt.title('Actual to Planned Budget Ratio by Initiative')
plt.xlabel('Initiative Name')
plt.ylabel('Budget Ratio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Visualization: Collaboration Network
G = nx.Graph()
for _, row in data.iterrows():
    collaborators = row['Collaborators'].split(';')
    for collaborator in collaborators:
        G.add_node(collaborator)
        for other in collaborators:
            if collaborator != other:
                G.add_edge(collaborator, other)

plt.figure(figsize=(12, 12))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='yellow', font_size=10, font_weight='bold')
plt.title('Collaboration Network')
plt.show()

# Predictive Analysis (Simple Linear Regression Example)
from sklearn.linear_model import LinearRegression

# Train a simple linear regression model on planned vs. actual benefits
X = data[['Planned Benefits']]
y = data['Actual Benefits']
model = LinearRegression()
model.fit(X, y)

# Predict future benefits
future_planned_benefits = [[100000], [200000], [300000]]
predicted_benefits = model.predict(future_planned_benefits)
print(f"Predicted Benefits: {predicted_benefits}")

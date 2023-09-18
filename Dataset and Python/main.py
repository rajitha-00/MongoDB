import pandas as pd

data = pd.read_csv("./cleaned_dataset.csv")

print(data.head())       # Display the first few rows
print(data.shape)        # Display the dimensions of the dataset (rows, columns)

sampled_data = data.sample(n=150, random_state=42)

print(sampled_data.head())
print(sampled_data.shape)

sampled_data.to_csv("ne.csv", index=False)

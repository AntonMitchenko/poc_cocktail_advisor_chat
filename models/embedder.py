import numpy as np
import pandas as pd
import ast
from sentence_transformers import SentenceTransformer
import pickle

file_path = "../data/cocktails.csv"

embeddings_path = "../data/cocktail_embeddings.pkl"
preprocessed_path = "../data/preprocessed_cocktails.csv"

'''
Create preprocessed coctail dataset
'''

df = pd.read_csv(file_path)

# Drop irrelevant columns
columns_to_keep = ['id', 'name', 'alcoholic', 'category', 'glassType', 'instructions', 'ingredients', 'ingredientMeasures']
df = df[columns_to_keep]


def parse_list_column(column):
    return column.apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])


df['ingredients'] = parse_list_column(df['ingredients'])
df['ingredientMeasures'] = parse_list_column(df['ingredientMeasures'])

# Create a new column combining ingredients and measures for better searchability

def combine_ingredients_and_measures(row):
    combined = []
    for ingredient, measure in zip(row['ingredients'], row['ingredientMeasures']):
        combined.append(f"{ingredient} ({measure.strip()})" if measure else ingredient)
    return combined


df['combinedIngredients'] = df.apply(combine_ingredients_and_measures, axis=1)

# Remove rows with missing or incomplete data
df = df.dropna(subset=['name', 'instructions', 'ingredients'])

df.to_csv(preprocessed_path, index=False)

print(f"Preprocessing completed. Preprocessed data saved to {preprocessed_path}.")

'''
Create embedding
'''

df = pd.read_csv(preprocessed_path)

# Combine relevant fields into one text input for embeddings
df['embedding_text'] = df['combinedIngredients'] + ' ' + df['instructions']

# Initialize the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and efficient model

# Generate embeddings
print("Generating embeddings...")
df['embeddings'] = df['embedding_text'].apply(lambda x: model.encode(x, convert_to_numpy=True))

with open(embeddings_path, 'wb') as f:
    pickle.dump({
        'ids': df['id'].tolist(),
        'embeddings': np.stack(df['embeddings']),
        'data': df[['id', 'name', 'ingredients', 'instructions']].to_dict('records')
    }, f)

print(f"Embeddings generated and saved to {embeddings_path}.")
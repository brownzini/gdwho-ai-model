import pandas as pd
from sentence_transformers import InputExample

def load_csv_as_input_examples(csv_path: str):
    df = pd.read_csv(csv_path)
    examples = []
    for _, row in df.iterrows():
        examples.append(InputExample(
            texts=[row['input'], row['output']],
            label=float(row['label'])
        ))
    return examples
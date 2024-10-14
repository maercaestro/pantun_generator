import openai
import json
import pandas as pd
from dotenv import load_dotenv
import os
import tiktoken
import time

# Load environment variables from a .env file (optional, if you use one)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the JSONL file into a DataFrame for easy viewing
jsonl_file = 'pantun_finetune_dataset.jsonl'

with open(jsonl_file, 'r', encoding='utf-8') as f:
    lines = [json.loads(line) for line in f]

# Create a DataFrame from the JSONL lines
df = pd.DataFrame(lines)

# Display the first few rows of the DataFrame
print(df.head())

# Calculate the number of tokens for each prompt and completion
def num_tokens_from_string(string: str, encoding_name: str = "gpt-3.5-turbo") -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    return len(encoding.encode(string))

# Add columns for the number of tokens in each prompt and completion
df['prompt_tokens'] = df['prompt'].apply(lambda x: num_tokens_from_string(x))
df['completion_tokens'] = df['completion'].apply(lambda x: num_tokens_from_string(x))
df['total_tokens'] = df['prompt_tokens'] + df['completion_tokens']

# Display the total number of tokens in the dataset
total_tokens = df['total_tokens'].sum()
print("Total number of tokens in the dataset:", total_tokens)

# Create a fine-tuning file
def create_fine_tuning_file(file_path):
    print("Processing fine-tuning file " + file_path)
    file = openai.File.create(
        file=open(file_path, "rb"),
        purpose='fine-tune'
    )

    # Get the file ID
    file_id = file['id']

    # Check the file's status
    status = file['status']

    while status != 'processed':
        print(f"File status: {status}. Waiting for the file to be processed...")
        time.sleep(10)  # Wait for 10 seconds
        file_response = openai.File.retrieve(file_id)
        status = file_response['status']
        print(file_response)
    return file_id

# Start the fine-tuning job directly using Python
training_file_id = create_fine_tuning_file(jsonl_file)

fine_tuning_response = openai.FineTune.create(
    training_file=training_file_id,
    model="gpt-4o-mini"
)

print("Fine-tuning job started. Job details:")
print(fine_tuning_response)

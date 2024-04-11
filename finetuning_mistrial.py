import os

# Step 1: Setup Environment
!pip install pandas autotrain-advanced -q

# Step 2: Connect to HuggingFace for Model Upload
from huggingface_hub import notebook_login

# Prompt user for Hugging Face token
notebook_login()

# Step 3: Prepare and Upload Your Dataset
# Make sure your dataset file 'train.csv' is in the current directory

# Step 4: Fine-Tuning Command
# You will need to replace `your_project_name` and `your_hf_username/your_repo_name`
# with your actual project and repository names.
!autotrain llm --train \
    --project_name your_project_name \
    --model bn22/Mistral-7B-Instruct-v0.1-sharded \
    --data_path . \
    --use_peft --use_int4 \
    --learning_rate 2e-4 \
    --train_batch_size 12 \
    --num_train_epochs 3 \
    --trainer sft \
    --target_modules q_proj,v_proj \
    --push_to_hub \
    --repo_id your_hf_username/your_repo_name

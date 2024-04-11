# Personalized Education System Using GPT-4 and MongoDB

This repository contains code for a personalized education system designed to enhance student learning through tailored educational content and interactive concept explanations. The system leverages OpenAI's GPT-4 model for natural language understanding and generation, coupled with MongoDB for storing and retrieving student-specific educational data.

## Key Features

- **Personalized Content Retrieval:** Fetches educational material that is adapted to the student's learning progress and preferences.
- **Interactive Concept Explanations:** Utilizes GPT-4 to provide detailed explanations and answers to student queries, enhancing understanding of complex subjects.
- **Progress Tracking:** Uses MongoDB to store and update student profiles and learning progress, enabling dynamic content adaptation.

## System Components

### 1. MongoDB Database Setup
- **`StudentProfiles` Collection:** Stores each student's unique ID, current educational level, and other relevant learning data.
- Connection is established using MongoDB's standard connection string, ensuring secure access to the database.

### 2. Flask Application
- A RESTful API is developed using Flask to handle student requests. The application includes endpoints for retrieving educational content and requesting explanations of concepts.

### 3. OpenAI GPT-4 Integration
- GPT-4 is integrated to process natural language queries and generate context-appropriate responses.
- Uses embeddings and completions to provide personalized learning experiences.

## Fine-Tuning LLMs with AutoTrain

The `finetuning_mistrial.py` script is responsible for adapting a pre-trained GPT-4 model to the nuanced requirements of our education system. It fine-tunes the model using educational datasets to improve its accuracy and relevance in generating educational content and explanations.

### Inference with the Fine-Tuned Model

After fine-tuning, the `inference_of_tuned_model.py` script generates inferences from the model. It serves as the querying interface that receives educational prompts and outputs the model's generated responses, providing real-time educational assistance.

## API Endpoints

### GET Explanation
- **Endpoint:** `/get_explanation`
- **Method:** `POST`
- **Data Required:** `student_id` (string), `question` (string)
- **Functionality:** Receives a student's question and returns a detailed explanation based on their current learning context.
- **Response Format:** JSON object containing the explanation text.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/personalized-education-system.git

2. ** Install Dependencies: **
3. ** Set Environment Variables: **
4. ** Run the Flask Application: **

### Example Usage 
To use the API, send a POST request to the `/get_explanation` endpoint with a JSON payload containing the `student_id` and `question`. The system will return an explanation tailored to the student's learning level.
   ```json
   {
     "student_id": "123456",
     "question": "Explain the theory of relativity."
   }
   ```
### Contributing
Contributions are welcome! For significant changes, please open an issue first to discuss what you want to change.

from pymongo import MongoClient
import openai
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = "your_openai_api_key_here"

def get_database_collection():
    """ Connect to MongoDB to access the education collection. """
    client = MongoClient("your_mongodb_connection_string")
    db = client['EducationalData']
    return db['StudentProfiles']

def generate_embedding(text: str) -> list:
    """ Generate an embedding for text using OpenAI to aid in personalized content retrieval. """
    response = openai.Embedding.create(
        model="text-embedding-ada-002", 
        input=text
    )
    return response['data'][0]['embedding']

def retrieve_educational_content(student_id: str, topic: str):
    """ Retrieve personalized content based on the student's progress and the specified topic. """
    collection = get_database_collection()
    student_data = collection.find_one({"student_id": student_id})
    # Simulate personalized content retrieval logic
    content = f"Advanced content for {topic}, based on student's level: {student_data['level']}"
    return content

def explain_concept(question: str, context: str):
    """ Use GPT-4 to generate explanations or answers to student queries. """
    prompt = f"Explain the following concept in detail suitable for a student:\nQuestion: {question}\nContext: {context}"
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=500
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return str(e)

@app.route('/get_explanation', methods=['POST'])
def get_explanation():
    """ Endpoint to handle student requests for concept explanations. """
    data = request.get_json()
    student_id = data['student_id']
    question = data['question']
    
    # Retrieve context based on student's history or topic
    context = retrieve_educational_content(student_id, question)
    
    explanation = explain_concept(question, context)
    return jsonify({"explanation": explanation})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

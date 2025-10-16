from flask import Flask, render_template, request
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF for PDF resume parsing
import pandas as pd
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load saved models
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'model')
MODEL_DIR = os.path.abspath(MODEL_DIR)
vectorizer = pickle.load(open(os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl'), 'rb'))
job_vectors = pickle.load(open(os.path.join(MODEL_DIR, 'job_vectors.pkl'), 'rb'))
df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'dataset', 'jobs.csv'))

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if 'resume' not in request.files:
        return "No resume uploaded"

    resume_file = request.files['resume']
    try:
        resume_text = extract_text_from_pdf(resume_file)
    except Exception as e:
        resume_file.stream.seek(0)
        resume_text = resume_file.stream.read().decode(errors='ignore')

    # Transform and compute similarity
    resume_vector = vectorizer.transform([resume_text])
    similarity = cosine_similarity(resume_vector, job_vectors).flatten()

    # Get top matches
    top_indices = similarity.argsort()[-5:][::-1]
    results = df.iloc[top_indices][['title', 'company', 'location', 'skills']]

    return render_template('results.html', tables=[results.to_html(classes='data', header=True, index=False)])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

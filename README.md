AI Job Recommendation System

**AI Job Recommendation System** is a real-world AI/ML project that recommends relevant job postings to users by analyzing the content of their resumes.  
It leverages **Natural Language Processing (NLP)** and **Machine Learning** to match user skills with job requirements using **TF-IDF vectorization** and 
**cosine similarity**.  The project includes a **Flask-based web interface** for resume upload and displays top matching job recommendations.


 Features

- Upload your resume in PDF format
- Automatically extract text from resume using PyMuPDF
- Preprocess text and convert to vector using TF-IDF
- Compute similarity between resume and job postings
- Display top 5–10 relevant job recommendations with:
  - Job Title
  - Company Name
  - Location
  - Required Skills
- Easy-to-use and visually appealing web interface


 Technologies Used

| Layer | Technology / Library | Purpose |
|-------|-------------------|---------|
| **Backend** | Python | Core programming |
|  | Flask | Web framework for serving the app |
|  | Pandas | Data processing and manipulation |
|  | PyMuPDF (`fitz`) | Extract text from PDF resumes |
|  | scikit-learn | TF-IDF vectorizer, cosine similarity |

| **Frontend** | HTML, CSS | Web interface and styling |

| **ML/NLP** | TF-IDF Vectorization | Represent resumes and job descriptions as vectors |
|  | Cosine Similarity | Compute similarity score between resume and job postings |

| **Environment** | Python 3.9+ | Runtime environment |

| **Optional Tools** | Git, GitHub | Version control and repository hosting |

 How It Works

1. User uploads a PDF resume via the web interface.
2. The backend extracts resume text using **PyMuPDF**.
3. Text is transformed into vectors using **TF-IDF**.
4. Cosine similarity is computed between the resume vector and all job postings.
5. Top matches are sorted and displayed on the results page.

................................................................................................................................................

1. Artificial Intelligence (AI)

Definition:
Artificial Intelligence is a broad field of computer science that focuses on creating machines that can perform tasks that typically 
require human intelligence — such as understanding language, recognizing patterns, making decisions, or learning from experience.
project usage:
The entire system is AI-driven because it mimics human decision-making — reading resumes, understanding job requirements, and suggesting suitable roles intelligently.

 2. Machine Learning (ML)

Definition:
Machine Learning is a subset of AI that enables systems to learn automatically from data without being explicitly programmed. 
Instead of writing rules, we feed data and allow the model to discover patterns.
project usage:
You use ML concepts to learn the relationship between job descriptions and resume text — the system uses learned representations (vectors) to match them automatically.
The TF-IDF vectorizer and cosine similarity together form a simple but powerful ML pipeline.

 3. Natural Language Processing (NLP)

Definition:
NLP is a subfield of AI that helps computers understand, interpret, and process human language (text or speech). It’s how machines “read” and “understand” words.
project usage:
NLP is the core component — it allows the system to:
1.Extract text from resumes.
2.Clean and process job descriptions.
3.Compare meaning between two text documents (resume and job posting).
4.So your job recommendation logic depends on how well NLP transforms unstructured text into structured numerical form for comparison.

 4. TF-IDF Vectorization (Term Frequency – Inverse Document Frequency)

Definition:
TF-IDF is a text representation technique used in NLP. It converts text into numerical vectors that reflect how important a word is in a document relative to the entire collection (corpus).
TF (Term Frequency): measures how often a word appears in a single document.

IDF (Inverse Document Frequency): reduces the weight of common words (like "the", "and", "is") that appear in many documents.
Example:
If the word “Python” appears often in a resume but not in many job descriptions, it will get a high TF-IDF score, showing it’s a unique and important skill.
project usage:
1.You used a TF-IDF Vectorizer from scikit-learn to convert:
2.The resume text into a numerical vector.
3.The job descriptions into vectors.
4.This allows mathematical comparison between text documents — forming the base of your recommendation logic.

 5. Cosine Similarity

Definition:
Cosine Similarity is a mathematical measure that calculates how similar two vectors are by measuring the angle between them.
It gives values between 0 and 1:
1 → exactly similar (same direction)
0 → completely different (orthogonal)

Formula:
Cosine Similarity=∣∣A∣∣×∣∣B∣∣ A⋅B
	​where A and B are vectors.
project usage:
1.Once you have TF-IDF vectors for:
2.Resume (vector_resume)
3.Each Job Description (vector_job)
   -->You calculate cosine similarity:
similarity_score = cosine_similarity(vector_resume, vector_job)
The higher the score → the more relevant the job is to the resume.

 6. Flask

Definition:
Flask is a lightweight Python web framework that allows you to build web applications easily.
project usage:
Flask acts as the bridge between the ML model and the user interface:
1.Handles file uploads (PDF resumes)
2.Calls your ML logic (TF-IDF + similarity)
3.Sends the results to the front-end (results.html)
4.It turns your ML logic into a real, interactive application.

 7. Scikit-learn

Definition:
Scikit-learn (or sklearn) is one of the most popular Python libraries for machine learning. It provides efficient tools for data preprocessing, model training, and evaluation.
 project usage:
You used:
1.TfidfVectorizer from sklearn.feature_extraction.text
2,cosine_similarity from sklearn.metrics.pairwise
3.These tools handle the heavy mathematical work of transforming and comparing text efficiently.

 8. PyMuPDF (fitz)

Definition:
PyMuPDF is a Python library used to read and extract text from PDF files.
 project:
When the user uploads a resume in PDF format:
fitz.open() reads the file.
The text from each page is extracted using .get_text().
The extracted text is then used for analysis.
This lets you analyze real resumes without needing users to manually type their information.

9. Pandas

Definition:
Pandas is a Python library used for data analysis and manipulation. It allows you to store data
in tables (DataFrames) and perform operations efficiently.
 project usage:
I use pandas to:
1.Read the jobs.csv dataset.
2.Combine multiple job-related columns into a single text.
3.Store and display the top recommended jobs neatly.

 10. HTML & CSS

Definition:
HTML (HyperText Markup Language) is used to structure web pages.
CSS (Cascading Style Sheets) defines how those pages look — colors, fonts, spacing, layout, etc.
project usage:
1.index.html — where the user uploads a resume.
2.results.html — displays recommended jobs.
3.style.css — makes it look clean, professional, and user-friendly.

 11. Cosine Similarity + TF-IDF Combined Conceptually
To summarize how they work together:
Step	Process	Tool....
1	Convert all text (resumes + jobs) to numerical vectors	TF-IDF
2	Compare vectors mathematically	Cosine Similarity
3	Sort results by score	Pandas / Numpy
4	Display best matches	Flask + HTML
That’s how  AI-powered job recommender turns plain text into smart, data-driven insights.

 12. Pipeline Overview

Here’s how everything connects:

User Uploads Resume (PDF)
          ↓
Extract Text (PyMuPDF)
          ↓
Vectorize Text (TF-IDF via scikit-learn)
          ↓
Compute Similarity (Cosine Similarity)
          ↓
Find Top Matches (Pandas DataFrame)
          ↓
Display Results (Flask + HTML/CSS)


 13. Why These Technologies Work Well Together

1.TF-IDF = interpretable, efficient, works well for text similarity tasks.
2.Cosine Similarity = simple and mathematically strong for document comparison.
3.Flask = lightweight and perfect for ML model deployment.
4.PyMuPDF = easy to extract resume data.
5.Pandas = simplifies dataset handling and output display.
6.HTML/CSS = makes your AI model usable through an elegant interface.


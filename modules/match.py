from sklearn.feature_extraction.text import TfidfVectorizer

def match_resume_with_job(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = (tfidf_matrix * tfidf_matrix.T).A[0,1]
    return similarity

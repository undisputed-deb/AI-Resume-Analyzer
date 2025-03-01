import re

def preprocess_text(text):
    """Clean and prepare text for analysis."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Keep alphanumeric characters, periods, commas, and common punctuation
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    
    # Ensure there's enough text for analysis
    if len(text.strip()) < 10:
        return ""
        
    return text.strip()

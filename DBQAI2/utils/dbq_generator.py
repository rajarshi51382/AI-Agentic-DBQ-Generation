import json
import os
from googlesearch import search
import google.generativeai as genai

# IMPORTANT: SET YOUR GEMINI API KEY HERE
# You can get your API key from Google AI Studio
# It is recommended to set this as an environment variable for security
API_KEY = ""

genai.configure(api_key=API_KEY)

def generate_dbq(question):
    """
    Generates a DBQ by brainstorming sources with Gemini and searching for them.
    """

    # 1. Brainstorm source ideas with Gemini
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"""
    As a history expert, generate a list of 7-10 potential primary source documents for a DBQ on the following topic: "{question}"

    For each document, provide a brief description of what it is and why it's relevant.
    """
    try:
        response = model.generate_content(prompt)
        source_ideas = response.text.split('\n')
    except Exception as e:
        print(f"An error occurred while brainstorming sources: {e}")
        return None

    #Find specific documents for each idea
    selected_docs = []
    for idea in source_ideas:
        if not idea.strip():
            continue

        # Search for the document on Google
        search_query = f"{idea} primary source document"
        try:
            search_results = search(search_query, num_results=1)
            if search_results:
                result = search_results[0]
                selected_docs.append({
                    "title": result,
                    "url": result,
                    "type": "text",  
                })
        except Exception as e:
            print(f"An error occurred while searching for a document: {e}")

    return {
        'question': question,
        'documents': selected_docs
    }
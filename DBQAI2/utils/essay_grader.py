import google.generativeai as genai
import os
import json

# IMPORTANT: SET YOUR GEMINI API KEY HERE
# You can get your API key from Google AI Studio
# It is recommended to set this as an environment variable for security
API_KEY = ""

genai.configure(api_key=API_KEY)

def grade_essay(essay):
    """
    Grades the essay using the Gemini API.
    """
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"""Grade the following DBQ essay based on the following rubric. The total score is out of 7 points.

**Rubric:**

*   **Thesis (0-1 point):**
    *   1 point: Responds to the prompt with a historically defensible thesis/claim that establishes a line of reasoning.
    *   0 points: Does not meet the criteria for 1 point.
*   **Contextualization (0-1 point):**
    *   1 point: Describes a broader historical context relevant to the prompt.
    *   0 points: Does not meet the criteria for 1 point.
*   **Evidence (0-3 points):**
    *   1 point: Uses the content of at least two documents to address the topic of the prompt.
    *   2 points: Supports an argument in response to the prompt using at least four documents.
    *   3 points: Uses at least one additional piece of specific historical evidence (beyond that found in the documents) relevant to an argument about the prompt.
*   **Analysis and Reasoning (0-2 points):**
    *   1 point: For at least three documents, explains how or why the document's point of view, purpose, historical situation, and/or audience is relevant to an argument.
    *   2 points: Demonstrates a complex understanding of the historical development that is the focus of the prompt, using evidence to corroborate, qualify, or modify an argument that addresses the question. (e.g., explaining nuance, explaining both similarity and difference, explaining both continuity and change, connecting to other historical periods).

**Instructions:**

Grade the essay below and provide a score for each category in the rubric. Return the scores and a detailed feedback in a JSON format. The JSON should have the following keys:
*   `"score"`: The total score, an integer from 0 to 7.
*   `"feedback_text"`: A string containing detailed feedback for the student, explaining the reasoning for the score in each category.
*   `"rubric"`: A JSON object with the breakdown of the score for each category: `"Thesis"`, `"Contextualization"`, `"Evidence"`, and `"Analysis_and_Reasoning"`.

**Essay:**
{essay}
"""
    try:
        response = model.generate_content(prompt)
        # Clean the response to extract only the JSON part
        cleaned_response = response.text.strip().replace('```json', '').replace('```', '')
        feedback_data = json.loads(cleaned_response)
        return feedback_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'score': 0,
            'feedback_text': 'There was an error grading the essay. Please try again later.',
            'rubric': {
                'Thesis': 0,
                'Contextualization': 0,
                'Evidence': 0,
                'Analysis_and_Reasoning': 0
            }
        }

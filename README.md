# DBQ AI Grader: Your AI-Powered History Assistant

DBQ AI Grader is a powerful web application built with Flask and powered by Google's Gemini AI. It's designed to revolutionize the way students and teachers approach Document-Based Questions (DBQs). This tool not only generates dynamic DBQs from a curated set of historical sources but also provides instant, AI-driven grading and feedback on student essays.

## Live Demo

*[Link to a live demo of the application would go here. You can host this on platforms like PythonAnywhere, Heroku, or a cloud provider.]*

## Features

*   **Dynamic DBQ Generation**: Creates unique Document-Based Questions using a predefined set of historical sources. The application simulates a search for sources, providing a more engaging user experience.
*   **AI-Powered Essay Grading**: Leverages the power of Google's Gemini 2.5 Flash model to provide instant, detailed, and rubric-based feedback on student essays.
*   **Comprehensive Feedback**: The feedback includes a score for each category of the DBQ rubric (Thesis, Contextualization, Evidence, Analysis and Reasoning), along with a detailed explanation for the score.
*   **User-Friendly Interface**: A clean and intuitive interface that makes it easy for students to generate DBQs, submit their essays, and view their feedback.
*   **Extensible and Customizable**: The application is built with a modular structure, making it easy to add new features, customize the rubric, or change the set of source documents.

## How It Works

1.  **Generate a DBQ**: The user navigates to the "Generate DBQ" page. The application then presents a DBQ based on a predefined set of documents.
2.  **Submit an Essay**: After analyzing the documents and the question, the user writes their essay and submits it through the "Submit Essay" page.
3.  **AI-Powered Grading**: The submitted essay is sent to the Google Gemini API, which grades it based on a detailed rubric.
4.  **View Feedback**: The application displays the feedback to the user, including a score for each category of the rubric and detailed comments.

## Technologies Used

*   **Backend**: Flask
*   **Frontend**: HTML, CSS, JavaScript
*   **AI Model**: Google Gemini 2.5 Flash
*   **Python Libraries**:
    *   `flask`
    *   `google-generativeai`
    *   `googlesearch-python`

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)
*   A Google Gemini API Key. You can get your API key from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  **Clone the repository (or download the source code)**
    ```sh
    git clone <your-repository-url>
    cd DBQAI2
    ```

2.  **Create and activate a virtual environment**
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your API Key**
    You need to set your Google Gemini API key in the following files:
    *   `utils/dbq_generator.py`
    *   `utils/essay_grader.py`

    It is highly recommended to set this as an environment variable for security.

    ```python
    # In utils/dbq_generator.py and utils/essay_grader.py
    API_KEY = "YOUR_API_KEY" 
    ```

## Usage

1.  Make sure you are in the root directory of the project (`DBQAI2/`) and your virtual environment is activated.

2.  Run the Flask application:
    ```sh
    python app.py
    ```

3.  Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

## Project Structure

```
DBQAI2/
├── .gitignore
├── app.py              # Main Flask application file
├── dbq_grader.txt
├── plan.txt
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── .git/
├── dbq_data/
│   └── sources.json    # Data for the DBQs
├── static/
│   └── style.css       # CSS stylesheets
├── templates/
│   ├── feedback.html       # Template for the feedback page
│   ├── generate_dbq.html   # Template for the DBQ generation page
│   ├── home.html           # Template for the home page
│   └── submit_essay.html   # Template for the essay submission page
└── utils/
    ├── dbq_generator.py    # Module for generating DBQs (currently not fully integrated)
    └── essay_grader.py     # Module for grading essays using the Gemini API
```

## Future Enhancements

- [ ] **User Authentication**: Add user accounts to track student progress and save their work.
- [ ] **Dynamic DBQ Generation**: Fully integrate the `dbq_generator.py` module to allow for the dynamic generation of DBQs based on user input.
- [ ] **Document Upload**: Allow users to upload their own source documents for DBQ generation.
- [ ] **More Sophisticated Feedback**: Enhance the feedback to provide more specific suggestions for improvement, such as identifying specific sentences or paragraphs that need work.
- [ ] **Add screenshots and demo GIFs to this README.**

## Contributing

Contributions are welcome! If you have any ideas for how to improve this application, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
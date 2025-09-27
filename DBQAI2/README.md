# DBQ AI Grader

DBQ AI is a web application designed to assist students and teachers with Document-Based Questions (DBQs). It generates DBQs from a set of source documents and automatically grades student-submitted essays, providing instant feedback.

## Features

*   **Dynamic DBQ Generation**: Creates unique Document-Based Questions using a predefined set of historical sources.
*   **Essay Submission Portal**: A user-friendly interface for students to write and submit their essays.
*   **Automated Grading**: Provides an instant score and constructive feedback on submitted essays.
*   **Simple & Clean UI**: Easy to navigate interface for a seamless user experience.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)

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

## How to Run the Application

1.  Make sure you are in the root directory of the project (`DBQAI2/`) and your virtual environment is activated.

2.  Run the Flask application:
    ```sh
    python app.py
    ```

3.  Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

## How to Use

1.  **Home Page**: The landing page of the application. From here you can navigate to the other sections.
2.  **Generate DBQ**: Click on the "Generate DBQ" link. The application will present a DBQ based on the documents located in `dbq_data/sources.json`.
3.  **Submit Essay**: After reviewing the documents and the question, navigate to the "Submit Essay" page to write and submit your response.
4.  **View Feedback**: Upon submission, the application will process your essay and display a feedback page with a score and suggestions for improvement.

*(Note: The DBQ generation and essay grading are based on pre-configured logic and data sources.)*

## Future Enhancements

- [ ] Add user authentication to track progress.
- [ ] Allow users to upload their own source documents for DBQ generation.
- [ ] Add screenshots and demo GIFs to this README.

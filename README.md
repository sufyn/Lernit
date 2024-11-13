# Lernit
An edtech platform using prompt engineering.
🤔 What is this?
Large language models (LLMs) are emerging as a transformative technology, enabling developers to build applications that they previously could not. However, using these LLMs in isolation is often insufficient for creating a truly powerful app - the real power comes when you can combine them with other sources of computation or knowledge.

# Flask Application for GPT-Based Question and Answer System

This is a Flask-based web application that integrates with the Hugging Face API to generate multiple-choice questions based on user input and provide both correct and incorrect answers. The project uses Flask for the web framework and LangChain to handle the GPT-3 model from Hugging Face.

## Features

- **User Authentication**: Login and signup pages for user interaction.
- **GPT Integration**: Uses GPT-3 to generate multiple-choice questions with answers.
- **Multiple GPT-3 Models**: Integrates different prompt templates to generate both correct and incorrect answers for the questions.
- **Web Interface**: Provides a clean user interface to interact with the GPT model and view the generated questions and answers.
- **API Integration**: Handles POST requests for generating questions and answers dynamically.

## Project Setup

To run this project locally, follow these steps:

### Prerequisites

- Python 3.7 or higher
- Flask
- Hugging Face API (Flan-T5 model)
- LangChain
- dotenv (for environment variable management)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Flask-GPT-Application.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Flask-GPT-Application
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file with your Hugging Face API key:
   ```env
   HUGGINGFACE_API_KEY=your_api_key_here
   ```

### Running the Application

1. Run the Flask app:
   ```bash
   python app.py
   ```

2. Visit `http://127.0.0.1:5000` in your web browser.

### API Endpoints

- **GET `/`**: Home page
- **GET `/login`**: Login page
- **GET `/signup`**: Signup page
- **GET `/youtube`**: YouTube page
- **GET `/features`**: Features page
- **GET `/resources`**: Resources page
- **POST `/gpt`**: Generates multiple-choice questions based on the user's search term.
- **POST `/gpt3`**: Another endpoint to generate unique multiple-choice questions based on a different prompt.

### Example Request for `/gpt`:

- Method: POST
- Body (form data):
  ```text
  search: "Science"
  ```

### Example Response:

```json
{
  "question": "Q: Generate random unique hard Multiple choice questions with answers on Science topic?",
  "answers": [
    {"text": "Answer A", "correct": true},
    {"text": "Answer B", "correct": false},
    {"text": "Answer C", "correct": false},
    {"text": "Answer D", "correct": false}
  ]
}
```

## Technologies Used

- **Flask**: Python web framework for building web applications.
- **LangChain**: A framework for building language model chains.
- **Hugging Face**: A platform that provides access to state-of-the-art machine learning models (used here with `flan-t5-xxl`).
- **HTML/CSS**: For the frontend design.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for providing the language models.
- LangChain for simplifying the integration of language models into Flask applications.
```

# Chatbot

A modern, interactive chatbot powered by Google's Gemini API, built using Streamlit. This chatbot features a sleek UI, supports multiple chat sessions, and allows users to save and delete chat histories.

## Features
- 🤖 **Interactive Chatbot**: Chat with an AI model using Google's Gemini API.
- 📁 **Chat History Management**: Save, delete, and manage multiple chat sessions.
- 🌙 **Dark Theme**: Modern UI with a smooth, gradient-based dark theme.
- 📅 **Dynamic Date Display**: Automatically displays the current date during chat.
- 🧹 **Session Persistence**: Keeps chat history until a new session is initiated.

## Requirements
- Python 3.9+
- Streamlit
- Google Generative AI SDK

## Installation

1. Clone the repository:
```bash
    git https://github.com/Urpita/Chatbot/blob/main/Chat_Bot.py
    
```

2. Set up a virtual environment (optional but recommended):
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
    pip install -r requirements.txt
```

## Usage

1. Add your Google Gemini API key:
   - Replace `api_key` in the script with your actual API key.

2. Run the chatbot:
```bash
    streamlit run chatbot.py
```

## File Structure
```
streamlit-chatbot/
├── chatbot.py        # Main Streamlit app
└── README.md         # Project documentation
```

## Customization
- **Chatbot Model**: Update `genai.GenerativeModel('gemini-1.5-pro')` to use other models.
- **UI Styling**: Modify CSS in the `st.markdown()` block for custom appearance.

## Troubleshooting
- Ensure your API key is valid and has the required permissions.
- Check Python and package versions if you encounter errors.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork the repo and submit a pull request.

## Author
Developed by [Urpita Das](https://github.com/Urpita).


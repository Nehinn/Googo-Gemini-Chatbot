# 🤖 GOOGO Gemini Chatbot

A clean, interactive multi-turn conversational AI chatbot built using Python, Streamlit, and the official Google GenAI SDK powered by `gemini-3.8-flash`.

---

## 🚀 Features

- **Multi-Turn Chat History:** Remembers conversational context across responses during an active session.
- **Optimized Performance:** Direct REST transport communication to prevent socket dropouts and ensure fast response delivery.
- **Streamlit Native UI:** Minimalist and responsive chat interface with custom session state management.
- **Secure Configuration:** Environment-based credential management via `.env` to protect API keys.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Engine:** [Google GenAI SDK](https://github.com/google-gemini/generative-ai-python) (`gemini-3.8-flash`)
- **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
Gemini_GenAI_Project/
│
├── main.py              # Streamlit UI & chat orchestration
├── gemini_utility.py    # Gemini client initialization & chat session loader
├── requirements.txt     # Python dependency specifications
├── .gitignore           # Git ignore configuration (protects API keys)
├── .env                 # Local API keys (excluded from source control)
└── README.md            # Project documentation
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/Nehinn/Googo-Gemini-Chatbot.git](https://github.com/Nehinn/Googo-Gemini-Chatbot.git)
cd Googo-Gemini-Chatbot
2. Set Up a Virtual Environment (Recommended)
Bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Windows (Command Prompt)
venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Your API Key
Obtain a free API key from Google AI Studio.

Create a .env file in the root directory:

Bash
touch .env
Add your key inside .env:

Code snippet
GEMINI_API_KEY="your_actual_gemini_api_key_here"
▶️ Running the Application
Launch the Streamlit dashboard:

Bash
python -m streamlit run main.py
The app will open automatically in your browser at http://localhost:8501.

🛡️ License
This project is licensed under the MIT License.


---

### Push `README.md` to your repository:

In Git Bash, run:

```bash
git add README.md
git commit -m "docs: add comprehensive project README"
git push origin main

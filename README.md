# 🦜 LangChain: Summarize Text From YouTube or Website

Welcome to **LangChain: Summarize Text**! This app allows you to extract text content from YouTube videos or websites, and get a summarized version of the content. It uses **LangChain**, **Groq API**, and advanced models to generate the summary. 

## Features ✨

- **📺 YouTube Video Summarization**: Enter a YouTube URL, and the app will extract the video's transcript and provide a concise summary.
- **🌐 Website Summarization**: Enter a website URL, and the app will summarize the main content of the page.
- **⚡ Fast Summaries**: Powered by **LangChain**'s integration with **Groq API**, the app provides accurate and fast summaries.
- **🔑 API Key Required**: To use the summarization feature, you need a valid **Groq API Key**.

## Tech Stack 🛠️

- **Streamlit**: A Python framework for building interactive web applications.
- **LangChain**: A framework that simplifies building language models and LLM-powered applications.
- **GROQ API**: The model **Gemma-7b-It** is used via the **GROQ API** for generating summaries.
- **Validators**: For validating the URL input.
- **YouTube Loader**: For extracting transcript from YouTube videos.
- **Unstructured URL Loader**: For scraping and extracting text from web pages.

## Installation ⚙️

To run this app locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/langchain-url-summarizer.git
cd langchain-url-summarizer
```

### 2. Install Dependencies
Ensure that you have Python 3.7+ installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Get Your GROQ API Key 🔑
- Sign up for **GROQ API** to obtain your **API Key**.
- Enter the key in the sidebar once the app is running.

### 4. Run the Streamlit App 🚀
Once the dependencies are installed and your API key is set, run the app using:
```bash
streamlit run app.py
```

The app will now be accessible at [http://localhost:8501](http://localhost:8501).

## Usage 📱

1. **Enter the URL**: Provide a valid YouTube or website URL.
2. **Enter the GROQ API Key**: Add your **GROQ API Key** in the sidebar to enable the summarization feature.
3. **Click "Summarize"**: The app will fetch the content and generate a 300-word summary.

## App Flow 🌊

1. The app first validates the provided URL and API key.
2. If the URL is a **YouTube URL**, the app loads the video’s transcript.
3. If it's a **Website URL**, it loads the page content using a web scraper.
4. The **Groq-powered LLM** generates a concise 300-word summary.
5. The summary is displayed on the app.

## Project Structure 🗂️

```plaintext
langchain-url-summarizer/
│
├── app.py                  # Main Streamlit app file
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── assets/
    └── (optional)          # Folder for storing assets (e.g., images, icons)
```

## Screenshots 📸

![LangChain Summarizer](screenshots/langchain_summary.png)
*Example of the app summarizing text from a YouTube video or website.*

## Contributing 🤝

We welcome contributions! If you'd like to help improve the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary modifications or enhancements.
4. Create a pull request with a description of the changes.

## Acknowledgements 🙏

- **LangChain**: For making it easy to integrate language models and create powerful workflows.
- **Groq API**: For providing the **Gemma-7b-It** model for text summarization.
- **Streamlit**: For providing a quick way to build interactive web apps.
- **Validators**: For URL validation.

---

**Note**: You need a valid **Groq API Key** to use the summarization functionality. Please provide your key in the sidebar to enable it. 🔑

---

This `README.md` includes all the essential details, setup instructions, and a clean structure to ensure your users can quickly get started with the app. 😊

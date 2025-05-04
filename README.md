# 🧞 WebGenie - AI Website Builder

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co)

An AI-powered website builder that generates complete HTML/CSS/JS code from natural language descriptions.

[![WebGenie Demo Video](https://img.shields.io/badge/▶️_Demo_Video-FF0000?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/15Z5yiX35u5Nb0tVgFObCeixgz4FNk_d9/view?usp=sharing)

## ✨ Features

- **AI-Powered Generation**: Creates websites using fine-tuned Qwen2.5-Coder-14B model
- **Customizable Designs**:
  - Color scheme picker
  - Font selection (6+ modern fonts)
  - Layout styles (Modern, Minimalist, Corporate, etc.)
- **Interactive Preview**: Real-time responsive preview
- **One-Click Export**: Download production-ready HTML/CSS/JS
- **Developer Friendly**: Clean code output with proper formatting

## 🚀 Quick Start

### 📦 Prerequisites

- Python 3.9+ (with pip)
- [Ngrok API endpoint](#-environment-variables)

### 🛠️ Installation

```bash
git clone https://github.com/yourusername/webgenie.git
cd webgenie
pip install -r requirements.txt
```

### 🔐 Environment Variables

Create a `.env` file in the root directory with:

```ini
# API Configuration
NGROK_API_URL="your_api_url_here"  # From either:
                                   # 1) Our provided notebook's ngrok endpoint OR
                                   # 2) Your own deployed model endpoint
API_TIMEOUT=600                    # Timeout in seconds (10 minutes)
```

### 🚀 Running the App

```bash
streamlit run app.py
```

### 🏗️ Project Structure

```
WebGenie/
├── app.py               # Main application (Streamlit UI)
├── generator.py         # Website generation logic
├── model.py             # AI model interface
├── prompt.py            # Prompt templates
├── requirements.txt     # Dependencies
├── utils/
│   ├── parser.py        # Code block parser
│   └── aggregator.py    # Code combiner
└── README.md
```

### 💡 Example Prompts

| Use Case       | Prompt                                                                                        |
| -------------- | --------------------------------------------------------------------------------------------- |
| **Portfolio**  | "Create a modern portfolio for a UX designer with a dark theme and a contact form."           |
| **E-commerce** | "Build an online store for sneakers with product filters and a checkout button."              |
| **SaaS Site**  | "Design a landing page for a productivity app with three features and a signup form."         |
| **Restaurant** | "Generate a website for a pizza restaurant with a photo gallery and online reservation form." |

### 🌐 Deployment

#### Docker

```bash
docker build -t webgenie .
docker run -p 8501:8501 -e NGROK_API_URL=$NGROK_API_URL webgenie
```

### 👥 Collaborators

\- **Lewaa Thebian**  
 [![GitHub](https://img.shields.io/badge/LeTh28-100000?logo=github&logoColor=white)](https://github.com/LeTh28)

\- **Sabine Farhat**  
 [![GitHub](https://img.shields.io/badge/srf5-100000?logo=github&logoColor=white)](https://github.com/srf5)

# 🖥️ AI ScreenReader: Smart Visual Assistant

Instantly analyze and understand your screen content using advanced AI technology!

## 🚀 Features

- **Interactive Screen Capture**: Select any screen region for detailed AI analysis
- **Multi-modal AI Processing**: Uses AI to describe and interpret screen contents
- **Flexible Prompting**: Describe specific details about the captured screen
- **Real-time WebSocket Communication**: Seamless interaction between frontend and AI backend

## 🔧 Prerequisites

- Python 3.8+
- Ollama
- WebSocket-compatible browser
- Required Python libraries:
  - `asyncio`
  - `websockets`
  - `pyautogui`
  - `opencv-python`
  - `numpy`
  - `requests`

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BaryonDev/Ai-ScreenReader.git
   cd Ai-ScreenReader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Ollama:
   - Install Ollama from [ollama.ai](https://ollama.ai)
   - Pull the `minicpm-v` model:
     ```bash
     ollama pull minicpm-v
     ```

## 🎮 Usage

1. Start Ollama server
2. Run the Python script:
   ```bash
   python visualscreen.py
   ```
3. Open `visualscreen.html` in your browser
4. Click "Capture Screen" or enter a text prompt

## 💡 How It Works

- Captures screen regions using PyAutoGUI
- Sends images to Ollama's AI model
- Processes image with custom prompts
- Returns detailed AI-generated descriptions

## 🤝 Contributing

Contributions welcome! Please check out our [Contributing Guidelines](CONTRIBUTING.md).

## 📄 License

[Your License Here - e.g., MIT License]

## 🌟 Star the Repo!

If you find this project useful, please give it a star ⭐

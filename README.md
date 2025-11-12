# Audio Translator

A modern web application that transcribes audio files and translates them into multiple languages using OpenAI's Whisper and GPT-4o-mini models.

![Audio Translator](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-orange.svg)

## Features

- **Audio Transcription**: Automatically transcribes audio to English using Whisper AI
- **Multi-Language Translation**: Translate to 20+ languages including Hindi, Spanish, French, German, Chinese, Japanese, and more
- **Multiple Audio Formats**: Supports MP3, M4A, MP4, MPEG, WAV, WebM
- **Modern UI**: Beautiful, responsive interface with real-time feedback
- **Cost-Efficient**: Uses GPT-4o-mini for affordable translations
- **Automatic Cleanup**: Uploaded files are automatically deleted after processing

## Supported Languages

Hindi, Spanish, French, German, Chinese, Japanese, Korean, Arabic, Portuguese, Russian, Italian, Turkish, Dutch, Polish, Swedish, Bengali, Tamil, Telugu, Marathi, Urdu

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/audio-translator.git
   cd audio-translator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**

   Navigate to `http://localhost:8080`

## Usage

1. **Upload Audio File**: Click "Choose Audio File" and select your audio file (MP3, M4A, etc.)
2. **Select Target Language**: Choose the language you want to translate to
3. **Click "Translate Audio"**: Wait for the processing to complete
4. **View Results**: See both the original English transcription and the translation

## Project Structure

```
audio-translator/
├── app.py              # Main Flask application
├── demo.py             # Demo script for testing Whisper API
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
├── static/            # Static files (uploaded audio)
└── templates/
    └── index.html     # Web interface
```

## API Endpoints

### `GET /`
Returns the main web interface

### `POST /translate`
Processes audio file and returns translation

**Parameters:**
- `file`: Audio file (multipart/form-data)
- `language`: Target language name (string)

**Response:**
```json
{
  "success": true,
  "original": "Original English transcription",
  "translation": "Translated text",
  "language": "Target Language"
}
```

## Technologies Used

- **Backend**: Flask (Python)
- **AI Models**:
  - OpenAI Whisper (Audio transcription)
  - GPT-4o-mini (Translation)
- **Frontend**: HTML, CSS, JavaScript
- **Environment Management**: python-dotenv

## Cost Optimization

This application uses GPT-4o-mini instead of GPT-4, which is approximately 60-80x cheaper while maintaining excellent translation quality for most use cases.

**Estimated costs per request:**
- Whisper transcription: ~$0.006 per minute of audio
- GPT-4o-mini translation: ~$0.0001-0.0005 per translation

## Demo Script

A standalone demo script is included to test the Whisper API:

```bash
python demo.py
```

This will transcribe the sample `Recording.mp3` file.

## Security Notes

- Never commit your `.env` file or API keys to version control
- The application automatically deletes uploaded files after processing
- Uploaded files are stored temporarily in the `static/` directory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Acknowledgments

- OpenAI for Whisper and GPT models
- Flask framework for the web application
- All contributors and users of this project

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

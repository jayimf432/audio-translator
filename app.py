from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"
app.config['JSON_AS_ASCII'] = False

# Allowed audio file extensions
ALLOWED_EXTENSIONS = {'mp3', 'm4a', 'mp4', 'mpeg', 'mpga', 'wav', 'webm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Validate language input
        language = request.form.get("language")
        if not language:
            return jsonify({"error": "Please specify a target language"}), 400

        # Validate file upload
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file format. Supported: mp3, m4a, mp4, mpeg, mpga, wav, webm"}), 400

        # Save uploaded file
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Open the uploaded file (not hardcoded Recording.mp3)
        with open(filepath, "rb") as audio_file:
            # Transcribe audio to English using Whisper
            transcript = client.audio.translations.create(
                model="whisper-1",
                file=audio_file
            )

        # Translate the English transcript to target language
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"You will be provided with a sentence in English, and your task is to translate it into {language}"
                },
                {
                    "role": "user",
                    "content": transcript.text
                }
            ],
            temperature=0,
            max_tokens=256
        )

        # Clean up uploaded file after processing
        if os.path.exists(filepath):
            os.remove(filepath)

        return jsonify({
            "success": True,
            "original": transcript.text,
            "translation": response.choices[0].message.content,
            "language": language
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
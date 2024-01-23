import whisper
from docx import Document
import os

model = whisper.load_model("base.en")

# audio_out = "audio.mp3"
audio_out = input("Enter the path of the audio file.mp3: ")
## check mp3 file
if audio_out[-4:] != ".mp3":
    print("Please enter a valid mp3 file")
    exit()

audio_out = os.path.normpath(audio_out)

# script_dir = os.path.dirname(os.path.abspath(__file__)) + "/models/"
# model_dir = os.path.join(script_dir, "base.en.pt")

# result = model.transcribe(audio_out, verbose=False, fp16=False, download_root=model_dir)
result = model.transcribe(audio_out, verbose=False, fp16=False)
transcription_data = result["transcription"]

# Specify the path and name of the Word file
output_word_file = "transcribed_text.docx"

# Create a Word document
doc = Document()

# Write the transcribed text with timestamps to the Word document
for entry in transcription_data:
    start_time = entry["start_time"]
    text = entry["text"]

    # Format the timestamp as HH:MM:SS
    timestamp = f"{start_time // 3600:02d}:{(start_time % 3600) // 60:02d}:{start_time % 60:02d}"

    # Add timestamp and transcribed text to the document
    doc.add_paragraph(f"{timestamp}\n{text}\n\n")

# Save the Word document
doc.save(output_word_file)

print(f"Transcribed text with timestamps has been saved to: {output_word_file}")
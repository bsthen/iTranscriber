# iTranscriber

## Introduction

iTranscriber can assist you in transcribing audio files (audio.mp3) to text files (text_file.docx) for free and without limitations.

## Requirement

- Python3.11
- OpenAI Wishper
- FFMPEG (Installation on [Windows](https://phoenixnap.com/kb/ffmpeg-windows), [Mac](https://phoenixnap.com/kb/ffmpeg-mac) or [Ubuntu](https://phoenixnap.com/kb/install-ffmpeg-ubuntu))
- Audio Speak In English

## Installations

Clone the iTranscriber repository:

```sh
git clone https://github.com/bsthen/iTranscriber.git && cd iTranscriber
```

Double click **install.bat** Or

Create a virtual environment:

```sh
python3 -m venv env
```

If you don't have virtual environments installed, you can find instructions [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Activate the environment on Linux or macOS:

```sh

source env/bin/activate
```

Or activate the environment on Windows:

```sh

\env\Scripts\activate.bat
```

Install dependencies:

```sh

pip3 install -r requirements.txt
```

## Running the Application

```sh
python3 main.py
```

Or double click on **iTranscriber.bat**

Follow the instructions on the console of iTranscriber.

## Note

- The transcription process may take a significant amount of time for your audio file.
- During the initial setup, the project will take one or two minutes to download AI models.

So, relax, grab a coffee, and enjoy the process ☕️💖.

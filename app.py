# app.py
import json
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os
import ffmpeg
from scipy.spatial import distance


def create_app():
    app = Flask(__name__, static_folder='uploads', static_url_path='/uploads')
    app.config['UPLOAD_FOLDER'] = '/app/uploads/'
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    # Other setup code...
    return app


app = create_app()


@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"


from fastapi import FastAPI, HTTPException
from moviepy.editor import VideoFileClip
import urllib.request
from io import BytesIO

app = FastAPI()

@app.post("/video-length/")
async def get_video_length(video_url: str):
    try:
        # Download the video file from the provided URL
        with urllib.request.urlopen(video_url) as response:
            video_bytes = BytesIO(response.read())

        # Use moviepy to load the video and get the duration
        clip = VideoFileClip(video_bytes)
        duration = clip.duration  # Duration in seconds

        return {"video_length": duration}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# If you're running the app locally, use this command:
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload

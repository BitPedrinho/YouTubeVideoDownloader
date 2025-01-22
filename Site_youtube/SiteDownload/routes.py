from flask import Flask, render_template, request, redirect, send_file
from SiteDownload import app
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import tempfile
import requests

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route('/receber_url', methods=['POST'])
def receber_url():
    url = request.form.get('url')
    if not url:
        return "URL não fornecida"
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    temp_dir = tempfile.mkdtemp()
    file_path = ys.download(output_path=temp_dir)#Repare que o output armazena no diretório 
    NomeDownload = os.path.basename(file_path)
    return send_file(file_path, as_attachment=True, download_name=NomeDownload)

@app.route('/receber_url_audio', methods=['POST'])
def receber_url_audio():
    url_audio = request.form.get('url_audio')
    if not url_audio:
        return "URL não fornecida"
    yt = YouTube(url_audio)
    ys = yt.streams.get_audio_only()
    temp_dir = tempfile.mkdtemp()
    file_path = ys.download(output_path=temp_dir)
    NomeDownload = os.path.basename(file_path)
    return send_file(file_path, as_attachment=True, download_name=NomeDownload)
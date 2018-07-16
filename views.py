import io
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import copy

from google.cloud import speech
from google.cloud.speech import enums, types


def input(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def output(request): 
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="C:\\Users\\dis\\Desktop\\STT\\sttDemo.json"
    # Sets Google API credentials
    client = speech.SpeechClient() # Connects to API
    content = None
    audio = None
    config = None
    #print(dir(request))
    try:
        content=request.FILES['audio'].read() # Read files from POST
        print(len(content)) 
        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
            sample_rate_hertz=48000,
            language_code='sl-SI')
        """
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='sl-SI')"""
    except Exception as e:
        content = request.read()
        print(len(content))
        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='sl-SI')
        """
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
            sample_rate_hertz=48000,
            language_code='sl-SI')"""
    
    with open("test.ogg", "wb") as f:
        f.write(content)
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    a = ""
    for result in response.results:
        string = result.alternatives[0].transcript
        print('Transcript: {}'.format(string))
        a+=string + '\n'
    
    return HttpResponse(a)

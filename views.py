import io
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from google.cloud import speech
from google.cloud.speech import enums, types


def input(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def output(request): 
    # Instantiates a client
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="C:\\Users\\dis\\Desktop\\STT\\sttDemo.json"
    client = speech.SpeechClient()
    
    content=request.FILES['audio'].read()
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='sl-SI')

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    a = ""
    for result in response.results:
        string = result.alternatives[0].transcript
        print('Transcript: {}'.format(string))
        a+=string + '\n'
    
    return HttpResponse(a)

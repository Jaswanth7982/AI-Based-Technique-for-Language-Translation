from django.shortcuts import render
from .translation import translate_text
import speech_recognition as sr
from PIL import Image
import pytesseract
from asgiref.sync import async_to_sync
import tempfile

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def chat_page(request):

    translated_text = ""
    speech_text = ""
    image_text = ""

    if request.method == "POST":

        # TEXT TRANSLATION
        text = request.POST.get("text")
        lang = request.POST.get("lang")

        if text and lang:
            try:
                translated_text = async_to_sync(translate_text)(text, lang)
            except Exception as e:
                translated_text = f"Translation error: {e}"

        # VOICE TO TEXT
        if request.FILES.get("audio_file"):
            try:
                audio_file = request.FILES["audio_file"]

                with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
                    for chunk in audio_file.chunks():
                        temp_audio.write(chunk)

                recognizer = sr.Recognizer()

                with sr.AudioFile(temp_audio.name) as source:
                    audio_data = recognizer.record(source)

                speech_text = recognizer.recognize_google(audio_data)

            except Exception as e:
                speech_text = f"Audio error: {e}"

        # IMAGE OCR
        if request.FILES.get("image_file"):
            try:
                image_file = request.FILES["image_file"]
                image = Image.open(image_file)

                image_text = pytesseract.image_to_string(image)

            except Exception as e:
                image_text = f"OCR error: {e}"

    return render(request, "chat_page.html", {
        "translated_text": translated_text,
        "speech_text": speech_text,
        "image_text": image_text
    })
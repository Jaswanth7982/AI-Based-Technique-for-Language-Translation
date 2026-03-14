from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image
import os

# VERY IMPORTANT (Windows Tesseract Path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def index(request):
    return render(request,'index.html')


def adminLoginForm(request):
    return render(request,'adminLoginForm.html')


def userLoginForm(request):
    return render(request,'userLoginForm.html')


def userRegisterForm(request):
    return render(request,'userRegisterForm.html')


# ✅ NEW FUNCTION FOR IMAGE TO TEXT
def image_to_text(request):
    text = ""

    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        file_path = fs.path(filename)

        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

    return render(request, "image_to_text.html", {"text": text})
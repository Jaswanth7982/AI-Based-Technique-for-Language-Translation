# from googletrans import Translator

# translator = Translator()

# def translate_text(text, target_language):
#     try:
#         result = translator.translate(text, dest=target_language)
#         return result.text
#     except Exception as e:
#         return "Translation Failed. Check Internet Connection."


from googletrans import Translator

translator = Translator()

async def translate_text(text, lang):
    translated = await translator.translate(text, dest=lang)
    return translated.text
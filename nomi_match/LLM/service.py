import google.generativeai as genai
from django.conf import settings

def suggest_store(event):
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    エリア:{event.area}
    ジャンル:{event.genre}
    予算:{event.budget_hint}
    """
    return model.generate_content(prompt).text

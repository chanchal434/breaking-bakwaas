# ai_handler.py
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def generate_gemini_news(place, person, news_type, tone):
    if not api_key:
        return f"Offline: {news_type} in {place}", f"API missing! {person} did something {tone}.", ""

    prompt = f"""You are a satirical news writer. Write a short, {tone} {news_type} fake news article involving a person named {person} in {place}. 
Include a catchy headline.

Also create a vivid, humorous, tabloid-style image prompt (max 80 words) for "Photographic Evidence" – something funny and safe like a blurry photo or shocking scene.

Format EXACTLY like this (do not add extra text):

Headline: [Your Headline]
Content: [Your Content]
ImagePrompt: [Image description]"""

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        text = response.text.strip()

        # Robust parsing
        headline = "Breaking Bakwaas!"
        content = text
        image_prompt = ""

        if "Headline:" in text:
            try:
                headline_part = text.split("Headline:")[1].split("Content:")[0].strip()
                headline = headline_part.replace("**", "").strip()
                
                content_part = text.split("Content:")[1].split("ImagePrompt:")[0].strip()
                content = content_part.replace("**", "").strip()
                
                if "ImagePrompt:" in text:
                    image_prompt = text.split("ImagePrompt:")[1].strip()
            except:
                pass  # fallback

        return headline, content, image_prompt

    except Exception as e:
        return "API Error", f"Oops! Error: {str(e)}", ""
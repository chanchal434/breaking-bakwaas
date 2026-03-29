# app.py
from flask import Flask, render_template, request, redirect, url_for, Response
import random
from ai_handler import generate_gemini_news
import db_handler

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    history = db_handler.load_history()
    active_tab = "custom"
    latest_news = None

    if request.method == "POST":
        mode = request.form.get("mode")
        active_tab = mode

        if mode == "auto":
            places = ["Bengaluru Traffic", "Delhi Metro", "Goa", "Mars", "The Moon"]
            people = ["Virat Kohli", "Shah Rukh Khan", "Elon Musk", "A stray street dog", "Batman"]
            types = ["Bollywood Gossip", "Cricket", "Tech Startup", "Politics", "Funny"]
            tones = ["Over-the-top Dramatic", "Sarcastic", "Absurd", "Satirical"]
            
            place = random.choice(places)
            person = random.choice(people)
            news_type = random.choice(types)
            tone = random.choice(tones)
        else:
            place = request.form.get("place", "Unknown")
            person = request.form.get("person", "Unknown")
            news_type = request.form.get("news_type", "Funny")
            tone = request.form.get("tone", "Sarcastic")
            
        headline, content, image_prompt = generate_gemini_news(place, person, news_type, tone)
        
        latest_news = db_handler.add_entry(headline, content, place, person, image_prompt)
        history = db_handler.load_history()

    return render_template("index.html", history=history, active_tab=active_tab, latest_news=latest_news)

@app.route("/news/<item_id>")
def view_news(item_id):
    """Unique shareable page for each article"""
    history = db_handler.load_history()
    item = next((i for i in history if i["id"] == item_id), None)
    if not item:
        return "Article not found!", 404
    return render_template("single_news.html", item=item)

@app.route("/delete/<item_id>")
def delete_item(item_id):
    db_handler.delete_entry(item_id)
    return redirect(url_for("home"))

@app.route("/clear")
def clear_history():
    db_handler.clear_all()
    return redirect(url_for("home"))

# Download routes (unchanged)
@app.route("/download/txt/<item_id>")
def download_txt(item_id):
    history = db_handler.load_history()
    item = next((i for i in history if i["id"] == item_id), None)
    if not item: return "Item not found", 404
    text_content = f"BREAKING BAKWAAS\n{'-'*20}\nTitle: {item['headline']}\nDate: {item['date']}\n\n{item['content']}"
    return Response(text_content, mimetype="text/plain", headers={"Content-disposition": f"attachment; filename=bakwaas_{item['id'][:5]}.txt"})

@app.route("/download/all")
def download_all_txt():
    history = db_handler.load_history()
    text_content = "=== ALL BREAKING BAKWAAS HISTORY ===\n\n"
    for item in history:
        text_content += f"[{item['date']}]\nHEADLINE: {item['headline']}\n{item['content']}\n\n{'-'*40}\n\n"
    return Response(text_content, mimetype="text/plain", headers={"Content-disposition": "attachment; filename=all_bakwaas_history.txt"})

if __name__ == "__main__":
    app.run(debug=True)
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify


load_dotenv()

OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/ask", methods=["POST"])
def ask():
    user_data = request.get_json()

    if not user_data:
        return jsonify({"error": "No JSON found"}), 400
    

    value = user_data.get("message")
    if not value:
        return jsonify({"error": "No message found"}), 400


    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": value}]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except RateLimitError:

    

if __name__ == "__main__":
    app.run(debug=True)
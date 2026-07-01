from flask import Flask,render_template,request,jsonify
from chatbot_data import chatbotData

app=Flask(__name__)

def find_answer(question):

    question=question.lower()

    for item in chatbotData:

        if question in item["question"].lower() or item["question"].lower() in question:
            return item["answer"]

    return "Sorry, I don't know the answer. Please ask about Captiv Techno Solutions."

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat",methods=["POST"])
def chat():

    data=request.get_json()

    question=data["message"]

    answer=find_answer(question)

    return jsonify({"response":answer})


if __name__=="__main__":
    app.run(debug=True)

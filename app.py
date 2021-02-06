from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)

bot = ChatBot("Moss")
# trainer = ChatterBotCorpusTrainer(bot)
trainer = ListTrainer(bot)

trainer.train(['What is your name?', 'My name is Moss'])
trainer.train(['Who are you?', 'I am a bot'])
trainer.train(['Where do I get a free t-shirt?', 'See Krista Sali in HR'])
trainer.train(['who is the king?', 'Jamie Jamiesons'])
# trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
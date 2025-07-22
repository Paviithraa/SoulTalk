from flask import Flask, render_template, request
from utils import get_bot_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_response():
    user_message = request.form['msg']
    bot_reply = get_bot_response(user_message)
    return bot_reply

if __name__ == '__main__':
    app.run(debug=True)
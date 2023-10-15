from flask import Flask, render_template, jsonify, request
import openai
import aiapi


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)

app.register_error_handler(404, page_not_found)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        res = dict()
        res['answer'] = aiapi.generate_response(prompt)
        return jsonify(res), 200

    return render_template('index.html', **locals())
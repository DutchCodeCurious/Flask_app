from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def handle_form_submission():
    if request.method == 'POST':
        user_input = request.form['input_text']
        reversed_text = user_input[::-1]
        return render_template('result.html', reversed_text=reversed_text)


if __name__ == '__main__':
    app.run(port=5000)

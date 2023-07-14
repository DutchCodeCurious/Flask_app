from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def handle_form_submission():
    if request.method == 'POST':
        user_input = request.form['input_text']
        return render_template('result.html', new_name=user_input)


if __name__ == '__main__':
    app.run(port=5000)

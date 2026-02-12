from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Теперь мы просто отдаем страницу, а JS сам всё посчитает
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

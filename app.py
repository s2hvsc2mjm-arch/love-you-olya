from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Дата начала
    start_date = datetime(2024, 4, 4, 22, 10)
    now = datetime.now()
    diff = now - start_date
    
    # Передаем данные
    data = {
        "days": diff.days,
        "hours": int(diff.total_seconds() // 3600),
        "minutes": int(diff.total_seconds() // 60),
        "seconds": int(diff.total_seconds())
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
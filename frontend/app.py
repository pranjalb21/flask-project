from flask import Flask, render_template, request
from datetime import datetime
from zoneinfo import ZoneInfo
import os
from dotenv import load_dotenv
import requests
load_dotenv()

backend_uri = 'http://0.0.0.0:5002'

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now(ZoneInfo('Asia/Kolkata'))
    day = now.strftime('%A')
    time = now.strftime('%I:%M:%S %p')
    return render_template('index.html', day=day, time=time)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(form_data)
    requests.post(f'{backend_uri}/api/submit', json=form_data)
    return 'Data submitted successfully'

if __name__ == '__main__':
    port = int(os.getenv('FRONTEND_PORT', 5001))
    app.run(host = '0.0.0.0', port=port, debug=True)
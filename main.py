from flask import Flask
# 匯入 render_template 以使用樣板
from flask import render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# route 名稱必須以斜線開頭
# 最佳五檔主頁
@app.route('/fibest')
def fibest():
    return render_template('fibest.html')
  
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/x-icon')
  
# 最佳五檔表格數據
@app.route('/fibest/table/<price>')
def fibest_table(price):
    bounds = [1000, 500, 100, 50, 10, 0.01]
    steps = [5.00, 1.00, 0.50, 0.10, 0.05, 0.01]

    step = 0
    price = float(price)
    for i in range(len(bounds)):
        if price >= bounds[i]:
            step = steps[i]
            break
    # print('step:', step)

    fibest = []
    for i in range(5):
        fibest.append(f'{price + (5-i) * step:.2f}')
    for i in range(5):
        fibest.append(f'{price - i * step:.2f}')
    return {'price': price, 'fibest': fibest}

app.run(host='0.0.0.0', port=81)
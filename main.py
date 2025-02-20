from flask import *

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства. </br> Человечеству мала одна планета. </br> Мы сделаем обитаемыми " \
           "безжизненные пока планеты. </br> И начнем с Марса! </br> Присоединяйся!"


@app.route('/image_mars')
def image_mars_page():
    return f"""<!doctype html>
                    <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>                    
                  <img src="{url_for('static', filename='img/download.jpg')}">
                  </br>
                  Вот она такая, красная планета.
                  </body>
                </html>"""


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/webserver-1-7.jpeg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
print('test')
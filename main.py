from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


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


@app.route('/promotion_image')
def promotion_image_page():
    return f"""<!doctype html>
                    <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>                    
                  <img src="{url_for('static', filename='img/download.jpg')}">
                  </br>
                  <div class="alert alert-primary" role="alert" 
                  link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  Человечество вырастает из детства
                  </div>
                  </body>
                </html>"""


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/webserver-1-7.jpeg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.1.0.1')
    app.config.from_envvar('EXPLAIN_TEMPLATE_LOADING')

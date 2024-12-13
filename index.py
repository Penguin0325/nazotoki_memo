from flask import Flask,render_template

app = Flask(__name__)

# 静的ファイルの配置ディレクトリを指定する
app.config['UPLOAD_FOLDER'] = '/usr/local/var/www/hisapp/project/app/controller/static/images'

@app.route("/testindex", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/atogaki')
def atogaki():
    return render_template('atogaki.html')


@app.route('/hints')
def hints():
    return render_template('hints.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/nazo1')
def nazo1():
    return render_template('nazo1.html')

@app.route('/nazo2')
def nazo2():
    return render_template('nazo2.html')

@app.route('/nazo3')
def nazo3():
    return render_template('nazo3.html')

@app.route('/character')
def character():
    return render_template('character.html')

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/story1')
def story1():
    return render_template('story1.html')

@app.route('/anser1')
def anser1():
    return render_template('mystery1anser.html')

@app.route('/anser2')
def anser2():
    return render_template('mystery2anser.html')

@app.route('/anser3')
def anser3():
    return render_template('mystery3anser.html')

@app.route('/middlestory')
def middlestory():
    return render_template('middlestory.html')

@app.route('/afterentering')
def afterentering():
    return render_template('afterentering.html')

@app.route('/inputchatbot1')
def inputchatbot1():
    return render_template('inputchatbot1.html')

@app.route('/story9')
def story9():
    return render_template('story9.html')

@app.route('/endstory1')
def endstory1():
    return render_template('endstory1.html')

if __name__ == "__main__":
    app.run()


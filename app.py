from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''
        <form action="/hello" method="get">
            Enter your name: <input type="text" name="name">
            <input type="submit" value="Say Hello">
        </form>
    '''

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Alifiyah')
    return f'<h1>Hello {name}!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

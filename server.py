from flask import Flask
app = Flask (__name__)



@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def hi(name):
    print (name)
    return "Hi " + name


@app.route('/repeat/35/hello')
def repeat_hello_35():
    print("hello"*35)
    return "hello"*35


@app.route('/repeat/80/bye')
def repeat_bye_80():
    print("bye"*80)
    return "bye"*80


@app.route('/repeat/99/dogs')
def repeat_dogs_99():
    print("dogs"*99)
    return "dogs"*99



if __name__ == "__main__":
    app.run(debug = True)
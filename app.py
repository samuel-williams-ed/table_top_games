from flask import Flask, render_template

from controllers.main_controller import home_blueprint


app = Flask(__name__)

app.register_blueprint(home_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/current_build')
def currentBuild():
    return render_template('currentBuild.html')

if __name__ == '__main__':
    app.run(debug=True)
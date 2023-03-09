from node_modules.flask import Flask, render_template

from controllers.main_controller import main_blueprint

app = Flask(__name__)

app.register_blueprint(shop_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
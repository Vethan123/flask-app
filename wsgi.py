from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/restaurant/<int:restaurant_id>')
# def restaurant_detail(restaurant_id):
#     return render_template('detail.html')

if __name__ == '__main__':
    app.run(debug=True)

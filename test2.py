from flask import Flask, request, render_template
import base64
from flask_cors import cross_origin

app = Flask(__name__)
@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    data=request.args.get('username')
    print(data)
    return 'login'

if __name__ == '__main__':
    app.run(debug=True)
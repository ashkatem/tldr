from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the frontend

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World from Arshiyan's SaaS Backend!"})

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DockerHub -Dami's EC2 on Ubuntu 24.04!, What is going on?"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
from flask import Flask,request,jsonify

app =Flask(__name__)

@app.route('/')
def index():
    return "Hello, World 2!"

@app.route('/sum/<num1>/<num2>', methods=['GET'])
def create_cm(num1, num2):
    try:
        n1 = int(num1)
        n2 = int(num2)
        return jsonify({"result": n1 + n2})

    except Exception as e:
        print ("Missing args")
        return jsonify({"error" : str(e), "message": "args not provided"})

if __name__ =="__main__":
    app.run()
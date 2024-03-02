from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/is_prime/<X>',methods= ['GET'])
def is_prime(X):
    try:
        X = int(X)
        result = True
        for i in range(2,int(X/2)+1):
            if X%i ==0:
                result = False
                break
    except ValueError:
        return jsonify({'message':'Invalid Input'}),400
    return jsonify({'result':result}),200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
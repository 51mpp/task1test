from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/is_prime/<a>',methods= ['GET'])
def is_prime(a):
    try:
        a = int(a)
        result = True
        for i in range(2,int(a/2)+1):
            if a%i ==0:
                result = False
                break
    except ValueError:
        return jsonify({'message':'Invalid Input'}),400
    return jsonify({'result':result}),200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
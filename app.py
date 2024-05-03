from flask import Flask, render_template, request

app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Welcome"

@app.route("/",methods=["GET","POST"])
def calculator():
    if request.method=="GET":
        return render_template("index.html")
    else:
        op = request.form["option"]
        num1 = float(request.form["num_1"])
        num2 = float(request.form["num_2"])
        if op=='add':
            ans = num1+num2
        elif op=='subtract':
            ans = num1-num2
        elif op=='multiply':
            ans = num1*num2
        else:
            ans = num1/num2
        return render_template("results.html",op=op, num_1=num1, num_2=num2, score=ans)


if __name__ == "__main__":
    app.run(debug=True)
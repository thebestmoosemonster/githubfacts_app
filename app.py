from typing import Text
from flask import Flask,render_template,session,request,redirect,url_for
import requests
from requests import api
app= Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/facts/math",methods=["POST","GET"])
def math():
    text=request.form.get("text")
    api = "http://numbersapi.com/random/math"
    response=requests.get(api).text
    return render_template("math.html",data=response)


@app.route("/facts/trivia",methods=["POST","GET"])
def trivia():
    text=request.form.get("text")
    api = "http://numbersapi.com/random/trivia"
    response=requests.get(api).text
    return render_template("trivia.html",data=response)



@app.route("/facts/dates",methods=["POST","GET"])
def dates():
    text=request.form.get("text")
    api = "http://numbersapi.com/random/date"
    response=requests.get(api).text
    return render_template("datesnew.html",data=response)


@app.route("/facts/years",methods=["POST","GET"])
def years():
    text= request.form.get("text")
    api = "http://numbersapi.com/random/year"
    response=requests.get(api).text
    return render_template("years.html",data=response)
    

if __name__ == '__main__': 
    app.run(debug=True)
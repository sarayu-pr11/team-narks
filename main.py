# import "packages" from flask
from flask import Flask, render_template, request, jsonify
import requests

import random
import math
import json

# create a Flask instance
app = Flask(__name__)
nextAnswerString = ""

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/kamryn_abt/', methods=['GET'])
def kamryn_abt():
    global nextAnswerString
    answerString = nextAnswerString

    arrayOfAnswers = ['Yes, you are correct!',
                      'No, you are wrong!',
                      'Maybe...call me baby',
                      'Thought you knew!',
                      'Dunno, ask Kammy',
                      'Ask the other 8-ball']

    randIdx = int(math.floor(random.random()*len(arrayOfAnswers)))
    nextAnswerString = arrayOfAnswers[randIdx]
    return render_template("kamryn_abt.html", currentAnswer=answerString)

@app.route('/riya_abt/')
def riya_abt():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = "{ \"key1\": \"value\",\"key2\": \"value\"}"
    headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
    'x-rapidapi-key': "066e279e11mshd6855dd2ac40d0dp19761ajsn088d1e5fbc92"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    text = response.text
    return render_template("riya_abt.html", results=text)
        #url = "https://covid-19-data.p.rapidapi.com/report/totals"
       # querystring = {"date":"2020-07-21"}
       # headers = {
          #  'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        #    'x-rapidapi-key': "066e279e11mshd6855dd2ac40d0dp19761ajsn088d1e5fbc92"
      #  }
       # response = requests.request("GET", url, headers=headers, params=querystring)
        #stats=[
        #{
       # 'name':'Audrin',
       # 'place': 'kaka',
       # 'mob': '7736'
       # },
     #   {
      #  'name': 'Stuvard',
       # 'place': 'Goa',
       # 'mob' : '546464'
      #  }
      #  ]
        #return(response.text)
       # results = response.text

       # return render_template("riya_abt.html", data=stats)





@app.route('/natalie_abt/')
def natalie_abt():
    #url = "https://numbersapi.p.rapidapi.com/1492/year"
    #querystring = {"fragment":"true","json":"true"}
    #headers = {
    #    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
     #   'x-rapidapi-key': "57a15be86bmsh8ab5c9d255b7689p1346f0jsnb3b6bfbfaba4"
    #}
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #results = json.loads(response.content.decode("utf-8"))['results']
    #year = []
    #for result in results:
    #        # result['year']
    #        year.append(result['year'])
    #    # tournament = json.loads(response.content.decode("utf-8"))['results'][0]['year']

    return render_template("natalie_abt.html")

@app.route('/abby_abt/')
def abby_abt():
    return render_template("abby_abt.html")


@app.route('/sarayu_abt/')
def sarayu_abt():
    return render_template("sarayu_abt.html")

@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

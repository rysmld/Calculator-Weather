from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def menu():
 return render_template('menu.html')

@app.route('/weather')
def index():
 return render_template('index3.html')

@app.route('/calculate', methods=['POST','GET'])
def calculate():

        ans=''
        if request.method == 'POST' and 'num1' in request.form and 'num2' in request.form and 'operators' in request.form:
            x = float(request.form.get('num1'))
            y = float(request.form.get('num2'))
            sign = request.form.get('operators')

            if sign == "addition":
                ans = x + y
            elif sign == "subtraction":
                ans = x - y
            elif sign == "multiplication":
                ans = x * y
            elif sign == "division":
                ans = x / y
            else:
                ans = "Invalid operator"

        return render_template("index.html", ans=ans)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    country = request.form['country']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+','+country+'&appid=fc91345d645834449717b1a32937c765')
    json_object = r.json()

    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15)
    formatted_float = "{:.2f}".format(temp_f)


    z = json_object["weather"]
    weather_description = z[0]["description"]

    x = json_object["name"]

    return render_template('index2.html', temp=formatted_float, desc=weather_description, name=x)


if __name__=="__main__":
    app.run(debug=True)

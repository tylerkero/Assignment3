"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from mbta_helper import find_stop_near
from flask import request
from flask import render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('form.html')

# @app.route('/location',methods = ["POST",'GET'])
# def location():
#     if request.method == "Post":
#         return find_stop_near()
@app.route('/location/', methods = ["POST","GET"])
def location():
    if request.method=="GET":
        return f" The url /location is accessed directly. Try going to / "
    if request.method == "POST":
        form_data = request.form
        print(form_data)
        for value in form_data.values():
            print(value)
            neareststop = find_stop_near(value)
        stop = neareststop[0]
        wheelchair = neareststop[1]
        return render_template('location.html', stop=stop, wheelchair = wheelchair )


# @app.route('/<location>', methods = ["GET","POST"])
# def showlocation(location):
#     return f'Location: {find_stop_near(location)}'

if __name__ == '__main__':
    app.run(debug=True)

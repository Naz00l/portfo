from flask import Flask, render_template, send_from_directory, request, redirect
import os 
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode ="a") as f:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = f.write(f'\n Email: {email} Subject: {subject} Message: {message}')

def write_to_csv(data):
    with open("database.csv", newline = "",  mode ="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        spamwriter = csv.writer(database, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     if request.method == 'POST':
      data = request.form.to_dict()  
      print(data)
      write_to_csv(data)
      return redirect("/thankyou.html")
     else:
        return "something went wrong"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')




    
    
    




from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('submit', methods=['GET','POST'])
def submit():
    full_name =request.form['fullName']
    id_number = request.form ['idNumber']
    personal_number = request.form ['personalNumber']
    with open ('data.csv', 'a' , newline ='' , encoding='utf8')as file:
        writer = csv.writer(file)
        writer.writerow([full_name,id_number, personal_number])
    return 'הנתנונים נשמרו בהצלחה! תודה על שיתוף הפעולה'

if __name__ == '__main__':

    app.run(debug=True)

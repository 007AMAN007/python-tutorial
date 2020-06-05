from flask import Flask, render_template, request
from dbconfig import mydb
app = Flask(__name__)


@app.route("/")
def index():
    # create index.html in templates folder
    return render_template('index.html')
    # print not working in flask, but in console you can see


@app.route("/balance", methods=('GET', 'POST'))
def balance():
    amount = ""
    if request.method == 'POST':
        account = request.form['account']
        mycursor = mydb.cursor()
        sql = "select * from bank where user_id=%s"
        val = (account,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            amount = x[2]
        print(amount)
    return render_template('account.html', amount=amount)


if __name__ == "__main__":  # it run without this
    app.run(debug=True)  # if not this it will run like simple python app

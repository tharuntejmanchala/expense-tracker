from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# MySQL Configuration
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    date = request.form['date']
    amount = request.form['amount']
    category = request.form['category']
    note = request.form['note']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO expenses (date, amount, category, note) VALUES (%s, %s, %s, %s)",
                (date, amount, category, note))
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "success"})

@app.route("/expenses")
def get_expenses():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM expenses WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)

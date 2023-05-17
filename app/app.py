import os
import psycopg2 as db
from dotenv import load_dotenv
from flask import Flask, render_template,request,jsonify


load_dotenv()
app=Flask(__name__)
@app.route("/")
def index():
        return render_template('index.html')

url = os.getenv("DATABASE_URL")
connection = db.connect(url)
#get all data
query= "SELECT * FROM user_data;"
@app.route('/user', methods=['GET'])
def getall():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            users=cursor.fetchall()
            return jsonify(users)
if __name__ == "__main__":
    app.run(debug=True)  
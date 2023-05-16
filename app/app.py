import os
import psycopg2 as db
# from dotenv import load_dotenv
from flask import Flask,request,jsonify


# load_dotenv()
app=Flask(__name__)
@app.route("/")
def index():
    return "This is for 'ServiceNow' technical assignment"
conn = db.connect(host='localhost', dbname='postgres', user='postgres', password='Admin')
connection=conn
# url = os.getenv("DATABASE_URL")
# connection = db.connect(url)
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
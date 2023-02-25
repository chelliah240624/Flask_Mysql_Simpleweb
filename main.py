from flask import Flask, render_template, json, request
import pymysql.cursors

app=Flask(__name__)

def insertrec( name, dept):
    print(name, dept)
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='test',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            ins_sql = "insert into users (name, dept) values ( %s, %s)"
            val = (name, dept)
            cursor.execute(ins_sql, (val))
            connection.commit()
            print("record inserted.")
    finally:
        connection.close()

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        i_name = request.form.get("Name")
        i_dept = request.form.get("dept")

        insertrec(i_name, i_dept)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
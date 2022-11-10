from flask import Flask, render_template, request
import pyodbc


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def exec():
    if request.method == "POST":
        query = request.form["query"]

        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                             'Server=WIN-8KKMMNKJPU7,1433;'
                             'Database=table;'
                             'UID=table_user;'
                             'Pwd=Passw0rd'
                             )

        cursor = con.cursor()

        cursor.execute(query)

        tmp = ''
        for x in cursor:
            tmp = tmp + str(x)

        tmp1 = tmp.replace('datetime.date', '').replace("'", '').split(')(')
        data = tmp1

        return render_template('tabela.html', data=data)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(host="193.126.1.124", port=80)

from flask import Flask
import sqlite3, json

app = Flask(__name__)


@app.route('/getAll')
def getAll():
    con = sqlite3.connect('todos.db')

    cur = con.cursor()
    ans = list()
    for row in cur.execute('SELECT * FROM todos'):
        
        ans.append(row[0])

    temp = {
        "todos": ans
    }
    
    con.close()
    return json.dumps(temp)

if __name__ == '__main__':
    app.run()
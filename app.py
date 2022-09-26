from flask import Flask,render_template,request,jsonify
import asyncio
from bleak import BleakScanner
from datetime import datetime
import pymysql
from flask_mysqldb import MySQL,MySQLdb
import pygame 
from pygame import mixer

app = Flask(__name__)
app.config['MYSQL_HOST'] = '10.35.10.47'
app.config['MYSQL_USER'] = 'thanatd'
app.config['MYSQL_PASSWORD'] = 'google555'
app.config['MYSQL_DB'] = 'mac_address'
mysql = MySQL(app)

MACID= ""
product_code= ""
mac_add= ""
find=0
result= ""

async def Scanner():
    global MACID
    global mac_add
    global find

    devices = await BleakScanner.discover()
    for d in devices:
        MACID=d.address.replace(':','')    
        if MACID==mac_add:
            if mac_add!= " ":
                find=1
                break
        else: find=2   
    compare()

def check():
    asyncio.run(Scanner())

def compare():
    global find
    global result

    pygame.mixer.init()

    if find==1:
        result="OK"
        mixer.music.load("Sound_OK.wav")
        mixer.music.play()
    else: 
        result="NG"
        mixer.music.load("Sound_NG.wav")
        mixer.music.play()
    db()

@app.route('/')
def match():
    global product_code
    global mac_add
    global result

    product=request.args.get('pcode')
    mac=request.args.get('mcad')

    product_code = product
    mac_add = mac
    
    check()
    return render_template("match.html", result=result)

def db():
    global product_code 
    global mac_add 
    global result
    
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    if product_code is not None:
        len_product = len(product_code) #20
        len_mac = len(mac_add) #12
        if len_product==20 and len_mac==12:
            conn = pymysql.connect(host='10.35.10.47',user='thanatd',password='google555',database='mac_address')
            myCursor = conn.cursor()
            myCursor.execute("INSERT INTO compare_result(product_code,mac_address,result,date_time) VALUES(%s,%s,%s,%s);",(product_code,mac_add,result,dt_string))
            conn.commit()
            conn.close()


@app.route('/report')
def report():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM compare_result WHERE DATE(date_time) = CURDATE() ORDER BY pid DESC")
    orders = cur.fetchall() 
    return render_template('report.html', orders=orders)

@app.route("/range",methods=["POST","GET"])
def range(): 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        From = request.form['From']
        to = request.form['to']
        print(From)
        print(to)
        query = "SELECT * from compare_result WHERE date_time BETWEEN '{}' AND '{}' ORDER BY pid DESC".format(From,to)
        cur.execute(query)
        ordersrange = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', ordersrange=ordersrange)})
    
if __name__=="__main__":
    app.run(debug=True)


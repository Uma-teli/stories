from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc
import re
import logging



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QT2Q335\SQLEXPRESS;'
                      'Database=login;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
res=cursor.execute(f"SELECT stories FROM story WHERE title='uma'")
print(res)





app = Flask(__name__)

app.secret_key = 'xyzsdfg'

@app.route('/')
def defaultHome():

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QT2Q335\SQLEXPRESS;'
                      'Database=login;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    res=cursor.execute("SELECT * FROM story")
    res3={}
    j=0
    res4=[]
    
    for i in res:
         res2=i.title
         
         print(res2)
         res4.append(res2)
          
    print(res4)
    return render_template('storeis.html',res1=res4)
         
         
         
         
    

@app.route('/edit',methods=['GET','POST'])
def edit():
    if request.method=='POST':
        title=request.form['title']
        stories=request.form['stories']
    #story=input("story")
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QT2Q335\SQLEXPRESS;'
                      'Database=login;'
                      'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO story(title,stories) VALUES (?,?)",(title,stories))

        conn.commit()
       # cursor.execute("SELECT * FROM story")
        #res=cursor.fetchall()
       # print(res)
        conn.close()
    return render_template('edit.html')


@app.route('/login', methods=['GET','POST'])
def login():
     mesage=''
     if request.method=='POST':
          username=request.form['username']
          password=request.form['password']


          conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QT2Q335\SQLEXPRESS;'
                      'Database=login;'
                      'Trusted_Connection=yes;')
          cursor = conn.cursor()
          cursor.execute(f"SELECT * FROM LOGIN1 WHERE username ='{username}' AND password ='{password}'")
          user = cursor.fetchone()
          if user:
            session['loggedin'] = True
            mesage = 'Logged in successfully !'
            return render_template('edit.html', mesage = mesage)
          else:
            mesage = 'Please enter correct email / password !'
     return render_template('login.html', mesage = mesage)
          
@app.route('/signup', methods =['GET', 'POST'])
def signup():
    mesage = ''
    if request.method == 'POST' and  'password' in request.form and 'username' in request.form :
        password = request.form['password']
        username = request.form['username']
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QT2Q335\SQLEXPRESS;'
                      'Database=login;'
                      'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM LOGIN1 WHERE username ='{username}'")
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', username):
            mesage = 'Invalid email address !'
        elif not password or not username:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute(f"INSERT INTO LOGIN1 (username,password) VALUES ( ?, ?)",(username,password))
            conn.commit()
            conn.close()
            mesage = 'You have successfully registered !'
            #return render_template('login.html')
    elif request.method == 'POST':
         mesage = 'Please fill out the form !'
    return render_template('signup.html', mesage = mesage)

@app.route('/readstories',methods=['POST','GET'])
def readstories():
   # selected_item = request.form['item']
 #   print(selected_item)
    #print(selectedStory")
    print('args:', request.args)
    print('form',request.form)
    form_data = request.form
    #print('form', form_data)
    print(form_data)
    values_list = list(form_data.values())
    print(values_list)
    second_value = values_list[0] 

    print('Second value:', second_value)
    #selected_item = request.form['story']
    #logging.debug("Received story: %s", details)
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QT2Q335\SQLEXPRESS;'
                      'Database=login;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    res=cursor.execute(f"SELECT * FROM story where title='{second_value}'")
       
    #for i in res:
        #print(i)
        #return render_template('readstories.html',stories=i)
    
    res4=[]
    
    for i in res:
         res2=i.stories
         
         print(res2)
         res4.append(res2)
          
    print(res4)
    return render_template('readstories.html',stories=res2)
         
    
    #j=0
    #res4=[]
    
    #res2=i.stories
         
         ### print(res4)
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)


          

    



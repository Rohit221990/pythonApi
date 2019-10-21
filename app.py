from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from models import *
import logging
from pymongo import MongoClient


client = Stitch.initializeDefaultAppClient('buddyshift-opvhi')
db = client.getServiceClient(MongoClient.factory, 'mongodb-atlas').db('buddyshiftDB')

# client = MongoClient('localhost:27017')
# db = client.ContactDB

app = Flask(__name__)
app.config.from_object('settings')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         try:
#             this_user = User.objects.get(email=request.form['username'])
#             if request.form['username'] != this_user.email:
#                 error = 'Invalid username'
#             elif bcrypt.check_password_hash(this_user.password, request.form['password']) == False:
#                 error = 'Invalid password'
#             else:
#                 session['logged_in'] = True
#                 session['this_user'] = {'first_name':this_user.first_name}

#                 flash('You were logged in')
#                 return redirect(url_for('index'))
#         except:
#             flash('User does not exist')
#     return render_template('login.html', error=error)

# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('index'))


@app.route('/register', methods = ['POST'])
def register():
     error = None
     if request.method == 'POST':
            data = json.loads(request.data)

            first_name = data['firstName']
            last_name = data['lastName']
            mobile = data['mobile']
            username = data['userName']
            password = data['password']
            confirm_password = data['confirmPassword']

            if userName and password and confirm_password:
                status = db.collection('buddies').insert_one({
                "firstname" : first_name,
                "lastname" : last_name,
                "mobile" : mobile,
                "username" : userName,
                "password" : password,
                "confirmpassword": confirm_password
                })
            return dumps({'message' : 'SUCCESS'})
          

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run(debug=True)




# const client = Stitch.initializeDefaultAppClient('buddyshift-opvhi');

# const db = client.getServiceClient(RemoteMongoClient.factory, 'mongodb-atlas').db('<DATABASE>');

# client.auth.loginWithCredential(new AnonymousCredential()).then(user => 
#   db.collection('<COLLECTION>').updateOne({owner_id: client.auth.user.id}, {$set:{number:42}}, {upsert:true})
# ).then(() => 
#   db.collection('<COLLECTION>').find({owner_id: client.auth.user.id}, { limit: 100}).asArray()
# ).then(docs => {
#     console.log("Found docs", docs)
#     console.log("[MongoDB Stitch] Connected to Stitch")
# }).catch(err => {
#     console.error(err)
# });
from flask import Flask, render_template,  session, redirect,url_for, Response, flash
from flask_sqlalchemy import SQLAlchemy
from flask import request
from datetime import datetime
from flask_mail import Mail
from werkzeug import secure_filename
import os
import json, math

with open('config.json','r') as c:
    params = json.load(c)['params']



local_server=True
app = Flask(__name__)
app.secret_key='secret-to-everyone'
app.config['UPLOAD_FILE']=params['upload_location']
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USER_SSL = True,
    MAIL_USERNAME=params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)

mail=Mail(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@P_mundra321@localhost/local--blog--database'
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db=SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    phone_number = db.Column(db.String(20))
    message = db.Column(db.String(80),  nullable=False)
    date = db.Column(db.String(20))

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(200),  nullable=False)
    content = db.Column(db.String(120),  nullable=False)
    tagline = db.Column(db.String(120),  nullable=False)
    author = db.Column(db.String(20),  nullable=False)
    date = db.Column(db.String(20),  nullable=True)
    img_file = db.Column(db.String(50),  nullable=True)
    img_file2 = db.Column(db.String(20),  nullable=True)
    img_file3= db.Column(db.String(20),  nullable=True)


@app.route("/")
def home():
    posts= Posts.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['number_of_posts']))

    page=request.args.get('page')
    
    if not str(page).isnumeric():
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['number_of_posts']):(page-1)*int(params['number_of_posts'])+int(params['number_of_posts'])]
    if page==1:
        prev='#'
        next="/?page="+str(page+1)
    if page==last:
        next='#'
        prev="/?page="+str(page-1)
    else:
        prev="/?page="+str(page-1)
        next="/?page="+str(page+1)

    return render_template('index.html',params=params, posts = posts, prev=prev, next=next)

@app.route("/about")
def about():
    return render_template('about.html',params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route("/dashboard", methods=['GET','POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html',params=params, posts=posts)

    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if (username==params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            session.permanent = True  # Use cookie to store session.
            posts = Posts.query.all()
            return render_template('dashboard.html',params=params, posts=posts)
    else:
        # flash('You are now logged out.', 'success')
        return render_template('login.html',params=params)
    
@app.route("/edit/<string:sno>", methods=['GET','POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method=='POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content=request.form.get('content')
            img_file = request.form.get('img_file')
            img_file2 = request.form.get('img_file2')
            img_file3 = request.form.get('img_file3')
            author = request.form.get('author')
            date=datetime.now()
        
            if sno=='0':
                post=Posts(title=box_title, tagline=tline, slug=slug, content=content, img_file=img_file, img_file2=img_file2,img_file3=img_file3,date=date,author=author)
                db.session.add(post)
                db.session.commit()
            
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.tagline=tline
                post.slug=slug
                post.content=content
                post.img_file=img_file
                post.img_file2=img_file2
                post.img_file3=img_file3
                post.author=author
                post.date=date
                db.session.commit()
                return redirect('/dashboard')
        post=Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params, post=post, sno=sno)

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        entry = Contacts(name=name,email=email,phone_number=phone,message=message,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('Greetings from Blog!!' + name, 
            sender = email, 
            recipients = [params['gmail_user']],
            body = message +  "\n" + phone
        )
    return render_template('contact.html',params=params)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method=='POST':
            if 'file' not in request.files:
                return redirect(request.url)
            file=request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                file.save(os.path.join(app.config['UPLOAD_FILE'],secure_filename(file.filename)))
                return "File Uploaded Successfully"
            return "You cannot upload this. Make sure you're using a supported file type."
    
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')
   
@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.errorhandler(404)
def not_found(exc):
    return Response('<h1>This URL is not found. Please check the URL.</h1>'), 404


# @app.route("/post")
# def sample():
#     return render_template('post.html',params=params)

app.run(debug=True)

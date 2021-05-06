from flask import Flask,render_template,request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

myApp=Flask(__name__)

myApp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site1.db'
db=SQLAlchemy(myApp)

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    intro= db.Column(db.Text, nullable=False)
    osnov_text= db.Column(db.Text, nullable=False)
    data_=db.Column(db.DateTime,default=datetime.utcnow())
    def __repr__(self):
        return'Blog %r'%self.id


@myApp.route('/index')
@myApp.route('/')
def index():
    notes = Blog.query.all()
    return render_template('index.html',notes=notes)


@myApp.route('/about')
def about():
    variable="Кендзьор Андрій"
    return render_template('about.html',autor=variable)

    return render_template('about.html')

@myApp.route('/adress')
def addr():
    names=[{'name':'Кендзьор Андрій','e-mail':'123@gmail.com','nemder':'1234567'},
           {'name': 'Name', 'email': 'Email', 'number': 'Number'},
           {'name': 'Ivan', 'email': '12354@gmail.com', 'call number': '0664297574'},
           {'name': 'Стефунін Арсен', 'email': 'stefunin.arsen@pml.if.ua', 'cell number': '+380672925255'},
           {"name": "Антон Юксін", "e-mail": 'qpowertrain@gmail.com', "number": "06668*****"},
           {'name': 'Dennis', 'e-mail': 'bachynskyi.denys@pml.if.ua', 'phone-number': '3001113344'}
           ]

    return render_template('my_adress.html',dname=names)


@myApp.route('/articles',methods=['POST','GET'])
def article():
    if request.method=='POST':
        title=request.form['title']
        intro=request.form['intro']
        osnov_text=request.form['osnov_text']
        blog=Blog(title=title,intro=intro,osnov_text=osnov_text)
        try:
            db.session.add(blog)
            db.session.commit()
            return redirect('/')


        except:
            return 'error'
    else:
        return render_template('articles.html')



@myApp.route('/sign_in',methods=['POST','GET'])
def sign():
    if request.method=='POST':
        nik=request.form['nik']
        pasw=request.form['psw']
        return nik + pasw
    return render_template('sign_in.html')


@myApp.route('/post_def/<int:id>')
def det_post (id):
    lyubiy_object=Blog.query.get(id)
    return render_template('post_def.html',obj=lyubiy_object)

@myApp.route('/post_def/<int:id>/delete')
def delet1(id):
    d_art=Blog.query.get_or_404(id)
    try:
        db.session.delete(d_art)
        db.session.commit()
        return redirect('/')
    except:
        return ('ПОМИЛКА')


if __name__ == '__main__':
    myApp.run(debug=True)
from flask import Flask
from flask import render_template
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'
db = SQLAlchemy(app)

head = r'''<!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <!-- custom styling -->
    <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Alegreya+Sans&display=swap" rel="stylesheet">

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">

    <style>
      body{
        padding-bottom: 5rem;
        font-family: 'Alegreya Sans', serif;
      }
      
      h1{
        padding-top: 2rem;
      }

      .form-group{
        padding-bottom: 0.5rem
      }
    </style>

'''

questions = list(enumerate((
    'большая дом стоять на гора',
    'бесцветные зеленые идеи яростно спят',
    'вася съел полмосквы',
    'петя съел акциональную вариативность',
    'тот александр семенович снова не пришел',
    'в салат стоит положить одно или два куриного яйца',
    'лиза попросила сына принести самой себе чаю',
    'фш фш фшшшш',
    '100101101110010010',
    'пожалуйста, оцените этот опрос от нуля до ста',
    'я не считаю генеративизм легитимным подходом к синтаксису',
    'мяу',
    )))


# database

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Text)
    age = db.Column(db.Integer)
    is_a_linguist = db.Column(db.Text)

class Answers(db.Model):
    __tablename__ = 'answers'
    qu_id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Integer)


# page code

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/survey')
def survey_page():
    return  render_template('survey.html', questions=questions, head=head)

@app.route('/stats')
def data_page():
    return render_template('stats.html')

if __name__ == '__main__':
    app.run(debug=True)

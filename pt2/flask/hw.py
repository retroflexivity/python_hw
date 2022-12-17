from flask import Flask
from flask import render_template
from flask import request
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from math import factorial, log10

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

    <style>
      body{
        margin-bottom: 5rem;
        font-family: 'Alegreya Sans', serif;
      }
      
      h1{
        margin-top: 2rem;
      }

      .form-group{
        margin-bottom: 1rem;
        margin-top: 1rem
      }

      .card{
        margin-bottom: 1.8rem
      }

    </style>

'''

questions = tuple(enumerate((
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

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Text)
    age = db.Column(db.Integer)
    bias = db.Column(db.Text)

class Answer(db.Model):
    __tablename__ = 'answer'
    usr_id = db.Column(db.Integer, primary_key=True)
    qu_id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Integer)


# page code

@app.route('/')
def home_page():
    return render_template('home.html', head=head)

@app.route('/survey')
def survey_page():
    return  render_template('survey.html', questions=questions, head=head)

@app.route('/submitted', methods=['get'])
def submitted_page():
    db.create_all()
    if not db.session.query(Question).first():
        for i, t in questions:
            db.session.add(Question(
                id=i,
                text=t
            ))
    if not request.args:
        return redirect(url_for('survey'))
    
    user = User(
        age=request.args.get('age'),
        gender=request.args.get('gender'),
        bias=request.args.get('bias')
    )
    db.session.add(user)
    db.session.commit()

    for i in range(len(questions)):
        db.session.add(Answer(
            usr_id=user.id,
            qu_id=i,
            answer=request.args.get(f'q{i}')
        ))

    db.session.commit()
    return render_template('submitted.html', head=head)


@app.route('/stats')
def data_page():
    stats = dict()
    stats['человек прошло опрос'] = db.session.query(User.age).count()
    stats['среди них мужчин'] = db.session.query(User.age).filter(User.gender == 'male').count()
    stats['среди них женщин'] = db.session.query(User.age).filter(User.gender == 'female').count()
    
    stats['среди них лингвистов'] = db.session.query(User.age).filter(User.bias == 'high').count()
    stats['среди них окололингвистов'] = db.session.query(User.age).filter(User.bias == 'low').count()
    stats['среди них нормальных людей'] = db.session.query(User.age).filter(User.bias == 'none').count()

    stats['среди них несовершеннолетних'] = db.session.query(User.age).filter(User.age < 18).count()
    stats['среди них пенсионеров'] = db.session.query(User.age).filter(User.age <= 60).count()
    stats['средний возраст'] = db.session.query(func.avg(User.age)).one()[0]
    stats['самому молодому участнику'] = db.session.query(func.min(User.age)).one()[0]
    stats['самому старому участнику'] = db.session.query(func.max(User.age)).one()[0]


    q_stats = dict()
    for q in questions:
        q_stats[q[1]] = db.session.query(func.avg(Answer.answer)).filter(Answer.qu_id == q[0]).one()[0]

    stats['какой-то странный коэффициент'] = (q_stats[questions[5][1]] + q_stats[questions[6][1]]) / (q_stats[questions[10][1]] * log10(factorial(round(q_stats[questions[11][1]])) / q_stats[questions[8][1]]) ** (-q_stats[questions[4][1]] * q_stats[questions[3][1]] ** -1) + q_stats[questions[1][1]] - q_stats[questions[0][1]])

    return render_template('stats.html', head=head, stats=stats, q_stats=q_stats)


@app.route('/clear')
def clear():
    db.drop_all()
    return 'cleared'

if __name__ == '__main__':
    app.run(debug=True)

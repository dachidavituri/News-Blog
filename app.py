from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'

db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(500))
    category = db.Column(db.String(20))
    author = db.Column(db.String(20))
    date = db.Column(db.String(20))


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'author': self.author,
            'date': self.date
        }

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about_html():
    students = ['Dachi Davituri', 'Eka Kesanashvili', 'Gega Gremelashvili', 'Avtandil Gegetchkori', 'Giorgi Gengashvili']
    return render_template('about.html', students = students)

@app.route('/api/articles')
def get_articles():
    category = request.args.get('category')
    date = request.args.get('date')
    if category and date:
        articles = [article.to_dict() for article in Article.query.filter(Article.category == category).filter(Article.date == date)]
    elif category:
        articles = [article.to_dict() for article in Article.query.filter(Article.category == category)]
    elif date:
        articles = [article.to_dict() for article in Article.query.filter(Article.date == date)]
    else:
        articles = [article.to_dict() for article in Article.query.all()]
    return jsonify(articles)



@app.route('/api/articles', methods=['POST'])
def create_article():
    data = request.get_json()
    title = data['title']
    description = data['description']
    category = data['category']
    author = data['author']
    date = data['date']
    article = Article(title=title, description=description, category=category, author=author, date=date)
    db.session.add(article)
    db.session.commit()
    return 'Article created successfully', 201

with app.app_context():
    db.create_all()
    app.run()
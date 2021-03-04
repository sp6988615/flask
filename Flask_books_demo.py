from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# 导入sql数据
import pymysql
pymysql.install_as_MySQLdb()


# 解决变量问题
# import sys
# reload(sys)
# sys.setdefaultencoding



app = Flask(__name__)
'''
1、创建flask项目。
2、配置数据库。
3、添加数据。
4、使用模板显示数据库查询的数据。
5、使用WTF显示表单。
6、实现相关的增删改查逻辑。
'''

# 数据库配置：  数据库地址。关闭自动跟踪修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Flask

app.secret_key = 'xes'

# 创建数据库对象
db = SQLAlchemy(app)

# 定义书籍和作者模型。
class Author(db.Model):
    # 定义表名
    __tablename__ = 'authors'
    # primary_key 表示是否主键。
    # unique 表示是否允许重复
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # 关系引用
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author: %s' % self.name

class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # db.ForeignKey代表是外键
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return '<Book: %s %s >' % (self.name, self.author_id)


    # 定义字段


# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField('作者：', validators=[DataRequired()])
    book = StringField('书籍：', validators=[DataRequired()])
    submit = SubmitField('提交')


# 删除书籍
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # 查询数据库，是否有该ID
    book_get = Book.query.get(book_id)

    if book_get:
        try:
            db.session.delete(book_get)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍失败')
            db.session.rollback()
    else:
        flash('找不到书籍')

    # return redirect('/')
    return redirect(url_for('index'))

# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # 查询数据库，是否存在该ID
    author_get = Author.query.get(author_id)

    # 先删除书籍，再删除作者

    if author_get:
        try:
            # 查询书籍并删除
            Book.query.filter_by(author_id=author_get.id).delete()

            db.session.delete(author_get)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者失败')
            db.session.rollback()

    else:
        flash('找不到作者')

    return redirect(url_for('index'))




@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建自定义的表单类
    author_form = AuthorForm()


    '''
    1、调取wtf函数实现验证
    2、验证通过获取数据
    3、判断作者是否存在
    4、如果作者存在，判断书籍是否存在，如果书籍存在给提示，不存在，添加数据
    5、如果作者不存在，添加作者和书籍
    6、验证不通过给提示
    '''

    # 1、调取wtf函数实现验证
    if author_form.validate_on_submit():
        # 2、验证通过获取数据
        author_name = author_form.author.data
        book_name = author_form.book.data

        author = Author.query.filter_by(name=author_name).first()
        book = Book.query.filter_by(name=book_name).first()

        # 3、判断作者是否存在
        if author:
            # 4、如果作者存在，判断书籍是否存在，如果书籍存在给提示，不存在，添加数据
            if book:
                flash('书籍已存在')
                pass
            else:
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('书籍添加异常')
                #     s数据库回滚
                    db.session.rollback()

                pass
            pass
        else:
            # 5、如果作者不存在，添加作者和书籍
            try:

                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                # 添加书籍
                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash('作者书籍添加错误')
                db.session.rollback()

    else:
        if request.method == 'POST':
            # 6、验证不通过给提示
            flash('参数不全')

        # flash('参数不全')





    authors = Author.query.all()

    return render_template('books.html', authors=authors, form=author_form)

if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 添加数据
    au1 = Author(name='王总')
    au2 = Author(name='张总')
    db.session.add_all([au1, au2])
    db.session.commit()

    bk1 = Book(name='python入门', author_id=au1.id)
    bk2 = Book(name='go入门', author_id=au1.id)
    bk3 = Book(name='美妆入门', author_id=au2.id)
    bk4 = Book(name='穿搭入门', author_id=au2.id)
    db.session.add_all([bk1, bk2, bk3, bk4])
    db.session.commit()






    app.run(debug=True)
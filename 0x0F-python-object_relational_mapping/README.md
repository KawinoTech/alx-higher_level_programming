CREATE USER jeremy@localhost IDENTIFIED WITH caching_sha2_password BY password
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, INDEX, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES; free cached memory
sudo mysqladmin -p -u sammy version - run admincommands
INSERT INTO table (column_name, .. (optional)) VALUES (values, values,), (values, values);
CREATE TABLE table ( column DATATYPE PRIMARY KEY AUTO_INCREMENT DEFAULT 'value e.g DATETIME DEFAUT NOW()', column DATATYPE NOT NULL CONSTRAINT check_something CHECK(column condition i.e >= or <, >);
ALTER TABLE table ADD CONSTRAINT check_something CHECK(column condition i.e >= or <, >) ADD CONSTRAINT PRIMARY KEY(column);
ALTER TABLE table DROP CHECK check_something
ALTER TABLE table ALTER COLUMN column SET DEFAULT 'value'
CREATE TABLE table (customer_id DATATYPE, FOREIGN KEY() REFERENCES customers(customer_id) ON DELETE SET NULL/ON DELETE CASCADE); creates foreign key in column cudtomer_id of transaction table
ALTER TABLE table ADD CONSTRAINT constraint_name FOREIGN KEY() REFERENCES customers(customer_id)
ALTER TABLE posts ADD CONSTRAINT fk_userid FOREIGN KEY (userid) REFERENCES people(user_id);
ALTER TABLE posts ADD COLUMN userid VARCHAR(40) AFTER another_column;
ALTER TABLE posts MODIFY COLUMN description VARCHAR(100);
select * from posts inner join people on people.user_id = posts.userid; * can be changed to individual columns

select a.first_name, a.last_name,
concat(b.first_name, b.last_name) as "referred_by"
from people as a
inner join people as b
on a.referral_id = b.user_id; inner can be changed to left and this will display every user even those who havent met the condition

Stored procedures
DELIMETER $$
create procedure do_something(IN parameter INT)
BEGIN
Any query;
END$$
DELIMITER ;
CALL do_something(parameters)

SELECT COUNT/AVG/SUM(column) AS "alias name" FROM table WHERE .. AND/OR/NOT column = -> others BETWEEN, IN
UPDATE table SET column = "value" WHERE column =
SELECT * FROM table WHERE column LIKE "%s - starts with s i.e any varying number of characters in the beginning, _oo - any single random character in the beginning"
SELECT * FROM table ORDER BY column ASC/DESC LIMIT - you can order by more than one column. LIMIT is used to paginate i.e LIMIT 10
SELECT * FROM table UNION SELECT * FROM table - They have to return the same number of columns, UNION ALL includes duplicates
CREATE VIEW view_name AS SELECT ... - virtual table, up to date
CREATE INDEX userid_idx ON people(user_id); You can put multiple columns, but note this will create a sequence
While using indexex update takes more time, select takes less time

This is a subquery
select concat(first_name, ' ', last_name)
from people
where user_id
in (select userid from posts where userid != "NULL")

GROUP BY aggregate all rows by a specific column
SELECT COUNT(amount), column FROM table GROUP BY column(aggregates based on this column) HAVING(used instead of WHERE) COUNT(amount) > 1 WITH ROLLUP(produces another  row and shows the GRAND TOTAL)


Importing Stored Procedures, triggers and functions
mysqldump -u your_username -p --no-create-info --no-data --no-create-db --routines your_database > procedures.sql
-u your_username: Specifies the MySQL username.
-p: Prompts for the MySQL password.
--no-create-info: Excludes table creation statements.
--no-data: Excludes data (only dumps stored procedures, functions, triggers, and events).
--no-create-db: Excludes the database creation statement.
--routines: Includes stored procedures and functions.
your_database: The name of your source database.
> procedures.sql: Saves the output to a file named procedures.sql.
mysql -u your_username -p your_target_database < procedures.sql

    for i in range(10):
        name = get_name()
        new_user = User(username=name, password_hash="vybzkartel", email=f"{name}@gmail.com",
                        department="SME Banking")
        new_idea = Idea(title="Python Programming", brief_description="Learn Python",
                        further_description="How to code in python", author=new_user)
        db.session.add(new_user)
        db.session.add(new_idea)
        db.session.commit()


SSH Tunneling
pip install ssh tunnel

tunnel = sshtunnel.SSHTunnelForwarder((hostname), ssh_username='username', 'ssh_password'='password', remote_bind_address=('ip_address', port(int)))
tunnel.start()


Reflecting database models into python objects.
from sqlalchemy.ext.automap import automap_base
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    Idea = Base.classes.idea
    new_idea = Idea(title="Java Programming", brief_description="Learn Java",
                    further_description="How to code in java", owner_id=1)

Using sql functions

db.session.query(db.func.avg(User.id)).scalar()


UPLOADING FILES
from flask import request, senf_file
from io import BytesIO
<form action="/the @app.route url" method="post" enctype="multipart/form-data">
<input class="form-control" type="file" id="fileInput" name="file" required>


class File(db.Model):
    id = db.Column(db.String(100), primary_key=True, default=uuid4())
    file_name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary) #store data in binary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        upload = File(file_name=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')

@app.route('/download/<file_id>', methods=['GET', 'POST'])
def download(file_id):
    upload = File.query.filter_by(id=file_id).first()
    return send_file(BytesIO(upload.data), as_attachment=True, download_name=upload.file_name)


FLASK EXTENSIONS

Extension	Description
Flask-SQLAlchemy	Adds support for SQLAlchemy, a popular ORM for databases.
Flask-Migrate	Handles database migrations using Alembic.
Flask-WTF	Simplifies form handling and validation using WTForms.
Flask-Login	Manages user authentication and session management.
Flask-Mail	Enables email sending from your Flask application.
Flask-Caching	Adds caching support to improve performance.
Flask-Bcrypt	Provides utilities for hashing passwords securely.
Flask-Restful	Helps in building REST APIs quickly and efficiently.
Flask-CORS	Enables Cross-Origin Resource Sharing (CORS).
Flask-SocketIO	Adds WebSocket support for real-time communication.


SQLALCHEMY STYLE
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from uuid import uuid4
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column('user_id', String(40), primary_key=True, default=str(uuid4()))
    first_name = Column("first_name", String(30))
    last_name = Column("last_name", String(30))
    age = Column('age', Integer)
    gender = Column("gender", String(5))
    next_of_kin = Column("next_of_kin", String(20))

    def __init__(self, first_name, last_name, age, gender, next_of_kin):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.next_of_kin = next_of_kin

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}\nGender: {self.gender}\nAge: {self.age}"

if __name__ == '__main__':
    engine = create_engine("mysql://jeremy:vybzkartel@localhost/test", echo=True)
    Base.metadata.create_all(bind=engine)

    Sess = sessionmaker(bind=engine)
    session = Sess()
    p1 = Person("Jeremy", "Okoth", 26, "Male", "Innocent")
    data = session.query(Person).filter_by(first_name="Jeremy").first()
    print(id(p1))
    print(id(data))
    print(p1.first_name)

FLASK_SQLALCHEMY STYLE
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, send_file
from io import BytesIO #Decode binary data to original file
from uuid import uuid4

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jeremy:vybzkartel@localhost/test"
app.config['SQLALCHEMY_BINDS'] = {'test1': "mysql://jeremy:vybzkartel@localhost/test1"}#Binding multiple datatbases
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Idea(db.Model):

    __searchable__ = ['title', 'brief_description', 'further_description'] #List of columns that will be full
    # text search enabled
    __bind_key__ = 'test1'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    brief_description = db.Column(db.String(100), nullable=False)
    further_description = db.Column(db.Text, nullable=False)
    is_implemented = db.Column(db.String(3), default='No')
    assigned_bonus = db.Column(db.String(3), default='No')
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Title: {self.title}\nDescription: {self.brief_description}"
class User(db.Model):
    """
    Class User used to create user objects.

    """
    #__table__args = {'schema': 'test'}  Assists in  Environment Segregation
    # (Dev, Test, Prod), Security and Access Control, Data Organization and Separation,
    __bind_key__ = 'test1' #Good for back up
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    password_hash = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    idea = db.relationship('Idea', backref='author', lazy=True)#the constraint uselist=False creates a one to one relationship,
    # you cane put a corresponding uniquie=True in the child to prevent duplicates
    score = db.Column(db.Integer, default=0)
    department = db.Column(db.String(100))
"""
    data = User.query.paginate(per_page=5, page=2) User.query.get_or_404
    for i in data:
        print(i.username)Paginate
    data = User.query.filter_by(password_hash='vybzkartel').update(
        { User.password_hash : 'Tgwotitwom@1998' })/.delete() - Bulk update and delete
        """
class File(db.Model):
    id = db.Column(db.String(100), primary_key=True, default=uuid4())
    file_name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary) #store data in binary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        upload = File(file_name=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html')

@app.route('/download/<file_id>', methods=['GET', 'POST'])
def download(file_id):
    upload = File.query.filter_by(id=file_id).first()
    return send_file(BytesIO(upload.data), as_attachment=True, download_name=upload.file_name)

   


PAGINATE
    data = User.query.paginate(per_page=5, page=2) User.query.get_or_404
    for i in data:
        print(i.username)Paginate
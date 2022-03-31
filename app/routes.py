from app import app, forms
from flask import redirect, render_template, url_for, flash
from flask_login import login_user
from app.forms import PhoneBook, Loginform, SignUpForm
from app.models import User, Post


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html')

@app.route('/pb', methods=["GET","POST"])
def phonebook():
    title = 'PhoneBook'
    form = PhoneBook()
    if form.validate_on_submit():
        # Get data from the validated form
        name = form.name.data
        # username = form.username.data
        phonenumber = form.phonenumber.data
        address = form.address.data

        users_with_that_info = User.query.filter((User.address==address)).all()
        if users_with_that_info:
            flash(f"There is already a user with this address", "danger")
            return render_template('pb.html', title=title, form=form)

        new_user = User(name=name, phonenumber=phonenumber, address=address)

        flash(f"{new_user.name} has added what was needed", "success")
        return redirect(url_for('index'))
    return render_template('pb.html', title=title, form=form)



@app.route('/favorites', methods=["GET", "POST"])
def favorites():
    title = 'Favorites'
    movies = [
        {
            'id': 1,
            'title': 'Heretitary',
            'body': "A grieving family is haunted by tragic and disturbing occurrences.",
            'year': '2018',
            'url' : 'https://www.imdb.com/title/tt7784604/'
        },
        {
            'id': 2,
            'title': 'It',
            'body': "In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.",
            'year': '2017',
            'url' : 'https://www.imdb.com/title/tt1396484/?ref_=fn_al_tt_1'
        },
        {
            'id': 3,
            'title': 'The invisible Man',
            'body': "When Cecilia's abusive ex takes his own life and leaves her his fortune, she suspects his death was a hoax. As a series of coincidences turn lethal, Cecilia works to prove that she is being hunted by someone nobody can see.",
            'year': '2020',
            'url' : 'https://www.imdb.com/title/tt1051906/?ref_=nv_sr_srsg_0'
        },
        {
            'id': 4,
            'title': 'Malignant',
            'body': "Madison is paralyzed by shocking visions of grisly murders, and her torment worsens as she discovers that these waking dreams are in fact terrifying realities.",
            'year': '2017',
            'url' : 'https://www.imdb.com/title/tt3811906/?ref_=fn_al_tt_1'
        },
        {
            'id': 5,
            'title': 'Get Out',
            'body': "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.",
            'year': '2017',
            'url' : 'https://www.imdb.com/title/tt5052448/?ref_=fn_al_tt_1'
        }
    ]
    extra = [
        {
            'id': 1,
            'title': 'His House',
            'year': '2018',
            'url' : 'https://www.imdb.com/title/tt8508734/?ref_=fn_al_tt_1'
        },
        {
            'id': 2,
            'title': 'Fear Street Part One, Two and Three',
            'year': '2017',
            'url' : 'https://www.imdb.com/title/tt6566576/?ref_=fn_al_tt_1'
        },
        {
            'id': 3,
            'title': 'Doctor Sleep',
            'year': '2020',
            'url' : 'https://www.imdb.com/title/tt5606664/?ref_=fn_al_tt_1'
        },
        {
            'id': 4,
            'title': 'Overlord',
            'year': '2017',
            'url' : 'https://www.imdb.com/title/tt4530422/?ref_=nv_sr_srsg_0'
        },
        {
            'id': 5,
            'title': 'A Quiet Place',
            'year': '2017',
            'url' : 'https://www.imdb.com/title/tt6644200/?ref_=nv_sr_srsg_0'
        }
    ]

    return render_template('favorites.html', title=title, movies=movies, extra=extra) 
    





@app.route('/signup', methods=["GET", "POST"])
def signup():
    title = 'Sign Up'
    form = SignUpForm()
    # check if a post request and that the form is valid
    if form.validate_on_submit():
        # Get data from the validated form
        # email = form.email.data
        username = form.username.data
        password = form.password.data
        # Create a new user instance with form data
        new_user = User(username=username, password=password)
        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)








@app.route('/login', methods=["GET","POST"])
def login():
    title = 'Log In'
    form = Loginform()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            flash(f'{user} has successfully logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username and/or password is incorrect')
        
    return render_template('login.html', title=title, form=form)    
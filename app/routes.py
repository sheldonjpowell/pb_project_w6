from app import app, forms
from flask import redirect, render_template, url_for
from app.forms import PhoneBook

@app.route('/base')
def index():
    title = 'Home'
    return render_template('index.html')

@app.route('/pb')
def phonebook():
    title = 'PhoneBook'
    form = PhoneBook()
    if form.validate_on_submit():
        # Get data from the validated form
        name = form.name.data
        phonenumber = form.phonenumber.data
        address = form.address.data
    return render_template('pb.html', title=title, form=form)

@app.route('/favorites')
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
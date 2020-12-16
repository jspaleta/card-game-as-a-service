from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, Cards, Judge
from wtforms import widgets
import random
from app.cards import new_cards, new_judge

##
# TODO: init statsd
##
from datadog import statsd, initialize


options = {
        'statsd_host': '127.0.0.1',
        'statsd_port':8125
        }
initialize(**options)


submit_count=0

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html', title='Home')


# Login page - not fully implemented
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
# Pick a persona 
@app.route('/judge', methods=['GET', 'POST'])
def judge():
    form = Judge()
    if form.validate_on_submit():
        judge=new_judge()
    else:
        judge=["",""]
    return render_template('judge.html', title='Judge', form=form,judge=judge)
        

# Draw some cards!  
##
# TODO: add statsd timer
##
@app.route('/cards', methods=['GET', 'POST'])
@statsd.timed("flask_cards")
def cards():
    global submit_count
    form = Cards()
    cards={}
    print("submit count:",submit_count)
    if form.validate_on_submit():
        submit_count+=1
        statsd.gauge("flask_cards.submit",submit_count)

        #
        # TODO: add statsd guage
        ##
        words=new_cards()
        if len(words) > 0:
        #    # Shuffle the words
        #    random.shuffle(words)
            j=0
            for i in range(7):
                c="card"+str(i)
                d="discard"+str(i)
                old_word=form[c].data
                discard=form[d].data
                form[d].checked=False
                if len(old_word) == 0 or discard is True:
                    # select new card if needed
                    cards[i]=words[j]
                    j+=1
                else:
                    # use old card otherwise
                    cards[i]=old_word
    else:
        # prepare blank page on first load
        for i in range(7): cards[i]=""
    return render_template('cards.html', title='Cards', form=form,cards=cards)


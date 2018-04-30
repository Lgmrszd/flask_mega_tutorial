from app import app, __version__
from flask import render_template, flash, redirect, g
from app.forms import LoginForm, CoderForm, MelodyEscapeHelperForm
from app.functions import do_pipeline
from werkzeug.utils import secure_filename
import os


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           version=__version__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("---------")
    print(form.openid.data)
    print(form.validate_on_submit())
    print("---------")
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/coder', methods=['GET', 'POST'])
def coder():
    form = CoderForm()
    if form.validate_on_submit():
        print("CODER", form.text_data.data, form.coders.data)
        form.text_data.data = do_pipeline(form.text_data.data, form.coders.data)
    return render_template('coder.html',
                           title='Coder',
                           form=form,
                           coders=app.config['CODERS'])


@app.route('/MelodyEscapeHelper', methods=['GET', 'POST'])
def upload():
    form = MelodyEscapeHelperForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.config["IMAGES_DIR"], filename
        ))
        return redirect('/index')

    return render_template('ME_helper.html',
                           form=form)

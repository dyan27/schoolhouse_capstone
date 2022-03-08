from app import app
import codecs
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required

# 3rd party
import pandas as pd
import plotly.express as px

@app.route('/')
@app.route('/index')
@login_required # remove to remove user login requirement
def index():
    f = codecs.open("project-evelyn.html", 'r')
    return f.read()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.checkpassword(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# add project route
@app.route("/project")
def project():
    # there are many different ways to pass data into a template
    # any level of nesting is acceptable, but wouldn't recommend more than one deep
    # displaying it this way should make it understanble as to how
    # you could load this "record" from the database
    kwargs = {
        "title": "US Adult Income Data Analysis By Evelyn",
        "overview": "This data was extracted from the U.S Census bureau database by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics). The goal of this project is to show some feature table and distribution graphs in the dataset.",
        "distribution": {
            "text": "Figure 1 shows the histogram distribution of education in the dataset, the observation appears the most density peak appears at the 9, which is high school graduation. The second peak appears at 10. The last rise seems at 13, which means after high school graduation, most working people decided to go to college and have some years of college education or a bachelor's degree.",
            "image": "/static/img/distribution.png",
            "caption": "Figure 1. Education Distribution"
        },
        "advanced": [
            {
                "text": "Figure 2 shows different age group income level, the observation appears people aged between 41 and 50 have the most count for income, more than 50k. It also seems to have the most percentage compared with less than 50k, which means most higher-income people have reached their peak for their career around mid 40 years old, and the chances people will get their higher-income age is around middle 40 years old. People usually start their career around the late 20s and early 30s, and some people might get a higher pay job so that they will have more than 50k at an earlier age, but the percentage for those in that age group was low. Later on, we will analyze what occupation will lead to higher income at an earlier age.",
                "image": "static/img/age.png",
                "caption": "Figure 2. Income vs Different Age Level Groups"
            },
            {
                "text": "Figure 3 shows the boxenplot for hours per week on different income levels. People also thought there is a direct connection between working hours and income, and the more hours one works, the more revenue one should earn. However, this hypothesis only works for hourly employees. The boxplot above shows people making more than 50k work mean hours per week greater than those earning less than 50k. At the same time, there is an extensive range of working hours for people making more than 50k, so there isn&#x27;t solid evidence to prove there is a direct connection between working hours and income for higher-income people.",
                "image": "static/img/hours.png",
                "caption": "Figure 3. Boxenplot On Work Hours For Different Income Levels"
            },
            {
                "text": "Figure 4 shows the mean age for different groups of education with different gender.",
                "image": "static/img/gender.png",
                "caption": "Figure 4. Mean Age For Education Gender Group"
            }
        ]
    }

    # load the table
    df = pd.read_csv("app/static/data/adult.csv")

    # change column names
    df.columns = [text.replace('.', ' ').title() for text in df.columns]

    # generate animated graph
    df_age_hours_income = df.groupby(['Age','Income']).apply(lambda x:x['Hours Per Week'].count()).reset_index(name='Hours')
    fig = px.line(df_age_hours_income,x='Age',y='Hours',color='Income',title='Age By Hours Of Work For Income Level')
    plotly_graph = fig.to_html()

    # pass the table and graph into kwargs to give to template
    kwargs["table"] = df.to_html()
    kwargs["plotly_graph"] = plotly_graph

    return render_template("project/template.html", **kwargs)
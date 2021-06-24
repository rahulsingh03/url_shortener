import requests
from decouple import config
api_key = config('api_key')

from flask import Flask,render_template
from form import MyForm
app = Flask(__name__)
app.config['SECRET_KEY'] = config("SECRET_KEY")

@app.route('/',methods=['GET','POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        url = form.url.data
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

        try:
            data = requests.get(api_url).json()["url"]
        except:
            pass

        if data["status"] == 7:
            shortened_url = data["shortLink"]
            return render_template('index.html',form=form,shortened_url=shortened_url)
        else:
            return render_template('index.html',form=form,error='Sorry, Try Again With Appropriate Address!')
    return render_template('index.html',form=form)


if  __name__  == '__main__':
    app.run(debug=True)
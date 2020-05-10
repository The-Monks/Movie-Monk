from flask import Flask, render_template, redirect, request
import recommender as rc

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        Title = request.form['Title']
        print(Title)
        task, Title, allData = rc.supreme(Title)
        print(allData)
    return render_template('recommend.html', task=task, Title=Title, allData=allData)


@app.route('/')
def redirection():
    return redirect('/home')


@app.route('/home')
def homePage():
    return render_template('home.html')


if __name__ == '__main__':
    # app.debug = True
    app.run()

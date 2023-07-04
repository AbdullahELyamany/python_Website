
from flask import Flask, render_template, url_for




app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html",
                            pagetitle="Home",
                            style="home"
                          )


@app.route('/path/')
def path():

    return render_template("path.html",
                            pagetitle="Path",
                            style="path"
                          )

@app.route('/information/')
def information():

    return render_template("information.html",
                            pagetitle="Infomation",
                            style="information"
                          )

@app.route('/libraries/')
def libraries():

    return render_template("libraries.html",
                            pagetitle="Libraries",
                            style="libraries"
                          )


@app.route('/projects/')
def projects():

    return render_template("projects.html",
                            pagetitle="Projects",
                            style="projects"
                          )



if __name__ == "__main__" :

    app.run(port=2004, debug=True)


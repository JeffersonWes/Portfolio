from flask import Flask, render_template,abort


app = Flask(__name__)

projects=[
    {
        "name" : "Microblog app with Python and MongoDB",
        "thumb" : "img/microblog.png",
        "hero" : "img/microblog-hero.png",
        "categories": ["python", "web"],
        "slug": "microblog",
        "prod":"https://python-microblog-ipd8.onrender.com",
    },
    {
        "name" : "Habit tracking app with Python and MongoDB",
        "thumb" : "img/habit-tracking.png",
        "hero" : "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod":"https://habit-tracker-enwj.onrender.com",
    },
    {
        "name" : "DSpace Digital Repository with Java and PostgreSQL",
        "thumb" : "img/dspace-library.png",
        "hero" : "img/dspace-library-hero.png",
        "categories": ["postgresql","java"],
        "slug": "dspace",
        "prod":"https://udemy.com",
    }
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html",projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html", project=slug_to_project[slug]
        )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


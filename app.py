from bocadillo import App, Templates
from models import db, Post

app = App()
templates = Templates(app)


@app.route("/")
async def index(req, resp):
    posts = Post.select()
    resp.html = await templates.render("index.html", {"posts": posts})


@app.route("/posts/{slug}")
async def post(req, resp, slug):
    post = Post.select().where(Post.slug == slug).get()
    resp.html = await templates.render("post.html", {"post": post})


if __name__ == '__main__':
    db.connect()
    db.create_tables([Post])
    app.run()

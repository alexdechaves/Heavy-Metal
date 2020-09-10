from heavy_metal import *
from app import app


c_app = app()
c_app.app_context().push()
db.create_all()
show = TVShowDB(show='The Act')
db.session.add(show)
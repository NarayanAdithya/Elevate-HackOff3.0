from app import app,db
from app.models import User,Patient


# Flask Shell Command Gives Access to DataBase Manipulation Facilated Through Flask SQLAlchemy
@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User':User,'Patient':Patient}


if __name__ == '__main__':
    app.run()

from ext import app, db
from models import Guitars, Bass, Keyboard, Microphone, Accessory, User


def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
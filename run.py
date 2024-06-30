from ext import app
from routes import (home, show_guitars, guitar_detail, show_basses, bass_detail,
    show_accessories, accessory_detail, show_keyboards, keyboard_detail, show_microphones,
    microphone_detail,login, register, add_item, logout, load_user)

app.run(host="0.0.0.0")

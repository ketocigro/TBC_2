from ext import app




if __name__ == "__main__":
    from routes import (home, show_guitars, guitar_detail, show_basses, bass_detail,
    show_accessories, accessory_detail, show_keyboards, keyboard_detail, show_microphones,
    microphone_detail,login, register, add_item, logout, load_user)

    app.run(debug=True)

from modules.UI import UI 
from modules.config import config

if __name__ == "__main__":
    conf=config()
    ui=UI(conf=conf)
    ui.create_window()
    ui.run()
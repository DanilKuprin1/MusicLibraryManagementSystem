from app.user_interface import UserInterface
from app.library import Library

if __name__ == "__main__":
    lib = Library()
    ui = UserInterface(lib)
    ui.run_interface()


import os
import sys

def resource_path(relative_path):
    """ Получает абсолютный путь к ресурсам для работы в EXE и исходниках """
    if getattr(sys, 'frozen', False):  # Если программа 'заморожена' (упакована в EXE)
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


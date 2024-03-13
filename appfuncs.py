# -- APP FUNCTIONS --

import os, pathlib



def red(txt):
    return f"\033[91m{txt}\033[0m"


def green(txt):
    return f"\033[92m{txt}\033[0m"


def yellow(txt):
    return f"\033[93m{txt}\033[0m"


def blue(txt):
    return f"\033[94m{txt}\033[0m"


def magenta(txt):
    return f"\033[95m{txt}\033[0m"


def cyan(txt):
    return f"\033[96m{txt}\033[0m"


# --------- APP FOLDER  AND FILE ACCESS ---------
def app_folder_path():
    return pathlib.Path(__file__).parent.absolute()


def app_folder():
    return str(app_folder_path()) + "/word_list"


def word_file(word):
    return str(app_folder_path()) + "/word_list/" + word


def save_word(word, wl, letters, combi):
    if not os.path.exists(app_folder()):
        os.mkdir(app_folder())
    
    with open(word_file(word), 'w') as wf:
            wf.write(str(letters) + " lettres.\n")
            wf.write(str(combi) + " combinaisons.\n")
            wf.write("----------------------------\n")
            wf.writelines(str('\n'.join(sorted(wl))))
            wf.write("\n")
    
    print(green(" DONE !"), end = "")
    print(" Le fichier a été généré dans le dossier \" ", end = "")
    print(blue("Anagrams -> word_list"), "\".")

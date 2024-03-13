#!usr/bin/env python3
# -*- coding: utf-8 -*-

# =======================================================================
# =   ANAGRAMS                                                          =
# =      - Version   : 1.0                                              =
# =      - Author    : Ayckinn                                          =
# =      - Mail      : ayckinn@icloud.com                               =
# =      - Release   : March 13' 2024                                   =
# =      - Github    : https://github.com/AyckinnLisa?tab=repositories  =
# =      - Copyright : ©2020-2024                                       =
# =======================================================================

import os, itertools, time
import appfuncs as af


def main():
    os.system('clear')

    print(f'''{af.green(''' 
 # ===================================================== #
 # =                      ANAGRAMS                     = #
 # =                        v1.0                       = #
 # =                ©2020-2024 - @Ayckinn              = #
 # =                 ayckinn@icloud.com                = #
 # =  https://github.com/AyckinnLisa?tab=repositories  = #
 # ===================================================== #\n''')}
                  Bienvenue dans {af.blue("ANAGRAMS")}
   Le programme qui mélange toutes les lettres d'un mot.\n\n''')
    
    user_word = input(" Quel est le mot ? ")
    len_word = len(user_word)

    word_list = [''.join(x) for x in itertools.permutations(user_word, len_word)]

    counter = 0
    for word in word_list:
        counter += 1

    print(f"\n Lettres dans le mot {af.red(user_word)} : {af.magenta(len_word)}")
    print(f" Combinaisons possibles : {af.yellow(counter)}\n")
    time.sleep(.5)
    print(af.red(" Création du fichier en cours...\n"))
    time.sleep(2)
    af.save_word(user_word, word_list, len_word, counter)
    

if __name__ == "__main__":
    os.system('clear')
    main()

# ====================================================================== #
# = - Si c'est difficile à expliquer, alors c'est une mauvaise idée  - = #
# = - If it's hard to explain, it's a bad idea                       - = #
# ====================================================================== #
    
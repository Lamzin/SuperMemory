__author__ = 'Oleh'

import pickle
import datetime
import os

FILE_NAME_DICT = "dictionary"

class word:
    def __init__(self, word, translation):
        """
        :param word: str
        :param translation: [] of str
        """
        self.word = word
        self.translation = translation
        self.time_add = datetime.date.today()
        self.time_last_mention = datetime.date.today()
        self.successful = 1

        #(datetime.date.today() - now).days > successful

    def __str__(self):
        return u"%s, %s, %s" % (self.word, self.translation, self.successful)


def dictionary_load():
    return pickle.load(open(FILE_NAME_DICT, "rb")) if os.path.exists(FILE_NAME_DICT) else []

def dictionary_dump(dictionary):
    pickle.dump(dictionary, open(FILE_NAME_DICT, "wb"))


if __name__ == "__main__":

    # open(FILE_NAME_DICT, "wb")

    while(True):
        command = input("command: ")
        if command == u"exit":
            break

        elif command == u"add":
            dictionary = dictionary_load()

            new_word = input("word = ")
            new_translation = input("translate = ").split(u",")
            dictionary.append(word(new_word, new_translation))

            dictionary_dump(dictionary)

        elif command == u"all":
            dictionary = dictionary_load()

            dictionary = sorted(dictionary, key=lambda x: x.successful)
            for item in dictionary:
                print(item)

        elif command == u"review":
            pass

        elif command == u"erase":
            pass

        else:
            print("command not found")
            print("available command: add, all, review, erase, exit")

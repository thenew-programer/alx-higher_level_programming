#!/usr/bin/python3
""" Defines a function called text_indentation"""


def text_indentation(text):
    new_text = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    char_place = -1
    for idx, letter in enumerate(text):
        if letter in (".", "?", ":"):
            new_text += letter + "\n\n"
            char_place = idx + 1
            continue
        if char_place == idx:
            continue
        new_text += letter
    print(new_text, end='')


if __name__ == "__main__":
    text_indentation(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres"""
    )
    print('\n----------------------------------\n')
    text_indentation(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres"""
    )

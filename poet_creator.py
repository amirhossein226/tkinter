import tkinter as tk
from random import choice


window = tk.Tk()
window.title("Make your own poem!")
window.columnconfigure(0, weight=1, minsize=600)


def split(entry):
    input_list = entry.get().split(",")
    return [value.strip().lower() for value in input_list]


def len_isvalid(content):
    for key in content:
        if (key == "adverbs") and (len(content[key]) in [1, 2]):
            continue

        if len(content[key]) < 3:
            return False
    return True


def generate_poem():

    poem_lbl = tk.Label(master=output_frame, text="")
    poem_lbl.grid(row=1, column=0)

    # get the content of each field and store them in list
    fields_content = {f_name.lower(): split(field_ref[f_name])
                      for f_name in field_name}

    # validating the inputs
    if not len_isvalid(fields_content):
        error_msg = "All of the fields(except Adverb field which can be one word) must contain 3 word separated by comma!"
        result_header["text"] = error_msg
        return

    # if no problem exist during validation, then the error label must be emptys
    result_header["text"] = "Your poem:"

    # generating the random words based on what the user entered to the fields,
    random_words = dict()
    for field, value in fields_content.items():
        rand_values = [choice(value) for i in range(3)]
        random_words[field] = rand_values

    vowels = ["a", "i", "o", "e", "u"]
    a_or_an = "An" if random_words["nouns"][0] in vowels else "a"

    poem = f"""
{a_or_an} {random_words["adjective"][0]} {random_words["nouns"][0]}

A {random_words["adjective"][0]} {random_words["nouns"][0]} {random_words["verbs"][0]} {random_words["prepositions"][0]} the {random_words["adjective"][1]} {random_words["nouns"][1]}
{random_words["adverbs"][0]}, the {random_words["nouns"][0]} {random_words["verbs"][1]}
the {random_words["nouns"][1]} {random_words["verbs"][2]} {random_words["prepositions"][1]} a {random_words["adjective"][2]} {random_words["nouns"][2]}
"""
    poem_lbl['text'] = poem


title = tk.Label(
    window, text="Enter your favorite words, separated by commas.")
title.grid(row=0, column=0, pady=10)

# this frame is the container for all fields
input_frame = tk.Frame(window)
input_frame.columnconfigure(0, weight=1,  minsize=600)
input_frame.grid(row=1, column=0)

# input_frame's fields
field_name = ["Nouns", "Verbs", "Adjective", "Prepositions", "Adverbs"]
field_ref = dict()

for i in range(len(field_name)):
    inner_frame = tk.Frame(master=input_frame)
    inner_frame.columnconfigure(0, weight=1, minsize=100)
    inner_frame.columnconfigure(1, weight=1, minsize=500)
    inner_frame.rowconfigure(0, minsize=40)

    f_name = field_name[i]
    lbl = tk.Label(inner_frame, text=f"{f_name}:")
    ent = tk.Entry(inner_frame)
    field_ref[f_name] = ent

    lbl.grid(row=0, column=0, sticky="e", pady=4, padx=5)
    ent.grid(row=0, column=1, sticky="wens", pady=4)
    inner_frame.grid(row=i, column=0)

# generate button
generate_btn = tk.Button(window, text="Generate", command=generate_poem)
generate_btn.grid(row=2, column=0, pady=10)


# and this one will be container for all thing which related to the result
output_frame = tk.Frame(window, relief=tk.SUNKEN, borderwidth=5)
output_frame.grid(row=3, column=0)
output_frame.columnconfigure(0, minsize=600)


result_header = tk.Label(master=output_frame, text="")
result_header.grid(row=0, column=0)

window.mainloop()

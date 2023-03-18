import os
import re
from collections import Counter

directory = "H:\Projects\Chatterino Log Parser\Chatterino-Log-Parser\Temp Input"

directory = input("Enter your directory: ")

input_mode = input("1: Username Counter\n2: Word Counter\n\nEnter run mode: ")

if input_mode == "1":
    # regex pattern to match the username
    username_pattern = re.compile(r"\[\d{2}:\d{2}:\d{2}\]  ?(\w+):")

    # dictionary to store username counts
    username_count = Counter()

    for filename in os.listdir(directory):
        if filename.endswith(".log"):
            with open(os.path.join(directory, filename), "rb") as file:
                data = file.read()
                # try to decode with utf-8
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError:
                    # if utf-8 fails, try with latin-1
                    text = data.decode("latin-1")
                matches = re.findall(username_pattern, text)
                # update username counts
                username_count.update(matches)

    # output username counts to a text file
    with open("username_counts.txt", "w") as file:
        for username, count in username_count.most_common():
            file.write(f"{username}: {count}\n")

if input_mode == "2":
    output_length = input("Enter the amount of words you want to be output(n for all words): ")
    # regex pattern to match the message portion
    message_pattern = re.compile(r"\[\d{2}:\d{2}:\d{2}\]  ?\w+: (.+)")

    # dictionary to store word counts
    word_count = Counter()

    for filename in os.listdir(directory):
        if filename.endswith(".log"):
            with open(os.path.join(directory, filename), "rb") as file:
                data = file.read()
                # try to decode with utf-8
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError:
                    # if utf-8 fails, try with latin-1
                    text = data.decode("latin-1")
                matches = re.findall(message_pattern, text)
                # split messages into words and update word counts
                for message in matches:
                    words = message.split()
                    word_count.update(words)

    # output word counts to a text file
    if output_length.isdigit():
        with open("word_counts.txt", "w", encoding="utf-8") as file:
            for word, count in word_count.most_common(n=int(output_length)):
                file.write(f"{word}: {count}\n")
    else:
        with open("word_counts.txt", "w", encoding="utf-8") as file:
            for word, count in word_count.most_common(n=len(word_count)):
                file.write(f"{word}: {count}\n")
    
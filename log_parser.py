import os

word_search_input = "hello"
directory = "H:\Data\Chatterino Logs\Twitch\Channels\clintstevens"

def search_files(directory, extension=".log"):
    total_count = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(subdir, file)
                with open(file_path, encoding='utf-8') as f:
                    content = f.read()
                    count = content.count(word_search_input)
                    print(f"{file_path}: {count}")
                    total_count += count
    print(f"Total count: {total_count}")

search_files(directory)
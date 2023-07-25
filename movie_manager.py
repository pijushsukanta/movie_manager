
import json

from user_action import UserAction


def open_file(path):
    print(path)
    
    try:
        with open(f'{path}', 'r') as openfile:

        # Reading from json file
            try:
                movies = json.load(openfile)
                user_action = UserAction(movies=movies)
            except Exception as e:
                print(e)
    except FileNotFoundError as not_found:
        print("The movie database does not exist")
        

        
def main():
    file_path = input("> python movie_manager.py ")
    open_file(file_path)

if __name__ == "__main__":
    main()
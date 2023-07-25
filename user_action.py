import json

class UserAction:
    
    instruction_for_action = '''Enter an action - Add Movie (a), Delete Movie(d), View Movie Summary (s), Search Movie by Rating (r), Search Movie by Title (t), Search Movie by Genre (g) o Quit (q) : '''
    
    def __init__(self,movies=[]):
        self.movies = movies
        self.user_action()
        
    def user_action(self):
        
        action = input(f"{self.instruction_for_action}")
        if action == 'a':
            self.__add_movie()
        elif action == 'd':
            self.__delete_movie()
        elif action == 's':
            self.__movie_summary()
        elif action == 'r':
            self.__search_movie_by_rating()
        elif action == 't':
            self.__search_movie_by_title()
        elif  action == "g":
            self.__search_movie_by_genre()
        elif action == 'q':
            self.__quit()
        else:
            print("Please Enter Valid Action")
            self.user_action()
            
    def __add_movie(self):
        title = self.__input_title()
        genre = self.__input_genre()
        running_length = self.__input_running_length()
        year = self.__input_year()
        rating = self.__input_rating()
        description = self.__input_description()
        
        movie = {
            "Title" : title.title(),
            "Genre" : genre.title(),
            "Running_Length" : running_length,
            "Year" : year,
            "Rating" : rating,
            "Description" : description
        }
        
        self.movies.append(movie)
        self.__create_file(movies=self.movies)
        print(f"{title} Created Successfully")
        
        
    def __delete_movie(self):
        title = input("Title : ")
        index = -1
        for i,movie in enumerate(self.movies):
            if movie["Title"] == title.title() or movie["Title"] is None:
                index = i
        if index != -1:
            self.movies.pop(index)
            print(f"Deleted 1 Movie")
            self.__create_file(movies=self.movies)
            
        else:
            print("Movie not found")    
        self.user_action()
    
    def __movie_summary(self):
        for item in self.movies:
            self.__print_summary(item)
                
        self.user_action()
        
    def __search_movie_by_rating(self):
        rating = self.__input_rating()
        print(rating)
        movie = None
        for item in self.movies:
            if item["Rating"] == rating:
                self.__print_summary(item)
                movie = 1
        if movie is None:       
            print("Movie Not found by this rating")
        
        self.user_action()
    
    def __search_movie_by_title(self):
        title = input("Please Enter Movie Tilte : ")
        title = title.title()
        movie = None
        for item in self.movies:
            if item["Title"].startswith(title):
                 self.__print_summary(item)
                 movie = 1
        if movie is None:
            print("No Movie Found")
        self.user_action()
    
    def __search_movie_by_genre(self):
        genre = input("Please Enter Movie Genre : ")
        genre = genre.title()
        movie = None
        for item in self.movies:
            if item["Genre"].startswith(genre):
                self.__print_summary(item)
                movie = 1
        if movie is None:
            print("No Movie Found")
        self.user_action()
    
    def __quit(self):
        print("Thank you")
        
    def __input_title(self):
        title = input("Title : ")
        if title == "":
            print("Value Error : Title must be 1 to 32 characters in length")
            self.__input_title()
        is_unique = self.__is_title_unique(input_title=title)
        if len(title) <= 32 and is_unique:
            return title
        else:
            print("Value Error : Title must be 1 to 32 characters in length")
            self.__input_title()
        
    def __input_genre(self):
        genre = input("Genre : ")
        if self.__has_numbers(genre):
            print("Please Input Valid Genre")
            self.__input_genre()
        return genre.title()
    
    def __input_running_length(self):
        try:
            hh,mm = input("Length : ").split(":")
            hh = self.__value_error(hh)
            if hh is None:
                self.__input_running_length() 
            if isinstance(hh,int):
                if 0 < hh <100:
                    mm = self.__input_minute(mm=mm)
                    return f"{hh}:{mm}"
                else:
                    print("Please Enter HH between 0 to 99")
                    self.__input_running_length() 
        
            print("Format - Length : HH:MM")
        except Exception as e:
            print("Format - Length : HH:MM")
            self.__input_running_length()
        
        
    def __input_year(self):
        year = input("Year : ")
        year = self.__value_error(value=year)
        if year is None:
            self.__input_year()
        
        print(year)
        if 10000 > year > 1920:
            return year
        print("Please Enter Year Greater Than Equals to 1920")
        self.__input_year()
            
                
    def __input_minute(self,mm):
        mm = self.__value_error(value=mm)
        if mm is None:
           self.__input_running_length()
        if isinstance(mm,int):
            if 0 < mm < 60:
                return mm
        print("Please Enter MM between 0 to 59")
        self.__input_running_length()
        return mm
             
             
    
    def __input_rating(self):
        rating = input("Rating : ")
        rating = self.__value_error(value=rating)
        if isinstance(rating,int):
            if 0 < rating <= 5:
                return rating
            else:
                print("Enter Valid Rating Between 0 to 5")
                self.__input_rating() 
        else:
            print("Enter Valid Rating Between 0 to 5")
            self.__input_rating()    
            
    def __input_description(self):
        description = input("Description : ")
        if len(description) > 128:
            self.__input_description()
            
        return description
    
        
    def __is_title_unique(self,input_title):
        if len(self.movies) >= 0:
            for movie in self.movies:
                if movie["Title"] == input_title:
                    return False
            return True
    
    def __has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)
    
    def __value_error(self,value):
        try:
            input = int(value)
            return input
        except ValueError as value_error:
            print("Please Enter Valid Input")
            return None    
        
    def __print_summary(self,movie):
        movie = str(movie).replace("{","")
        movie = movie.replace("}","")
        movie = movie.replace("'","")
        
    def __create_file(self,movies=[]):
        with open("movies.json", "w") as outfile:
            outfile.write(json.dumps(self.movies))
            self.user_action()
    
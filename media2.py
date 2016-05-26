#import sys
#sys.path.append("Yoshiyasu/Documents/coding/Udacity/Full_stuck_nanodegree/movies")
import webbrowser
import fresh_tomatoes2

class Movie(object):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
iron_man = Movie("Iron Man", "After being held captive in an Afghan cave, an engineer creates a unique weaponized suit of armor to fight evil.", "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", "https://www.youtube.com/watch?v=8hYlB38asDY")
the_da_vinci_code = Movie("The Da Vinci Code", "A murder in Paris' Louvre Museum and cryptic clues in some of Leonardo da Vinci's most famous paintings lead to the discovery of a religious mystery. For 2,000 years a secret society closely guards information that -- should it come to light -- could rock the very foundations of Christianity.", "https://upload.wikimedia.org/wikipedia/en/6/6b/DaVinciCode.jpg", "https://www.youtube.com/watch?v=zMba3fckhuQ")
transcendence = Movie("Transcendence", "Dr. Will Caster (Johnny Depp), the world's foremost authority on artificial intelligence, is conducting highly controversial experiments to create a sentient machine. When extremists try to kill the doctor, they inadvertently become the catalyst for him to succeed. Will's wife, Evelyn (Rebecca Hall), and best friend, Max (Paul Bettany), can only watch as his thirst for knowledge evolves to an omnipresent quest for power, and his loved ones soon realize that it may be impossible to stop him.", "https://upload.wikimedia.org/wikipedia/en/e/ef/Transcendence2014Poster.jpg", "https://www.youtube.com/watch?v=VCTen3-B8GU")

movies = [iron_man, the_da_vinci_code, transcendence]
fresh_tomatoes2.open_movies_page(movies)
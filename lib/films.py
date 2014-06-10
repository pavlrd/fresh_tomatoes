import media
import fresh_tomatoes

avatar = media.Movie("Avatar", "Marine on alien planet", "http://upload.wikimedia.org/wikipedia/en/3/39/Avatar_world_map.jpg", "https://www.youtube.com/watch?v=FQznpYjqZBE")

man_of_steel = media.Movie("Man of Steel", "Man with great power, from planet far away from the Earth", "http://fc01.deviantart.net/fs71/i/2013/238/8/8/supergirl__man_of_steel_version_by_silentarmageddon-d6jmbbv.jpg", "https://www.youtube.com/watch?v=zzvXXaT70JU")

dark_knight = media.Movie("The Dark Knight", "Night knight, who fight for good", "http://hd.wallpaperswide.com/thumbs/batman_the_dark_knight_2-t2.jpg", "https://www.youtube.com/watch?v=TQfcgaNdBCA")

movies = [avatar, man_of_steel, dark_knight]

fresh_tomatoes.open_movies_page(movies)

man_of_steel.show_trailer()


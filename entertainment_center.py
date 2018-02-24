import media
import fresh_tomatoes
"""
to add a new movie  :
    <movie_name> = media.Movie("<movie name",
                               "<movie description>",
                               "<movie image link>",
                               "<movie trailer>")
"""
toy_story = media.Movie("Toy Story",
                        "Toy Story is a 1995 American computer-animated buddy comedy adventure film produced by Pixar Animation Studios for Walt Disney Pictures. The directorial debut of John Lasseter, Toy Story was the first feature-length computer-animated film and the first feature film produced by Pixar. ",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Maze_Runner = media.Movie("Maze Runner",
                          "A teenager wakes up inside an underground elevator with no memory of his identity. A group of male youths greet him in a large grassy area called the  enclosed by tall stone walls. The boys have formed a rudimentary society, with each assuming specialized tasks. Their leader, Alby, says that every boy eventually recalls his name but not his past. The boy learns that a vast Maze surrounding them may be the only way out. During the day, designated Runners search the Maze for an escape route, returning before nightfall when the entrance closes. No one has ever survived a night in the Maze.", 
                          "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/The_Maze_Runner_poster.jpg/220px-The_Maze_Runner_poster.jpg",
                          "https://www.youtube.com/watch?v=4-BTxXm8KSg")

Inception = media.Movie("Inception",
                        "The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for the implantation of another person's idea into a target's subconscious.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

Interstellar  = media.Movie("Interstellar",
                            "Interstellar is a 2014 science fiction film directed, co-written, and co-produced by Christopher Nolan. It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, and Michael Caine. Set in a dystopian future where humanity is struggling to survive, the film follows a group of astronauts who travel through a wormhole in search of a new home for humanity.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")

Insurgent = media.Movie("Insurgent",
                        "The Divergent Series: Insurgent (also known simply as Insurgent) is a 2015 American science fiction action film directed by Robert Schwentke, based on Insurgent, the second book in the Divergent trilogy by Veronica Roth.", 
                        "https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg",
                        "https://www.youtube.com/watch?v=suZcGoRLXkU")

The_Fault_in_Our_Stars = media.Movie("The Fault in Our Stars", 
                                     "The Fault in Our Stars is a 2014 American romantic drama film directed by Josh Boone, based on the novel of the same name by John Green. The film stars Shailene Woodley, Ansel Elgort, and Nat Wolff, with Laura Dern, Sam Trammell, and Willem Dafoe playing supporting roles. Woodley plays Hazel Grace Lancaster, a sixteen-year-old cancer patient who is forced by her parents to attend a support group, where she meets and subsequently falls in love with Augustus Waters, another cancer patient, played by Elgort." ,
                                     "https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png" ,
                                     "https://www.youtube.com/watch?v=9ItBvH5J6ss")

Idiots = media.Movie("3 Idiots" , 
                     "he film is about the friendship of three students at an Indian engineering college,[5] and is a satire about the social pressures under an Asian education system.[6][7][8] It also incorporated real Indian inventions, from Remya Jose,[9] Mohammad Idris,[10] Jahangir Painter,[11] and Sonam Wangchuk.[12]." , 
                     "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg", 
                     "https://www.youtube.com/watch?v=K0eDlFX9GMc")

The_Martian = media.Movie("The Martian", 
                          "The Martian is a 2015 science fiction film directed by Ridley Scott and starring Matt Damon. The screenplay by Drew Goddard is based on Andy Weir's 2011 novel of the same name about an astronaut who is mistakenly presumed dead and left behind on Mars. The film depicts his struggle to survive and others' efforts to rescue him.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")
#add all movies to list
movies = [toy_story, Maze_Runner, Inception, Interstellar, Insurgent,The_Fault_in_Our_Stars, Idiots, The_Martian]

#create movie page HTML
fresh_tomatoes.open_movies_page(movies)

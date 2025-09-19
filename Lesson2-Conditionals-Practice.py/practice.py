age = int(input("Enter your age: "))
movie_rating = input(f"Enter the movie rating (G, PG, PG-13, R): ")

if age >= 6 and movie_rating == "G":
    print("You can watch the movie.")
elif age >= 13 and movie_rating == "PG":
    print("You can watch the movie")
elif age >= 17 and movie_rating == "PG-13":
    print("You can watch the movie")
else:
    print("Not recommended for your age")

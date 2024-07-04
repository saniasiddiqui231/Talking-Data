#Talking Data 


import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = input("Enter your fav movie name: ")





#Part 3 Investigate the data
#print(movieData["movie_title"])



#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList]
#print(favMovieData)




print("\n\n")

#Create a new variable to store a new data set with a certain genre
animationBooleanList = movieData["genres"].str.contains("Animation")
#print(animationBooleanList)
animData = movieData.loc[animationBooleanList]
#print(animData)



numOfMovies = animData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Animation in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Animation.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min1 = animData["audience_rating"].min()
diff = int(favMovieData["audience_rating"]) - min1
print("The min audience rating of the data set is: " + str(min1))
print(favMovie + " is rated " + str(diff) + " points higher than the lowest rated movie.")
print()

#find max
max = animData["audience_rating"].max()
diffe = max - int(favMovieData["audience_rating"])
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(diffe) + " points lower than the highest rated movie.")
print()
#making function for comparison
def compare(num1: int, num2: int ) -> str:
      return "higher than" if num1 > num2 else("lower than" if num1 < num2 else "same as")
#find mean
mean = animData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + "'s rating is " + compare(int(favMovieData["audience_rating"]), mean) + " the mean movie rating.")

#find median

median = animData["audience_rating"].median()

print("The median audience rating of the data set is: " + str(median))
print(favMovie + "'s rating is " + compare(int(favMovieData["audience_rating"]), median) + " the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(animData["audience_rating"])



plt.grid(True)
plt.title("Audience Ratings of Animation Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = animData, x = "audience_rating", y = "critic_rating" )



plt.grid(True)
plt.title("Audience rating vs Critic rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)




print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")

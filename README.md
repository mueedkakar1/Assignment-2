# Assignment-2
Get data from an API and store it in a Data Frame

I took an api from the website named "themoviedb"

Code Workings:
In this Assignment, I imported the Python pandas, JSON, and requests libraries and used the request. get()function to get my data from API. After that I stored that data in a data frame using the command 'pd.DataFrame.from_dict()' but after running the code I realized that the data we in nested dictionary format so I separated the result columns from the data frame as a Dictionary using the command 'df2['results'].to_dict()' and stored it in another dictionary.

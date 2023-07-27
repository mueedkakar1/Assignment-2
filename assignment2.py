# Made by Mohib Ullah

import requests
import json
import pandas as pd
responce = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=2ade49b41e86fd80a771c3a85cd3059e');
a = responce.json();
# puts data in DataFrame
df2 = pd.DataFrame.from_dict(a);
# data frame contained nested dictionary so we seperated the result columb as a dictionary
df= df2['results'].to_dict();
# I created an other Data frame for our results .
df1 = pd.DataFrame.from_dict(df);
print(df1)

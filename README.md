# ✌️ [Airbnb Kaggle](https://www.kaggle.com/c/airbnb-madrid-ironhack/data) competiton: ✌️
![elgif](https://i.pinimg.com/originals/e4/9e/d9/e49ed95f9e8ecc0d31a89950834d1c0a.gif)
### Introduction:
In this repo I am sharing the code that I used in a kaggle competition.   
We worked with data from airbnb. Originally we were given two different csv files, with information of Airbnb flats and the hosts who owned that flats that were offered. One of the files had the price of the airbnb offers, this column was missing in the other file and was the one to be guessed by our models. In the following text I am going to try and guide you through the processes I followed and what were the main keys that lead to finally winning the competition. You can find the data in the kaggle competition [here](https://www.kaggle.com/c/airbnb-madrid-ironhack/data).

I have shared all the code I have used, and the data is aviable in the link above, but I haven't shared the processed data or results. If the reader is interested can contact me or just run the code in the files above. 

Lastly I would also like to remark that this competition had a duration of less than a week, so this project can be easly improved with a little further work. I invite you to do so and improve my first aproaches. 

### The Data 🤔:
I have mainly worked with the *train.csv* file. First I did a first cleaning of the data, deleting all the columns that I thought had no relevance whatsoever with the price, such as the host ID or the host's picture url. After that I followed 3 main processes before starting with the Machine Learining techniques. In the following section I am going to go through this processes. 


### The keys:

* Scrapping, one of the first things I noticed was that there was a column with the urls of the flats that were offered in airbnb. This was a huge opportunity to gather more data. I started to work with a code to scrap this urls with selenium. This was very challenging, and after trying different methods I was able to scrap most of the urls and get the actual price of the flats. The addition of this new column, a column I called "price_now", was one of the main keys, obviously, but not the only one. 

* Further clean and vectorization. Once I had all the information I could gather I had to vectorize the data to make it easier to read for the models I was going to generate. What I did was basically dropping all those columns I didn't think I could vectorize and with the rest I created functions to vectorize them, for instance:
- With the column of amenities. I transformed all the strings to lists and then I made a list with the amienities I considered most important, and for the others I just included another value to those lists called others. Once the lists were included in the dataframe (with a simple apply method) I used the function, from the pandas library, getdummies, creating a column for each of the amenities I considered relevant. 
- It was harder to gather information from the descriptions, however I did used this columns to gather some information. I studied what language were they written, basically I studied wether they were written in english, in dutch or other languages. 

* Lastly I studied what was the correlation between all the columns and tried to keep only the ones that were more strongly correlated with the price, as the others could misslead the models I was going to train. 

### The Machine Learning:
As the time to study the data was very short, most of the time I had I dedicated to clean and study the data, that is why I didn't have much time to work with my Machine Learning Model. I had some ideas I wasn't able to apply. I started by trying some basic models such as Random Forstet Regressor or Linear Regression, but finally I decided to use the library H2O, which with the that I gave it reached the sucesful results I was able to hand in.


### The results:
The results were very satisfying, I got to win the competition with an RMSE of 70,79€. However this was done within a week, I must insist that there are many ways to improve and better understand this project, I invite you to do so and report me with any feedback I can use to improve it. 

### Bibliography,
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/doc/1.18/)
* [Plotly](https://plotly.com/python/)
* [H2O](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/intro.html)
* [Langdetect](https://github.com/fedelopez77/langdetect)
* [ReGex](https://docs.python.org/3/library/re.html)
* [Matplotlib](https://matplotlib.org/)
* [Scikit-Learn](https://scikit-learn.org/stable/)

#### Source of the data:
* [Kaggle](https://www.kaggle.com/)
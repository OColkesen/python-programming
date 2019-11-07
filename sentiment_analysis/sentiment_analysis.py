"""
This program gives the average sentiment value for a given topic on Twitter
with respect to the last 100 tweets posted.

Authors: Maxine Tang, Oğuzhan Çölkesen
Time Spent: 2 hours 
"""

from csc121.twitter import get_tweets

def create_valences_dictionary():
    """
    This function creates a dictionary of valences for all words based on the
    file named "AFINN-111.txt". It places the words as keys and the valences as
    values in the dictionary and returns the dictionary itself.
    
    Returns:
        A dictionary, which includes the words in "AFINN-111.txt" file as keys and
        the respective words' valences as values.
        
        If the "AFINN-111.txt" file is not in the same directory with the program,
        the function returns False.
    """
    try:
        with open("AFINN-111.txt",'r') as in_file:
            valence_dictionary = {}
            for lines in in_file:
                words = lines.split()
                valence_dictionary[words[0]] = int(words[1])
        
        return valence_dictionary
    
    except IOError:
        print("File not found")
        return False
        #Used a boolean variable to write an if statement easily in the
        #analyze_tweets() function.

def get_tweets_text(topic):
    """
    This function communicates with Twitter API to get the latest 100 tweets
    on the topic that is taken as the parameter of the function. Then, the
    function extracts the text of tweets from the information received and
    appends it to a seperate list, which is returned in the end.
    
    Parameters:
        topic - a string, which is the topic that the user is interested to
                get the tweets about. The tweets extracted must include this
                string in the text.
    
    Returns:
        A list, which includes 100 strings that are the texts of the latest 100
        tweets. The function only returns the tweets' text in a list.
    """
    Api_data = get_tweets(topic)
    statuses_list = Api_data["statuses"]
    tweets_list = []
    
    for i in range(len(statuses_list)):
        tweets_list.append((statuses_list[i])["text"])
    
    return tweets_list


def create_sentiment_list(tweets_list, valence_dictionary):
    """
    This function creates a list, which includes the sentiment value of each
    tweet in a list of integers. Firstly, it calculates the an individual tweet's
    sentiment by using the valence values in the valance_dictionary. Then, the
    individual sentiment values for each tweet is appended to a list, which is
    then returned.
    
    Parameters:
        tweets_list - a list, which includes the strings of tweets whose
        individual sentiment values will be calculated.
        
        valence_dictionary - a dictionary, which includes the valence values
                             for many different words that will be used to
                             calculate the total sentiment for each tweet

    Returns:
        A list, which includes integers that are the total sentiment values for each
        individual tweet.
    """
    tweet_sentiment_list = []
    
    for i in range(len(tweets_list)):
        tweet_sentiment = 0
        #setting tweet_sentiment to 0 at the beginning of the loop to reset it for
        #each tweet.
        words = tweets_list[i].split()
        for word in words:
            word = word.lower()
            if word in valence_dictionary:
                tweet_sentiment += valence_dictionary[word]
                
        tweet_sentiment_list.append(tweet_sentiment)
        
    return tweet_sentiment_list
    

def analyze_tweets(topic):
    """
    This function is the main function that should be called in the program.
    It accepts a string as the topic of the tweets that will be analyzed
    to find the average sentiment towards that topic. By using the helper
    functions create_valences_dictionary(), get_tweets_text(), and create_sentiment_list(),
    the function gets the sentiment value for each individual tweet in a list and
    computes the average sentiment towards the topic, which is then returned.
    
    Parameters:
        topic - a string, which the user is interested in finding the average
        sentiment value of on Twitter based on latest 100 tweets.

    Returns:
        A float value, which is the average sentiment that is computed by taking
        the average of the sentiment for each tweet for the topic inputed by the
        user.
        
        0 if the "AFINN-111.txt" file is not in the same directory with the program,
        so the valence_dictionary cannot be created.
        
        0 if there are no tweets, which includes the string written by the user.
    """
    valence_dictionary = create_valences_dictionary()
    if valence_dictionary is False:
        return 0
    
    tweets_list = get_tweets_text(topic)
    if len(tweets_list) == 0:
        return 0
    
    tweet_sentiment_list = create_sentiment_list(tweets_list, valence_dictionary)
    
    total_sentiment = 0
    for i in tweet_sentiment_list:
        total_sentiment += i
    
    sentiment_value = 0
    sentiment_value = total_sentiment/len(tweet_sentiment_list)
    
    return sentiment_value
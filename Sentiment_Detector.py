import string

# Lists of positive words categorized by type
positive_emotions = ['happy','joyful','excited','pleased',
                     'grateful','proud','content','hopeful',
                     'satisfied','relieved'
                     ]

positive_descriptions = ['good','great','excellent',
                         'wonderful','amazing','fantastic',
                         'beautiful', 'brilliant','impressive',
                         'outstanding','helpful','perfect',
                         'pleasant'
                         ]

positive_actions = ['love','enjoy','appreciate',
                    'succeed','improve','recommend',
                    'praise','accomplish','thrive',
                    'win','celebrate','achieve'
                    ]

# Lists of negative words categorized by type
negative_emotions = ['sad', 'angry', 'upset', 'disappointed',
                    'frustrated', 'annoyed', 'worried', 'afraid',
                    'stressed', 'miserable', 'depressed', 'anxious'
                    ]

negative_descriptions = ['bad', 'terrible', 'awful', 'horrible',
                        'poor', 'dreadful', 'disappointing', 'useless',
                        'unpleasant', 'inferior', 'flawed', 'inadequate'
                        ]

negative_actions = ['hate', 'dislike', 'fail', 'struggle',
                   'break', 'ruin', 'reject', 'suffer',
                   'complain', 'criticize', 'regret', 'avoid'
                   ]

# Combine all positive and negative words into master lists for easier lookup
positive_list = positive_actions + positive_descriptions + positive_emotions
negative_list = negative_emotions + negative_descriptions + negative_actions


def clean_text(text):
    """
    Clean the input text by converting to lowercase and removing punctuation
    
    Args:
        text (str): The input text to be cleaned
    
    Returns:
        str: The cleaned text with punctuation removed
    """
    punctuation= ",@:!?.'"
    cleaned_text = text.lower()
    for mark in punctuation:
            cleaned_text = cleaned_text.replace(mark, " ")
    return cleaned_text

def tokenization(cleaned_text):
    """
    Split cleaned text into individual words (tokens)
    
    Args:
        cleaned_text (str): Text that has been processed by clean_text()
    
    Returns:
        list: List of individual words
    """
    stripped_text = cleaned_text.strip()
    tokens = stripped_text.split()
    return tokens

def get_word_sentiment(token):
    """
    Determine the sentiment of a single word
    
    Args:
        token (str): A single word
    
    Returns:
        str: 'positive', 'negative', or 'neutral'
    """
    if token in positive_list:
        return 'positive'
    elif token in negative_list:
        return 'negative'
    else:
        return 'neutral'
    
def count_word_sentiment(tokens):
    """
    Count the number of positive, negative, and neutral words in the text
    
    Args:
        tokens (list): List of words from the tokenization function
    
    Returns:
        tuple: Counts of (negative, positive, neutral) words
    """
    positive_count = 0
    negative_count = 0
    neutral_count = 0 

    for token in tokens:
        # Analyze each word individually
        sentiment = get_word_sentiment(token) 
        if sentiment == 'negative':
            negative_count += 1
        if sentiment == 'positive':
            positive_count += 1
        if sentiment == 'neutral':
            neutral_count += 1

    return negative_count, positive_count, neutral_count    
    
def determine_sentiment(negative_count, positive_count, neutral_count):
    """
    Calculate the overall sentiment based on word counts
    
    Args:
        negative_count (int): Number of negative words
        positive_count (int): Number of positive words
        neutral_count (int): Number of neutral words
    
    Returns:
        tuple: (Sentiment label, normalized score)
    """
    # Return "insufficient data" if we don't have enough sentiment words
    if (positive_count + negative_count) < 2:
        return "insufficient data", 0
    else:
        # Calculate normalized score between -1 and 1
        normalized_score = round((positive_count - negative_count) / (positive_count + negative_count + neutral_count), 1)

    # Apply thresholds to determine overall sentiment
    if normalized_score < -0.2:
        return "Negative", normalized_score 
    elif normalized_score >= -0.2 and normalized_score <= 0.2: 
        return "Neutral", normalized_score
    else:
        return "Positive", normalized_score


def analyze_text_sentiment(text):
    """
    Main function to analyze sentiment of a given text
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        None: Prints the sentiment and score
    """
    # Process text through the sentiment analysis pipeline
    cleaned_text = clean_text(text)
    tokens = tokenization(cleaned_text)
    negative_count, positive_count, neutral_count = count_word_sentiment(tokens)
    output = determine_sentiment(negative_count, positive_count, neutral_count)

    # Display the result
    print(f"Sentiment & Score: {output}")

# Analyze the sample text
analyze_text_sentiment(my_text)


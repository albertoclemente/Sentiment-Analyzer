# Sentiment Analyzer

A lightweight Python-based sentiment analysis tool that classifies text as positive, negative, or neutral based on lexical analysis.

## Description

This sentiment analyzer uses a rule-based approach with predefined lexicons to evaluate the emotional tone of text. The implementation categorizes words into positive and negative groups (further subdivided into emotions, descriptions, and actions) and calculates an overall sentiment score based on their frequency in the input text.

## Features

- **Lexicon-based classification**: Uses curated word lists for sentiment detection
- **Categorized sentiment words**: Organizes vocabulary by emotions, descriptions, and actions
- **Text preprocessing**: Handles lowercase conversion and punctuation removal
- **Normalized scoring**: Produces a sentiment score between -1 and 1
- **Confidence threshold**: Requires minimum sentiment words for reliable classification
- **Zero dependencies**: Implemented in pure Python with no external packages required

## How It Works

1. Text is cleaned by converting to lowercase and removing punctuation
2. The cleaned text is tokenized into individual words
3. Each word is classified as positive, negative, or neutral based on predefined lexicons
4. Sentiment counts are tallied and a normalized score is calculated
5. The final sentiment label is determined based on score thresholds

## Limitations

- Does not account for negations (e.g., "not good")
- Cannot detect sarcasm or context-dependent sentiment
- Limited vocabulary compared to machine learning approaches
- Treats all sentiment words equally (no weighting by intensity)

Perfect for educational purposes or as a starting point for more advanced sentiment analysis implementations.

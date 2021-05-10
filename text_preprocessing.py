"""
This preprocesses text data in order to clean it, standardize it. So we are able to analyzse and extract
information from the text data.
"""

import spacy


def clean_text(text):
    """
    Cleans the text with spacy lemmatization.
    https://spacy.io/usage/linguistic-features#lemmatization

    Spacy needs to download en_core_web_sm in order to work.
    Please place the following code inside your notebook in order to
    use the function.
    !python -m spacy download en_core_web_sm
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    cleaned_text = [token.lemma_ for token in doc]
    cleaned_text = " ".join([word.lower() for word in cleaned_text])
    return cleaned_text

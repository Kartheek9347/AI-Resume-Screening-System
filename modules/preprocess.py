from utils.text_utils import clean_text


def preprocess_text(text):

    processed = clean_text(text)

    return processed
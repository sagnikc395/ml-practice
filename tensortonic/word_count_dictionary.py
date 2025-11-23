def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    word_freq_dict = {}

    for sentence in sentences:
        for word in sentence:
            if word not in word_freq_dict:
                word_freq_dict[word] = 1
            else:
                word_freq_dict[word] += 1
    
    return word_freq_dict

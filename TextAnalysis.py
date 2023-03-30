import itertools

import os
import re
import nltk
from nltk.tokenize import sent_tokenize


class TextAnalysis:
    filtered_article_array = []
    def flitere(name):
        print('sd', str(name))
        filtered_article_array = []
        with open(name, "r") as f:
            for line in f.readlines():
                k = line.split(" ")
                for i in k:
                    filtered_article_array.append(re.sub('[^a-zA-Z0-9 \- \']', '', i))
            f.close()
            print('yyuu', filtered_article_array)
            return filtered_article_array
    def average_word_length(word_array):
        print(word_array)
        one_word_array = ''.join(word_array)
        print(one_word_array)
        count = len(one_word_array)
        return count / len(word_array)

    def personal_pronouns(word_array):
        pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b', re.I)
        pronouns = []
        for i in word_array:
            pronouns.append(pronounRegex.findall(i))
        count = len(pronouns)
        return count

    def syllable_count_per_word(word_array):
        array_of_syllables = []
        for i in word_array:
            array_of_syllables.append(re.findall('(?!e$)[aeiouy]+', i, re.I))
        array_of_syllables = [x for x in array_of_syllables if x != []]
        return len(array_of_syllables)

    def word_count(word_array):
        filtered_words = [word for word in word_array if word not in nltk.corpus.stopwords.words('english')]
        return len(filtered_words)

    def complex_word_count(word_array):
        array_of_syllables = []
        for i in word_array:
            array_of_syllables.append(re.findall('(?!e$)[aeiouy]+', i, re.I))
        array_of_syllables = [x for x in array_of_syllables if x != []]
        count = 0
        for j in array_of_syllables:
            print(j)
            if len(j) > 2:
                count = count + 1
        return count

    def average_number_of_words_per_sentence(word_array, original_word_array):
        count = 0
        if(word_array[1]):
            number_of_sentences = sent_tokenize(word_array[1])
            count = len(original_word_array) / len(number_of_sentences)
        return count

    def analysis_of_readability(word_array, original_word_array):
        print(word_array)
        if (word_array[1]):
            number_of_sentences = sent_tokenize(word_array[1])
        else:
            number_of_sentences = 1
        average_sentence_length = len(original_word_array) / len(number_of_sentences)
        percentage_of_complex_words = len(original_word_array)
        fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
        return {average_sentence_length, percentage_of_complex_words, fog_index}

    def sentimental_analysis(word_array):
        stopword_path = os.listdir('StopWords/')
        dictionary_path = os.listdir('MasterDictionary/')
        for entry in stopword_path:
            print(entry)
            path = 'StopWords/' + entry
            stopwords = []
            with open(path, "r") as f:
                for line in f.readlines():
                    j = line.split("|")
                    for i in j:
                        stopwords.append(i.strip().lower())
            f.close()
            stopwords_set = set(stopwords)
            output = [w for w in word_array if not w.lower() in stopwords_set]
        print(output)
        negative_count = 0
        positive_count = 0
        for entry in dictionary_path:
            print(entry)
            path = 'MasterDictionary/' + entry
            master_dictionary_words = []
            with open(entry, "r") as f:
                for line in f.readlines():
                    j = line.split("|")
                    for i in j:
                        master_dictionary_words.append(i.strip().lower())
            f.close()
            signed_words = set(master_dictionary_words)
            if entry == 'postive-words.txt':
                for w in output:
                    if w in signed_words:
                        positive_count = positive_count + 1
            elif entry == 'negative-words.txt':
                for w in output:
                    if w in signed_words:
                        negative_count = negative_count + 1

            print(positive_count, negative_count)
        polarity_score = (positive_count - negative_count) / ((positive_count + negative_count) + 0.000001)
        subjectivity_score = (positive_count + negative_count) / ((len(output)) + 0.000001)
        return {positive_count,negative_count,polarity_score,subjectivity_score}

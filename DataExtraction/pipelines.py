# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import re

import pandas as pd
from itemadapter import ItemAdapter
import TextAnalysis
class DataextractionPipeline:
    # def open_spider(self, spider):
    #     self.file = open('items.json', 'w')
    #
    # def close_spider(self, spider):
    #     self.file.close()

    def process_item(self, item, spider):
        name = "quotes"
        data = pd.read_excel(r'Input.xlsx')
        df = pd.DataFrame(data, columns=['URL_ID', 'URL'])
        res = {}
        for i,j in zip(df['URL'],df['URL_ID']):
            print(i)
            res[j] = i
        # filename = f'quotes-{page}.html'
        print(res)
        my_list = []
        for i in item.values():
            print(i)
            my_list.append(i)
        new_list = []
        new_list1= "".join(my_list[1])
        new_list.append(my_list[0])
        new_list.append(new_list1)
        key_list = list(res.keys())
        val_list = list(res.values())

        # print key with val 100
        position = val_list.index(my_list[2])
        file_name = f'{key_list[position]}.txt'
        file = open(file_name, 'w')
        for item in new_list:
            file.write(item + "\n")

        class_object = TextAnalysis.TextAnalysis

        unfiltered_article_array = []
        filtered_article_array = []
        with open(f'{file_name}', "r") as f:
            for line in f.readlines():
                unfiltered_article_array.append(line)
            f.close()

        filtered_article_array = class_object.flitere(file_name)
        analysis_of_readability = class_object.analysis_of_readability(filtered_article_array, unfiltered_article_array)
        average_number_of_words_per_sentence =  class_object.average_number_of_words_per_sentence(filtered_article_array, unfiltered_article_array)
        average_word_length = class_object.average_word_length(filtered_article_array)
        complex_word_count = class_object.complex_word_count(filtered_article_array)
        personal_pronouns = class_object.personal_pronouns(filtered_article_array)
        sentimental_analysis = class_object.sentimental_analysis(filtered_article_array)
        syllable_count_per_word = class_object.syllable_count_per_word(filtered_article_array)
        word_count = class_object.word_count(filtered_article_array)
        print(word_count)

        return item

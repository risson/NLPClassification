import numpy as np
from keras.preprocessing.text import Tokenizer

def read_file(txt_file):
    contents, labels = [], []
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            label, content = line.strip().split('\t')
            labels.append(label)
            contents.append(list(content))
    return contents, labels

def word_idx_dict(idx_word_dict):
    vocab_dict = {word:idx for idx,word in idx_word_dict.items()}
    return vocab_dict

def return_category():
    categories = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']
    cat_id = dict(zip(categories, range(len(categories))))
    return categories, cat_id

def process_file():
    
import numpy as np
import 


class CNNClassifier():
    
def read_file(txt_file):
    contents, labels = [], []
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            label, content = line.strip().split('\t')
            labels.append(label)
            contents.append(list(content))
    return contents, labels

def 
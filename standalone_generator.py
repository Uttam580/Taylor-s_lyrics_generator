# importing required librabries
import tensorflow
import pandas as  pd 
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import sys
print('import successfully')

# model loading 
MODEL = './model/Lyrics_generator.h5'
model= load_model(MODEL)
model.summary()
print('model loded')

# generate lyrics
def gen_char(generated_characters):
    a=[]
    seq_len=100#Inputs of the model will be sequences of 100 characters
    data_X=[] #initializing an empty list data_X that will store sequences of 100 characters
    data_y= [] #initializing an empty list data_y that will store targets of data_X
    textFileName = './model/lyricsText.txt'
    raw_text = open(textFileName, encoding = 'UTF-8').read()
    raw_text = raw_text.lower()
    chars = sorted(list(set(raw_text)))
    #created two dictionaries , one to convert chars to ints, the other to convert ints back to chars in order to map characters :
    int_chars = dict((i, c) for i, c in enumerate(chars))
    chars_int = dict((i, c) for c, i in enumerate(chars))
    n_chars = len(raw_text)
    n_vocab = len(chars)

    for i in range(0, n_chars - seq_len, 1):#looping from 1 to number of sequences of length 100 in raw_text
        seq_in  = raw_text[i:i+seq_len] #taking a sequence of length 100 from raw_text
        seq_out = raw_text[i + seq_len]#taking the character that follows the sequence
        data_X.append([chars_int[char] for char in seq_in])#mapping seq_in to integers and append it to data_X
        data_y.append(chars_int[seq_out])#mapping the seq_out to integer and append it to data_y
    n_patterns = len(data_X)

    print( 'Total number of sequences : ', len(data_X))
    # set a random seed :
    start = np.random.randint(0, len(data_X)-1)
    print(start)
    pattern = data_X[start]
    print(pattern)
    print('Seed : ')
    print("\"",''.join([int_chars[value] for value in pattern]), "\"\n")
    print('generating lyrics ,Please wait !!')
    for i in range(generated_characters):
        x = np.reshape(pattern, ( 1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x,verbose = 0)
        index = np.argmax(prediction)
        result = int_chars[index]
        #seq_in = [int_chars[value] for value in pattern]
        sys.stdout.write(result)# printing result over screen 
        a.append(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    output = ''.join(a)
    return output 

# How many characters you want to generate
generated_characters = 300
gen_char(generated_characters)
print('\nDone')

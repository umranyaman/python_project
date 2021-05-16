#Things to remember 
#Before processing any text, you need to remove all the punctuation marks. To do this, you can go through each line of text, character-by-character, using the isalpha() method. This will check whether or not the character is a letter.
#To split a line of text into words, you can use the split() method.
#Before storing words in the frequency dictionary, check if they’re part of the "uninteresting" set of words (for example: "a", "the", "to", "if"). Make this set a parameter to your function so that you can change it if necessary.

# Python program to generate WordCloud
  
# importing all necessery modules
#import pip

#def install(package):
#    if hasattr(pip, 'main'):
#        pip.main(['install', package])
#    else:
#        pip._internal.main(['install', package])

# Example
#if __name__ == '__main__':
#    install('matplotlib')
#if __name__ == '__main__':
#    install('pandas')
#if __name__ == '__main__':
#    install('wordcloud')

from PIL.Image import NONE
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

book = pd.read_csv('65348-0.txt', delimiter = "\t")
comment_words = ''
stopwords = set(STOPWORDS)


for value in book.CONTENT:
    value = str(value)
    book_splitted = book.split()


for i in range(len(book_splitted)):
    book_splitted[i] = book_splitted[i].lower()
      
    comment_words += " ".join(book_splitted)+" "
  
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

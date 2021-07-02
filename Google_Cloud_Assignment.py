import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

str = "Any fool can try to defend his or her mistakes – and most fools do – but it raises one above the herd and gives one a feeling of nobility and exultation to admit one’s mistakes. For example, one of the most beautiful things that history records about Robert E. Lee is the way he blamed himself and only himself for the failure of Pickett’s charge at Gettysburg."

def calculate_frequencies(str):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    '''LEARNER CODE START HERE'''
    count = 0
    cloud_dict = dict()
    cloud_arr = str.split(" ")
    new_cloud = list()
    # Removing uninteresting words from the text file
    for word in cloud_arr:
        for uninteresting_word in uninteresting_words:
            if word is not uninteresting_word:
                new_cloud.append(word)
        
    # removing punctuations from the text file
    for word in new_cloud:
        if not word.isalpha():
            word = ''.join([letter for letter in word if word.isalpha()])
            
    # Counting frequency of words in cloud_arr and saving it in cloud_dict
    for word in new_cloud:
        if word not in cloud_dict:
            cloud_dict[word] = count
        else:
            cloud_dict[word] = count + 1
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(cloud_dict)
    return cloud.to_array()
            
# Display your wordcloud image

myimage = calculate_frequencies(str)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

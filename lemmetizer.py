'''
Lemmatization is another way of reducing words to their base forms. 
The base forms that were obtained from Stemmers didn't make sense. 
For example, all the three stemmers said that the base form of calves is calv, which is not a real word. 

Lemmatization takes a more structured approach to solve this problem.
The lemmatization process uses a vocabulary and morphological analysis of words. It
obtains the base forms by removing the inflectional word endings such as ing or ed. This
base form of any word is known as the lemma. If you lemmatize the word calves, you
should get calf as the output. One thing to note is that the output depends on whether the
word is a verb or a noun. Let's take a look at how to do this using NLTK.

'''
from nltk.stem import WordNetLemmatizer

input_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize', 'possibly', 'provision', 'hospital', 'kept', 'scratchy', 'code']


# Create lemmatizer object
lemmatizer = WordNetLemmatizer()

# Create a list of lemmatizer names for table display and format the text accordingly:
lemmatizer_names = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
formatted_text = '{:>24}' * (len(lemmatizer_names) + 1)
print('\n', formatted_text.format('INPUT WORD', *lemmatizer_names), '\n', '='*75)

#Iterate through the words and lemmatize the words using Noun and Verb lemmatizers:
# Lemmatize each word and display the output
for word in input_words:
	output = [word, lemmatizer.lemmatize(word, pos='n'), lemmatizer.lemmatize(word, pos='v')]
	print(formatted_text.format(*output))
  
  
# to execute    python3 lemmetizer.py 
# output

               INPUT WORD         NOUN LEMMATIZER         VERB LEMMATIZER 
 ===========================================================================
                 writing                 writing                   write
                  calves                    calf                   calve
                      be                      be                      be
                 branded                 branded                   brand
                   horse                   horse                   horse
               randomize               randomize               randomize
                possibly                possibly                possibly
               provision               provision               provision
                hospital                hospital                hospital
                    kept                    kept                    keep
                scratchy                scratchy                scratchy
                    code                    code                    code

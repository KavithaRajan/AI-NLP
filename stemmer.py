'''
Working with text has a lot of variations included in it. 

We have to deal with different forms of the same word and enable the computer to understand that these different words
have the same base form. 
For example, the word sing can appear in many forms such as sang, singer, singing, singer, and so on. 
Humans can easily identify these base forms and derive context. When we analyze text, it's useful to extract these base forms. It will enable us to extract useful statistics to analyze the input text. 
Stemming is one way to achieve this. The goal of a stemmer is to reduce words in their different forms into a common base form. It is basically a heuristic process that cuts off the ends of words to extract their base forms. Let's see how
to do it using NLTK.

'''

# Import the following packages:
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

# Define some input words:
input_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize', 'possibly', 'provision', 'hospital', 'kept', 'scratchy', 'code']

# Create objects for Porter, Lancaster, and Snowball stemmers:
# Create various stemmer objects
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

# Create a list of names for table display and format the output text accordingly:
#Create a list of stemmer names for display
stemmer_names = ['PORTER', 'LANCASTER', 'SNOWBALL']
formatted_text = '{:>16}' * (len(stemmer_names) + 1)
print('\n', formatted_text.format('INPUT WORD', *stemmer_names),
'\n', '='*68)

#Iterate through the words and stem them using the three stemmers:
# Stem each word and display the output
for word in input_words:
	output = [word, porter.stem(word), lancaster.stem(word), snowball.stem(word)]
	print(formatted_text.format(*output))



# to execute - python3 stemmer.py
# OUTPUT IS 
$python3 stemmer.py 

       INPUT WORD          PORTER       LANCASTER        SNOWBALL 
 ====================================================================
         writing           write            writ           write
          calves            calv            calv            calv
              be              be              be              be
         branded           brand           brand           brand
           horse            hors            hors            hors
       randomize          random          random          random
        possibly         possibl            poss         possibl
       provision          provis          provid          provis
        hospital          hospit          hospit          hospit
            kept            kept            kept            kept
        scratchy        scratchi        scratchy        scratchi
            code            code             cod            code




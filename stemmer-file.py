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
#input_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize', 'possibly', 'provision', 'hospital', 'kept', 'scratchy', 'code']

#fhand = open('token.txt')
fhand = open('test.txt')
input_words = fhand.read()

# Create objects for Porter, Lancaster, and Snowball stemmers:
# Create various stemmer objects
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

# Create a list of names for table display and format the output text accordingly:
#Create a list of stemmer names for display
stemmer_names = ['PORTER', 'LANCASTER', 'SNOWBALL']
formatted_text = '{:>16}' * (len(stemmer_names) + 1)
print('\n', formatted_text.format('INPUT WORD', *stemmer_names), '\n', '='*68)

#Iterate through the words and stem them using the three stemmers:
# Stem each word and display the output
for word in input_words:
	output = [word, porter.stem(word), lancaster.stem(word), snowball.stem(word)]
	print(formatted_text.format(*output))



# to execute - python3 stemmer-file.py > stem.txt


# OUTPUT IS GIVEN BELOW
stem.txt



       INPUT WORD          PORTER       LANCASTER        SNOWBALL 
 ====================================================================
               '               '               '               '
               w               w               w               w
               r               r               r               r
               i               i               i               i
               t               t               t               t
               i               i               i               i
               n               n               n               n
               g               g               g               g
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               c               c               c               c
               a               a               a               a
               l               l               l               l
               v               v               v               v
               e               e               e               e
               s               s               s               s
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               b               b               b               b
               e               e               e               e
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               b               b               b               b
               r               r               r               r
               a               a               a               a
               n               n               n               n
               d               d               d               d
               e               e               e               e
               d               d               d               d
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               h               h               h               h
               o               o               o               o
               r               r               r               r
               s               s               s               s
               e               e               e               e
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               r               r               r               r
               a               a               a               a
               n               n               n               n
               d               d               d               d
               o               o               o               o
               m               m               m               m
               i               i               i               i
               z               z               z               z
               e               e               e               e
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               p               p               p               p
               o               o               o               o
               s               s               s               s
               s               s               s               s
               i               i               i               i
               b               b               b               b
               l               l               l               l
               y               y               y               y
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               p               p               p               p
               r               r               r               r
               o               o               o               o
               v               v               v               v
               i               i               i               i
               s               s               s               s
               i               i               i               i
               o               o               o               o
               n               n               n               n
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               h               h               h               h
               o               o               o               o
               s               s               s               s
               p               p               p               p
               i               i               i               i
               t               t               t               t
               a               a               a               a
               l               l               l               l
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               k               k               k               k
               e               e               e               e
               p               p               p               p
               t               t               t               t
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               s               s               s               s
               c               c               c               c
               r               r               r               r
               a               a               a               a
               t               t               t               t
               c               c               c               c
               h               h               h               h
               y               y               y               y
               '               '               '               '
               ,               ,               ,               ,
                                                                
               '               '               '               '
               c               c               c               c
               o               o               o               o
               d               d               d               d
               e               e               e               e
               '               '               '               '
               
               
               
               


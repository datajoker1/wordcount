import nltk
import operator
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from collections import defaultdict
import sys
import re

allow_only_word_en = re.compile(r'[^ 0-9|a-z|A-Z]+')

def _nltk_tagger(text):
    tagged_term = []
    tagged = nltk.pos_tag(text)
    tagged_term = [word for word,pos in tagged if pos in ['NN','NNP','NNS','NNPS']]
    #tagged_term = [word for word,pos in tagged]
    
    return tagged_term

if len(sys.argv) == 2:
    try:
        fr = open(sys.argv[1],'r')
        c=fr.read()
        c=c.lower()
        c=re.sub(allow_only_word_en,' ',c)

        tagger = _nltk_tagger(c.split())
        word_freq = defaultdict(int)

        for tag in tagger:
            word_freq[tag]+=1

        sorted_x = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
        fw = open('res_'+sys.argv[1],'w')
        for word, value in sorted_x:
            fw.write(word+": "+str(value)+"\n")
        fw.close()

    except:
        print 'error'

#Using search method to find if the elements inside the list are in a given text

import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print 'Looking for "%s" in "%s" ->' % (pattern, text),

    if re.search(pattern,  text):
        print 'found a match!'
    else:
        print 'no match'
        
#Using search method to find if a word is in a given text
import re

pattern = 'match'
kalajamai = 'Does this text match the pattern?'


if re.search(pattern,  kalajamai):
    print 'found a match!'
else:
    print 'no match'

#https://docs.python.org/2/library/re.html          

import re

#Question 1
print("\n\nQ1.\n")

email = "zuck26@facebook.com"" \
""page33@google.com"" \
""jeff42@amazon.com"
                            #emails converted to byte stream to pass in the below funtion of findall

stripped = re.findall(r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})',email,re.I)
print(stripped)


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 2
print("\n\nQ2.\n")

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
match = re.findall(r'\b\w+',text,re.I)      #ignores case and checks for all strings starting with b
print(match)


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 3
print("\n\nQ3.\n")

sentence = "A, very very; irregular_sentence"
regular = re.split('[;,\s_]+', sentence)            #splits the sentence , removing ,;_ and even blank space
print(' '.join(regular))                            #joins it back after adding blank space


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

#Question 4
print("\n\nQ4.\n")


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+



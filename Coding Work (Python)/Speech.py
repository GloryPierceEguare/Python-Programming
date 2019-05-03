import string

file = open("Output.html", "w")
file.write('<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: yellow; background-color:cyan; border:1px solid black">')

fo = open("Speech.txt", "r")
fo = fo.read()
fo = fo.lower()
count_dict = {}

punct = string.punctuation

for i in punct:
    line = fo.replace(i, '')
fo = fo.split()

#Count for words in dictionary
for word in fo:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

for key,value in count_dict.items():
    file.write('<span style="font-size: {}px"> {} </span>'.format(value * 10, key))

file.write('</div>\
    </body>\
    </html>')

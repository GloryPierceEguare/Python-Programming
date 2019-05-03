fo = open("hnr(2).abc","r")

oneT = 0

lines = []
for line in fo:
    lines.append(line.strip())

ID = ''
Title = ''
Time = ''
Key = ''

for line in lines:

    if line.startswith('X:'):
        ID = "ID: "+line[2:]

    if line.startswith('T:'):
        if oneT == 0:
            Title = "Title: "+line[2:]
            oneT = 1

    if line.startswith('M:'):
        Time = "Time Signature: "+line[2:]

    if line.startswith('K:'):
        Key = "Key Signature: "+line[2:]

        oneT = 0

    if ID != '' and Title != '' and Time != '' and Key != '':
        #print('{{}, {}, {}, {}'.format(ID, Title, Time, Key))

        print( ID + ',' + Title + ',' + Time + ',' + Key)

        ID = ''
        Title = ''
        Time = ''
        Key = ''


#Close opend file
fo.close()


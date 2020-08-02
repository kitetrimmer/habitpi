string = str(input("string = "))
string2 = string.replace('.','')
dot_loc = []
count = 0
for a in range(0,len(string)):
    print(a,string[a],int(a-1))
    if string[a] == '.':
        count += 1
        dot_loc.append(a-count)
print("String = ",string)
print("without dots = ",string2)
print("location of dots = ",dot_loc)

# Desired results:
# String: 1.2.3.4
# string2: 1234
# dot_loc: 0,1,2

# String: 123.4
# string2: 1234
# dot_loc: 3

#Alternate idea (need to test:
index = 0
count = 0
while index < len(string):
    index = text.find('.',index)
    if index == -1:
        break
    count += 1
    dot_loc.append(index-count)

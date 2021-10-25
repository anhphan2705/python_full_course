#slicing = creat a substring by extracting elements from another String
#We can use indexing[] or slice()

#String[start:stop:step] or String[slice(start, stop, step)]
#start index is inclusive
#stop index is exclusive
#step is how much you increased the index by between starting and stopping
#reverse String by passing -1 to step

#For every String, there are 2 index type: negative index and postive index
#Positive index starts from left to right
#Negative index starts from right to left


#Method 1: Indexing[]
name = "Anh Phan"

first_name = name[:3]
print(first_name)

last_name = name[4:]
print(last_name)

funky_name = name[::2]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

#Method 2: slice()
website_gg = "http://google.com"
website_wiki = "http://wikipedia.com"

slice = slice(7, -4)
print(website_gg[slice])
print(website_wiki[slice])



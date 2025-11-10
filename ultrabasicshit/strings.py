text = "mere hi ishaaro pe chalay hai waqt bhi mai hoo Wo khilaadi jisnay sabko maat di hai"
name = "Salman"

print(text.upper()) #all letters to uppercase
print(text.lower()) #all letters to lowercase
print(text.capitalize()) #first letter to uppercase
print(text.title()) #first letter of each word to uppercase
print(text.replace("hai", "tha")) #replace a word with another word
print(text.split(" ")) #split the string into a list of words
print("Length of the text:", len(name)) #length of the string
print("Does the text contain 'Wo khilaadi'?", "Wo khilaadi" in text) #check if a substring is present
print("Index of 'hi(2nd word)':", text.index("hi")) #find the index of a substring
print("Count of 'hai':", text.count("hai")) #count occurrences of a substring
print("a" in name, name.count("a"))
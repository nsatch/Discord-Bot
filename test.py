nameQuote = "Hello there this is a test"
split = nameQuote.split(' ', 1)    #Split the string by white space, but only do once (so we have [name, quote])
name = split[0]
quote = split[1]
print(len(split))
print(name)
print(quote)
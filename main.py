


sentence = "the quick brown fox"
words = sentence.split()
secret = [word[0] for word in words if word != "the"]
print(secret)
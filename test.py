RAW_LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z']



quantity = 5

position = 24


position += quantity

if position >= len(RAW_LETTERS):
    position -= len(RAW_LETTERS)

print(position)
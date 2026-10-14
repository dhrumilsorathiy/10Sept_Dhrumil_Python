description = input("Enter Flipkart product description: ")

words = description.split()

if len(words) > 0:
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Total words:", len(words))
else:
    print("No words found.")
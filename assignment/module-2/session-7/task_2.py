review = """I love using Swiggy.Swiggy delivers food quickly.The food is tasty and Swiggy service is good."""

review = review.lower()
new_review = ""
words = {}
for i in review:
    if i == "." or i =="," or i == "!" or i =="'":
        continue
    new_review +=i 

review_arr = new_review.split()

for i in review_arr:
    if i in words:
        words[i] +=1
    else:
        words[i] = 1
print(words)
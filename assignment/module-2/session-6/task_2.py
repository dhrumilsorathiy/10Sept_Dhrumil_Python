usernames = ["meet", "raj", "yash", "hardik"]
followers = [1200, 2500, 800, 4000]
user_dict = {}
for i in range(len(usernames)):
    user_dict[usernames[i]] = followers[i]
print(user_dict)
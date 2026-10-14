def display_friends(friends):
    for username, followers in friends.items():
        if followers >= 1000:
            print(f"{username}: {followers / 1000:.1f}K followers")
        else:
            print(f"{username}: {followers} followers")


friends = {
    "raj": 2300,
    "meet": 1500,
    "yash": 850
}
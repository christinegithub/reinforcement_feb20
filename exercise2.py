# Pick three names and store them in a list.

# Prompt the user to enter their name.
# If their name is one of the names in the list, display a greeting message that includes their name.
# If their name isn't in the list, display "Who goes there?"

def name_match(user_name, name_list):
    for name in name_list:
        if name == user_name:
            return "Hello, {}".format(name)
    return "Who goes there?"

list = ["Peter", "James", "Leona"]

print("Please enter your name")
user_name = input()
print(name_match(user_name, list))

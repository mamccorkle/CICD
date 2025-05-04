import re








def test_get_valid_name():
    while True:
        # Get the users name from their input:
        name = input("What is your name? ")



        # Check that letters and spaces are what was entered, and it must not be empty:
        if re.fullmatch(r"[A-Za-z ]+", name.strip()):
            return name.strip()
        else:
            print("Invalid name. Please use only letters and spaces.")

# Get the users name:
name = get_valid_name()

# Print their name:
print("Hello, " + name + "!")

print("""What a type of rio's Brazilian people are you?
Cria or Gringo, you're welcome in same way!""")
print(
    """\nAnswer Answer ‘yes’ or ‘no’ pecifically to the questions to find out!
(Only 'yes' or 'no', please)""")

while True:
    behavior = input(
        "\nThe principal activity in your day is to get out of the fireline?? (yes/no) "
    ).lower()
    if behavior == "yes":
        print("OK😎")
        break
    elif behavior == "no":
        print("But fine...🙄")
        break
    else:
        print("\033[31m"
              "\nPlease answer 'yes' or 'no'"
              "\033[0m")
while True:
    attitude = input(
        "\nAnd when the streets are dangerous, you run to your house? (yes/no) "
    ).lower()
    if attitude == "yes":
        print("You're right, but...🤔")
        break
    elif attitude == "no":
        print("Let's Go!😉")
        break
    else:
        print("\033[31m"
              "\nPlease answer 'yes' or 'no'"
              "\033[0m")
while True:
    market = input(
        "\nIf you're hungry or thirsty and hear a food truck announcing exactly what you're looking for, you rush to buy it without a second thought? (yes/no) "
    ).lower()
    if market == "yes":
        print("Hold on!😅")
        break
    elif market == "no":
        print("That’s it, ‘Cria’!🤩")
        break
    else:
        print("\033[31m"
              "\nPlease answer 'yes' or 'no'"
              "\033[0m")

print("\033[33m\n\nLet’s see if you’re ‘Cria’ or ‘Gringo’!\033[0m 😁")
if behavior == "yes":
    print("You have the coolness of a Rio's Cria!")
else:
    print(
        "From a distance we can see that you were not born here... But fine.")
if attitude == "yes":
    print(
        "Protect yourself, you're right, you can run. But here, you won't fly."
    )
else:
    print(
        "Here, we need to work hard. If you beed samething, you have to walk.")
if market == "yes":
    print(
        "But hold on! Don’t appear too eager! Here, you need to be ‘suave’ subtle, and calm."
    )
else:
    print(
        "That’s it, ‘Cria’! You’re already understanding that to navigate around here, you’ve got to be ‘suavão’ really smooth!"
    )
print(
    """'Don’t worry about a thing, ‘cause every little thing’s gonna be alright.’
Rio de Janeiro is not Disney, but the streets have their own magic!""")
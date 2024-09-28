import webbrowser

user_term = input("enter what you want to search").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q="+user_term)


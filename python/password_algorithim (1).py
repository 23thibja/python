
website = input("Input the website name: ")
final_website = website[:4]
mom = input("Input your mother's first name: ")
number = input("Input your mother's house number: ")

if final_website == 'x':
    exit();
else:
    final_websitetwo = final_website;
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in final_website.lower():
        if x in vowels:
            final_websitetwo = final_websitetwo.replace(x,"");
   


print(f"{final_websitetwo}{mom}{number}")





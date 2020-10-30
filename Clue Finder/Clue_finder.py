def clue(key):
    key=key.lower()
    clue={"tessaract":"Congratulations! \nYour next clue is \n4 \np 12\no 20\nb 15\nr 18\nx/-2, 3\nProgram code: 531", "heart":"Congratulations!! \nYour next clue is \n8 7\n3\na 3 c b % ! ^ \n& i P ~ l e t \nG n ` a ! - u \nr f 4 i e a s \na i r s < h i\nb $ e h t T w \n0 i ! % e h g \n7 t y @ L e N\n 0 Program code: 615", "scepter":"Congratulations!!! \nYour next clue is \nekae*\nclc*\nn****\n**** \nProgram code: 725", "orb":"Congratulations!! \nYour next clue is \n****P**E*S**C*\n****E**R***********T*\n Program code: 383", "aether":"Congratulations!!!!! \nYou have found all the clue go to below website to get the code https://bit.ly/2HBupV0", "necklace":"Congratulations!! \nYour next clue is \n3 2\n150 145\n0 141\n164 162\n Program code: 101"}

    if key not in clue:

        print("Sorry try again")

    else:

        print(clue[key])

x = input().strip()

clue(x)

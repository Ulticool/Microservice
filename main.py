import requests

def list_of_posts(id_of_post):
    """Ukaze prispevok staci zadat iba ID prispevku"""
    api_url = f"https://jsonplaceholder.typicode.com/posts/{id_of_post}"
    response = requests.get(api_url)
    json_response = response.json()
    print(json_response)
    response_print = response.status_code
    print(response_print)

def add_post(userID, title, body):
    """Prida prispevok, treba zadat userId, aky chceme title, a body"""
    api_url = "https://jsonplaceholder.typicode.com/posts"
    post = {"userId": userID,"title": title,"body": body}
    response = requests.post(api_url, json=post)
    json_response = response.json()
    print(json_response)
    response_print = response.status_code
    print(response_print)

def put_post(id_of_post, userId, title, body):
    """Tymto modifikujeme konkretny prispevok kde treba zadat id prispevku, ale treba ho modifikovat cely aj userId, title a body"""
    api_url = f"https://jsonplaceholder.typicode.com/post/{id_of_post}"
    put = {"userId": userId, "title": title, "body": body}
    response = requests.put(api_url, json=put)
    print(response.json())

def delete_post(id_of_post):
    """Tymto vymazeme konkretny prispevok"""
    api_url = f"https://jsonplaceholder.typicode.com/post/{id_of_post}"
    delete = requests.delete(api_url)
    print(delete.json)

print(""" /$$      /$$ /$$                                                                        /$$                            /$$$$$$  /$$$$$$$  /$$$$$$
| $$$    /$$$|__/                                                                       |__/                           /$$__  $$| $$__  $$|_  $$_/
| $$$$  /$$$$ /$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$    /$$ /$$  /$$$$$$$  /$$$$$$       | $$  \ $$| $$  \ $$  | $$  
| $$ $$/$$ $$| $$ /$$_____/ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$|  $$  /$$/| $$ /$$_____/ /$$__  $$      | $$$$$$$$| $$$$$$$/  | $$  
| $$  $$$| $$| $$| $$      | $$  \__/| $$  \ $$|  $$$$$$ | $$$$$$$$| $$  \__/ \  $$/$$/ | $$| $$      | $$$$$$$$      | $$__  $$| $$____/   | $$  
| $$\  $ | $$| $$| $$      | $$      | $$  | $$ \____  $$| $$_____/| $$        \  $$$/  | $$| $$      | $$_____/      | $$  | $$| $$        | $$  
| $$ \/  | $$| $$|  $$$$$$$| $$      |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$         \  $/   | $$|  $$$$$$$|  $$$$$$$      | $$  | $$| $$       /$$$$$$
|__/     |__/|__/ \_______/|__/       \______/ |_______/  \_______/|__/          \_/    |__/ \_______/ \_______/      |__/  |__/|__/      |______/
                                                                                                                                                  """)
run = True
while run:
    print("Dobrý deň vitajte v managerovi svojich príspevkov v pripade ukoncenia zadajte (end)")
    command = input("Pre ukazanie prispevku zadajte (list)\n Pre pridanie prispevku zadajte (add) \nPre upravy na prispevku zadajte(modify)\n Pre vymazanie prispevku zadajte (delete):  ")
    if command == "list":
        list_choice = int(input("Pre pouzitie funkcie list_of_posts(id_of_post) musite napisat cislo prispevku :)  "))
        list_of_posts(list_choice)
    elif command == "add":
        add_choice = int(input("Pre pouzitie funkcie add_post(userID, title, body) zadajte najprv userID:  "))
        add_choice2 = input("Potom zadajte text nadpisu:  ")
        add_choice3 = input("A nakoniec text prispevku:   ")
        add_post(add_choice, add_choice2, add_choice3)
    elif command == "modify":
        put_choice = int(input("Pre pouzitie funkcie put_post(id_of_post, userId, title, body ) zadajte najprv cislo prispevku:  "))
        put_choice2 = int(input("Potom zadajte userId:  "))
        put_choice3 = input("Ako predposledne zadajte nazov prispevku:  ")
        put_choice4 = input("Nakoniec zadajte text prispevku:  ")
    elif command == "delete":
        delete_choice = int(input("Pre pouzitie funkcie delete_post(id_of_post) zadajte cislo prispevku:  "))
    elif command == "end":
        run = False
        print(""" /$$$$$$$            /$$                                                      
| $$__  $$          | $$                                                      
| $$  \ $$  /$$$$$$ | $$   /$$ /$$   /$$ /$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$  | $$ |____  $$| $$  /$$/| $$  | $$|__/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$  | $$  /$$$$$$$| $$$$$$/ | $$  | $$ /$$| $$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$  | $$ /$$__  $$| $$_  $$ | $$  | $$| $$| $$_____/| $$ | $$ | $$| $$_____/
| $$$$$$$/|  $$$$$$$| $$ \  $$|  $$$$$$/| $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
|_______/  \_______/|__/  \__/ \______/ | $$ \_______/|__/ |__/ |__/ \_______/
                                   /$$  | $$                                  
                                  |  $$$$$$/                                  
                                   \______/                                   """)
    else:
        run = False
        print("Pri pisani ste pravdepodobne spravili chybu zapnite program znova")


        

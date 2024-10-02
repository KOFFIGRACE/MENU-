shopping_list = []
while True:
    print("\n--- MENU ---")
    print("1. AJOUTER UN ARTICLE")
    print("2. SUPPRIMER UN ARTICLE")
    print("3. AFFICHER LA LISTE DES ARTICLES")
    print("0. RETOURNER / QUITTER")
    choix = input("Entrez un nombre : ")
    if choix == '1': 
        while True:
            article = input("Ajoutez le nom de l'article (ou entrez 0 pour retourner au menu) : ")
            if article == '0':
                break 
            shopping_list.append(article)
            print(f"'{article}' a été ajouté à la liste.")
    elif choix == '2':
        while True:
            article = input("Supprimez le nom de l'article (ou entrez 0 pour retourner au menu) : ")
            if article == '0':
                break 
            if article in shopping_list:
                shopping_list.remove(article)
                print(f"'{article}' a été supprimé de la liste.")
            else:
                print(f"L'article '{article}' n'est pas dans la liste.")
    elif choix == '3': 
        if shopping_list:
            print("Les articles dans la liste sont :")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("La liste est vide.")
        input("Appuyez sur Entrée pour retourner au menu...")
    elif choix == '0': 
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer SVP.")
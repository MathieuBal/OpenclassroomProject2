import book_info_scrap

def main ():
    print("début d'application")
    print("récupération informations des livres")
    book_info_scrap.get_book_info()
    print("informations récupérées")
    print("création d'un fichier csv ")
    book_info_scrap.write_csv_file()
    print("fichier csv créé avec succès")
    print("fin d'application")



if __name__ == "__main__":
    # execute only if run as a script
    main()
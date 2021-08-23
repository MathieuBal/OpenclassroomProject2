"""programme analyse et extractions des information des livres disponibles sur le site booktoscrap"""
import scrap_book_urls
import book_info_scrap
import category_url_scrap


def main():
    print("*****    début d'application    *****")
    print("*****    scrap category urls    *****")
    print("*****       chargement          *****")
    category_url_scrap.get_category_urls()
    print("*****    liens récupérés        *****")
    print("*****  création de fichier csv  *****")
    print("*****       chargement          *****")
    category_url_scrap.write_csv_category_urls_file()
    print("*****    fichier csv créé       *****")
    print("***** scrap des liens des books *****")
    print("*****       chargement          *****")
    scrap_book_urls.get_books_links()
    print("*****    liens récupérés        *****")
    print("*****  création de fichier csv  *****")
    print("*****       chargement          *****")
    scrap_book_urls.write_csv_books_urls_file()
    print("*****    fichier csv créé       *****")
    print("*****  début du scrap des books *****")
    print("*****       chargement          *****")
    book_info_scrap.get_book_info()
    print("*****    infos récupérés        *****")
    print("*****  création de fichier csv  *****")
    print("*****       chargement          *****")
    book_info_scrap.write_csv_books_infos_file()
    print("*****    fichier csv créé       *****")


if __name__ == "__main__":
    # execute only if run as a script
    main()

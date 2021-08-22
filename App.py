"""programme analyse et extractions des information des livres disponibles sur le site booktoscrap"""
import category_url_scrap
import scrap_book_urls



def main():
    print("*****    début d'application    *****")
    print("***** scrap des liens des books *****")
    scrap_book_urls.get_books_links()
    print("*****    liens récupérés        *****")
    print("*****  création de fichier csv  *****")
    scrap_book_urls.write_csv_books_urls_file()
    print("*****    fichier csv créé       *****")


if __name__ == "__main__":
    # execute only if run as a script
    main()

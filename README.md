Extract pricing informations from other online bookstores

## Objective of the project

Books Online is a large online bookstore specializing in used books. She needs a on-demand executable application to 
retrieve book prices from Book to Scrape, a book reseller online.

## Specifications

3 scripts necessary: 
* A python script with specific url product page, for extracting above information above. Exporting these informations 
with above title in a CSV file.
    *  product_page_url
    * universal_ product_code (upc)
    * title
    * price_including_tax
    * price_excluding_tax
    * number_available
    * product_description
    * category
    * review_rating
    * image_url
    
* A python script with specific category, for extracting url product page of each product in these category. Use the
first script to extract all books data of these category, in a CSV file.

* A python script for extracting all categories of Books to scrape site, and use the second script for extracting in
separate category CSV file, all books data. Download and store the image file of each product.


## Deliverables

* A link to a GitHub repository which should contain the following:
    * all of your application code;
    * the requirements.txt file, but not the virtual environment itself;
    * a README.md file explaining how to create and activate the virtual environment, then run the application code;
The extracted data/images should not be part of the repository itself.
A compressed file containing all the extracted data and associated images in an easy to follow format or structure.


## Constraints
* code in a GitHub repository and perform regular commits with clear commit messages.
* save a requirements.txt file without saving virtual environment in the repository itself. 
* not need to save CSV files there. 
* send a link to GitHub repository and a compressed file of the data it generates. 
* write a README.md file explain running the code and producing data, add it to the repository.


## Install

Virtual environment Linux/macOS
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate

Warning ! this program has been optimized on linux, it may encounter problems on microsoft.

Virtual environment Windows
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate

Install the libraries
pip install -r requirements.txt

## Run application
 
python3 App.py

## Test
 


## Platforms

This application was testing on
* Ubuntu 18.10 + python 3.8

import requests
from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('amazon20.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div',
                     class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-include-content-margin puis puis-v3b48cl1js792724v4d69zlbwph s-latency-cf-section s-card-border')

# Initialize lists to store extracted data
names = []
prices = []
reviews = []
ratings = []
product_details = []

# Iterate through each div and extract the desired information
for div in divs:
    # Extract Name
    name_span = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    names.append(name_span.get_text() if name_span else '')

    # Extract Price
    price_span = div.find('span', class_='a-price-whole')
    prices.append(price_span.get_text() if price_span else '')

    # Extract Reviews
    review_span = div.find('span', class_='a-size-base puis-normal-weight-text')
    reviews.append(review_span.get_text() if review_span else '')

    # Extract Ratings
    rating_span = div.find('span', id='acrCustomerReviewText', class_='a-size-base')
    ratings.append(rating_span.get_text() if rating_span else '')

    # Extract Product Details
    product_details_span = div.find('span', class_='a-list-item')
    product_details.append(product_details_span.get_text() if product_details_span else '')

# Write the extracted data to a CSV file
csv_filename = 'amazon_products20.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Price', 'Reviews', 'Ratings', 'Product Details'])

    for name, price, review, rating, details in zip(names, prices, reviews, ratings, product_details):
        csv_writer.writerow([name, price, review, rating, details])

print(f'Data has been written to {csv_filename}')

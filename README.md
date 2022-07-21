Scrape Corgi Things

This project implies a web scraper that is used for retrieving all the products from an e-commerce website, with their
name, price, number of reviews and representative image.

All these fields will be stored in a NOsql database (MongoDB) in a json format, with the remark that the database will
store only the link to the image.

The .jpg images will be downloaded and automatically uploaded in a S3 bucket in AWS.
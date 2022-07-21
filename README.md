# Scrape Corgi Things

This project implies a web scraper that is used for retrieving all the products from an e-commerce website, with their
name, price, number of reviews and representative image.

All these fields will be stored in a NOsql database (MongoDB) in a json format, with the remark that the database will
store only the link to the image.

![image](https://user-images.githubusercontent.com/93611644/180319595-cd2e3d59-1617-429d-bdff-c2ebe153f899.png)

The .jpg images will be downloaded and automatically uploaded in a S3 bucket in AWS.

![image](https://user-images.githubusercontent.com/93611644/180319781-ce460456-800a-468d-afa9-254c55af7d22.png)

This can be achieved by running to the corgi_things folder and running <code>scrapy crawl corgi</code>

# Basic Scraper Application

This is a simple Python application designed for web scraping. It allows you to extract data from web pages based on specified criteria.

## Features

- **Easy-to-Use**: Simple interface for initiating scraping tasks.
- **Customizable**: Ability to specify target URLs and data extraction criteria.
- **Modular Design**: Easily extendable for additional functionality.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RofferTorres/Scraper.git
2. Navigate into the project directory:

   ```bash
   cd Scraper
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
## Usage
1. Define your scraping logic into 'mysite/myapp/views.py' file.
2. Run the application:

   ```bash
   cd ./Scraper/mysite && python manage.py runserver
3. Open you browser and go to 'http://localhost:8000/'
4. Insert your target URL.
5. The scraped data will be temporary saved inside the local datamodel and displayed into a table.
   
## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/RofferTorres/Scraper/blob/main/LICENSE) file for details.


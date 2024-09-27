# IMDb Top Movies Scraper

This Python project scrapes the top 5 movies and their IMDb links for each year from 2000 to 2024. The data is extracted from IMDb's website and saved into a text file.

## Features

- Scrapes top 5 movies for each year between 2000 and 2024 from IMDb.
- Extracts movie titles and links.
- Saves the data into a text file (`data.txt`).
- Handles HTTP errors gracefully and includes a delay to prevent overwhelming the server.

## Requirements

Before running the scraper, you need to install the following Python libraries:

- `BeautifulSoup4`
- `urllib`
- `fake_useragent` (optional)

You can install the required libraries with the following command:

```bash
pip install beautifulsoup4 fake-useragent
```

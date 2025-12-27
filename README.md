# Movie Success Predictor 🎬

### Overview
This project is an end-to-end data analysis pipeline that visualizes the relationship between **movie release years** and **box office revenue**.
It automatically scrapes the "List of Highest-Grossing Films" from Wikipedia, cleans the messy raw data (removing footnotes, currency symbols, and text glitches), and plots the results on a scatter plot. This tool helps analysts visualize how blockbuster revenue has exploded over recent decades.

### Features
* **Automated Web Scraping:** Fetches and parses raw HTML tables from Wikipedia using `BeautifulSoup`.
* **Advanced Data Cleaning:** Uses **Regex** to strip hidden characters, currency symbols, and footnotes (e.g., `[1]`) from financial data.
* **Outlier Detection & Removal:** Automatically identifies and filters out data glitches (like the "Fate of the Furious" parsing error) to ensure statistical accuracy.
* **Data Visualization:** Generates a professional Matplotlib scatter plot to reveal trends in cinema history.

### Tech Stack
* **Python 3.x**
* **Requests:** HTTP requests to fetch the Wikipedia page.
* **BeautifulSoup4 (bs4):** Parsing HTML tables and extracting text.
* **Pandas:** Dataframe manipulation, type conversion, and filtering.
* **Matplotlib:** Generating the Year vs. Revenue scatter plot.

## How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/python-movie-scraper.git](https://github.com/YOUR_USERNAME/python-movie-scraper.git)
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the dashboard:**
    ```bash
    python movie_project.py
    ```

## Sample Output

The script generates a visualization window showing:
* **Green Dots:** Individual movies plotted by Release Year (X-axis) and Revenue (Y-axis).
* **Trend Visualization:** Visual confirmation of "recency bias," with the majority of multi-billion dollar blockbusters clustering after 2010.
* **Console Output:** Execution logs verifying that 50 films were scraped and that data anomalies (like the ~$81B glitch) were successfully filtered out.

---
*Created as part of a Data Science portfolio project.*

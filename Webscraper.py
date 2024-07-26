def Agent(url, filename):
    '''
    Saves the html file from the url and saves it
    Prints success or error message based on the retrieval status
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = req.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.content.decode('utf-8'))
        print(f"HTML content from {url} saved to {filename} successfully.")
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

def prettify_html(filename):
    '''
    Reads the HTML file and returns a BeautifulSoup object for parsing the HTML content.
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return soup  #Return the BeautifulSoup object

def shorten_text(text):
    '''
    Shortens the Information by removing content from Countries_output.txt
    '''
    shortened_text = text.split(' (')[0] #shortens info
    return shortened_text.strip() #returns the info


def country_info(soup, filename):
    '''
    Extracts and formats country information from an HTML table.
    Writes the function to a formatted country information to the specified file.
    '''
    table = soup.find('table')  #Assuming the data is within a <table> element
    if table:
        with open(filename, 'w', encoding='utf-8') as file:
            rows = table.find_all('tr') #finds all tr data
            for row in rows:
                columns = row.find_all(['th', 'td'])  #Find all the th and td data
                if columns:
                    for col in columns:
                        cleaned_text = shorten_text(col.text.strip())
                        file.write(f"{cleaned_text:<30} ")  #Write each column's text, stripped and formatted
                    file.write("\n")  #Move to the next line after writing all columns for a row
    else:
        print("No table found in the HTML.")



url = "https://de.wikipedia.org/wiki/Liste_der_Staaten_der_Erde"
filename = "output.html"
Agent(url, filename)

soup = prettify_html(filename)
country_info(soup, "Countries_output.txt")


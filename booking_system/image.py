import requests
from bs4 import BeautifulSoup
from movie.models import MovieTickets

def update_image_urls():
    movie_tickets = MovieTickets.objects.all()

    for ticket in movie_tickets:
        movie_name = ticket.movie_name
        image_url = get_image_url_from_movie_name(movie_name)

        # Update the image_url field in the database
        ticket.image_url = image_url
        ticket.save()

def get_image_url_from_movie_name(movie_name):
    # Construct a search URL or query based on the movie name
    search_url = f'https://example.com/search?q={movie_name.replace(" ", "+")}'

    # Send an HTTP request to the search URL
    response = requests.get(search_url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the image URL from the page (this depends on the specific website structure)
    image_url = extract_image_url(soup)

    return image_url

def extract_image_url(soup):
    # Example: Assuming the image URL is inside an <img> tag with the 'src' attribute
    img_tag = soup.find('img', {'class': 'movie-poster'})  # Replace with the actual HTML structure

    if img_tag:
        # Get the 'src' attribute of the <img> tag
        image_url = img_tag.get('src')

        if image_url:
            return image_url

    # If no image URL is found, return None or an appropriate default value
    return None

# Call the function to update the database with image URLs
update_image_urls()

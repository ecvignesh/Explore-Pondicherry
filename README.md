Explore Pondicherry - Tourism Web App

A comprehensive tourism web application designed to showcase the best places to visit in Pondicherry, with a feature for booking tours and managing accounts. This project is built using Django, Python, PostgreSQL, and Docker.

Features                                                                                                                          
    Tourist Booking System: Allows users to book tours to various places around Pondicherry.
    Place Listings: Provides detailed information about popular tourist spots such as beaches, temples, churches, and more.
    Account Management: User registration, login, and profile management features.
    Responsive Design: Optimized for both desktop and mobile views.
    Search Functionality: Search places based on categories (e.g., beaches, temples, markets).

Technologies Used      
    Frontend: HTML, CSS, Bootstrap
    Backend: Python, Django
    Database: PostgreSQL
    Containerization: Docker, Docker Compose
    Version Control: Git, GitHub

 
Installation
Clone the Repository

git clone https://github.com/your-username/Explore-Pondicherry.git
cd Explore-Pondicherry

Set Up the Virtual Environment

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Set Up the Database

Make sure PostgreSQL is installed and running. Configure the database connection in pondicherry_tourism/settings.py with your PostgreSQL credentials.

Run the following commands to set up the database:

python manage.py migrate

Create a Superuser

Create a Django superuser to access the admin panel:

python manage.py createsuperuser

Run the Application

To start the development server:

python manage.py runserver

The app will be available at http://127.0.0.1:8000.
Docker Setup (Optional)

You can also run the project with Docker for easy setup.
Build the Docker Containers

docker-compose build

Start the Docker Containers

docker-compose up


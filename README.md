# gavaconnect
# Government Projects and Citizen Engagement Web App

This Django-based web application serves as a platform for government entities to post various projects, citizens to comment on these projects, report issues in their area, and students to apply for bursaries. Additionally, it facilitates a system for trash transportation, managed by Uber.

## Features

- **Government Projects**: Government officials can log in and post details about various projects, including descriptions, locations, budgets, and timelines.

- **Citizen Engagement**: Citizens can create accounts, browse through government projects, and leave comments or feedback. They can also report issues in their area, such as infrastructure problems or public service issues.

- **Student Bursary Application**: Students can register on the platform and apply for bursaries provided by the government. They can submit necessary documents and track the status of their applications.

- **Trash Transportation System**: Uber drivers registered on the platform can receive requests to transport trash from designated locations to disposal sites. Citizens can request trash pickup through the app, and drivers can accept these requests based on their availability.

## Technologies Used

- **Django**: Python-based web framework used for backend development.
- **Django REST Framework**: To create RESTful APIs for frontend communication.
- **HTML/CSS/JavaScript**: Frontend development technologies for user interface and interactivity.
- **Bootstrap**: Frontend framework for responsive and mobile-first design.
- **PostgreSQL**: Database management system for storing project, user, and application data.
- **OAuth2**: Authentication mechanism for government officials, citizens, students, and drivers.
- **Google Maps API**: Integration for location-based services and mapping functionalities.
- **Uber API**: Integration for trash transportation service.

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/ignatiusratemo26/gavaconnect.git
Use the foolwing code to set up
cd gavaconnect

#Setup the database
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Access the application in your web browser at http://localhost:8000.

## Contribution
Ignatius Ratemo - ignatiusratemo26@gmail.com
Linet Gitonga - linetgitonga55@gmail.com

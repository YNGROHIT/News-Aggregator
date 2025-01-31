News Aggregator with AI-Powered Topic Classification
This project is a news aggregator platform that collects and curates news articles from various sources. It leverages AI-powered topic classification to categorize news articles based on their content and provides users with a personalized experience.

Features:
Custom User Authentication: A custom user model with registration, login, and logout functionality.
AI-Powered Topic Classification: Automatically classifies news articles into topics using machine learning.
News Aggregation: Aggregates news from multiple sources, ensuring fresh and relevant content.
Fact-Checking: Integrates with the GROK API for automatic fact-checking of news articles.
User-friendly Interface: A clean, responsive design to enhance user experience.
Technologies Used:
Django: Backend framework for building the web application.
Python: Primary language for backend development and machine learning integration.
HTML/CSS/JavaScript: Frontend technologies for building the user interface.
AI & ML: Used for topic classification of news articles.
Setup:
To run the project locally, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/news-aggregator.git
cd news-aggregator
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (if needed):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Contribution:
Feel free to fork this repository and submit pull requests. Contributions are welcome!

# Mini Games Website

A Django-based web application featuring various mini games that users can play online.

## Features

- **Multiple Mini Games**: Collection of browser-based games
- **User Authentication**: Register, login, and track your progress
- **Responsive Design**: Works on desktop and mobile devices
- **Score Tracking**: Keep track of your best scores

## Games Included

- Tic Tac Toe (coming soon)
- More games to be added!

## Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development)
- **Styling**: Bootstrap 5 + Custom CSS

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd MiniGame
```

2. Create a virtual environment:
```bash
python -m venv minigame
```

3. Activate virtual environment:
```bash
# Windows
minigame\Scripts\activate

# macOS/Linux
source minigame/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser (optional):
```bash
python manage.py createsuperuser
```

7. Start development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the website.

## Project Structure

```
MiniGame/
├── accounts/          # User authentication app
├── games/            # Games app
├── templates/        # HTML templates
├── static/          # CSS, JS, images
├── minigames_website/  # Main project settings
├── manage.py
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source and available under the MIT License.
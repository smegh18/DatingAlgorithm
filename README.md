# Dating App Project

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Running the Backend](#running-the-backend)
  - [Running the Frontend](#running-the-frontend)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview
This project is a dating app with two primary components:

- **Backend:** Built using Flask and SQLAlchemy, this part handles user registration, storing user data, finding matches, and reacting to matches.
- **Frontend:** Built using Flutter, the frontend communicates with the backend, allowing users to register, view potential matches, and react to them.

The backend supports a REST API for user registration, finding matches, and reacting to matches, while the frontend provides an interactive interface for users.

---

## Technologies

### Backend:
- **Flask:** Python web framework for API development.
- **SQLAlchemy:** ORM for interacting with the database.
- **SQLite:** Database (can be replaced with any other database).
- **Python 3.x:** Programming language used to build the backend.

### Frontend:
- **Flutter:** Framework for building mobile applications.
- **Dart:** Programming language used for Flutter development.
- **HTTP:** Flutter package used to make API calls.

---

## Folder Structure

### Backend Folder Structure (`dating_app_backend`)
```
/dating_app_backend
│
├── app.py                     # Main entry point for the Flask app
├── models.py                  # Database models for users and matches
├── create_db.py               # Script to initialize and create the database
├── utils.py                   # Helper functions for match recommendations and data processing
└── requirements.txt           # Required Python dependencies
```
- **`app.py:`** Contains the Flask routes for the backend API such as `/add_user`, `/find_matches`, and `/react_to_match`.
- **`models.py:`** Defines the SQLAlchemy models for user profiles and other necessary entities.
- **`create_db.py:`** Script to initialize the SQLite database and create tables.
- **`utils.py:`** Contains helper functions like those for the recommendation system.
- **`requirements.txt:`** Lists the Python dependencies needed for the project.

### Frontend Folder Structure (`dating_app_frontend`)
```
/dating_app_frontend
│
├── lib/
│   ├── main.dart                # Entry point with user registration screen
│   ├── match_screen.dart        # Screen to show and react to matches
│   ├── reactions.dart           # Reactions handling (like/dislike)
│   └── network.dart             # Network handling for better API integration
│
├── pubspec.yaml                 # Flutter project dependencies
└── assets/
    └── images/                  # Image assets (if needed)
```
- **`main.dart:`** Entry point of the Flutter app. Contains the user registration screen and initializes the app.
- **`match_screen.dart:`** Displays a list of potential matches for the user and provides the interface to react with likes/dislikes.
- **`reactions.dart:`** Handles the reactions (like/dislike) for each match.
- **`network.dart:`** Centralizes network-related logic to handle API calls more efficiently.
- **`pubspec.yaml:`** Specifies the dependencies required for the Flutter app.
- **`assets/images/`**: Folder for storing image assets (e.g., logos, icons).

---

## Setup Instructions

### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/dating-app.git
cd dating-app
```

### Install Dependencies

#### Backend
To install the backend dependencies, navigate to the `dating_app_backend` directory and install the required Python packages:
```bash
cd dating_app_backend
pip install -r requirements.txt
```

#### Frontend
To install the frontend dependencies, navigate to the `dating_app_frontend` directory and install the required Flutter packages:
```bash
cd dating_app_frontend
flutter pub get
```

### Running the Backend
Navigate to the `dating_app_backend` directory and run the Flask app:
```bash
python app.py
```
This will start the backend server at `http://127.0.0.1:5000/`.

### Running the Frontend
Navigate to the `dating_app_frontend` directory and run the Flutter app:
```bash
flutter run
```
The Flutter app should now be running on your emulator or device, and it will communicate with the backend at `http://127.0.0.1:5000/`.

---

## API Endpoints

### POST `/add_user`
**Description:** Adds a new user to the system.

**Request Body:**
```json
{
    "name": "John Doe",
    "interests": "Reading, Traveling",
    "affiliations": "University A",
    "demographics": {"age": 25, "gender": "Male", "location": "City A"}
}
```
**Response:**
```json
{
    "user_id": 1
}
```

### POST `/find_matches`
**Description:** Finds users that match the specified user based on interests.

**Request Body:**
```json
{
    "user_id": 1
}
```
**Response:**
```json
[
    "Jane Smith",
    "Michael Brown"
]
```

### POST `/react_to_match`
**Description:** Allows a user to react to a match with a "like" or "dislike".

**Request Body:**
```json
{
    "user_id": 1,
    "match_id": 2,
    "reaction": "like"
}
```
**Response:**
```json
{
    "message": "Reaction recorded"
}
```

---

## Contributing
We welcome contributions! If you would like to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

Make sure your code follows the style of the project, and include tests for any new functionality.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.


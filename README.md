# Finance Tracker App

What started as a curious dive into full-stack development turned into one of the most rewarding projects I've ever worked on. I wanted to build something useful—something that could solve a problem I personally faced: tracking my finances in a simple and intuitive way.

During this journey, I learned how to connect a FastAPI backend with a React frontend, build and structure endpoints, handle a database using SQLAlchemy, and bring it all together with a clean UI using Bootstrap. The sense of accomplishment I got from seeing my first transaction pop up on the table was amazing.

This project helped me bridge the gap between backend and frontend development, making me more confident in full-stack work. And honestly, I had a lot of fun doing it.

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* React
* Axios
* Bootstrap

---

## Features

* Add financial transactions (income or expenses)
* View all transactions in a table
* Bootstrap styling for a simple UI
* FastAPI endpoints for data handling
* SQLite database for persistence

---

## Screenshots

Below is a screenshot of the Finance Tracker App running locally:

https://github.com/Jack-khalif/Finance-Tracker-App/blob/main/Finance%20tracker1.png
---

## Installation

### Backend (FastAPI)

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/finance-tracker.git
   cd finance-tracker/backend
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Start the FastAPI server**

   ```bash
   uvicorn main:app --reload
   ```

### Frontend (React)

1. **Go to frontend folder**

   ```bash
   cd ../frontend
   ```

2. **Install dependencies and start React app**

   ```bash
   npm install
   npm start
   ```

> Make sure your FastAPI server is running on `http://127.0.0.1:8000` and React is set to connect to it in `api.js`.

---

## API Endpoints

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| POST   | `/transactions/` | Add a new transaction  |
| GET    | `/transactions/` | Fetch all transactions |

---

## Folder Structure

```
finance-tracker/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── api.js
│   └── public/
│       └── index.html
```

---

## Future Improvements

* User authentication
* Edit/Delete transactions
* Data visualization (charts, graphs)
* Deploy to a cloud service (e.g., Vercel + Render)

---

## License

MIT License

---

## Author

Built with Khalif

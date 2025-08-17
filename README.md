# 🚀 DevConnector GraphQL API

A full-featured GraphQL backend built with FastAPI and Strawberry for managing developer profiles, skills, and connections. This project demonstrates real-world GraphQL usage with modular architecture, SQLAlchemy ORM, and clean resolver logic.

## 📦 Tech Stack

- **FastAPI** – High-performance Python web framework
- **Strawberry GraphQL** – Modern GraphQL library for Python
- **SQLAlchemy** – ORM for database interactions
- **SQLite** – Lightweight database for development
- **Pydantic** – Data validation

## 🧩 Features

- Create, update, and delete developer profiles
- Register new users
- Query all developers or filter by skills
- Authenticate users on updation and deletion of profiles
- Nested Queries for skills and connections
- Modular architecture with resolvers and services
- GraphQL endpoint with Strawberry integration

## 📁 Project Structure
devconnector/<br>
├── app/<br>
│   ├── main.py<br> 
│   ├── schema.py<br>
│   ├── resolvers/<br>
│   ├── db/<br>
│   ├── services/<br>
│   └── types/<br>
└── devconnectors.db<br>
├── requirements.txt<br>
└── README.md<br>

## 🚀 Getting Started
1. **Clone the repository:**
   ```bash
   git clone
2. **Navigate to the project directory:**
   ```bash
   cd GraphQL_tutorial
   ```
3. **Install dependencies:**
   ```bash 
    pip install -r requirements.txt
    ```
4. **Setup database:**
   ```bash
   python -m app.db.init_db
   ```
5. **Run the application:**
   ```bash 
    uvicorn app.main:app --reload
    ```
6. **Access the GraphQL playground:**
   Open your browser and go to `http://localhost:8000/graphql`
7. **Explore the API:**
   Use the GraphQL playground to test queries and mutations.

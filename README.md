# Brevet Time REST API

A REST API that provides brevet control opening and closing times stored in MongoDB. Users can request data in either JSON or CSV format.

---

## Table of Contents

- Features
- How It Works
- Why I Built It
- Technology Used
- Installation
- API Endpoints
- Usage
- Future Improvements

---

## Features

- REST API built with Flask
- MongoDB database
- JSON and CSV responses
- Query parameter support
- Docker deployment

---

## How It Works

1. Brevet control times are stored in MongoDB.
2. The Flask API retrieves requested data.
3. Results are returned in JSON or CSV.
4. Users can limit results using query parameters.

---

## Why I Built It

This project helped me learn how to design REST APIs, work with databases, and build backend applications using Flask.

---

## Technology Used

### Backend
- Python
- Flask

### Database
- MongoDB

### Tools
- Docker
- Git

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/brevet-time-api.git
cd brevet-time-api
docker compose up --build
```

---

## API Endpoints

- `/listAll`
- `/listOpenOnly`
- `/listCloseOnly`

Available formats:

- JSON
- CSV

---

## Usage

Run the application and access the API using the available endpoints.

---

## Future Improvements

- Better frontend
- API documentation
- Authentication
- Additional filtering

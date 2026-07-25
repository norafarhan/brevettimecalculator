# Brevet Time Calculator REST API

A RESTful API built with Flask and MongoDB that provides brevet control opening and closing times through multiple endpoints. The API supports both JSON and CSV responses, allowing users to retrieve all control times or filter results by open and close times.

---

## Table of Contents

- Features
- How It Works
- Why I Built It
- Tech Stack
- Installation
- API Endpoints
- Usage
- Future Improvements

---

## Features

- REST API built with Flask and Flask-RESTful
- Stores brevet control times in MongoDB
- Returns data in both JSON and CSV formats
- Supports filtering with a `top` query parameter
- Interactive PHP frontend for viewing API results

---

## How It Works

1. Brevet control data is stored in a MongoDB database.
2. The Flask API retrieves the requested data.
3. Users can request:
   - All control times
   - Open times only
   - Close times only
4. Responses can be returned as either JSON or CSV.
5. Results can optionally be limited using the `top` query parameter.

---

## Why I Built It

This project was developed to strengthen my understanding of RESTful API development, database integration, and backend software engineering. It provided experience designing API endpoints, interacting with MongoDB, and exposing data in multiple formats for client applications.

---

## Tech Stack

### Backend
- Python
- Flask
- Flask-RESTful

### Database
- MongoDB

### Frontend
- PHP
- HTML

### Tools
- Docker
- Docker Compose
- Git

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/brevet-time-api.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
docker-compose up --build
```

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/listAll` | Returns all open and close times |
| `/listOpenOnly` | Returns only open times |
| `/listCloseOnly` | Returns only close times |

### Available Formats

Append either:

- `/json`
- `/csv`

Example:

```text
/listAll/json
/listOpenOnly/csv
```

### Query Parameters

Limit results using:

```text
?top=5
```

Example:

```text
/listOpenOnly/json?top=3
```

---

## Usage

After starting the application:

- REST API: `http://localhost:5050`
- Web Interface: `http://localhost:5002`

Use the web interface or send requests directly to the API endpoints.

---

## Future Improvements

- Interactive API documentation with Swagger/OpenAPI
- Authentication and authorization
- Additional filtering and sorting options
- Pagination support
- Improved frontend interface

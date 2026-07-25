# Brevet Time Calculator REST API

**Author:** Nora Farhan  
**Email:** noraf@uoregon.edu

## Overview
REST API service that exposes brevet control times stored in MongoDB.

## Endpoints

- `GET /listAll` — returns all open and close times (JSON default)
- `GET /listOpenOnly` — returns open times only
- `GET /listCloseOnly` — returns close times only

## Formats
Append `/json` or `/csv` to any endpoint:
- `GET /listAll/json`
- `GET /listAll/csv`

## Query Parameter
Append `?top=k` to get the top k results in ascending order:
- `GET /listOpenOnly/json?top=3`
- `GET /listCloseOnly/csv?top=2`

## How to Run
docker-compose up --build

- REST API available at: http://localhost:5050
- Website available at: http://localhost:5002

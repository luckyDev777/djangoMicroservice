# Django Microservices Application

A Django microservices application that includes user, post, and notification services with an API Gateway for routing requests. The application uses Kafka for communication between services.

## Basic Features

- **User Service**: Handles user registration and authentication.
- **Post Service**: Allows users to create and manage posts.
- **Notification Service**: Sends notifications based on post creation events.
- **API Gateway**: Routes requests to the appropriate microservice.
- **Kafka**: Used for inter-service communication.

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Setup Instructions

1. **Clone the repository**

```bash
git clone git@github.com:luckyDev777/djangoMicroservice.git
cd django-microservices
```

2. Run the following commands with Makefile to setup.

```
$ make up # to compose up
$ make down # to compose down
```

2. or with docker commands

```
$ docker-compose up # to compose up
$ docker-compose down # to compose down
```

3. user-service => go to http://localhost:8001/users/ 
4. posts_service => go to http://localhost:8002/posts/ 
5. notification_service => go to http://localhost:8003/notifications/ 
6. Kafdrop => Open a browser and go to http://localhost:9000/ (Kafka web UI for monitoring)
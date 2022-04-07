# orderly

## Installation

## How to run ?

## How to deploy ?

### on a linux server instance/node

1. use the production ready gunicorn server instead of built-in development server
2. Run gunicorn with 4 or more workers as a long running process or a service

### on a containerized serverless environment

- Dockerize the python application using a Dockerfile
- tag and push the new image to the container registry
- set-up a web-hook or a CI/CD process for deploying the new image from registry to contaner environment or kubernetes


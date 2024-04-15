---
date: 2024-04-15T19:17:35.248054
author: AutoGPT <info@agpt.co>
---

# QR Code Generator API

Based on the information gathered from the interviews, the task involves creating an endpoint that fulfills the following requirements: - Accepts input data which can vary from URLs, text, contact information, etc. This signifies the endpoint needs to be flexible enough to encode different types of data into a QR code. - Generates a QR code image from the input data. This process will involve converting the supplied data into a format that can be encoded into a QR code image. - Allows for customization of the generated QR code. This includes adjustments to the size, color, and error correction level. Each of these customizations serves a purpose; size ensures the QR code fits within various designs, color alignment with brand guidelines, and error correction level for maintaining scannability under damage or obstruction. - Returns the QR code image in a specified format as requested by the user, for example in SVG format. This demands the system to be capable of generating and providing the QR code in multiple image formats to meet diverse user preferences or requirements. The tech stack selected for implementing this solution includes Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the ORM. This stack is suitable for creating a performant, scalable, and maintainable application capable of handling the specified functionalities efficiently.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'QR Code Generator API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow

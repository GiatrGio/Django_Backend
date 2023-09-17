# Django Back-end Engineering Assessment

Create a back-end infrastructure that stores and exposes specific data provided by the Ontology Lookup Service repository https://www.ebi.ac.uk/ols/index

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Examples](#examples)
- [Testing](#testing)
    - [Unit Tests](#unit-tests)
    - [Integration Tests](#integration-tests)

## Overview

Create a Django Rest API that stores and exposes EFO terms, EFO term synonyms and EFO term ontology information.
Main technologies used are Django, Django Rest Framework, PostgreSQL, Docker.

## Getting Started

### Prerequisites

Following technologies should be installed locally before you can use your project.

- Python 3.x
- Docker

### Installation

Step-by-step instructions for setting up the project locally.

```bash
# Get the later Postgres docker image
docker pull postgres

# Initialize a Postgres docker container
docker run --name myPostgresContainer -e POSTGRES_USER=myUsername -e POSTGRES_PASSWORD=mySecretPassword -e POSTGRES_DB=EfoDB -p 5432:5432 -d postgres

# Clone the repository
git clone https://github.com/GiatrGio/Django_Backend.git

# Change directory
cd Django_Backend

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### Configuration
API connection to the database is configured in the settings.py file. You can change the database name, user, password and url there.

Pagination is configured in the settings.py file. You can change the default page size and the maximum page size there.


## Usage

### Endpoints

The API exposes the following endpoints:

- EFOTerm Endpoints: Access it at http://localhost:8000/api/efo-terms/
- - List all EFO terms: GET http://localhost:8000/api/efo-terms/
- - Create a new EFO term: POST http://localhost:8000/api/efo-terms/
- - Retrieve, update, or delete a specific EFO term by ID:
- - - GET http://localhost:8000/api/efo-terms/{id}/
- - - PUT http://localhost:8000/api/efo-terms/{id}/
- - - DELETE http://localhost:8000/api/efo-terms/{id}/


- EFOTermSynonym Endpoints: Access it at http://localhost:8000/api/efo-term-synonyms/
- - List all EFO term synonyms: GET http://localhost:8000/api/efo-term-synonyms/
- - Create a new EFO term synonym: POST http://localhost:8000/api/efo-term-synonyms/
- - Retrieve, update, or delete a specific EFO term synonym by ID:
- - - GET http://localhost:8000/api/efo-term-synonyms/{id}/
- - - PUT http://localhost:8000/api/efo-term-synonyms/{id}/
- - - DELETE http://localhost:8000/api/efo-term-synonyms/{id}/


- EFOTermOntology Endpoints: Access it at http://localhost:8000/api/efo-term-ontologies/
- - List all EFO term ontology relationships: GET http://localhost:8000/api/efo-term-ontology/
- - Create a new EFO term ontology relationship: POST http://localhost:8000/api/efo-term-ontology/
- - Retrieve, update, or delete a specific EFO term ontology relationship by ID:
- - - GET http://localhost:8000/api/efo-term-ontology/{id}/
- - - PUT http://localhost:8000/api/efo-term-ontology/{id}/
- - - DELETE http://localhost:8000/api/efo-term-ontology/{id}/


- Load EFO terms from OLS url to the local database: Access it at http://localhost:8000/api/load-efo-terms/ 
- - POST http://localhost:8000/api/load-efo-terms/ (You can change the default OLS url from the LOAD_EFO_DATA_URL parameter in the settings.py file)


## Testing

### Unit Tests
Located in the test/services_test.py file. To run the tests, run the following command:

```bash
python manage.py test api.test.services_test.ServicesTestCase
```

### Integration Tests
Located in the test/services_integration_test.py file. (Not implemented)

```bash
python manage.py test api.test.services_intergration_test.ServicesIntegrationTestCase
```

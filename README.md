# Resume Processor API

The Resume Processor API is a Django-based REST API that processes resume files (PDF or Word documents), extracts the candidate's first name, email ID, and mobile number, sanitizes the extracted data, and saves it to a PostgreSQL database.

## Features

- Upload a resume file (PDF/Word).
- Extract key details such as first name, email, and mobile number.
- Sanitize the extracted data before saving to the database.
- Provides an API endpoint for submitting resumes and receiving the processed data.

## Installation

### Prerequisites

- Python 3.10 or higher
- PostgreSQL
- Virtual environment tools (`virtualenv` or `venv`)

### Step 1: Clone the repository

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd ResumeParserProject
```

### Step 2: Set up the virtual environment

Create and activate a virtual environment:

```bash
python3 -m venv newEnv
source newEnv/bin/activate
```

### Step 3: Install dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Set up PostgreSQL

Make sure PostgreSQL is installed and running. Create a database for the project:

```bash
psql -U postgres
CREATE DATABASE ResumeData;
CREATE USER <user_name> WITH PASSWORD 'your_password';
ALTER ROLE <user_name> SET client_encoding TO 'utf8';
ALTER ROLE <user_name> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <user_name> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ResumeData TO <user_name>;
```

Update the `DATABASES` configuration in `ResumeParser/settings.py` to match your PostgreSQL credentials.

### Step 5: Run migrations

Run the migrations to set up the database:

```bash
python manage.py migrate
```

### Step 6: Start the server

Run the development server:

```bash
python manage.py runserver
```

The API will now be available at `http://127.0.0.1:8000`.

## API Endpoints

### POST `/api/extract-resume/`

#### Description

This endpoint accepts a POST request with a resume file (PDF or Word document) and returns the extracted and sanitized candidate details.

#### Request Body

The request body should include a file field:

```bash
POST http://127.0.0.1:8000/api/extract-resume/
Content-Type: multipart/form-data
```

```plaintext
file: <path_to_resume_file>
```

#### Response

The response will contain the candidate's first name, email, and mobile number in the following format:

```json
{
  "first_name": "John",
  "email": "john.doe@example.com",
  "mobile_number": "123-456-7890"
}
```

## Data Sanitization

The API ensures that the extracted data is sanitized before being saved to the database. This includes:

- Stripping any leading or trailing whitespaces.
- Ensuring the email follows a valid format.
- Ensuring the mobile number is in a standardized format.

## Testing with Postman

1. Open Postman and create a new POST request.
2. Set the URL to `http://127.0.0.1:8000/api/extract-resume/`.
3. Set the request type to `POST`.
4. Under the `Body` tab, select `form-data`.
5. Add a key named `resume`, choose the `File` option, and upload a resume file.
6. Send the request.

You should receive the extracted and sanitized candidate data in the response.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

This README includes instructions on setting up the environment, installing dependencies, configuring PostgreSQL, running the server, using the API, and data sanitization.
```

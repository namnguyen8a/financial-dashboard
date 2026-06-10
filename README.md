# Financial-dashboard

## Phase 1: Core API & Data Ingestion
**Phase Goal:** Establish a working pipeline where external financial data is fetched and served via a basic API endpoint.
**Success Criteria:** You can send a request to your local server with a stock ticker and receive a structured JSON response containing real market data.

- [X] **Step 1: Research & Mental Mapping**
    - **Goal:** Understand the tools for web routing, data fetching, and data validation.
    - **Keywords:** `FastAPI hello world`, `yfinance documentation`, `Pydantic schemas`.
- [X] **Step 2: Scripting the Data Source**
    - **Goal:** Create a standalone Python script that successfully pulls history and company info from Yahoo Finance.
- [X] **Step 3: Building the First Endpoint**
    - **Goal:** Integrate the script into a FastAPI GET route: `/api/v1/companies/{ticker}`.
- [X] **How to Test:** 
    - Use a browser or an API client (like Postman or Insomnia).
    - Request `localhost:8000/api/v1/companies/AAPL`.
    - **Pass condition:** You see a JSON object with Apple’s financial data.

---

## Phase 2: Database & Containerization
**Phase Goal:** Move from "on-the-fly" fetching to persistent storage within a standardized environment.
**Success Criteria:** The application and database run inside containers, and requested data is saved to a table for future use.

- [ ] **Step 1: Research Infrastructure**
    - **Goal:** Learn how to package applications and communicate with databases via code.
    - **Keywords:** `Docker Compose multi-container`, `SQLAlchemy ORM` or `SQLModel`, `Alembic migrations`.
- [ ] **Step 2: Orchestration**
    - **Goal:** Write a `docker-compose.yml` to launch both the FastAPI app and a database (PostgreSQL/NoSQL) simultaneously.
- [ ] **Step 3: Persistence Logic**
    - **Goal:** Update the API logic: when a ticker is requested, the app checks the DB or saves the new `yfinance` data into the DB.
- [ ] **How to Test:** 
    - Shut down the containers and restart them; verify data still exists.
    - Use a database GUI (like DBeaver or pgAdmin) to inspect the tables.
    - **Pass condition:** A record appears in your database table every time a new ticker is requested through the API.

---

## Phase 3: Data Processing & Advanced Queries
**Phase Goal:** Transform the raw data into a searchable, professional-grade interface.
**Success Criteria:** Users can find specific financial records using complex filters without downloading the entire dataset.

- [ ] **Step 1: Research Query Logic**
    - **Goal:** Learn how to write complex database filters and handle large datasets efficiently.
    - **Keywords:** `SQLAlchemy filter operators`, `Limit-Offset vs Cursor pagination`, `Pandas cleaning`.
- [ ] **Step 2: The Search Engine**
    - **Goal:** Build the `/api/v1/financials` endpoint with support for query parameters.
- [ ] **Step 3: Logic Implementation**
    - **Goal:** Add functionality to filter by company name, numeric ranges (e.g., Net Income > $1B), and result limits.
- [ ] **How to Test:** 
    - Send a request like `/api/v1/financials?min_revenue=1000000&limit=5`.
    - **Pass condition:** The API returns exactly 5 records that meet the revenue criteria, and the response time remains fast.

---

## Phase 4: Security (Authentication & RBAC)
**Phase Goal:** Protect the data and restrict administrative actions to authorized users.
**Success Criteria:** Sensitive endpoints (like data updates) are blocked to the public, requiring a valid "Admin" token.

- [ ] **Step 1: Research Security Protocols**
    - **Goal:** Understand how to identify users and manage permissions securely.
    - **Keywords:** `JWT (JSON Web Tokens)`, `Passlib bcrypt`, `FastAPI Dependencies (Depends)`, `RBAC Architecture`.
- [ ] **Step 2: Identity Management**
    - **Goal:** Create a User table and build `/auth/register` and `/auth/login` endpoints.
- [ ] **Step 3: Access Control**
    - **Goal:** Apply "Guards" to your routes: Viewers can GET data; only Admins can POST/DELETE data.
- [ ] **How to Test:** 
    - Attempt to trigger a data refresh without a token (should return `401 Unauthorized`).
    - Login as a "Viewer" and try to delete data (should return `403 Forbidden`).
    - **Pass condition:** Only a user with the "Admin" role can successfully modify data.

---

## Phase 5: Automation & CI/CD
**Phase Goal:** Ensure code quality and automate the deployment pipeline.
**Success Criteria:** Every code "push" to GitHub triggers an automated suite of tests and style checks.

- [ ] **Step 1: Research Automation Tools**
    - **Goal:** Learn how to write automated tests and configure cloud workflows.
    - **Keywords:** `Pytest FastAPI TestClient`, `GitHub Actions workflows`, `Ruff/Black linting`.
- [ ] **Step 2: Defensive Programming**
    - **Goal:** Write unit tests that simulate API calls and verify the JSON structure and status codes.
- [ ] **Step 3: The Pipeline**
    - **Goal:** Create a `.github/workflows/main.yml` file to run your linter and tests on every commit.
- [ ] **How to Test:** 
    - Push a "broken" piece of code (e.g., a syntax error) to your repository.
    - **Pass condition:** GitHub Actions marks the build as "Failed," and only marks it "Success" when all tests and linting rules pass.
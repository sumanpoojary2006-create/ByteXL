# FastAPI - Curriculum Table of Contents

**Draft for finalization.** Follows the same house structure as the Python and DBMS curricula: a clean Unit -> Topic layout for teaching content, followed by separate Mini Projects and Capstone Projects chapters, sequenced in teaching order over a 15-week term. Each unit opens with a one-line goal, then lists its topics in the exact order they should be taught. Reading materials will follow the established house style: professional, beginner-friendly, no emojis, no em dashes, standardized Introduction heading, narrative flow, and every code block runnable on its own.

The arc mirrors how backend engineers actually grow: understand the web before writing a server (Units 1-2), get an API running and validate its data (Units 3-6), structure a real application backed by a database (Units 7-9), secure it and make it do real work (Units 10-12), then test it and ship it (Units 13-14).

**Assumed prerequisites:** Python Semester 1 and Semester 2 (functions, classes, modules, exceptions, decorators, virtual environments) and the DBMS course (SQL, keys, joins, transactions). No prior web development experience is assumed.

---

## Unit 1: Web and API Foundations

Understand what an API actually is and how a request travels, before writing a single line of server code.

1. Client and Server: What Happens When You Open a Website
2. What is an API, and Why Backends Exist
3. The HTTP Request: Method, URL, Headers, and Body
4. The HTTP Response: Status Codes, Headers, and Payload
5. HTTP Methods and Their Meaning: GET, POST, PUT, PATCH, DELETE
6. JSON: The Language APIs Speak
7. REST Principles: Resources, Representations, and Statelessness
8. Designing Good Endpoints: URL Naming, Nouns over Verbs, Consistency
9. Inspecting Real Traffic: Browser DevTools, curl, and API Clients
10. Where FastAPI Fits: Frameworks, WSGI vs. ASGI, and Why Speed Matters

## Unit 2: Modern Python for FastAPI

Pick up the specific Python features FastAPI is built on, so nothing in later units looks like magic.

1. Type Hints: Annotating Variables, Parameters, and Return Values
2. Typing Collections: list, dict, Optional, Union, and the Modern Syntax
3. Data Classes and Typed Objects: Structuring Data in Python
4. Decorators Revisited: How `@app.get(...)` Actually Works
5. Synchronous vs. Asynchronous Execution: Blocking and Waiting
6. `async` and `await`: Coroutines in Plain Language
7. The Event Loop: One Worker Handling Many Requests
8. Project Setup: Virtual Environments, `pip`, and `requirements.txt`
9. Reading Library Documentation and Tracebacks Like an Engineer

## Unit 3: Your First FastAPI Application

Get a real, documented API running on your machine within the first session.

1. Installing FastAPI and Uvicorn
2. The Minimal App: `FastAPI()` and Your First Route
3. Running the Server with Uvicorn and Live Reload
4. Path Operation Decorators: Mapping Methods to Functions
5. Returning Data: Dicts, Lists, and Automatic JSON Conversion
6. Automatic Interactive Documentation: Swagger UI and ReDoc
7. OpenAPI: The Schema Behind the Docs
8. Anatomy of a FastAPI Project: Files, Imports, and the App Object

## Unit 4: Request Inputs: Path, Query, Headers, and Cookies

Take input from the caller in every form an HTTP request can carry.

1. Path Parameters: Capturing Values from the URL
2. Type Conversion and Automatic Validation of Path Parameters
3. Route Order and Path Conflicts: Why `/users/me` Must Come First
4. Query Parameters: Optional Inputs and Default Values
5. Required vs. Optional Query Parameters
6. Validating Inputs with `Path()` and `Query()`: Length, Range, and Patterns
7. Enums for Fixed Choices in Paths and Queries
8. Reading Headers and Cookies
9. Form Data and When to Use It Instead of JSON

## Unit 5: Data Validation with Pydantic

Make invalid data impossible to get past the front door of your API.

1. Why Validation Belongs in the Framework, Not in Every Function
2. Pydantic Models: Declaring the Shape of Your Data
3. Request Bodies: Accepting JSON as a Model
4. Field Types, Defaults, and Optional Fields
5. Constraining Values with `Field()`: Ranges, Lengths, and Descriptions
6. Nested Models and Lists of Models
7. Special Types: `EmailStr`, `HttpUrl`, `UUID`, Dates, and Times
8. Custom Validators: Rules Your Business Actually Needs
9. Combining Path, Query, and Body in a Single Endpoint

## Unit 6: Responses, Status Codes, and Error Handling

Give callers exactly the data, status, and error messages they can rely on.

1. Response Models: Declaring What Goes Out
2. Hiding Internal Fields: Why the Output Model Differs from the Input Model
3. Choosing Status Codes Correctly: 200, 201, 204, and the 4xx Family
4. `response_model_exclude_unset` and Partial Responses
5. Raising `HTTPException` with Meaningful Messages
6. Understanding FastAPI's Automatic 422 Validation Errors
7. Custom Exception Handlers for Application-Wide Behavior
8. A Consistent Error Format: Designing Error Payloads Clients Can Parse
9. Returning Non-JSON Responses: Plain Text, HTML, Files, and Redirects
10. Documenting Responses and Errors in OpenAPI

## Unit 7: Structuring Real Applications: Routers, Dependencies, and Configuration

Grow a single file into a maintainable project without losing your way.

1. Why One Big `main.py` Stops Working
2. `APIRouter`: Splitting Endpoints by Resource
3. Prefixes, Tags, and Organized Documentation
4. A Standard Project Layout: routers, models, schemas, services, core
5. Dependency Injection: The Idea in Plain Terms
6. Writing and Using Dependencies with `Depends()`
7. Shared Dependencies: Pagination, Common Filters, and Current User
8. Dependencies with `yield`: Setup and Teardown
9. Configuration and Secrets: Environment Variables and Settings Objects

## Unit 8: Databases with SQLAlchemy

Connect your API to a real database and keep the data layer clean.

1. From In-Memory Lists to a Real Database
2. What an ORM Does, and When to Use Raw SQL Instead
3. Setting Up SQLAlchemy: Engine, Session, and Base
4. Defining Models: Tables as Python Classes
5. Sessions per Request: The Database Dependency Pattern
6. Creating and Reading Rows from an Endpoint
7. Updating and Deleting Rows Safely
8. Relationships: One-to-Many and Many-to-Many in the ORM
9. ORM Models vs. Pydantic Schemas: Keeping the Two Layers Separate
10. Schema Migrations with Alembic

## Unit 9: Building a Complete CRUD API

Assemble everything so far into one coherent, production-shaped service.

1. From Requirements to Endpoints: Planning a Resource API
2. Create: Validating Input and Returning 201
3. Read: Single Item, Not-Found Handling, and Listing
4. Filtering, Sorting, and Pagination on List Endpoints
5. Update: Full Replacement (PUT) vs. Partial Update (PATCH)
6. Delete: Hard Deletes, Soft Deletes, and Idempotency
7. The Service Layer: Keeping Business Logic Out of Route Functions
8. Reviewing Your Own API: A Practical Design Checklist

## Unit 10: Authentication and Authorization

Decide who is calling and what they are allowed to do.

1. Authentication vs. Authorization: Two Different Questions
2. Password Storage Done Right: Hashing with bcrypt, Never Plain Text
3. User Registration and Login Endpoints
4. Token-Based Authentication: Why Tokens Replaced Sessions in APIs
5. JSON Web Tokens: Structure, Signing, and Expiry
6. OAuth2 Password Flow with FastAPI's Security Utilities
7. Protecting Routes with a `get_current_user` Dependency
8. Roles and Permissions: Admin-Only and Owner-Only Endpoints
9. Refresh Tokens and Session Lifetime
10. Common Security Mistakes: Leaking Secrets, Weak Tokens, and Overexposed Data

## Unit 11: Async, Background Tasks, and Calling Other Services

Do slow work without making users wait, and talk to the rest of the world.

1. `def` vs. `async def` in FastAPI: What Runs Where
2. The Blocking Call Problem: How One Bad Line Stalls the Server
3. Async Database Access: When It Helps and When It Does Not
4. Calling External APIs with `httpx`
5. Timeouts, Retries, and Failing Gracefully
6. `BackgroundTasks`: Work That Happens After the Response
7. When Background Tasks Are Not Enough: Queues and Workers (introduction)
8. Sending Email and Notifications from an API
9. Application Lifespan: Startup and Shutdown Events

## Unit 12: Middleware, CORS, File Handling, and Real-Time APIs

Cover the cross-cutting features every real service eventually needs.

1. Middleware: Code That Runs Around Every Request
2. Writing Custom Middleware: Timing, Request IDs, and Logging
3. CORS: Why the Browser Blocks Your Frontend, and How to Fix It Properly
4. Uploading Files: `UploadFile`, Size Limits, and Validation
5. Storing and Serving Uploaded Files
6. Downloads and Streaming Large Responses
7. Serving Static Files and HTML Templates with Jinja2
8. WebSockets: Two-Way Communication in FastAPI
9. Server-Sent Events and Streaming Responses (introduction)

## Unit 13: Testing FastAPI Applications

Prove your API works, and keep it working as it changes.

1. Why API Tests Matter More Than Manual Clicking
2. pytest Essentials: Test Files, Assertions, and Fixtures
3. `TestClient`: Calling Your API from a Test
4. Testing Success Paths, Validation Errors, and Not-Found Cases
5. Test Databases: Isolated Data for Every Test Run
6. Overriding Dependencies in Tests
7. Testing Protected Endpoints and Authentication
8. Mocking External Services
9. Coverage, Test Organization, and What Not to Test

## Unit 14: Deployment, Performance, and Production Operations

Take the service off your laptop and keep it healthy under real traffic.

1. Development vs. Production: Configuration, Debug Modes, and Secrets
2. Uvicorn Workers, Gunicorn, and Process Management
3. Containerizing a FastAPI App with Docker
4. Docker Compose: API and Database Together
5. Deploying to a Cloud Host: A Practical Walkthrough
6. Logging That Helps You at 2 A.M.
7. Health Checks, Monitoring, and Basic Observability
8. Performance Basics: Profiling, N+1 Queries, and Caching
9. Rate Limiting and Protecting Against Abuse
10. API Versioning, Deprecation, and Documenting Changes for Clients

## Project Chapter: Mini Projects

Focused, standalone builds that apply unit concepts without nesting project briefs inside teaching units.

1. Unit Converter API (path and query parameters)
2. Student Records API with Validation (Pydantic)
3. Notes API with Full CRUD and Pagination
4. Library Catalog API Backed by SQLAlchemy
5. Secure Task Manager with JWT Authentication
6. Weather Aggregator Calling an External API
7. File Upload and Report Download Service
8. Live Chat Room with WebSockets
9. Test Suite for an Existing API

## Project Chapter: Capstone Projects

Integrate the full course in an end-to-end, deployable backend.

1. Complete E-Commerce Backend API (users, catalog, cart, orders, payments stub, admin roles, tests, Docker deployment)

---

## Summary

| # | Unit | Topics |
|---|------|--------|
| 1 | Web and API Foundations | 10 |
| 2 | Modern Python for FastAPI | 9 |
| 3 | Your First FastAPI Application | 8 |
| 4 | Request Inputs: Path, Query, Headers, and Cookies | 9 |
| 5 | Data Validation with Pydantic | 9 |
| 6 | Responses, Status Codes, and Error Handling | 10 |
| 7 | Structuring Real Applications | 9 |
| 8 | Databases with SQLAlchemy | 10 |
| 9 | Building a Complete CRUD API | 8 |
| 10 | Authentication and Authorization | 10 |
| 11 | Async, Background Tasks, and External Services | 9 |
| 12 | Middleware, CORS, Files, and Real-Time APIs | 9 |
| 13 | Testing FastAPI Applications | 9 |
| 14 | Deployment, Performance, and Production Operations | 10 |
| | **Teaching topic total** | **129** |

Project briefs are counted separately: 9 mini projects and 1 capstone project.

## Suggested 15-Week Pacing

| Week | Coverage |
|------|----------|
| 1 | Unit 1 |
| 2 | Unit 2 |
| 3 | Unit 3 + Mini Project 1 |
| 4 | Unit 4 |
| 5 | Unit 5 + Mini Project 2 |
| 6 | Unit 6 + Mini Project 3 |
| 7 | Unit 7 |
| 8 | Unit 8 + Mini Project 4 |
| 9 | Unit 9 |
| 10 | Unit 10 + Mini Project 5 |
| 11 | Unit 11 + Mini Project 6 |
| 12 | Unit 12 + Mini Projects 7-8 |
| 13 | Unit 13 + Mini Project 9 |
| 14 | Unit 14 |
| 15 | Capstone build and review |

**Notes for finalization**

- 14 units keeps the course in the same band as Python Semester 1 (13 units, 99 topics) and DBMS (13 units, 106 topics), with a slightly higher topic count because backend work spans more distinct concerns.
- Units 1 and 2 exist because most FastAPI courses fail here: students who never learned HTTP or `async` treat the framework as magic and cannot debug it. These two units are the main structural difference from typical online FastAPI content.
- Database work (Unit 8) assumes the DBMS course, so SQL itself is not re-taught. Only the ORM mapping, the session-per-request pattern, and migrations are new.
- Pydantic content is written for Pydantic v2 syntax; any v1 differences appear as short compatibility notes rather than parallel material.
- Testing (Unit 13) is deliberately placed before deployment so students ship something they have proven works, matching industry practice rather than treating tests as optional.
- Authentication is taught with FastAPI's built-in OAuth2 utilities and standard libraries rather than a third-party auth framework, so the concepts transfer to any stack.
- Once this TOC is approved, unit folders and READMEs can be scaffolded the same way as the Python, DBMS, and AI courses, and reading materials authored unit by unit in the existing house style.

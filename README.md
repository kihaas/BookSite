# BookSite — FastAPI Backend Project

**BookSite** is a beginner-friendly web application built with **FastAPI**, designed to serve as a hands-on learning platform for backend development. This project demonstrates essential backend concepts through a simple book-themed site and acts as a foundational base for future FastAPI-based applications.

---

##  Project Overview

- **Purpose**: Learn and practice FastAPI fundamentals in a practical setting.
- **Core Features**:
  - RESTful API for managing book-related data (CRUD operations).
  - FastAPI-powered endpoints with automatic OpenAPI documentation.
  - Optionally integrated with a templated frontend using HTML, if applicable.
- Emphasis on clean design, Pydantic-based data validation, and rapid development.

---

##  Why FastAPI?

FastAPI is a powerful Python framework for building APIs with modern features, including:

- **High performance**, often comparable to frameworks like Node.js and Go, thanks to Starlette and Pydantic. :contentReference[oaicite:0]{index=0}
- **Automatic documentation**: Instantly generate interactive Swagger UI (`/docs`) and ReDoc (`/redoc`) interfaces. :contentReference[oaicite:1]{index=1}
- **Type safety & validation**: Utilizes Python type hints and Pydantic for request validation and serialization. :contentReference[oaicite:2]{index=2}
- **Asynchronous support**: Built for modern async operations with excellent scalability. :contentReference[oaicite:3]{index=3}

This makes FastAPI an ideal choice for creating clean, robust, and maintainable backend services.

---

##  Getting Started

### Prerequisites

- **Python 3.8+**
- A virtual environment (e.g., `venv`, `pipenv`, or `Poetry`)
- **Uvicorn** as the ASGI server

### Installation & Launch

```bash
git clone https://github.com/kihaas/BookSite.git
cd BookSite

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies (adjust as needed)
pip install fastapi uvicorn[standard] pydantic

# Start the application
uvicorn main:app --reload


<img width="1599" height="890" alt="image" src="https://github.com/user-attachments/assets/d06a4ab9-723d-49d7-9601-c7866000e24b" />


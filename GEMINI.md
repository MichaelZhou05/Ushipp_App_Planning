# Gemini Context: University Shipping Operations Command Center (OCC)

## Project Overview

This repository contains the **University Shipping Operations Command Center (OCC)**, a comprehensive logistics platform built to manage the company's entire operational lifecycle. The project is a monorepo consisting of a FastAPI backend, a Next.js frontend dashboard, and a Capacitor-based mobile app for drivers.

The system is designed to handle order management (via JSON import), route optimization using Google OR-Tools, real-time driver tracking via WebSockets, and photo-based proof of delivery. A single "Admin/Dispatcher" role has full control over the system.

-   **Backend (`/backend`):** A Python API using FastAPI to handle business logic, database interaction, and the core logistics engine.
-   **Frontend (`/frontend`):** A Next.js web dashboard for admins/dispatchers to manage orders, generate routes, and view the live driver map.
-   **Driver App (`/driver-app`):** A React/Capacitor mobile app for drivers to view their routes, update order statuses, and capture photos.

## Building and Running

### 1. Backend (FastAPI)

The backend runs on Python and uses a virtual environment for dependency management.

```bash
# Navigate to the backend directory
cd backend

# TODO: Create a requirements.txt file
# ./venv/bin/pip freeze > requirements.txt

# Install dependencies (run this if requirements.txt exists)
# ./venv/bin/pip install -r requirements.txt

# Activate the virtual environment (optional, but good practice)
# source venv/bin/activate

# Run the development server
# uvicorn main:app --reload --port 8000
```

### 2. Frontend (Next.js)

The frontend is a standard Next.js application.

```bash
# Navigate to the frontend directory
cd frontend

# TODO: This project has not been initialized yet.
# Expected commands after initialization:

# Install dependencies
# npm install

# Run the development server
# npm run dev
```

### 3. Driver App (React/Capacitor)

The driver app is a React application wrapped with Capacitor.

```bash
# Navigate to the driver app directory
cd driver-app

# TODO: This project has not been initialized yet.
# Expected commands after initialization:

# Install dependencies
# npm install

# Run the web-based development server
# npm start

# Sync the web build to the native platforms
# npx cap sync

# Open the native project in its IDE (e.g., Xcode)
# npx cap open ios
```

## Development Conventions

-   **Monorepo Structure:** The project is strictly divided into `backend`, `frontend`, and `driver-app`. There should be no cross-contamination of code. All communication between them must happen via the backend's API.
-   **State Management:** The core of the application is the order state machine. All status changes must follow the defined flow: `CONFIRMED` -> `ROUTED` -> `ENROUTE` -> `PICKED_UP` -> `DELIVERED`.
-   **Database:** The database is the single source of truth. All data is stored in a PostgreSQL database, and the backend uses SQLAlchemy with GeoAlchemy2 to interact with it.
-   **Real-Time Communication:** Real-time features (like driver tracking) are to be implemented using WebSockets, managed by the FastAPI backend.

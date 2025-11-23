# Project Plan: University Shipping Operations Command Center (OCC)

This document outlines the development plan for the OCC project, breaking it down into logical phases.

---

## Phase 1: Project Setup & Core Models

**Goal:** Establish the project foundation, set up all services, and model the core data.

1.  **Initialize Monorepo:** Set up the directory structure with `/backend`, `/frontend`, and `/driver-app`.
2.  **Backend Setup (FastAPI):**
    *   Initialize a Python project with a virtual environment.
    *   Install FastAPI, Uvicorn, and other base dependencies.
    *   Set up a basic "Hello World" endpoint to confirm it works.
3.  **Database Setup (PostgreSQL):**
    *   Set up a PostgreSQL server (e.g., using Docker or a cloud service).
    *   Enable the PostGIS extension.
    *   Connect the FastAPI backend to the database.
4.  **Frontend Setup (Next.js):**
    *   Initialize a new Next.js project with TypeScript and Tailwind CSS.
    *   Create a basic layout and placeholder pages.
5.  **Database Schema & Models:**
    *   Define the database tables using an ORM (like SQLAlchemy with GeoAlchemy2 for PostGIS support).
    *   **Users:** A simple table for `Admin/Dispatcher` accounts (username, hashed_password).
    *   **Orders:** The core table including fields for `student_name`, `pickup_address`, `delivery_address`, `pickup_time_window_start`, `pickup_time_window_end`, `status` (for the state machine), and other details from the JSON file.
    *   **OrderPhotos:** A table to link photos to orders (`order_id`, `photo_url`, `type` ['pickup'/'delivery']).
6.  **Initial Feature: JSON Order Import:**
    *   Create an admin-only API endpoint to upload a JSON file.
    *   Implement the logic to parse the file and create `Order` records in the database.
    *   Build a simple UI in the frontend for an admin to perform the upload.

---

## Phase 2: Logistics Engine & Routing

**Goal:** Implement the core VRP logic to create optimized routes.

1.  **Integrate OR-Tools:** Add Google OR-Tools to the backend.
2.  **Routing Service:**
    *   Create a service that takes a list of `Orders` for the day and a list of available `Trucks` (initially just defined by capacity).
    *   Use OR-Tools to solve the Vehicle Routing Problem, considering time windows.
3.  **API & Data Structures:**
    *   Create database tables for `Routes` and `Stops` (or `RouteLegs`). A `Route` is assigned to a `Driver`, and consists of an ordered list of `Stops` (each stop corresponding to an `Order`'s pickup or delivery).
    *   Create an API endpoint that triggers the routing service and stores the resulting routes in the database.
4.  **Frontend UI:**
    *   Create a "Routing" page in the admin dashboard.
    *   The UI should allow the admin to select a date, view unrouted orders, and click a "Generate Routes" button.
    *   Display the generated routes, showing which orders are on which route and in what sequence.

---

## Phase 3: Driver App & Basic Tracking

**Goal:** Empower drivers with a mobile app to follow routes and update order statuses.

1.  **Driver App Setup (Capacitor):**
    *   Initialize a React project inside `/driver-app`.
    *   Integrate Capacitor to enable native mobile features.
2.  **Driver Login & Route View:**
    *   Implement a simple login for drivers.
    *   After login, the app should fetch and display the driver's assigned route for the day, showing a list of stops.
3.  **Stop Details & Actions:**
    *   For each stop, show the address and order details.
    *   Add buttons to update the order status (`ENROUTE` -> `PICKED_UP` -> `DELIVERED`). These buttons will call the backend API to update the `Order` status.
4.  **Photo Capture:**
    *   Use Capacitor's Camera API to allow the driver to take a photo.
    *   Implement logic to upload the photo to a storage service (e.g., S3, Cloudinary) and associate the URL with the order via a backend API call.
5.  **Dispatcher View v1:**
    *   On the frontend dashboard, create a map view (using a library like React Leaflet).
    *   Display the planned routes on the map (as polylines). This is not yet real-time.

---

## Phase 4 & Beyond: Real-Time, CRM, and Advanced Features

**Goal:** Add real-time capabilities and other advanced modules.

1.  **Real-Time GPS Tracking:**
    *   Implement background location tracking in the driver app.
    *   The app will periodically send GPS coordinates to a new API endpoint on the backend.
2.  **WebSocket Integration:**
    *   Implement WebSockets in FastAPI.
    *   When the backend receives a location update, it will push the new coordinates to all connected dashboard clients.
    *   The frontend map will listen for these updates and move driver icons in real-time.
3.  **CRM & Ticketing:**
    *   Design and implement the `Tickets` table in the database, linked to `Orders`.
    *   Build the Kanban-style board in the frontend for support.
    *   Implement an email-parsing service to automatically create tickets (can use a service like SendGrid Inbound Parse).
4.  **Notifications:**
    *   Integrate Twilio/SendGrid for SMS/email.
    *   Create backend logic to trigger notifications based on order status changes (e.g., send an email when status changes to `DELIVERED`).
5.  **Analytics & Audit Logs:**
    *   Implement an immutable logging system for all major actions.
    *   Create a basic analytics dashboard to show key metrics.

# University Shipping Operations Command Center (OCC)

## Project Overview

The Operations Command Center (OCC) is an independent logistics and management platform for University Shipping. It is designed to be the central nervous system for the business, handling the entire order lifecycle from an initial JSON import to final dorm delivery.

The platform is architected to optimize delivery routes, manage and track drivers in real-time, provide photo-based proof of delivery, and handle customer support through an integrated ticketing system. The system is managed by a single "Admin/Dispatcher" user role with full permissions.

This project is a monorepo containing three distinct applications:
-   **/backend**: A Python API built with FastAPI.
-   **/frontend**: A web dashboard built with Next.js (React).
-   **/driver-app**: A mobile app for drivers built with React and Capacitor.

## Tech Stack & Architecture

-   **Backend:** Python, FastAPI (with WebSockets for real-time communication)
-   **Database:** PostgreSQL with the PostGIS extension for geospatial data.
-   **Logistics Engine:** Google OR-Tools for Vehicle Routing Problem (VRP) optimization.
-   **Task Queue:** Celery & Redis for handling background jobs.
-   **Frontend:** TypeScript, Next.js (React), Tailwind CSS
-   **Driver App:** React, Capacitor (for native GPS and Camera access)

## Core Modules & Features

-   **Order Management:** Orders are imported via JSON and managed through a `CONFIRMED` -> `ROUTED` -> `ENROUTE` -> `PICKED_UP` -> `DELIVERED` state machine.
-   **Logistics & Routing:** The VRP engine processes orders with time-window constraints to generate optimized routes for drivers.
-   **Real-Time Tracking:** Dispatchers can see driver locations updated live on a map.
-   **Driver App:** Provides drivers with their route, allows for status updates, and uses the camera to capture photos as proof of pickup and delivery.
-   **CRM / Ticketing:** A tracking system for customer support issues.

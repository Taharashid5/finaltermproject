# Car Company API

A FastAPI project simulating a car company backend with user authentication, staff authorization, and persistent storage using JSON files.

## Features

1. **User Management**
   - Signup (`/signup`)
   - Login (`/login`)
   - Roles: `customer` or `staff`

2. **Car Management**
   - Add cars (staff only) (`/cars` POST)
   - View cars (`/cars` GET)
   - Each car has:
     - `name`
     - `brand`
     - `year`
     - `price`
     - `color`
     - `available` (boolean)
     - `mileage` (km/miles driven)
     - `fuel_type` (Petrol, Diesel, Electric)
     - `transmission` (Automatic / Manual)
     - `engine_capacity` (e.g., 1.8L)

3. **Persistent Storage**
   - Users → `users.json`
   - Cars → `cars.json`

4. **Authorization**
   - Only staff users can add cars
   - Anyone can view cars

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/car_company_api.git
cd car_company_api

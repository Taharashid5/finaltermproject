from fastapi import FastAPI, HTTPException, Header
import json
import os

app = FastAPI()

USERS_FILE = "users.json"
CARS_FILE = "cars.json"

# ---------------- FILE HELPERS ----------------
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_cars():
    if not os.path.exists(CARS_FILE):
        return []
    with open(CARS_FILE, "r") as f:
        return json.load(f)

def save_cars(data):
    with open(CARS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- AUTHORIZATION ----------------
def authorize_staff(username):
    users = load_users()
    if username not in users:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if users[username]["role"] != "staff":
        raise HTTPException(status_code=403, detail="Staff only")

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return {"message": "Car Company API Running"}

# ---------------- SIGNUP ----------------
@app.post("/signup")
def signup(username: str, password: str, role: str = "customer"):
    users = load_users()
    if username in users:
        raise HTTPException(status_code=400, detail="User exists")

    users[username] = {
        "password": password,
        "role": role
    }

    save_users(users)
    return {"message": f"User '{username}' created successfully"}

# ---------------- LOGIN ----------------
@app.post("/login")
def login(username: str, password: str):
    users = load_users()
    if username not in users:
        raise HTTPException(status_code=401, detail="Unauthorized login")
    if users[username]["password"] != password:
        raise HTTPException(status_code=401, detail="Unauthorized login")
    return {
        "message": f"Login successful for '{username}'",
        "username": username,
        "role": users[username]["role"]
    }

# ---------------- ADD CAR (STAFF ONLY) ----------------
@app.post("/cars")
def add_car(
    name: str,
    brand: str,
    year: int,
    price: float,
    color: str,
    available: bool,
    mileage: float,
    fuel_type: str,
    transmission: str,
    engine_capacity: str,
    username: str = Header()
):
    authorize_staff(username)

    cars = load_cars()
    cars.append({
        "name": name,
        "brand": brand,
        "year": year,
        "price": price,
        "color": color,
        "available": available,
        "mileage": mileage,
        "fuel_type": fuel_type,
        "transmission": transmission,
        "engine_capacity": engine_capacity
    })
    save_cars(cars)

    return {"message": f"Car '{name}' added successfully"}

# ---------------- VIEW CARS ----------------
@app.get("/cars")
def view_cars():
    return load_cars()

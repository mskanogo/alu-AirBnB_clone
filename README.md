# AirBnB Clone - The Console

## Project Description
This is the first step of building a full AirBnB web application clone.
We build a command-line interpreter (console) to manage AirBnB objects
such as Users, Places, Cities, States, Amenities, and Reviews.

This foundation will be reused across all later phases:
HTML/CSS templating, database storage, REST API, and front-end integration.

## Command Interpreter Description

### How to Start
```bash
./console.py
```

### How to Use (Interactive Mode)
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a...'}
(hbnb) quit
$
```

### How to Use (Non-Interactive Mode)
```bash
$ echo "create User" | ./console.py
(hbnb) 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb)
```

### Available Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `quit` | `quit` | Exit the program |
| `EOF` | `Ctrl+D` | Exit the program |
| `create` | `create <ClassName>` | Create a new instance and print its id |
| `show` | `show <ClassName> <id>` | Print string representation of an instance |
| `destroy` | `destroy <ClassName> <id>` | Delete an instance |
| `all` | `all` or `all <ClassName>` | Print all instances, optionally filtered by class |
| `update` | `update <ClassName> <id> <attr> "<value>"` | Update an instance attribute |

### Examples
```bash
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a...'}

(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 name "My Model"

(hbnb) all BaseModel
["[BaseModel] (49faff9a-...) {'name': 'My Model', ...}"]

(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

(hbnb) quit
```

## Models Available
- **BaseModel** - Parent class: id, created_at, updated_at
- **User** - email, password, first_name, last_name
- **State** - name
- **City** - state_id, name
- **Amenity** - name
- **Place** - city_id, user_id, name, description, rooms, price, etc.
- **Review** - place_id, user_id, text

## Storage
All objects are saved to `file.json` via the `FileStorage` engine.
Serialization flow: `Object → dict → JSON string → file.json`
Deserialization flow: `file.json → JSON string → dict → Object`

## Authors
See [AUTHORS](./AUTHORS)
# CLI Banking System

A Python-based Command Line Interface (CLI) banking application that integrates with PostgreSQL for persistent data storage.

## Architecture

- **Language**: Python 3.12
- **Database**: PostgreSQL (Replit built-in)
- **Libraries**: psycopg2-binary, python-dotenv

## Project Structure

- `main.py` - Main application file with all banking logic
- `requirements.txt` - Python dependencies

## Database

Uses Replit's built-in PostgreSQL database. The `DATABASE_URL` environment variable is set automatically.

### Schema

```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    pin VARCHAR(4) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0
);
```

## Running

The app runs as a console workflow:
```
python main.py
```

## Features

- Create new accounts with unique usernames and 4-digit PINs
- Sign into existing accounts
- Deposit and withdraw funds
- Check account balance
- All data persisted to PostgreSQL

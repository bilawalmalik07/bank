# 🏦 CLI Banking System

A professional Python-based Command Line Interface (CLI) application that integrates with a PostgreSQL cloud database (Neon). This project demonstrates core backend engineering principles, including data persistence, secure credential management, and relational database design.

## 🚀 Key Features

- **Secure Authentication**: Implements a robust sign-in flow using unique usernames and 4-digit PIN validation.
- **Cloud Data Persistence**: All user data and transactions are synchronized in real-time to a remote PostgreSQL database, ensuring data is never lost when the program closes.
- **Core Banking Operations**:
  - **Account Creation**: Validates unique usernames and enforces a minimum initial deposit.
  - **Real-time Transactions**: Supports instant deposits and withdrawals with automated balance updates.
  - **Integrity Checks**: Built-in logic to prevent overdrafts and ensure sufficient funds for all withdrawals.
- **Security First**: Utilizes environment variables (`.env`) to protect sensitive database connection strings.

## 🛠️ Tech Stack

- **Language**: Python 3
- **Database**: PostgreSQL (Cloud-hosted via Neon)
- **Libraries**:
  - `psycopg2`: For advanced PostgreSQL database interaction and query execution.
  - `python-dotenv`: For secure management of environment variables.

## ⚙️ How It Works

1. **Connection**: The app establishes a secure link to the Neon cloud database using a hidden connection URL.
2. **Authentication**: Users can either create a new account (which performs a "duplicate check" on the database) or sign into an existing one.
3. **Transaction Flow**: When a user deposits or withdraws, the app calculates the new balance and sends an `UPDATE` SQL command to the cloud to ensure the database matches the local state.
4. **Error Handling**: The system uses `try/except` blocks to handle database downtime or invalid user inputs gracefully.

## 🧠 Skills Demonstrated

- **Relational Databases**: Designing table schemas and implementing CRUD (Create, Read, Update) operations.
- **Backend Architecture**: Managing global states and complex user decision loops in Python.
- **Environment Security**: Safeguarding API keys and database credentials from public exposure.

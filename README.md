# GuildGP-Auth  

GuildGP-Auth is a Django REST API designed for user authentication and management. It leverages the Django REST Framework to provide efficient and secure endpoints for user registration, login, and token refresh.  

## Features  

- User registration  
- User login and token authentication  
- Token refresh for session continuity  
- Comprehensive user management  

## Endpoints  

### User Management  
- **`GET /api/users/`** - List all users  
- **`GET /api/users/{id}/`** - Retrieve a user by ID  
- **`POST /api/users/`** - Create a new user  
- **`PUT /api/users/{id}/`** - Update a user by ID  
- **`DELETE /api/users/{id}/`** - Delete a user by ID  

### Authentication  
- **`POST /api/auth/register/`** - Register a new user  
- **`POST /api/auth/login/`** - Authenticate a user and obtain a token  
- **`POST /api/auth/refresh/`** - Refresh the authentication token  

## Installation  

1. **Clone the repository:**  
   ```bash  
   git clone https://github.com/tmalik258/GuildGP-Auth.git  
   cd GuildGP-Auth  
   ```  

2. **Create and activate a virtual environment:**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`  
   ```  

3. **Install dependencies:**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Apply database migrations:**  
   ```bash  
   python manage.py migrate  
   ```  

5. **Run the development server:**  
   ```bash  
   python manage.py runserver  
   ```  

## Usage  

You can interact with the API using tools like [Postman](https://www.postman.com/) or `cURL`. Ensure you include the appropriate headers (e.g., `Authorization: Bearer <token>`) for protected endpoints.   

## License  

This project is licensed under the [MIT License](LICENSE).
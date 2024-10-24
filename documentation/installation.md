### To install your Django app with frontend libraries using `package.json`, follow these steps:
### N.B assumes you have followed instructions in the readme.md

### Backend (Django)
1. Clone the Repository:
   
   git clone <repository-url>
   cd <project-directory>
  
2. Set up a Virtual Environment:
   
   - python -m venv venv
   - source venv/bin/activate  # (Linux/Mac)
   - venv\Scripts\activate  # (Windows)
  
3. Install Backend Dependencies:
   
  -  pip install -r requirements.txt
  

4. Apply Migrations:
   
   - python manage.py migrate
  

5. Run the Django Development Server:
   
   - python manage.py runserver
  

### Frontend (Node.js)
1. Install Node.js Dependencies:
   
   - npm install
  

2. Run Frontend Build (if necessary):
   
   - npm run build  # or your specified build script
  

3. Start Frontend Development Server:
   
   - npm start  # or any frontend server setup
  

- Make sure to update any configurations in `settings.py` and other environment variables as needed for your specific project.
How to Run the Django App
=========================

To run the Django app, follow these steps:

1. Navigate to the project directory:

   .. code-block:: bash

      cd /path/to/your/project

2. Create and activate a virtual environment (if not already done):

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

3. Install the project dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Apply database migrations:

   .. code-block:: bash

      python manage.py migrate

5. Create a superuser (if needed):

   .. code-block:: bash

      python manage.py createsuperuser

6. Run the development server:

   .. code-block:: bash

      python manage.py runserver

7. Access the app in your web browser at http://localhost:8000/ (by default).

8. To stop the server, press `Ctrl+C`.

That's it! Your Django app should now be running locally, and you can start using it.

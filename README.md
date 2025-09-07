# Task Manager API 
Project Description: Task Management API for creating, updating, deleting, and marking tasks.

Tech Stack: Django, Django REST Framework

Setup Instructions: How to install dependencies, run migrations, and start the server.

How to Run Locally: python manage.py runserver

<h4>Overview</h4>

The Task Manager API is a backend project built with Django and Django REST Framework (DRF).
It allows users to manage tasks by creating, updating, deleting, and marking them as complete or incomplete.
Each user can only see and manage their own tasks.


<h4>Features</h4>

User authentication (login required to manage tasks).

CRUD operations for tasks.

Mark tasks as complete with a timestamp.

Prevent editing completed tasks unless reverted to Pending.

Filters:

status (Pending / Completed)

priority (Low / Medium / High)

due_date (exact, greater-than, less-than)

Sorting:

due_date (ascending/descending)

priority (ascending/descending)

<h4>Endpoints</h4>
Authentication

/api-auth/login/ → Login page (DRF session auth).

/api-auth/logout/ → Logout.

<h4>Task Management</h4>
Method	Endpoint	                   Description
GET	    /api/tasks/	                 List user’s tasks
POST	/api/tasks/	                 Create a new task
GET	    /api/tasks/<id>/	         Retrieve a task by ID
PUT	    /api/tasks/<id>/	         Update a task
PATCH	/api/tasks/<id>/	         Partial update of a task
DELETE	/api/tasks/<id>/	         Delete a task
PATCH	/api/tasks/<id>/complete/	 Mark a task as completed (adds timestamp)


<h4>Filters & Sorting</h4>

<h4>Filters</h4>

By status:

/api/tasks/?status=Pending


By priority:

/api/tasks/?priority=High


By due date (range):

/api/tasks/?due_date__gte=2025-12-01
/api/tasks/?due_date__lte=2026-01-31

<h4>Sorting</h4>

By due date (ascending):

/api/tasks/?ordering=due_date


By due date (descending):

/api/tasks/?ordering=-due_date


By priority (ascending/descending):

/api/tasks/?ordering=priority
/api/tasks/?ordering=-priority

<h4>Technical Stack</h4>

Django 5.x

Django REST Framework

Django Filter

<h4>Testing</h4>

Use DRF’s Browsable API (/api/) to interact with endpoints.

Or use Postman/Insomnia for testing with filters and sorting.

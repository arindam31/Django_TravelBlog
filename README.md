# Django_TravelBlog
This is my personal Tourism Blog Site.

URL : http://arindam31.pythonanywhere.com

# Requirements:

1) **Language**: Python 2.7
2) **Framework**: Django 1.11
3) **Database**: Default (SQLite)
4) **Deployment (Web hosting)**: www.pythonanywhere.com
5) **External Modules to be installed:**
   * CKEditor
   * djangorestframework
   * django-allauth
   * [django-crispy-forms ](http://django-crispy-forms.readthedocs.io/en/latest/install.html)

# Features (Implemented):
1) ## Home Page :
   Shows favourite posts, NavBar with search (on title and description),
   City Section (City details with travel plans)

2) ## Post details Page:
   * Shows post details with a like button showing a count of likes .
   * Shows approved comments at the bottom (if any).
   * Post Details URL is human friendly.

3) ## Post Add & Edit:
   If user is logged in, user can add a Post from frontend form.
   Same for Editing an existing Post.
   Added feature: Rich Text editor provided that provides better text editing tools.

4) ## REST Api
   _All Posts_:
   http://arindam31.pythonanywhere.com/api/v1/posts

   Above link shows all posts on JSON format .

5) ## Comments
   Visitors can log in and post comments . Comment is dynamically added without page reload.

6) ## Social Logins
   No need to register . One can use Google and Github to login . Login allows user to post comments .

7) ## Tests

   Tests are included under blog/tests/ . These include test for models, views, and API.
   To run them , you can use standard command or use **nose plugin**.

   Standard format:

   * **To run all tests**: python manage.py test blog
   * **To run a specific file**: python manage.py test blog.tests.test_api
   * **To run a specific test class**: python manage.py test blog.tests.tests_blog.TestPostModel
   * **To run a single test**: python manage.py test blog.tests.tests_blog.TestPostModel.test_get_images_from_post_description


# To be implemented:

1. Dashboard with details (post views, likes , date created etc)
1. Add share buttons for FB , Quora , and others.
1. Create a travel planner To-Do list . User should be logged-in to avail this.

### Snapshot (Website Home Page)
![Home page](https://photos.google.com/album/AF1QipM3bnI3nmStYbqJEwh7d08KgTBVs2DtoZNZnx1Q/photo/AF1QipPcKvGc5a9qyWVvRx916AqL2DBE566o3aU7eDnn)


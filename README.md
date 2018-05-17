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

# Features (Implemented):
1) ## Home Page :
   Shows favourite posts, NavBar with search (on title and description)
   
2) ## Post details Page: 
   * Shows post details with a like button showing a count of likes . 
   * Shows approved comments at the bottom (if any).
   * Post Details URL is human friendly.
   
3) ## Post Add & Edit: 
   If user is logged in (via Django Admin), user can add a Post from frontend form.
   Same for Editing an existing Post.
   Added feature: Rich Text editor provided in form that provides better text editing tools.
   
4) ## REST Api 
   _All Posts_: 
   http://arindam31.pythonanywhere.com/api/v1/posts  
   
   Above link shows all posts on JSON format . 
   
5) ## Comments
   Visitors can log in using Github and post comments . Comment is dynamically added without page reload.
   
# To be implemented:

1. Dashboard with details (post views, likes , date created etc)
1. Show Tags beside a post.
1. In home page, let user select posts by Tags.
1. Show in home page , details of latest post.

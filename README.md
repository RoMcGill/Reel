# Guess The Boozer <img src="" style="width: 40px;height:40px;">


**Developer: Ronan McGill**

💻 [Visit live website](https://reel-2022-new.herokuapp.com)

![Mockup image]()


## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing of user stories](#manual-testing-of-user-stories)
    - [Automated testing](#automated-testing)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Configuration](#configuration)
    - [Google emails](#google-emails)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## About

Guess the boozer is a social media game to play with friends, the object of the game is to guess what pub,bar,resteraunt your friends are in based on their vague images and hints, this is a game that my friends and I personaly Play most weekends and by creating guess the boozer we will bring the game to a wider audience.

## User Goals

Register and Login to a new Social media site.

Join in on the fun and Create posts and give hints to other users so they can try tio guess where i am or have been.

guess where other users are or have been using the information they supply.


## Site Owner Goals

Create a platform for people to connect with eachother

Implement a gaming/puzzel aspect to the social media site

Spread awareness about new, fun, diffrent bars/pubs and resteraunts


## User Experience

### Target Audience

People who enjoy socialising.

People who enjoy puzzels.

People who enjoy gaming.

### User Requirements

Easy navigation, familiar layout and UX/UI design.

Easy to use.

Responsive layout for users on all devices.

User feedback from user actions.

Constant stream of new content from other users.

Ability to connect with other users.

Ability to share posts, connect and converse with other users.

Dedicated Page/blog to advertise and support businesses and inform users of updates to the site and any other relavant news.


## User Stories


### site Owner

user search bar/ list of users MUST HAVE
#24 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

create contact us form
#23 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

create a blog
#22 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

users create + view hashtags MUST HAVE
#21 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

users comment on posts MUST HAVE
#20 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

users create posts MUST HAVE
#19 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

build login/signup page MUST HAVE
#18 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

setup repository prep
#17 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

deploy to heroku prep
#16 opened on 27 Jun by RoMcGill
 PBI ITERATION 1

install django + supporting libraries
#15 opened on 27 Jun by RoMcGill
 PBI ITERATION 1


 ### Users

USER STORY should be able to log into my account MUST HAVE
#1 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY have a log in page MUST HAVE
#2 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY have an explore page COULD HAVE
#3 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY have a personal profile COULD HAVE
#4 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY be able tom follow other users SHOULD HAVE
#6 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY add gps location of solved boozers COULD HAVE
#7 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY add photos to posts COULD HAVE
#8 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY comment on other users posts COULD HAVE
#9 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY view other users posts COULD HAVE
#10 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY upload details of recent trips to the pub/resteraunt COULD HAVE
#11 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY discover more unique bars and restaurants near me MUST HAVE
#12 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY find good pubs, bars, restaurants local to me MUST HAVE
#13 opened on 22 Apr by RoMcGill
 PBI ITERATION 1

USER STORY : connecting people who enjoy socialising and puzzels MUST HAVE
#14 opened on 22 Apr by RoMcGill
 PBI ITERATION 1



## Design

## Colours
the colour scheme was chosen as there is a nice contrast between diffrent elements which makes for a pleasurable user experience also the colour schem plays a role in helping the user feel familiar with the site as the gradient used is similar to instagram just with the colours changedm, the fade from dark green to bright green in the background is like instagrams gradient from dark purple to bright pink.

## Fonts
***all fonts are standard at the time of writing this.***


## Structure
ease of use was the goal for this site. the navagation bar at ther top of the page provides easy clikable links to each section of the site, from there you can dive deeper into other features of the site.

## Website pages
The website is made up of the following pages:
Home page/feed this page is your landing page once logged in and will propt you to update your profile information and instruct you what to do next, following these instructions you will find other users and populate this page with there posts after following some users.
Register page, this is where a user can create an account.
Login page, on this page users can login to their account.
search page, this page will show users a list of other users and provide a button to search for users by name.
Logout page allowing user to log out of the website, this page will also provide the user with an option to log back in.
Profile page where users can add their profile picture first/last name, bio and website. This page will display thier profile image,bio, name, posted posts and favourited posts. If a user is on another users Profile they will not have the option to edit their profile but will have an option to follow the user in its place.
post detail page is used for specific posts that a user clicks on, this page will show all of the details of a given post and also provide a button to view the comments and post/delete a comment, view the hashtags and likes associated with the post.
the tags page is where all posts with corrisponding tags are displayed.
the favourites page is in the profile page and when clicked the user posts will no loger show but the posts that the given user has favourited will display instead.
the cooment page/modal is used to display, post and delete comments on nay given post.
the blog page is a site owner run blog to promote businesses and provide users with information.
Contact page with contact form which allows users to send an email to the site owner and provide their feedback or questions.
***no 404 error page yet.***

## Database
The backend is built on the Django framework using Postgres for the deployed Heroku version I have created a graph model of the site using django-extensions and graphviz to display the model relationships.

<img src="/workspace/Reel/REEL_sans_foo_bar.png">

### blogpost app

the blog post model contains title, slug, intro, body, date_added, picture,
the title field contains the title of the blog post
the slug field contains the individal slug for each blog post
the intro contains a breif subject line for the blog post
the body contains the main content for the blog post
the date added contains the date and time the blog was created
the picture field contains the image that is uploaded to support the text of the blog post.

### comment app
the comment model contains post, user, body, date
The post field contains a ForeignKey to id the post.
The user field contains a ForeignKey to id the user.
The body field contains a textfield to manage user input
The date field contains contains the date and time which the comment was posted.

### contact app
the contact model contains name, email, subject, message
The name field contains the users name
The email field contains the users email address
The subject field contains the subject/ reason for contact
The message field contains the main body/contact of the correspondance.

### post app

the post app contains 5 models follow, stream, likes, post and tag

the follow model contains follower and following
both fields contain foreignkey fields to identify users.

the stream model contains following, user, post, date.
the following field contains the following status of the user.
the user field contains the id of the user.
the post field contains the data being posted by the user.
the date field contains the date and time the stream was created.

the likes model contains user and post
the user field is to identify the user id
the post field is to identify the post id

the post model contains id, picture, caption, posted, tag, user, likes
The id field contains a unique id for the post.
The picture field contains a ImageField for users to upload photos.
The caption field contains a CharField for users to uplad a caption to their post.
The posted field contains DateTimeField to capture the date and time the post was posted.
The tag field contains a ManyToManyField for the hashtags.
The user field contains a ForeignKey to identify the user.
The likes field contains a IntergerField to handle the number of likes on a post.

the tag model contains title and slug
the title field is a CgarField for users to enter thier hashtags
the slug field is a SlugField for creating unique slugs for each hashtag

### userauthentication app
the userauthentication app contains the profile model
the profile model contains 9 Fields user, first_name, last_name, location, url, profile_info, created, favourite, image
the first_name, last_name, location, url fields are all CharFields for users to input their own information.
the user field is a OnetoOneField that contains the users username.
the profile_info Field is a textfield for the user to input information about themselves.
the created field is a DateTimeField to capture when the profile has been created,
the Favourite Field is a ManyToManyField that users can have their favourite posts by them selfs or by other users saved.
the image field is a ImageField for users to upload their Profile image






## Wireframes


## Technologies Used
### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python 3.10.2
- Django 3.2

## Features


## Validation


## Testing


## Manual testing of user stories


## Automated testing


## Performing tests on various devices


## Browser compatibility


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
|29th June: tried to create user models. without having django User authentication in my imports| import from django.contrib.auth.models import User|
|4th July: could not display my deployed site on heroku anymore|there was heroku maintance which chnaged my cofig vars on heroku, I updated my env.py file with the correct information.|
|4th July: the error was cannot type cast int to uuid, cused by migrating my user model with primary key, then changing to uuid|migrate model with no primary key then migrate with uuid|
|12th July:    |     |
|    |     |
|    |     |
|    |     |
|    |     |
|    |     |
|    |     |
|    |     |
|    |     |





## Configuration


## Google emails


## Heroku Deployment
### Heroku Deployment
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "reel-2022-new") and choose your region
3. Click on create app
4. Under resources search for postgres, and add a Postgres database to the app
5. Install the plugins dj-database-url and psycopg2-binary
6. Install django and gunicorn
7. Add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
8. Create a Procfile in your app:
   ```
   wsgi:PROJECT_NAME.wsgi
   ```
   (web: gunicorn reel.wsgi)
9.  In the settings.py ensure the connection is to the Heroku postgres database
10. Ensure Debug is set to False in the settings.py file
11. Add localhost/127.0.0.1, and reel-2022-new.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
12. Go to Settings in your Heroku and set the environment variables in the Config Vars
    ![Config vars](docs/readme/heroku-config-vars.jpg)
13. Remove DISABLE_COLLECTSTATIC from Heroku settings
14. Push the code to Heroku using the command git push heroku main

Final steps:

- Go to "Deploy" in the menu bar on the top
- Deployment method: Heroku Git (direct connection to GitHub is no longer available)
- Follow steps as shown:
  ![Deployment steps](docs/readme/heroku-deployment.jpg)


### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.

### Making a Local Clone
1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open commandline interface on your computer
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard
7. Press Enter to create your local clone


## Credits


## Acknowledgements





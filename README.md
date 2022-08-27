# Guess The Boozer
**Developer: Ronan McGill**

[Visit live website](https://reel-2022-new.herokuapp.com)

[view project board](https://github.com/users/RoMcGill/projects/1) > **_NOTE:_** This project board is linked to my repository but for some reason does not show up in the projects tab in the repository

<img src="./readme-images/amiresponsive.jpg" width="800">

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
    - [Manual testing](#manual-testing-of-user-stories)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)
---
## About

Guess the boozer is a social media game to play with friends. The objective of the game is to guess what pub,bar,resteraunt your friends are in based on their vague images and hints. This is a game that my friends and I Play most weekends over whatsapp and by creating guess the boozer we will bring the game to a wider audience and promote pubs,bars and resteraunts.

----------

## User Goals

Register and Login to a new Social media site.

Join in on the fun and Create posts and give hints to other users so they can try tio guess where i am or have been.

Guess where other users are or have been using the information they supply.

----
## Site Owner Goals

Create a platform for people to connect with eachother

Implement a gaming/puzzel aspect to the social media site

Spread awareness about new, fun, diffrent bars/pubs and resteraunts

----

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

----
## User Stories

### site Owner


User search
#25

Create contact us form
#24

Create a blog
#23

Users can create hashtags and view posts with same hashtags on one page
#22

Users can Comment on posts
#21

Users can create posts
#20

Build login/signup page
#1

Setup repository prep
#3

Deploy to heroku prep
#2

Install django + supporting libraries
#4

### Users

USER STORY  Create Post
#27

USER STORY  Be able to Like posts
#26

USER STORY  contact site owner
#19

USER STORY should be able to log into my account
#5


USER STORY have a log in page MUST HAVE
#6


USER STORY have an explore page
#7


USER STORY have a personal profile
#8


USER STORY a buy and sell section of the fourm.
#10


USER STORY be able tom follow other users
#9


USER STORY add gps location of solved boozers
#11


USER STORY add photos to posts
#12


USER STORY comment on other users posts
#13


USER STORY view other users posts
#14


USER STORY upload details of recent trips to the pub/resteraunt
#15


USER STORY discover more unique bars and restaurants near me
#16


USER STORY find good pubs, bars, restaurants local to me
#17


----


## Design

## Colours
<img src="./readme-images/Screenshot 2022-08-26 at 23.25.19.png">
The colour scheme was chosen as there is a nice contrast between diffrent elements which makes for a pleasurable user experience. The colour scheme plays a role in helping the user feel familiar with the site as the gradient used is similar to instagram just with diffrent colours. The fade from dark green to bright green in the background is like instagrams gradient from dark purple to bright pink.


## Fonts
The fonts implemented on the site are Fira sans with sans-serif as a fallback. The fonts were used thoughout the site to add charachter, style and legibility


## Structure
Ease of use was the goal for this site. the navagation bar at ther top of the page provides easy clikable links to each section of the site, from there you can dive deeper into other features of the site.

### Website pages
### The website is made up of the following pages:

### Home page/feed
This page is your landing page once logged in and will prompt you to update your profile information and instruct you what to do next, following these instructions you will find other users and populate this page with their posts after following some users.

### Register page
This is where a new user can create an account.

### Login page
On this page users can login to their account.

### search page
This page will show users a list of other users and provide a button to search for users by name.

### Logout page
This page will allow users to log out of the website, this page will also provide the user with an option to log back in.

### Profile page
This is where users information is shown. Users can add their profile picture first/last name, bio and website. This page will display thier profile image,bio, name, posted posts and favourited posts. If a user is on another users Profile page they will not have the option to edit their profile from there but will have an option to follow the user in its place.

### post detail page
This page is used for specific posts that a user clicks on, this page will show all of the details of a given post and also provide a button to view the comments and post/delete a comment, view the hashtags and likes associated with the post.

### the tags page
This page is where all posts with corrisponding tags are displayed.

### the favourites page
This page is located in the profile page and when clicked the user posts will no loger show but the posts that the given user has favourited will display instead.

### the comment page/modal
This page is used to display, post and delete comments on nay given post.

### the blog page
This page is a site owner run blog to promote businesses and provide users with information.

### Contact page
This page displays a contact form which allows users to send an message to the site owner and provide their feedback or questions.

### 404 error page
This page is used in place of a standard 404 page. It will be shown in the event of an error which does not allow the page to loadT
----


## Database
The backend is built on the Django framework using Postgres for the deployed Heroku version I have created a graph model of the site using django-extensions and graphviz to display the model relationships.

<img src="./readme-images/REEL_sans_foo_bar.png">

### blogpost app

The blog post model contains title, slug, intro, body, date_added, picture,
The title field contains the title of the blog post
The slug field contains the individal slug for each blog post
The intro contains a breif subject line for the blog post
The body contains the main content for the blog post
The date added contains the date and time the blog was created
The picture field contains the image that is uploaded to support the text of the blog post.

### comment app
The comment model contains post, user, body, date
The post field contains a ForeignKey to id the post.
The user field contains a ForeignKey to id the user.
The body field contains a textfield to manage user input
The date field contains contains the date and time which the comment was posted.

### contact app
The contact model contains name, email, subject, message
The name field contains the users name
The email field contains the users email address
The subject field contains the subject/ reason for contact
The message field contains the main body/contact of the correspondance.

### post app

The post app contains 5 models follow, stream, likes, post and tag

The follow model contains follower and following
both fields contain foreignkey fields to identify users.

The streTm model contains following, user, post, date.
The following field contains the following status of the user.
The user field contains the id of the user.
The post field contains the data being posted by the user.
The date field contains the date and time the stream was created.

The likes model contains user and post
The user field is to identify the user id
The post field is to identify the post id

The post model contains id, picture, caption, posted, tag, user, likes
The id field contains a unique id for the post.
The picture field contains a ImageField for users to upload photos.
The caption field contains a CharField for users to uplad a caption to their post.
The posted field contains DateTimeField to capture the date and time the post was posted.
The tag field contains a ManyToManyField for the hashtags.
The user field contains a ForeignKey to identify the user.
The likes field contains a IntergerField to handle the number of likes on a post.

The tag model contains title and slug
The title field is a CgarField for users to enter thier hashtags
The slug field is a SlugField for creating unique slugs for each hashtag

### userauthentication app
The userauthentication app contains the profile model
The profile model contains 9 Fields user, first_name, last_name, location, url, profile_info, created, favourite, image
The first_name, last_name, location, url fields are all CharFields for users to input their own information.
The user field is a OnetoOneField that contains the users username.
The profile_info Field is a textfield for the user to input information about themselves.
The created field is a DateTimeField to capture when the profile has been created,
The Favourite Field is a ManyToManyField that users can have their favourite posts by them selfs or by other users saved.
The image field is a ImageField for users to upload their Profile image

----

## Wireframes
<details>
<summary>Edit profile</summary>
<img src="./readme-images/wireframes/wireframe1.jpg">
</details>

<details>
<summary>Register</summary>
<img src="./readme-images/wireframes/wireframe2.jpg">
</details>

<details>
<summary>Login</summary>
<img src="./readme-images/wireframes/wireframe3.jpg">
</details>

<details>
<summary>Logout</summary>
<img src="./readme-images/wireframes/wireframe4.jpg">
</details>

<details>
<summary>Index</summary>
<img src="./readme-images/wireframes/wireframe5.jpg">
</details>

<details>
<summary>Blog</summary>
<img src="./readme-images/wireframes/wireframe6.jpg">
</details>

<details>
<summary>Contact us</summary>
<img src="./readme-images/wireframes/wireframe7.jpg">
</details>

<details>
<summary>Search</summary>
<img src="./readme-images/wireframes/wireframe8.jpg">
</details>

<details>
<summary>Feed</summary>
<img src="./readme-images/wireframes/wireframe9.jpg">
</details>

<details>
<summary>Profile</summary>
<img src="./readme-images/wireframes/wireframe10.jpg">
</details>


----

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python 3.10.2
- Django 3.2

### Libraries & Tools
Am I Responsive - Was used to create the multi screen display at the top of this document.

Cloudinary - Was used to manage Images/Media.

Favicon.io - Was used to create The Favicon.

Chrome dev tools - Was used to test the responsiveness of the site and generate lighthouse reports.

Gitpod
GitHub - Was used to write and host the code for this project .

CrispyForms- Was used to manage Django forms.

Google Fonts

django_extentions - Was used in conjunction with graphviz to create my database diagram.

Heroku - Was used to Deploy The finished product.

jQuery and Bootstrap - Was used for creating fast and responsive html pages.

Postgres – Was used for database management.

gunicorn - Was used for running multiple Python processes within a single dyno.

Pillow - Was used to add support for opening, manipulating, and saving images.

psycopg2 - Was used to perform operations on postgres.

Balsamiq - Was used to generate the wireframes for the site.

----

## Features

### Nav bar
- Part of base.html
- Visible on all pages
- Fully responsive
- Features included on the nav bar will be diffrent for logged in users and logged out users as logged out users do not have access to as many Features as logged in users.
- Easy to navigate
<details>
<summary>screenshot</summary>
<img src="./readme-images/loged-out-features/nav.png">
<img src="./readme-images/loged-out-features/nav-res.png">
<img src="./readme-images/loged-out-features/nav-menu-res.png">
</details>

### Register
- page for  new users to create their account
- Easy to follow
- User must provide a valid username, password and password confirmation and email address

<details>
<summary>screenshot</summary>
<img src="./readme-images/loged-out-features/register.png">
<img src="./readme-images/loged-out-features/regester-res.png">
</details>

### Login
- Page for users to log in to their account
- Easy to follow
- User must fill out 2 form fields Username and Password
- Logged in user will be redirected to  the feed and have access to all features
- User story [#1](https://github.com/RoMcGill/Reel/issues/1), User story [#6](https://github.com/RoMcGill/Reel/issues/6)

<details>
<summary>screenshot</summary>
<img src="./readme-images/loged-out-features/login.png">
<img src="./readme-images/loged-out-features/login-res.png">
</details>

### Create/edit profile
- Easy to follow form
- gives users the option to add a personal profile picture, first name, last name, bio, location and website
- Once form is submitted users will be redirected to their updated profile page
- [#8](https://github.com/RoMcGill/Reel/issues/8)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/edit.png">
<img src="./readme-images/logged-in-features/edit-res.png">
</details>


### Add Post
- Easy to follow form
- users can add a picture, caption and hashtag/'s
- this will be displayed on a card as a post
- Once form is complete users will be redirected to their profile page where the post will show, thier new post will also show up in the Feed
- [#27](https://github.com/RoMcGill/Reel/issues/27), [#22](https://github.com/RoMcGill/Reel/issues/22),[#15](https://github.com/RoMcGill/Reel/issues/15)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/newpost.png">
<img src="./readme-images/logged-in-features/newpost-res.png">
</details>

### Search for users
- The search page will Provide a List of all of the users
- The search page has a search button where users can type in the names of their friends and have their profile show
- [#25](https://github.com/RoMcGill/Reel/issues/25), [#18](https://github.com/RoMcGill/Reel/issues/18)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/search.png">
<img src="./readme-images/logged-in-features/search-res.png">
<img src="./readme-images/logged-in-features/search-result.png">
<img src="./readme-images/logged-in-features/res-search-result.png">
</details>

### View Users Profiles
- Users can access other users Profiles in 2 ways
- The search Feature or through the Feed: each post will have a clickable link to the users Profile

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/profile.png">
<img src="./readme-images/logged-in-features/profile-res.png">
</details>

### Follow Users
- Once in another users profile users will have the option to follow or unfollow a user
- if a user is not following the user the follow button will apear
- if a user is following the user the unfollow button will apear
- [#9](https://github.com/RoMcGill/Reel/issues/9)


<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/follow.png">
<img src="./readme-images/logged-in-features/follow-res.png">
<img src="./readme-images/logged-in-features/unfollow.png">
<img src="./readme-images/logged-in-features/unfollow-res.png">
</details>

### Like users posts
- Users can like other users posts from the feed
- If  a user likes a post they will be redirected to the post details page
- If a user has already liked a post and clicks the like button again it will unlike the post
- [#26](https://github.com/RoMcGill/Reel/issues/26)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/like.png">
<img src="./readme-images/logged-in-features/unlike.png">
</details>

### Comment on users posts
- Users can comment on other users post
- simple and familiar comment form
- [#21](https://github.com/RoMcGill/Reel/issues/21), [#13](https://github.com/RoMcGill/Reel/issues/13)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/comment.png">
<img src="./readme-images/logged-in-features/res-comment.png">
</details>

### Delete comments you have made

- Users can delete comments they have made at any time
- once pomment is posted a button will apear under each comment posted by the user giving them an option to delete the comment

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/delete-comment.png">
</details>

### Add users posts to favourites
- Users can add other users posts to their favourites
- favourites will show up in place of users posts on their profile when favourites is clicked

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/fav-in-profile.png">
<img src="./readme-images/logged-in-features/res-fav-in-profile.png">
</details>

### View feed
- logged in Users will see posts from other users on their feed
- familiar layout of posts Simialr to instagram
- [#14](https://github.com/RoMcGill/Reel/issues/14), [#7](https://github.com/RoMcGill/Reel/issues/7)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/feed.png">
<img src="./readme-images/logged-in-features/res-feed.png">
</details>

### View Hashtag page's
- Users can see hashtags at the bottom of other users posts
- To view a page for that hashtag and see other posts that use it, the user needs to click on the hashtag and they will be redirected to the page
- [#22](https://github.com/RoMcGill/Reel/issues/22)

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/tag.png">
<img src="./readme-images/logged-in-features/tag-res.png">
</details>

### Blog
- Logged in and logged out users can view the blog
- Blog posts created by admin
- [#23](https://github.com/RoMcGill/Reel/issues/23), [#16](https://github.com/RoMcGill/Reel/issues/16)

<details>
<summary>screenshot</summary>
<img src="./readme-images/loged-out-features/blog.png">
<img src="./readme-images/loged-out-features/blog-res.png">
</details>

### Contact
- Simple contact form
- 4 fields, name, email, subject, message
- User messages sent straight to admin
- [#24](https://github.com/RoMcGill/Reel/issues/24), [#19](https://github.com/RoMcGill/Reel/issues/19)

<details>
<summary>screenshot</summary>
<img src="./readme-images/loged-out-features/contact.png">
<img src="./readme-images/loged-out-features/contact-res.png">
</details>

### Log out
- Button located in navbar
- Logout page has clear message user has been logged out
- Gives user an option to log back in

<details>
<summary>screenshot</summary>
<img src="./readme-images/logged-in-features/logout.png">
<img src="./readme-images/logged-in-features/res-logout.png">
</details>
-------

## Validation
### Chrome Dev Tools Lighthouse
Lighthouse was used to test the performance, accessibility, best practice and SEO of the site.

<details>
<summary>Edit profile</summary>
<img src="./readme-images/lighthouse/lighthouse-edit-profile.jpg">
</details>

<details>
<summary>Register</summary>
<img src="./readme-images/lighthouse/lighthouse-register.jpg">
</details>

<details>
<summary>Login</summary>
<img src="./readme-images/lighthouse/lighthouse-login.jpg">
</details>

<details>
<summary>Logout</summary>
<img src="./readme-images/lighthouse/lighthouse-logout.jpg">
</details>

<details>
<summary>Index</summary>
<img src="./readme-images/lighthouse/lighthouse-index.jpg">
</details>

<details>
<summary>Blog</summary>
<img src="./readme-images/lighthouse/lighthouse-blog.jpg">
</details>

<details>
<summary>Contact us</summary>
<img src="./readme-images/lighthouse/lighthouse-contact.jpg">
</details>

<details>
<summary>Search</summary>
<img src="./readme-images/lighthouse/lighthouse-search.jpg">
</details>

<details>
<summary>Feed</summary>
<img src="./readme-images/lighthouse/lighthouse-feed.jpg">
</details>

<details>
<summary>Profile</summary>
<img src="./readme-images/lighthouse/lighthouse-profile.jpg">
</details>

----

### HTML

I used The W3C Markup Validation Service to validate the HTML of the website, some changes had to be made to account for the validation service not recognising django static tags.

<details>
<summary>Contact us</summary>
<img src="./readme-images/html-validator/contact-us.png">
</details>

<details>
<summary>Edit Profile</summary>
<img src="./readme-images/html-validator/edit-profile.png">
</details>


<details>
<summary>Feed</summary>
<img src="./readme-images/html-validator/feed.png">
</details>


<details>
<summary>Login</summary>
<img src="./readme-images/html-validator/login.png">
</details>


<details>
<summary>Logout</summary>
<img src="./readme-images/html-validator/logout.png">
</details>


<details>
<summary>Profile</summary>
<img src="./readme-images/html-validator/profile.png">
</details>


<details>
<summary>New Post</summary>
<img src="./readme-images/html-validator/newpost.png">
</details>


<details>
<summary>Post Details/Comments</summary>
<img src="./readme-images/html-validator/post-details-and-comments.png">
</details>


<details>
<summary>Register</summary>
<img src="./readme-images/html-validator/register.png">
</details>


<details>
<summary>Search</summary>
<img src="./readme-images/html-validator/searchbar.png">
</details>


<details>
<summary>Tags</summary>
<img src="./readme-images/html-validator/tags.png">
</details>

----

### CSS

I used the  W3C Jigsaw CSS Validation Service to validate the CSS of my website. When validating all of my css on the site, it passes with no errors.

<details>
<summary>CSS</summary>
<img src="./readme-images/css-validation/css.png">
</details>

----

### JavaScript Validation

I used JSHint JS Validation Service to validate my Javascript files. No errors were found.

<details>
<summary>Java Script</summary>
<img src="./readme-images/js-validation/js.png">
</details>


----

### PEP8 Validation
I used PEP8 Validation Service to check the code for PEP8 requirements. All the code passes with no errors and no warnings to show Bar one url file that one line was 2 charachters too log, I decided to leave it as when it was formated to meet requirements it was less legible

### Blog

<details>
<summary>Models</summary>
<img src="./readme-images/blog-pep8/blog-models.png">
</details>

<details>
<summary>Admin</summary>
<img src="./readme-images/blog-pep8/blog-admin.png">
</details>

<details>
<summary>Url</summary>
<img src="./readme-images/blog-pep8/blog-url.png">
</details>

<details>
<summary>Views</summary>
<img src="./readme-images/blog-pep8/blog-views.png">
</details>

### Comment

<details>
<summary>Models</summary>
<img src="./readme-images/comment-pep8/comment-model.png">
</details>

<details>
<summary>Admin</summary>
<img src="./readme-images/comment-pep8/comment-admin.png">
</details>

<details>
<summary>Url</summary>
<img src="./readme-images/comment-pep8/comment-url.png">
</details>

### Search

<details>
<summary>Views</summary>
<img src="./readme-images/search-pep8/search-views.png">
</details>

<details>
<summary>Url</summary>
<img src="./readme-images/search-pep8/search-url.png">
</details>


### Contact us

<details>
<summary>Models</summary>
<img src="./readme-images/contact-pep8/contact.models.png">
</details>

<details>
<summary>Views</summary>
<img src="./readme-images/contact-pep8/contact-views.png">
</details>

<details>
<summary>Url</summary>
<img src="./readme-images/contact-pep8/contact-url.png">
</details>

<details>
<summary>Admin</summary>
<img src="./readme-images/contact-pep8/contact.admin.png">
</details>

### Post


<details>
<summary>Url</summary>
<img src="./readme-images/post-pep8/post-urls.png">
</details>

<details>
<summary>Admin</summary>
<img src="./readme-images/post-pep8/post-admin.png">
</details>

<details>
<summary>Form</summary>
<img src="./readme-images/post-pep8/post-form.png">
</details>

<details>
<summary>Models</summary>
<img src="./readme-images/post-pep8/post-models.png">
</details>

<details>
<summary>Views</summary>
<img src="./readme-images/post-pep8/post-views.png">
</details>

### Userauthentication

<details>
<summary>Models</summary>
<img src="./readme-images/userauth-pep8/userauth-models.png">
</details>

<details>
<summary>Admin</summary>
<img src="./readme-images/userauth-pep8/userauth-admin.png">
</details>

<details>
<summary>Form</summary>
<img src="./readme-images/userauth-pep8/userauth-form.png">
</details>

<details>
<summary>Url</summary>
<img src="./readme-images/userauth-pep8/userauth-url.png">
</details>

<details>
<summary>Views</summary>
<img src="./readme-images/userauth-pep8/userauth-views.png">
</details>

### Members

<details>
<summary>Views</summary>
<img src="./readme-images/members-pep8/members-views.png">
</details>

<details>
<summary>Url</summary>
<img src="./readme-images/members-pep8/members-url.png">
</details>

<details>
<summary>Models</summary>
<img src="./readme-images/members-pep8/members-models.png">
</details>

<details>
<summary>Form</summary>
<img src="./readme-images/members-pep8/members-form.png">
</details>

---
## Testing
### Manual testing

I performed manual testing throughout the whole prcess of building this site, I also took into account my user storys while creating my manual testing plan.


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|from landing page Register a new account <sup>User Story #1,5</sup> |new account would be created| new account created and welcome message apears letting me know I have created an account|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/loged-out-features/register.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Login as New user <sup>User Story #6</sup>| have acccess to the rest of the features on the site|all sites features are available once user is logged in.|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/loged-out-features/login.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Setup profile <sup>User Story #8</sup>|have the ability to personalise my profile|users can add their own personal profile picture, firstname, last name, bio, location and website|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/edit.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|create a post <sup>User Story #20, #27</sup>|to be able to create a post that other users can see and interact with|post created with picture, hashtag, and caption with the ability for other users to like comment and favourite it.|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/newpost.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|browse the feed <sup>User Story #14, #17, #7</sup>|see other users posts|the ability to see other users posts and interact with them|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/feed.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|search for other users <sup>User Story #25</sup>|see a list of other users|a list of users + a searchbar to search for specific users|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/search.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|follow other users <sup>User Story #9</sup>|be able to follow other users|ability to follow users and have it reflect in the number of users on both profiles|


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|browse other users posts on other users profile <sup>User Story #13, #8</sup>|list of posts on users profile page|list of posts displayed on users profile|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/profile.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|add other users posts to my favourites|add posts to a favourite folder|favorited posts go into a page on my profile for anyone to see if they click the favourites button beside the the posts button|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/fav-in-profile.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|like other users posts <sup>User Story #26</sup>|users will see that I have liked other users post|the number of likes on a post raises by 1 every time a user likes it|



**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|unlike a post|the like will go away| the number of likes on the post droped by 1|


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|comment on other users posts <sup>User Story #13</sup>|comment will show up under post|comment is displayed in the post details which can be accessed through the feed or users profile or anywhere the post is on the site|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/comment.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|delete my comments <sup>User Story #13</sup>|.button to remove comments posted by me|button below my comments deletes them and shows a message confirming i delketed the comment|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/delete-comment.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|search the hastags from other users posts <sup>User Story #22</sup>|look at what hashtags people are posting on other users posts and click them to see other users popularity|all posts with the same hashtags are displayed to get to that page just click the hashtag you want to see|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/tag.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|look at other users favorited posts|click other users favourites button and see a list of other users favourite posts|favourites are displayed in place of the users posts when the favourite button is clicked|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/fav-in-profile.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|contact the site owner <sup>User Story #24, #19</sup>|enter in my information an messsage and send message|message sent and message apears to confirm I have sent a message to site owner|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/loged-out-features/contact.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|read the site owners blog <sup>User Story #23, #16</sup>|see a list of blog posts|blog posts are displayed on the blog page|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/loged-out-features/blog.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|logout of my account|not be able to access some of the sites features|log out stops users from being able to see some site features|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/logout.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|log back in<sup>User Story #1, #6</sup>|be able to click a button to log back in |there is an option to log back in once logged out|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/logout.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|edit/ update my profile <sup>User Story #8</sup>|edit my profile and update/change some information|all updated information changes instantly and a message apears to confirm I have updated my profile|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/logged-in-features/edit.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|login on a mobile device|be able to login to my account |all features available on the desktop site are available on mobile|
<details>
<summary>Screenshot</summary>
<img src="./readme-images/loged-out-features/login-res.png">
</details>


**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
|re trace all steps taken again on mobile device|all steps work the same as on desktop site|all steps work the same as on desktop site|


## Performing tests on various devices

The website was tested using Google Chrome Developer Tools on all devices available asell as the sesponsive toggle where you can drag to your prefered screensize. I also tested all available screen sizes on responsinator.com and amiresponsive.com

The website was tested on the following devices:

MacBook Pro
Samsung Galaxy s21 ultra
Samsung Galaxy Tab2


## Browser compatibility
Testing has been carried out on the following browsers:

google chrome Version 103.0.5060.53 (Official Build) (x86_64)

Safari Version 14.1.2 (14611.3.10.1.7)

Samsung Internet Version (18.0.0.58)

----

## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
|29th June: tried to create user models. without having django User authentication in my imports| import from django.contrib.auth.models import User|
|4th July: could not display my deployed site on heroku anymore|there was heroku maintance which chnaged my cofig vars on heroku, I updated my env.py file with the correct information.|
|4th July: the error was cannot type cast int to uuid, cused by migrating my user model with primary key, then changing to uuid|migrate model with no primary key then migrate with uuid|
|7th July: issue with database|reset database, still was not working, started new repo from scratch <details><summary>Tutor support chat log</summary>https://docs.google.com/document/d/16XlYW9u0hWma5bD7lxAs2pWkMaWi_GtUyotDagPRKVg/edit?usp=sharing</details>|
|12th July:heroku not showing anything| created runtime txt file and moved my procfile to be in the same app as manage.py|
|12th July: I cannot create a post with a hashtag that has already been created|I was using title unique =True so i removed that, and added it to my SlugField which is where it was supposed to be all along.|
|12th July:After Heroku deployment, no css shown on deployed site|installed whitenoise middleware to serve static files for production, later installed cloudinary.|
|26th July:comments working in post-details but not in profile or index|(unconventional fix) instead of displaying comments on index + profile I linked the post-details to Post and index.|
|27th July: template for login/logout not showing|create templates folder with login/logout html files directly in members app|
|2nd August:profile details not displaying|my model for profile details had an field called bio but i was showing profile-info in my view, made them both the same and it worked|
|22nd August:logout button was not logging user out| created a logout function in members.views|
|TBA: getting a success message when user logs in|have tried placing the success message after the function to login, before it redirects and after but still no message shown.|

----

## Heroku Deployment

This Django application has been deployed from GitHub to Heroku by following the steps:

Installing Django and deploying to heroku

- 1. In the Terminal: Install Django and gunicorn: pip3 install 'django<4' gunicorn
- 2. In the Terminal: Install supporting libraries: pip3 install dj_database_url psycopg2
- 3. In the Terminal: Install Cloudinary Libraries pip3 install dj3-cloudinary-storage
- 3. In the Terminal: Create requirements file pip3 freeze --local > requirements.txt
- 4. In the Terminal: Create Project (Reel): django-admin startproject Reel.
- 5. In the Terminal: Create App (blog) python3 manage.py startapp Post
- 6. Settings.py: Add to installed appsINSTALLED_APPS = ['Reel',] *Save file*
- 7. In the Terminal: Migrate Changes: python3 manage.py migrate
- 8. In the Terminal: Run Server to Test python3 manage.py runserver

Step 2: Deploying an app to Heroku

- 2.1 Create the Heroku app In heroku.com: create account/ login
- 2.2 Create new Heroku App Reel, Location = Europe
- 2.3 Add Database to App Resources Located in the Resources Tab, Add-ons, search and add e.g. ‘Heroku Postgres’
- 2.4Copy DATABASE_URL value: Located in the Settings Tab, click reveal Config Vars, Copy Text
- 2.5 Attach the Database: In gitpod, Create new env.py file on top level directory
- 2.6 In env.py Import os library, import os
- 2.7 Set environment variables os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
- 2.8. Add in secret key os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
- 2.9 In heroku.com: Add Secret Key to Config Vars SECRET_KEY, “randomSecretKey”

step 3: Prepare environment and settings.py file
- 3.1 In settings.py: Reference env.py from pathlib import Path, import os, import dj_database_url
```
if os.path.isfile("env.py"):
   import env
```
- 3.2 Remove the insecure secret key and replace - links to the SECRET_KEY variable on HerokuSECRET_KEY = os.environ.get('SECRET_KEY')
- 3.2 Comment out the old DataBases Section
- 3.3 Add new DATABASES Section
```
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
3.4 In the Terminal: Save all files and Make Migrations
```
$python3 manage.py migrate
```
- 3.5 Get  static and media files stored on Cloudinary In Cloudinary.com: register/login
- 3.6 Copy your CLOUDINARY_URL e.g. API Environment Variable. From Cloudinary Dashboard Into  env.py:
- 3.7 Add Cloudinary URL to env.py
```
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
```
- 3.8 In Heroku: Add Cloudinary URL to Heroku Config Vars Add to Settings tab in Config Vars e.g. COUDINARY_URL, cloudinary://************************
- 3.9 Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment)e.g. DISABLE_COLLECTSTATIC, 1
- 4.0 In settings.py: Add Cloudinary Libraries to installed apps
```
INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    …,
]
```
- 4.1. Tell Django to use Cloudinary to store media and static files
Place under the Static files Note
```
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
- 4.2 Link file to the templates directory in Heroku Place under the BASE_DIR line
```
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```
- 4.3 Change the templates directory to TEMPLATES_DIR, Place within the TEMPLATES array
- 4.4 Add Heroku Hostname to ALLOWED_HOSTS
```
ALLOWED_HOSTS = ["reel.herokuapp.com", "localhost"]
```
- 4.5 In Gitpod: Create 3 new folders on top level directory media, static, templates
- 4.6 Create procfile on the top level directory
- 4.7 In Procfile: Add code web: gunicorn Reel.wsgi
- 4.8 In the Terminal: Add, Commit and Push
- 4.9 In Heroku: Deploy Content manually through heroku
- 5.0 in heroku: setup and configure automatic deployments linked to Github account


-----


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

-----

## Credits
### helpfull links I relied on

Finding the cause and solution to bugs
- https://stackoverflow.com/
Inspiration for buttons and forms
- https://codepen.io/
Docs to find out how to do diffrent operations in django
- https://docs.djangoproject.com/en/4.1/
Docs to find out how to do diffrent operations in bootstrap
- https://getbootstrap.com/docs/4.1/getting-started/introduction/
Quick, Easy tutorials for almost everything
- https://www.w3schools.com/
Great Front-end tips and tricks
- https://thesassway.com/
Helpful for python related tutorials
- https://realpython.com/tutorials/django/
Refresh memory on subjects already covered
- Code Institute course material

### Video Tutorials
Navigation
- https://www.youtube.com/watch?v=ZzQdVy8b8n4&t=1s
- https://www.youtube.com/watch?v=OFKBep95lb4
Django app setup with helpful timestamps
- https://www.youtube.com/watch?v=rHux0gMZ3Eg
Making and saving favourite post
- https://www.youtube.com/watch?v=K5ksJVq5qGw&list=PL_KegS2ON4s7aVgtk-UI6jaXazt6KyntZ&index=8
Like and Dislike
- https://www.youtube.com/watch?v=u8zMLHAaDXY&list=PL_KegS2ON4s7aVgtk-UI6jaXazt6KyntZ&index=7
Django refresher
- https://www.youtube.com/watch?v=0sMtoedWaf0
User authentication
- https://www.youtube.com/watch?v=CTrVDi3tt8o&t=976s
Cloudinary install
- https://www.youtube.com/watch?v=JV_GoKqj1mg&t=283s
Heroku deployment
- https://www.youtube.com/watch?v=6DI_7Zja8Zc

-----

## Acknowledgements
My class mates and the students of Code Institute.

My Cohort facilitator Kasia for all of her help and encouragement throughout the project.

My Mentor Mo for keeping me on schedual and giving helpfull feedback throughout the Project.

The stackoverflow community for responding to questions and having built up a massive database of invaluable tips,tricks and bug fixes.

Code Institute for supplying an amazing course, from the content to the staff and alumni.




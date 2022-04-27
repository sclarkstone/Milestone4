# RUN YOUR WAY
--------------- TURN DEBUG TO FALSE --------------------------------

The live link can be found here - [site link](https://milestone4-sclarkstone.herokuapp.com/)

This site is targeted at people who are looking to reach specific distance goals. The site offers merchandise and running plans where a registered account is required to purchase the plans so that the detailed plans can be accessed. Honest reviews for each product and plan is encouraged and reviews can be read by other users.  

![Mock up screen shots](https://res.cloudinary.com/dyx1tw86r/image/upload/media/ScreenMockUpsFinal.png)

## User experience (UX)

### Strategy
### Scope
#### User stories
### Structure
### Skeleton
### Surface
* Following the C.R.A.P (consistancy, repetition, alignment and proximity) design methodology the pages will all have the same nav bar, footer and color scheme. This will help create a positive user experience.

## Design and features
## Testing
* [Chrome developer tools](https://developer.chrome.com/docs/devtools/) on the browser was used to see any errors on the pages.
* [Chrome developer tools](https://developer.chrome.com/docs/devtools/) device toggle toolbar was utilised to view the site via emulators of different screen sizes and devices.
* Chrome Lighthouse audit (attempt 1) (Chrome -> dev tools -> Lighthouse) was run to for performance, accessibility, SEO and best practices. On the first attempt the accesibility, best practices and SEO were in the orange. So the following amendments were made follwing the recommendations;
    
    * Accessibility - Links do not have a discernible name - add title text and aria-hidden="true" to the font aweseome social mead icons in the footer.
    * Accessibility - Buttons do not have an accessible name - add name text to the search button.
    * Accessibility - Heading elements are not in a sequentially-descending order - removed the un used h4 around the homepage button.
    * Best Practices - Includes front-end JavaScript libraries with known security vulnerabilities - updated jquery CDN from version 3.4.1 to 3.6.0
    * Accessibility - Background and foreground colors do not have a sufficient contrast ratio. amended the card template to have a darker background so the ahref text is compliant.
    * SEO - document does not have a meta description. Added a meta name="description" inside the head of the base template.

* Chrome Lighthouse audit (attempt 2) (Chrome -> dev tools -> Lighthouse) was run to for performance, accessibility, SEO and best practices. On the second attempt all categories scored in the green.
![LighthouseAudit](https://res.cloudinary.com/dyx1tw86r/image/upload/media/lighthouseAudit.png)


* JSHint was used to to detect errors and potential problems in your JavaScript code.
* Python -  using [pep8online](http://pep8online.com/) - app.py
* in Gitpod - to see all errors in all files - python3 -m flake8

### User Acceptance Testing

The UAT was carried out on desktop, tablet and mobile screen sizes. The UAT was also caried out on Chrome, firefox and Edge. This was to ensure cross broswer and cross device compatability and to acieve a positive user experience. 
* HTML - using W3C validator


* CSS - using [W3C Jigsaw](https://jigsaw.w3.org/css-validator)  By direct input - /static/css/base.css. Running the w3c validator the following message came 'Congratulations! No Error Found.'.

* JavaScript using JSHint - index.html

### First mentor meeting
* discussed the concept of the website and the best way to do the database design. Initially i was planning to have 3 seperate tables for sessions, effort and type but it was recommended that this was not needed and to combine them into one.

### Second mentor meeting
* compress all images as they were taking too long to load
* change 'products' to 'plans for plans page
* add a footer

### Third mentor meeting
* set a fixed height on the products cards so they all appear the same giving a uniform and symetrical look.
* made review subject is review details bolder
* found an error when not logged in as a user could not view product details. Needed to put an if statement around the profile_name in the product_detail view.
* use card layout for My plans and My reviews to keep layout and design consistant
* rename review_complete and review_complete2 in review view to more menaingful names (review_complete_product and review_complete_order)
* made subject and review on review form required fileds with placeholder helper text
* refactor plan_detail def in plans view to loop through days inside a parent loop of week to reduce code making it much less complicated.
* add in the desiarable features to have the recommended products what other customer purchased with the selected item
* renamed views and templates from reviews and plans to my_reviews and my_plans

### Bugs
* chrome error - jquery must be before bootstrap. the CDN link had stopped working.

* deploying to heroku - ModuleNotFoundError: No module named 'application'. amended procfile to fix
* deploying to heroku - Failed to find attribute 'app' in 'milestone4'. amended procfile to fix
* heroku - admin css not showing. in seetings file STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] corrected to STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
* django error 'Reverse for 'add_review' with no arguments not found'. Although i had the product_id parameter in the url.py, views.py and reviews.html template i had not got it in the form POST action on the add_review template itself.
* using the search - local variable 'plans' referenced before assignment error. needed the 'plans' if inside the search if
* when live on heroku - 'MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled' - corrected link on base template to use cloudinary and not local static file.
* emails stopped coming through with no errors. gmail required an app specific password, after creating these and setting at the local variables emails then began to be recived again. 

## Desirable features
* in the product_details page rather then recommended products that are fixed, to have them dynamic and based on the top 3 of what other customers purchased alongside the selected product.
* have a pace calculator to give more personalised pace ranges in the my plans

## Set up

'pip3 install Django==3.2' to install Django
'django-admin startproject milestone4 .' to set up basic folder structure and files for Django
'touch .gitignore' to create ignore file and then add to file *.sqlite3, *.pyc

'python3 manage.py runserver' to check it is runner as expected. a Django screen will appear on the browser with the message 'The install worked successfully! Congratulations!
You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.'

stop the server then 'python3 manage.py migrate'
'python3 manage.py createsuperuser', input a username (sclarkstone7153), email (samclarkstone@hotmail.com) and password (Unicorn2001)

git add .
git commit -m "commit message"
git push

### authentication set up

'pip3 install django-allauth==0.41.0'
add 'import os' to top of settings.py file

go to https://django-allauth.readthedocs.io/en/latest/installation.html and copy and paste AUTHENTICATION_BACKENDS plus 'SITE_ID = 1' and add any missing required apps to INSTALLED_APPS.

python3 manage.py migrate
'python3 manage.py runserver' to check it is runner as expected.

'pip3 freeze > requirements.txt'

### templates
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/

python3 manage.py startapp home

### font awesome
sign up for free account and get kit code. put this in the base.html template corejs block. 

### database
pip3 install pillow to allow url image use
add products to installed apps in settings.py
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
python3 manage.py loaddata categories
python3 manage.py loaddata products
tables can now be seen in admin area and data can be manually added




### Payment

#### checkout forms
* run command 'pip3 install django-crispy-forms'
* run command 'pip3 install django-countries' - for drop down of country codes

#### checkout payment
* run command 'pip3 install stripe'

#### set environment variables
* save STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET in gitpod (settings, variables) and Heroku (settings, config vars)

test card details
name - test
email - test@test.com
phone - 1234567890
address - anywhere
card number - 4242 4242 4242 4242
card date - 04/24
CVC - 242
zip - 42424
---------------
card number - 4000 0025 0000 3155
card date - 04/24
CVC - 242
zip - 44242


## Deployment
Use [Heroku] (https://www.heroku.com/) to host, first set up an account.
* heroku - add new app and provisipn postgres free
* run command 'pip3 install dj_database_url'
* run command 'pip3 install psycopg2-binary'
* run command 'pip3 install gunicorn'
* run command 'heroku login -i'. email address and use api key for password (get from heroku,account settings, reveal api key)
* run command 'config:set DISABLE_COLLECTSTATIC=1 --app milestone4-sclarkstone'
* run command 'git:remote -a milestone4-sclarkstone'
* run command 'git checkout -b master'
* run command 'git push heroku master'
* Go to [miniwebtool] (https://miniwebtool.com/django-secret-key-generator/) to get secrete key for heroku

for static files set up a [cloudinary] (https://cloudinary.com/) account
* run command 'pip3 install cloudinary'
* run command 'pip3 install django-cloudinary-storage'
* then add cloud_name, CLOUDINARY_URL, api_key and api_secret to git pod and heroku variables
* run command 'python3 manage.py collectstatic' to push static files


During development deployment method changed;
A number of user login tokens for Heroku had been compromised in a security attack. In response, Heroku have removed the automatic deployment method. 
The new method then became;
* run command 'heroku login -i' email address and use api key for password (get from heroku,account settings, reveal api key)
* run command 'heroku git:remote -a milestone4-sclarkstone'. This will link the app to your Gitpod terminal.
* run command 'git push heroku main'


## Credits

### Layout
* github - code institute/gitpod-full-template

* [Bootstrap](https://getbootstrap.com/)

    * navbar
    * grid layout with rows and columns
    * responsivness and styling
    * Cards
    * Table layout

* [Code institute](https://learn.codeinstitute.net/) course material. Specifically the Boutique Ado project for the log in, register and logout authentication and Stripe payment set up. This module was also used to inspire the fixtures and data structure along with the add, edit and delete management forms and actions.

### Content

* The icons in the forms were taken from [Font awesome](https://fontawesome.com/)

* [google fonts](https://fonts.google.com/) was used to give the project a more professional and unique feel. Google fonts gave fonts that go together and as i had already seen the Lanto font in use on the Code institute 'love running' project and felt it fit in well with my project i went with Lant and Roboto. 

* [Website Mockup Generator](https://websitemockupgenerator.com/) was used to generate the multi device website mock up used in the readme file.

* [material.io](https://material.io/resources/color/#!/?view.left=1&view.right=1&primary.color=0277bd]) was used to check accessibility of text colours on background colours. Also used to find complemetary colours. This is where i decided on my combination of white, black and grey backgrounds with complimentary text. Credit to my mentor Akshat for showing me this resource. 

### Media

* [TinyPNG] (https://tinypng.com/) was used to compress all images to reduce the load time of the site.
* [pexels] (https://www.pexels.com/) - for free use of running photos
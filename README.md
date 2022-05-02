# RUN YOUR WAY
--------------- TURN DEBUG TO FALSE --------------------------------

The live link can be found here - [site link](https://milestone4-sclarkstone.herokuapp.com/)

This site is targeted at people who are looking to reach specific distance goals. The site offers merchandise and running plans where a registered account is required to purchase the plans so that the detailed plans can be accessed. Honest reviews for each product and plan is encouraged and reviews can be read by other users.  

![Mock up screen shots](https://res.cloudinary.com/dyx1tw86r/image/upload/media/ScreenMockUpsFinal.png)

## User experience (UX)

### Strategy
* Defining the goals - Due to the global pandemic of Covid, over the last few years the number of people that has taken up running has significantly increased, this can be seen by recently published data from the popular running app, Strava. The increase in people that are new to running or people that are returning to running has lead to a huge demand for coach to 5km plans and virtual community lead running groups.   
* what is the idea? From this research i narrowed down my idea to having a site that could allow users to get running plans and merchandise and to use those plans to reach their running goals (Run Your Way) and allow users to review products, providing feedback to others.
* who is the target audience? My target audience would be all people with an interest in taking up running or to progress on their current level of running. From my reserach this was an ever expanding pool of potential users.
* why should it be created? Offering users the possibility to reach goals and review for others, encouraging others to take up the sport is a huge wellbeing bonus in a time where wellbeing and communuity support is inspirational. 

### Scope
* features and functions - several different ways to view all of the plans and products (search, filter, sort and all).
* content requirements - simple but effective. 

#### User stories
#### Admin
* Objective - what does the user want to accomplish? 
    * To view, write, edit and delete products using the product managment forms. 
* Functional - what does the user need to do to accomplish the objective? whats involved?
    * Admin can log in and have instant access to manage (view, edit and delete) all products.

#### Logged in user
* Objective - what does the user want to accomplish? 
    * To view product details.
    * To view plan details.
    * To view all reviews for products and plans.
    * To purchase products.
    * To view all users plans and products
    * To purchase any plan or products
    * To view all purchased plans
    * To write edit and delete reviews for products and plans they have purchased
    * To view all users reviews when a specific product or plan is selected
* Functional (user) - what does the user need to do to accomplish the objective? whats involved?
    * Once logged in, the 'My Plans' item on the My Account menu gives the user access to view purchased plans
    * Once logged in, the 'My Reviews' item on the My Account menu gives ther user access to edit existing reviews and to add new reviews for purchased plans and products 
    * Once logged in, all plans can be purchased.
    * No log in is required for products to be purchased.

#### Viewer
* Objective - what does the user want to accomplish? 
    * To view product details.
    * To view plan details.
    * To view all reviews for products and plans.
    * To purchase products.
* Functional - what does the user need to do to accomplish the objective? whats involved?
    * Simply visit the site. No log in required. No effort involved. Minimal clicks to get to content. Guest checkout is available for products.

### Structure
* how will content be organised and presented - site map
    * This build is based on the Course content of the Boutique Ado and the apps bag, checkout, home, profiles, products and templates remain primarily unalterted following the tutorial. The only alterations made are;
        * Products - the addition of a recommended products section on the product_details page. This displays up to 3 recommended products associated with the selected plan/product. These are added as recommended1, recommended2 and recommeneded3 into the fixtures, model and admin forms and are a foreign key to Product. 
    * Additional to this are the 2 new apps;
        * Plans - This app is for logged in users who have purchased a plan only. The my_plans and plan_details pages check that the user is logged in and has purchased a plan, using the product_id to check against the users order, itemlines. If the user meets these criteria then they can view the selected plans details which displays each days session over the specified number of weeks. The details for these plans are put together in the fixtures for Distance and Session. No admin access to add, edit or delete is required here as they are fixed plans and will not vary. 
        * Reviews - This app is used in different ways for logged in users and guests. 
            * Guests use it via the Products app when a product or plan details page is selected. A out of 5 score is shown which is an average of all the review ratings given for the selected product/plan. This can then be clocked on for further details (review_details), such as all the reviews, subjects and ratings, dates the reviews were left and the name of who left the review so that it can be seen a verified review.
            * logged in users use this app by visiting the 'My Reviews' item on the my account menu. This then shows the my_reviews page where all the reviews for the user can be seen. The reviews to be completed (add) are at the top, with the reviews already left (which can be edited or deleted) at the bottom. Giving full CRUD functionality.

### Skeleton
### Surface
* Following the C.R.A.P (consistancy, repetition, alignment and proximity) design methodology the pages will all have the same nav bar, footer and color scheme. This will help create a positive user experience.

## Design and features
## Testing
### Manual
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


* in Gitpod - to see all errors in all files - python3 -m flake8

### Automated testing
Following the 'Hello django - testing' course material videos (as advised by student services) i created automated testing for the additional apps i had created on top of the Boutique Ado template. This lead to the creation of the following files;
* reviews app
    * test_forms.py  - tests that the fields in the form that should be displayed are displayed and that all mandatory fields require an input. 
    * test_views.py - tests that the reviews_details, my_reviews, add_review and edit_review pages can be accessed and that the add_review and edit_review form submits and the delete_review functions as expected. The my_review, add_review, edit_review and delete_review check that the user is logged in.
    * test_models.py - tests the string output of Review model
* plans app
    * test_views.py - tests that the my_plans pages can be accessed as expected. The my_plans check that the user is logged.
    * test_models.py - tests the string output of Plans model
15 tests were created in total and all pass.
To run the files i ran the commmand 'python3 manage.py test'. As a result of these tests i the following issue;
    * test_views.py - reviews highlighted an issue where if you put in a url to the reviewd_details pages with a product id that did not yet have any reviews it would give an error 'type NoneType doesn't define '__round__' method' due to the review_sum calculation not working. i put an if statement around the review_sum in the review_details def in the reviews view which corrected the error.


### User Acceptance Testing

The UAT was carried out on desktop, tablet and mobile screen sizes. The UAT was also caried out on Chrome, firefox and Edge. This was to ensure cross broswer and cross device compatability and to acieve a positive user experience. 

#### Home page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Background image and font awesome social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Lanto font load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass
Search - empty|empty search gives relevant toast warning, matching search term display the related products/plans, non matching term display no products found| Empty search redirects to products page and displays all products with a toast 'You didnt enter any search cirteria'. | Pass
Search - matching criteria|matching search term to product title only and displays the relevant products/plans| search term 'tail' used, redirects to products page and displays one relevant product - tailwind| Pass
Search - matching criteria|matching search term to product title only and displays the relevant products/plans| search term 'marathon' used, redirects to products page and displays three relevant plans - half marathon (beginners), half marathon (improvers) and marathon plans.| Pass
Search - no matching criteria|non matching term redirects to products page and displays relevant message| Empty search redirects to products page and displays all products with a toast 'You didnt enter any search cirteria'. | Pass 
Internal links|internal links to remain in current window and external links to open in new tab| 'Get your plan now' link opens internal link in same window to products/?category=Plans page. Run your way logo text link opens internal link in same window to the homepage |Pass
External links|External links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic bag Content|display running total of all products currently in the bag| £0.00 displays when no items in bag. total displays when items are added and total adjusts when quantities of items are amended or removed from bag.| Pass

#### Login page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'sign up' link opens internal link in same window to Register page. footer social media links open in new tab to external relevant sites|Pass
Form - valid entry|validated responses to login|An existing username and password matching what is in the users table and redirects to the homepage|Pass
Form - invalid entry|no responses, username that does not exist or username and password not matching to users table should not login| missing values prompt the form validation. incorrect username and/or password prompts form validation message, 'The username and/or password you specified are not correct.' |Pass

#### Register page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'sign in' link opens internal link in same window to Login page. footer social media links open in new tab to external relevant sites|Pass
Form - valid entry|validated responses to create new account|a unique username and password matching the minimum requirements creates account in users table and redirects to confirm email page with a message 'verify your email address'|Pass
Form - invalid entry|no responses, responses not meeting minimum requirements or existing username should not create an account| missing values prompt the form validation. existing 'admin' username gives 'incorrect username and/or password' flash message. less then minimum length on password prompts form validation |Pass

#### My Profile page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Interal links|internal link to remain in current window| Order number links opens internal link in same window to order history page, passing through the order_number parameter. |Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|display all orders that the user has submitted. If no orders have been submitted then relevant message displayed| user (sclarkstone7153) displays the 5 orders that were submitted. User that has not submitted any endings (testytest) displays 'You dont have any orders yet. Check out the plans or the merchandise' with internal links to the products page |Pass
Form|responses to profile form updates|fileds update in the users table and stays on the profile page with a toast message 'profile updated successfully'|Pass

#### My plans page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Interal links|internal link to remain in current window| if user has not plans, link to check out 'plans' opens products/?category=Plans in same tab |Pass
External links|external links to open in new tab| footer and page social media links open in new tab to external relevant sites |Pass
Dynamic Content|display all plans that the user has purchased. If no plans have been purchased then relevant message displayed| user (sclarkstone7153) displays the 2 plans that were purchased. User that has not submitted any endings (testytest) displays 'You dont have any plans set up yet. Check out the plans to set up your first plan.' with internal link to the products page |Pass
Cards|plans details match the plans id selected to view| multiple plans selected and each plans details page then displays the correct plans details that corresponds to the plan id that was selected.|Pass

#### My reviews page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|Card images appear against the correct product_id and appear visably ok| Pass
Interal links|internal link to remain in current window| if user has not plans, link to check out 'plans' opens products/?category=Plans in same tab |Pass
External links|external links to open in new tab| footer and page social media links open in new tab to external relevant sites |Pass
Dynamic Content|display a card per product for reviews that the user has purchased a product for. If no products have been purchased then relevant message displayed| user (sclarkstone7153) displays the 13 review cards that match the purchased products. User that has not made any purchases (testytest) displays 'You dont have any reviews to leave yet. Make a purchase of a plan or merchandise first.' with internal links to the products page |Pass
Cards - current reviews |reviews displayed with 'leave review' button only for purchased products by that logged in user where a reivew has not already been left. that review details match the product id and order number selected to view| multiple reviews selected by clicking the 'leave review' button and each add review page then displays the correct add review that corresponds to the product id and order number that was selected.|Pass
Cards - previous reviews|reviews displayed with 'update review' and 'delete review' buttons only for purchased products by that logged in user where a review has already been left. review details match the product id and order number selected to view| multiple reviews selected by clicking the 'update review' button and each edit review page then displays the correct edit review page that corresponds to the product id and order number that was selected with the form fields populated with correct data. multiple reviews selected by clicking the 'delete review' button and each delete review then displays the my reviews page with the selected review now in the current reviews section.|Pass

#### Add review page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Form - valid entry|validated responses to add review|all required fields creates a new review in the reviews table and redirects to the my reviews page with a toast message 'Successfully added review!'|Pass
Form - invalid entry|no responses, responses not meeting rating range (0-5) should not create an ending| missing values prompt the form validation with a message of 'please fill out this field'. Rating field outide of range (0 -5) on submit gives a toast message 'Failed to add review. Please ensure the form is valid.
'  |Pass

#### edit review page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Form - initial load | loads corresponding form data to review selected | multiple reviews selected and correct form data populated form | Pass
Form - valid entry|validated responses to add review|all required fields creates a new review in the reviews table and redirects to the my reviews page with a toast message 'Successfully updated review!'|Pass
Form - invalid entry|no responses, responses not meeting rating range (0-5) should not create an ending| missing values prompt the form validation with a message of 'please fill out this field'. Rating field outide of range (0 -5) on submit gives a toast message 'Failed to update review. Please ensure the form is valid.
'  |Pass


#### products (merchandise) page
Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|Card images appear against the correct product_id and appear visably ok| Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|display a card per product with relevant image and details. Products from all other categories show products as title with category availabile as a filter and sort option. | 'Products' appears as the title and all products except category 5 (plans) products are displayed.  |Pass
filter | Filter options for categories (recovery, nutrition, hydration and attire) should be visable and functioning. Catergory 5 (plans) should not visable| The option to filter by categories (recovery, nutrition, hydration and attire) are available. Catergory 5 (plans) is not visable. each filter option was clicked and the relevant products displayed as expected | Pass
sort | All sort filter options (price, name and categories) should be visable and functioning  | each sort option was clicked (for both ascending and descending) and the relevant products displayed as expected | Pass
Cards - current reviews |reviews displayed with 'leave review' button only for purchased products by that logged in user where a reivew has not already been left. that review details match the product id and order number selected to view| multiple reviews selected by clicking the 'leave review' button and each add review page then displays the correct add review that corresponds to the product id and order number that was selected.|Pass
Cards - previous reviews|reviews displayed with 'update review' and 'delete review' buttons only for purchased products by that logged in user where a review has already been left. review details match the product id and order number selected to view| multiple reviews selected by clicking the 'update review' button and each edit review page then displays the correct edit review page that corresponds to the product id and order number that was selected with the form fields populated with correct data. multiple reviews selected by clicking the 'delete review' button and each delete review then displays the my reviews page with the selected review now in the current reviews section.|Pass

#### products(plans) page
Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|Card images appear against the correct product_id and appear visably ok| Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|display a card per product with relevant image and details. products in category 5 (plans) to show plans as headerwith no category filter or sort option. | 'Plans' appears as the title and only category 5 (plans) products are displayed. |Pass
filter | No filter options should be visable | The filter options for categories (recovery, nutrition, hydration, plans and attire) is not visable | Pass
sort | Sort filter options (price and name) should be visable and functioning. sort filter (categories) should not be visable  | each sort option was clicked (for both ascending and descending) and the relevant products displayed as expected. Category was not available on the sort. | Pass
Cards - current reviews |reviews displayed with 'leave review' button only for purchased products by that logged in user where a reivew has not already been left. that review details match the product id and order number selected to view| multiple reviews selected by clicking the 'leave review' button and each add review page then displays the correct add review that corresponds to the product id and order number that was selected.|Pass
Cards - previous reviews|reviews displayed with 'update review' and 'delete review' buttons only for purchased products by that logged in user where a review has already been left. review details match the product id and order number selected to view| multiple reviews selected by clicking the 'update review' button and each edit review page then displays the correct edit review page that corresponds to the product id and order number that was selected with the form fields populated with correct data. multiple reviews selected by clicking the 'delete review' button and each delete review then displays the my reviews page with the selected review now in the current reviews section.|Pass

#### products (merchandise) details page
Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|product image appear against the correct product_id and appear visably ok| Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic product Content|image, product name, price, category, rating and description corresponding to the selected product id should be visable. Quantity selector should be visable and functional, it should not allow negative quantities | multiple products selected and the correct details and image displayed as expected. quantitly selector visable and 1 is the lowest it will allow |Pass
Dynamic product rating Content|The rating should be an average of all the reviews for the selected product id. If there are no reviews for the selected product id then a relevant message should display. If there are reviews for the selected product id it should be a whole number or to 1 decimal place. If there are reviews for the selected product id the total number of reviews should show the total reviews for the selected product id and be an internal link to the reviews details page| multiple products selected and the correct number and total was visable as expected. The total internal link opened the review details page in the same tab. Where there are no reviews for a product the messasage 'No ratings yet' is visable |Pass
Dynamic recommended products Content|a card with image and product name for recommend 1, 2 and 3 associated with the selected product id | Multiple products selected. C25K (Beginner) shows recommend 1 card as buff. Half marathon (Improvers) shows cards 1 and 2 as gels and salt tablets. Marathon shows recommend 1, 2 and 3 as tailwind, bladder and salt tablets.  |Pass
Dynamic links|user must be logged in to add plan to shopping bag. A logged in user that has already purchased the slected plan should not be able to purchase it again | A not logged in user see a message 'Login or Register to set up a plan.' with internal links to login and register that open in the same tab.  A logged in user that has already purchased the plan sees message 'You already own this plan. Checkout My plans to view your plans.' with an internal link to the my plans pages that opens in the same tab. A logged in user that does not own the plan sees the 'add to bag' button with a 'keep shopping' button that opens in the same tab the products/?category=Nutrition,Recovery,Hydration,Attire page.  |Pass
Admin | a logged in admin user should see the edit and delete product options | The edit and delete options are not visable to a not logged in user. The edit and delete options are not visable to a logged in user that is not an admin (testytest).  The edit and delete options are visable to a logged in user that is an admin (sclarkstone7153). The edit link opens the product management edit page in the same tab. The delete option deletes the selected product| Pass

#### products (plans) details page
Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|product image appear against the correct product_id and appear visably ok| Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic product Content|image, product name, price, category, rating and description corresponding to the selected product id should be visable. no quantity selector should be visable as it is fixed for 1 per user | multiple products selected and the correct details and image displayed as expected. |Pass
Dynamic product rating Content|The rating should be an average of all the reviews for the selected product id. If there are no reviews for the selected product id then a relevant message should display. If there are reviews for the selected product id it should be a whole number or to 1 decimal place. If there are reviews for the selected product id the total number of reviews should show the total reviews for the selected product id and be an internal link to the reviews details page| multiple products selected and the correct number and total was visable as expected. The total internal link opened the review details page in the same tab. Where there are no reviews for a product the messasage 'No ratings yet' is visable |Pass
Dynamic recommended products Content|a card with image and product name for recommend 1, 2 and 3 associated with the selected product id | Multiple products selected. C25K (Beginner) shows recommend 1 card as buff. Half marathon (Improvers) shows cards 1 and 2 as gels and salt tablets. Marathon shows recommend 1, 2 and 3 as tailwind, bladder and salt tablets.  |Pass
Dynamic links|user must be logged in to add plan to shopping bag. A logged in user that has already purchased the slected plan should not be able to purchase it again | A not logged in user see a message 'Login or Register to set up a plan.' with internal links to login and register that open in the same tab.  A logged in user that has already purchased the plan sees message 'You already own this plan. Checkout My plans to view your plans.' with an internal link to the my plans pages that opens in the same tab. A logged in user that does not own the plan sees the 'add to bag' button with a 'keep shopping' button that opens in the same tab the products/?category=Plans page.  |Pass
Admin | a logged in admin user should see the edit and delete product options | The edit and delete options are not visable to a not logged in user. The edit and delete options are not visable to a logged in user that is not an admin (testytest).  The edit and delete options are visable to a logged in user that is an admin (sclarkstone7153). The edit link opens the product management edit page in the same tab. The delete option deletes the selected product| Pass


#### my bag page
Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|product image appear against the correct product_id and appear visably ok| Pass
Interal links|internal link to remain in current window| 'keep shopping' button opens in same tab to the products/?category=Nutrition,Recovery,Hydration,Attire page.'Secure checkout' button opens the checkout page in the same tab. |Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|display all products added to the bag. if no products in the bag a relevant message should display. if product is a category 5 (plan) then quantity selector is fixed at 1 but should be able to remove product from bag. if product is not a category 5 (plan) then quantity selector can go higher than 1 but should not be able to go below 1, product can be removed from bag. Delivery cost is deducted if total is over £50. if total is not over £50 then the £2.60 delivery chage is added to the grand total with a message to show how much more is required to get free delivery. | logged in user (testytest) added 10km (improver) plan to bag, bag page shows 10km (improver) name, image, size n/a and sku PP68767774442, price £26.00 and quantitly selector is fixed at 1. bag total is £26.00 and delivery is £2.60 with the grando total of £28.60. a message says 'You could get free delivery by spending just £24.00 more!' The remove option removes the item from the basket and the bag total resets to £0.00. Re adding the 10km (improver) plan  along with a quantity of 2 tailwind hydration powder products shows the total of £75.98 with delivery at £0.00 and a grand total of £ 75.98. Where no products had been added to bag the message 'Your bag is empty' is visable.|Pass

#### checkout page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Images|All images appear, sized correctly with alt tags|product image appear against the correct product_id and appear visably ok| Pass
Interal links|internal link to remain in current window| 'adjust bag' button opens in same tab to the bag page.'complete order' button opens the checkout success page in the same tab. |Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic order summary Content|displays all products added to the bag. product name, image, quantity, size, a running subtotal, order total, delivery and grand total. | multiple orders put through to checkout page and all product details appear as expected where the totals adjust and match that from the bag page.|Pass
Dynamic checkout form Content|displays the checkout form with full name, email address, phone number, street address 1, street address 2, town, county, postcode text fields with country selector and a card payment field. Where the user is logged in and has saved profile details the relevent fields are auto populated. Where the user is a guest or does not have saved profile details then the fields are empty. Requiered fields (full name, email address, phone, street address 1, town, country and card details) fields must be populated to submit. | form validator message (please fill out this field) appears where required fields are empty and form is submitted. form validator message (please include an '@' in the email address) appears where a non valid email address format is needed. a form validator message (please select an item in the list) where the country selector is empty. form validator message ' Your card number is incomplete.' appears where card details left blank. |Pass
payment | loading image displays whilst details are passed to Swipe. Correct information is passed to Swipe. | on successful completion of the checkout form a blue overlay image is displayed until checkout process is complete. On logging into Swipe the order details (items and delivery information) have been stored correctly. | Pass

#### checkout success page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Dynamic Content|displays order details (order number, email address, order date, item names, quantities and prices and delivery information and total).| multiple orders put through and show the correct item and delivery information as expected. |Pass
Dynamic links |shows different links for logged in users then guest users| logged in user shows a 'dont forget to leave a review' button which opens the my reviews page in the same tab. guest user shows 'keep shopping' button which opens the products/?category=Nutrition,Recovery,Hydration,Attire page. |Pass


#### reviews details page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Interal links|internal link to remain in current window| Order number links opens internal link in same window to order history page, passing through the order_number parameter. |Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|display all reviews for the selected product id.| multiple products/ plans selected where users had left reviews for and for each selected product id the reviews for that product were displayed with the average total rating from each of the relevant reviews and the total number of reviews for the selected product id. Each individual review had the subject, review , rating, date review completed and the name of the user that had left the review. |Pass

#### plans details page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
Interal links|internal link to remain in current window| Order number links opens internal link in same window to order history page, passing through the order_number parameter. |Pass
External links|external links to open in new tab| footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|display all details from sessions and distance fixtures displayed as relevant weeks and days with session details for the selected plan where the user has purchased the plan. Show message if user has not purcahsed plan| multiple plans selected where users had purchased the plan and the correct weeks, days and session details were displayed for the selected product id. where the plan id had not been purchased by user and the url manaually entered a toast message was given 'Sorry, you have not purchased this plan.' and redirected to my_plans page  |Pass

#### User types

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
guest - My Account menu|Should see Login and register. should not see product management, my profile, my plans, my reviews and logout|Login and register| Pass
guest - can view pages|Should be able to view homepage, products, products_details, login, register, bag, checkout pages, review_details|can view homepage, products, products_details, login, register, bag, checkout pages, review_details| Pass
guest - can not view pages|Should not be able to view my profile, my_plans, my_reviews, plans_details, add review, edit review and product management| redirects to login page if urls manually entered for my /profile, /plans, /reviews, /plans/14, /reviews/add/2/DFD4BF49AC54453996F18BF4B5D2CBBA, /reviews/edit/2/DFD4BF49AC54453996F18BF4B5D2CBBA and /products/add/ and /products/edit/10/| Pass
admin user logged in - My Account menu|Should see product management, my profile, my plans, my reviews and logout|can see see product management, my profile, my plans, my reviews and logout| Pass
admin user logged in - pages|Should be able to view all pages|view all pages and access the django /admin area if needed| Pass
non admin user logged in - My Account menu|Should see my profile, my plans, my reviews and logout. should not see product management|can see my profile, my plans, my reviews and logout| Pass
non admin user logged in - can view pages|Should be able to view my profile, my_plans, my_reviews, plans_details, add review, edit review| can views pages when menu or page links clicked as expected| Pass
non admin user logged in - can not view pages|Should not be able to view product management pages, plans_details pages of plans not purchased| displays toast message 'Sorry, only store owners can do that.' if urls manually entered for /products/add/ and /products/edit/10/. if a plan that has not been purchased by user url is manaually entered then a toast message is given 'Sorry, you have not purchased this plan.' and redirect to my_plans page| Pass

### Validator testing

* HTML - using [W3C validator] (https://validator.w3.org/nu/?doc=https%3A%2F%2Fmilestone4-sclarkstone.herokuapp.com%2F)
    * Duplicate ID user-options - gave unique name to mobile version 'user-options-mobile'
    * No space between attributes - Main-nav.html had id="merch-link"", i removed the second ".
    * Stray end tag div - base.html had an extra closing div in the footer. i removed this. 
    * The type attribute is unnecessary for JavaScript resources - removed the type attribute on base.html
    * After making these amendments i got the message 'Document checking completed. No errors or warnings to show.'
* CSS - using [W3C Jigsaw](https://jigsaw.w3.org/css-validator)  By direct input - /static/css/base.css. Running the w3c validator the following message came 'Congratulations! No Error Found.'.
* JavaScript using [JSHint](https://jshint.com/) - checkout/static/js/stripe_elements.js
    * 'Missing semicolon.' - after reviewing the code, the missing semicolon was found to be on line 117. After correcting this i then re run the validator and the issue was resolved.
* Python -  using [pep8online](http://pep8online.com/)
    * plans app - views.py
        * line 45 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 64 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 67 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message
    * plans app - urls.py - All right
    * plans app - tests_views.py
        * line 11 - blank line contains whitespace - removed white space.This corrected the error 
        * line 14 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 20 - blank line at end of file - removed blank line. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * plans app - tests_models.py
        * line 9 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 11 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 17 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * plans app - models.py - All right
    * plans app - apps.py - All right
    * plans app - admin.py - All right
    * reviews app - views.py
        * line 28 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 29 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 84 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 113 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 125 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * reviews app - urls.py
        * line 7 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 8 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 9 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * reviews app - test_views.py
        * line 36 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 37 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 49 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 50 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 62 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 63 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 64 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 75 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 76 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 77 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 78 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 87 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 88 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 90 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 92 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 95 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * reviews app - test_models.py
        * line 12 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 13 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * line 15 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * reviews app - test_forms.py - All right
    * reviews app - models.py
        * line 14 - line too long - put each part of the inside of the brackets on a new line, seperate with a comma. This corrected the error
        * After making these corrections i re tested it and got an 'All right' message.
    * reviews app - forms.py - All right
    * reviews app - apps.py - All right
    * reviews app - apps.py - All right

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
* chrome error - jquery must be before bootstrap. the CDN link had stopped working, found a new CDN link and replaced it which resolved the issue.
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
Following these steps i carried out the set up;
* run command 'pip3 install Django==3.2' to install Django
* run command 'django-admin startproject milestone4 .' to set up basic folder structure and files for Django
* run command 'touch .gitignore' to create ignore file and then add to file *.sqlite3, *.pyc
* run command 'python3 manage.py runserver' to check it is runner as expected. a Django screen will appear on the browser with the message 'The install worked successfully! Congratulations! You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.'
* stop the server then run command 'python3 manage.py migrate'
* run command'python3 manage.py createsuperuser', input a username (sclarkstone7153), email (samclarkstone@hotmail.com) and password (Unicorn2001)
* run command git add .
* run command git commit -m "commit message"
* run command git push

### authentication set up
Following these steps i carried out the authentication set up;

* run command 'pip3 install django-allauth==0.41.0'
* add 'import os' to top of settings.py file
* go to https://django-allauth.readthedocs.io/en/latest/installation.html and copy and paste AUTHENTICATION_BACKENDS plus 'SITE_ID = 1' and add any missing required apps to INSTALLED_APPS.
* run command python3 manage.py migrate
* run command 'python3 manage.py runserver' to check it is runner as expected.
* run command'pip3 freeze > requirements.txt'

### templates
* run command 'cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/'
* run command python3 manage.py startapp home

### font awesome
* sign up for free account at [font awesome](https://fontawesome.com/) and get kit code. put this in the base.html template corejs block. 

### database
* run command pip3 install pillow to allow url image use
* add products, plans, reviews to installed apps in settings.py
* for products app add categories and products json files to fixtures folder
* for plans app add distance and sessions json files to fixtures folder
* run command python3 manage.py makemigrations --dry-run
* run command python3 manage.py makemigrations
* run command python3 manage.py migrate --plan
* run command python3 manage.py migrate
* run command python3 manage.py loaddata categories
* run command python3 manage.py loaddata products
* run command python3 manage.py loaddata distance
* run command python3 manage.py loaddata sessions
* create admin.py file in products app so that tables can be seen in admin area and data can be manually added


### Payment

#### checkout forms
* run command 'pip3 install django-crispy-forms'
* run command 'pip3 install django-countries' - for drop down of country codes

#### checkout payment
* run command 'pip3 install stripe'

#### set environment variables
* save STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_SECRET in gitpod (settings, variables) and Heroku (settings, config vars)

Test card details

Name | Email | Phone | Address | Postcode | Card number | Card date | CVC | Zip  
-----|-------|-------|---------|----------|-------------|-----------|----- |----
Test | test@test.com | 1234567890 | anywhere | 12345 | 4242 4242 4242 4242 | 04/24 | 242 | 42424 
Test | test@test.com | 1234567890 | anywhere | 12345 | 4000 0025 0000 3155 | 04/24 | 242 | 44242 



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

* [google fonts](https://fonts.google.com/) was used to give the project a more professional and unique feel. Google fonts gave fonts that go together and as i had already seen the Lanto font in use on the Code institute 'love running' project and felt it fit in well with my project i went with Lanto. 

* [Website Mockup Generator](https://websitemockupgenerator.com/) was used to generate the multi device website mock up used in the readme file.

* [material.io](https://material.io/resources/color/#!/?view.left=1&view.right=1&primary.color=0277bd]) was used to check accessibility of text colours on background colours. Also used to find complemetary colours. This is where i decided on my combination of white, black and grey backgrounds with complimentary text. Credit to my mentor Akshat for showing me this resource. 

### Media

* [TinyPNG] (https://tinypng.com/) was used to compress all images to reduce the load time of the site.
* [pexels] (https://www.pexels.com/) - for free use of running photos
* All other images were taken by myself of running kit and items that belong to me.
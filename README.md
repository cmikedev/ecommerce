# Moto Madness

## 1. Introduction

Moto Madness is a fictional ecommerce site offering for sale discounted factory-second motorcycles imported from Japan.

### Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://moto-madness.herokuapp.com/).


### Repository
The GitHub repository can be found [here](https://github.com/cmikedev/ecommerce).

____
</br>


## 2. Planning

The purpose of this ecommerce site is to provide the user with a clear, intuitive interface which allows them to immediately understand the services being offered, navigate easily through the various pages, interact via comments and ultimately purchase a product. To achieve this, Agile methodology was used within the planning and design process. Github's Kanban board was implemented to design and track user stories which were vital in developing a user-focused experience:

1. As a Site User I can register an account so that add items to my cart
2. As a Site User I can view a list of products for sale so that I can select one to view
3. As a Site User I can open up a product page so that I can view more details
4. As a Site User I can use the integrated PayPal button so that I can purchase products
5. As a Site User I can leave comments under a product so that I can ask questions or leave a review
6. As a Superuser I can add a product to the main product page so that the inventory is kept up to date
7. As a Superuser I can edit a product so that I can correct any errors or make changes to the details
8. As a Superuser I can delete a product so that I can keep the inventory up to date

The completed Kanban Board can be found [here](https://github.com/users/cmikedev/projects/8).

___
</br>

## 3. Site Design

## 3.1 Layout & Visual Design

A key feature of the proposed site was a clear, concise layout where the products were to the fore. The products should be immediately visible and not crowded. A simple navigation bar should allow the user to see move through the site. The user should also be aware of their logged in status.</br>
</br>

![image]()</br>
</br>

The construction of the site is based on Dennis Ivy's [Django Ecommerce Website tutorial](https://www.youtube.com/watch?v=_ELCMngbM0E&list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng&index=1&t=1738s) (see references). The following features were added:

* A Welcome page to allow the user to understand the site's purpose
* Full authentication to allow a visitor to register an account, sign-in and to ensure that only authenticated users may view certain pages and complete certain actions
* Notifications to users of their login status and the completion of actions
* Role-based login
* Full front-end CRUD functionality for the Superuser allowing them to add, read, update and delete products
* A responsive products page which does not statically list the products allowing them to be updated at the front-end
* A Detail page which allows the user to view further information on a product
* The ability for users to interact with the site by leaving comments
* Notification of payment processing is no longer handled by JavaScript Alerts but by directing a user to a dedicate notification page

Based on researching similar sites which sold either motorcycles or other vehicles it became apparent that a judiscious use of a small number of dark and light colours, usually shades of black and white, accentuated the colours of the products being sold and pushed them to the fore of the site. Site's such as [BMW's Autorrad](https://www.joeduffy.ie/motorrad) and [Kawasaki's Motorcycle site](https://www.kawasaki.co.uk/en/products) make use of a such a scheme.

___
</br>

## 4. Testing

This section focuses on testing the website from the point of view of the user in line with the user stories utilised in this project's Kanban. The testing is spread across four areas:

3.1 User Story Testing
3.2 Admin / Superuser CRUD Capability Testing
3.3 Authentication Testing
3.4 Code and Responsiveness Testing

## 4.1 User Story Testing
___
User Story:

As a Site User I can register an account so that add items to my cart.
* Acceptance Criteria:
    * User can register an account
    * User can login
    * User is made aware of their login status
    * User can logout
    * User is made aware of their logout status
___

A site visitor can click on the "Register" button on the navbar.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/1%20-%20registration.png?raw=true)</br>
</br>

The visitor will then be directed to a registration form. The user needs to choose a name and a password and press "Submit".</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/2%20-%20registration.png?raw=true)</br>
</br>


If their submission is successful they will be redirected to the Store page whereby the "Login" and "Register" buttons on the top right of the navbar will have changed to reflect their loged in status.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/3%20-%20registration-successful.png?raw=true)</br>
</br>

To logout, a user just needs to click on the "Logout" button.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/5%20-%20logout.png?raw=true)</br>
</br>

The user will then be redirected to the Welcome page and they will receive confirmation of their logged out status via a message and that the buttons on the navbar will once again have changed.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/6%20-%20logout-successful.png?raw=true)</br>
</br></br></br>


___
User Story:

As a Site User I can view a list of products for sale so that I can select one to view.

* Acceptance Criteria:
    * User can view and browse all available products
    * User can select a product and view further details
___

A user can view all of the products in the Store. Eight products appear on each page. The user can navigate to different pages to see all of the products.

___
User Story:

As a Site User I can open up a product page so that I can view more details.

* Acceptance Criteria:
    * User can select a product and be directed to a details page
    * User is presented with expanded details of the product on a dedicated page
___

If a user clicks on "View", they will be directed to a Detail page which contains more details about the product they are interested in as well as the ability to read and post comments.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/7%20-%20view-products.png?raw=true)</br>
</br>

___
User Story:

As a Site User I can leave comments under a product so that I can ask questions or leave a review.

* Acceptance Criteria:
    * User can view comments pertaining to a product
    * User if authenticated can add a comment
    * User is notified that their comment has been posted
___

On the Details page a user will be able to see any comments that have been posted.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/8%20-%20comment.png?raw=true)</br>
</br>

The option to add a comment will only be visible for authenticated users - see Authentication Testing section below.

By selecting to add a comment an authenticated user will be directed to a form to post their comment under their username.

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/9%20-%20comment-submit.png?raw=true)</br>
</br>

Once submitted the user will be notified that their comment has been posted.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/10%20-%20comment-success.png?raw=true)</br>
</br>

Comments will appear in order of date posted.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/11%20-%20comment-posted.png?raw=true)</br>
</br>


___
User Story:

As a Site User I can use the integrated PayPal button so that I can purchase products.

* Acceptance Criteria:
    * User can select a product and add it to their cart
    * User can edit their cart
    * User can add details at checkout
    * User can pay for the product using PayPal
    * User is redirected back to the main product/shop page
___

The User can click on the "Add to Cart" button of a product they wish to purchase. When the user navigates to the Cart page they product will be visible. (See Bugs Section below with regards to the comment)</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/12%20-%20add-to-cart.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/13%20-%20cart.png?raw=true)</br>
</br>

If the user decides that they would like to order more than one of the same product they can increase the quantity using the up arrows. Conversely the item will be removed if the user clicks the down arrow when the quantity is equal to one. The total price will update.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/14%20-%20change-qty.png?raw=true)</br>
</br>

When the user navigates to the Checkout page they will be asked for their name, email and shipping address. When inputted, if the user clicks "Continue" the PayPal button will appear.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/15%20-%20checkout.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/16%20-%20checkout-submit.png?raw=true)</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/17%20-%20checkout-paypal.png?raw=true)</br>
</br>

When the user has submitted their payment they will be redirected to a page informing them that their order has been received and is being processed. They can then navigate back to the Store page using the button.

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/user_stories/18%20-%20checkout-success.png?raw=true)</br>
</br></br></br>


## 4.2 Admin / Superuser CRUD Capability Testing

Adding a Product
___
User Story:

As a Superuser I can add a product to the main product page so that the inventory is kept up to date.

* Acceptance Criteria:
    * An authenticated user can access a page to upload a product
    * All uploads are done at the front-end
    * The authenticated user is presented with additional options when logged in than regular users ie - an 'add product button'
    * User is notified that the product has been successfully added
___

When a Superuser logs in and navigates to the Store they are presented with additional options on the main body ("Add Product") and in each of the product cards ("Edit", "Delete").</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/1%20-%20superuser%20-%20view.png?raw=true)</br>
</br>

The Superuser can click on the "Add new product" and they will be brought to a form containing fields from the Products model.</br>
</br> 

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/2%20-%20superuser%20-%20add.png?raw=true)</br>
</br>

The Superuser fills out the details, adds a photograph and submits the form.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/3%20-%20superuser%20-%20add-product.png?raw=true)</br>
</br>

If successful the Superuser will be returned to the Store page and will receive a confirmation message that the item has been added. The product appears as the first item on the page because we chose "AAA" as the manufacturer. The products are currently sorted according to manufacturer.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/4%20-%20superuser%20-%20add-success.png?raw=true)</br>
</br>

We can also see that the details are as we chose.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/5%20-%20superuser%20-%20add-details.png?raw=true)</br>
</br>

But it looks like there was a mistake. The price is too low and the wrong image has been used.
___
User Story:

As a Superuser I can edit a product so that I can correct any errors or make changes to the details.

* Acceptance Criteria:
    * Authenticated user can edit a products details
    * User is notified of the changes that are made
___

The Superuser can easily amend this by selecting the "Edit" button.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/6%20-%20superuser%20-%20update.png?raw=true)</br>
</br>

The Superuser simply changes the details that they want - in this case the image and the price - and submits the form.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/7%20-%20superuser%20-%20update-details.png?raw=true)</br>
</br>

Once again the page has been updated with the details chosen by the Superuser.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/8%20-%20superuser%20-%20update-success.png?raw=true)</br>
</br>

___
User Story:

As a Superuser I can delete a product so that I can keep the inventory up to date.

* Acceptance Criteria:
    * Authenticated user can select a product to delete
    * User must confirm that the product is to be deleted
    * Once deleted, user is redirected back to the main product page
___


The Superuser has the option to delete the product entirely simply by selecting the delete button.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/9%20-%20superuser%20-%20delete.png?raw=true)<br>
</br>

Once selected the Superuser will be asked to confirm that they really want to delete the product and that the action is permanent.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/10%20-%20superuser%20-%20delete-confirm.png?raw=true)</br>
</br>


The product has been deleted!</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/superuser_crud/11%20-%20superuser%20-%20delete-success.png?raw=true)</br>
</br>

## 4.3 Authentication Testing

Throughtout the site, various actions such as the posting of forms are handled by authenticating users. Certain sections of the website will not be visible to a user that is not authenticated. However, this alone does not prohibit an unauthorised user accessing an area if they know the URL so authentication also takes place at the page level whereby a user that is not authenticated, or in the case of the product CRUD functionality, not a Superuser, will not be able to view that section of the site even with the URL.

A user who has is not logged in will in the first instance be presented with a full welcome page which offers them the opportunity to register. Login and registration buttons (as opposed to a welcome message and logout button) will render in the top right of the navbar.

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/1%20-%20welcome-view.png?raw=true)</br>
</br>

The user may decide to go straight to the store. From there they might see an item they like and decide to add it to their cart.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/2%20-%20add-item.png?raw=true)</br>
</br>

Doing this triggers a modal and the visitor is advised that they must login or register an account in order to add an item to the cart.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/3%20-%20add%20-%20login.png?raw=true)</br>
</br>

The user can click on "Cart" in the navbar if they wish and the Cart page will load showing zero products.

If the user decides to visit the checkout page which they can via the link in the Cart page or the navbar, the checkout page will recognise that the user is not authenticated and instead render a message asking them to login or register.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/4%20-%20checkout.png?raw=true)</br>
</br>

The user instead decides to go back to the Store page and click on the product's details. The Detail page will render the product details along with the option to read comments (if any have been posted) or post one. If the user is not registered then the link to post a comment will not appear.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/5%20-%20comment.png?raw=true)</br>
</br>

Again, if the visitor ascertains the correct url to post a comment, the comment page will recognise the visitor as not being authenticated and will render a message informing them that they are not authorised to view this page along with a link back to the Welcome page.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/6%20-%20add-comment.png?raw=true)</br>
</br>

The option to add a product is only rendered for a Superuser. If an unregistered or registered user obtains the URL for the page to add a product, the page will ascertain that they are not a Superuser and will render with a message informing them that they do not have permission to view the page.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/authentication/7%20-%20add-product.png?raw=true)</br>
</br>


## 4.4 Code and Responsiveness Testing
All code and site responsiveness has been tested as available [here](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/testing.md).
This document details:

1. Python PEP8 Testing
2. HTML W3C Testing
3. CSS W3C Testing
4. JavaScript JShint Testing
5. Lighthouse Testing
6. Responsiveness Testing


___
</br>

## 5 Bugs

## 5.1 Fixed Bugs

* Mixed Content Error

This appeared in the Console when a file was requested from Cloudinary through Django context (e.g. src="{{product.image.url}}" ). </br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/bugs/mixed-content.png?raw=true)</br>
</br>

Requests using standard URLs were over https. Requests as above had to be converted. This error was fixed by adding "http-equiv" and content="upgrade-insecure-requests" to the meta tags in the base.html head.</br >
</br >


## 5.2 Unfixed Bugs

* Modal not displaying

When an item is added to the cart the page page updates. In order to notify the user that they have successfully added an item to their cart a modal was created. As the page updated the modal would close without any input from the user. A workaround was to restyle it so that the user wouldn't need to interact with the modal but instead it would display for a short time and then self-close.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/bugs/modal.png?raw=true)</br>
</br>

This worked well in the development environment but with the Heroku deployment the modal displays and closes too quickly for a user to see or read it.</br>
</br>

* Carousel Speed is Variable

The speed of the carousel on the welcome.html page which advertises newly added products to the user varies. On occasion it can take quite some time before it changes making it appear as though it is not loading whereas other times it moves fluidly. A possible cause is the image resolution/size.</br>
</br>

* PayPal Sandbox Checkout Freezing

This has been a rare occurrence whereby the PayPal sandbox checkout has frozen.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/bugs/paypal-freeze.png?raw=true)</br>
</br>

* PayPal Sandbox Timeout

This error has been identified in the Console. This error is just linked to the Sandbox api and does not affect the processing of payments.</br>
</br>

![!image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/bugs/paypal-timeout.png?raw=true)



___
</br>

## 6 Deployment

### 6.1 Deploying the repository via Heroku
* The app was created using Heroku via the following steps:
    * On the https://dashboard.heroku.com/apps page, click <mark style="background-color: grey">New</mark> and then select <mark style="background-color: grey">Create New App</mark> from the drop-down menu.
    * When the next page loads insert the <mark style="background-color: grey">App name</mark> and <mark style="background-color: grey">Choose a region</mark>. The click <mark style="background-color: grey">Create app</mark>
    * In the settings tab click on <mark style="background-color: grey">Reveal Config Vars</mark> and add the key <mark style="background-color: grey">Port</mark> and the value <mark style="background-color: grey">8000</mark>. The other credentials used are:
        * [Cloudinary](https://cloudinary.com/) for using static images over Heroku
        * The Database which is [ElephantSQL](https://www.elephantsql.com/)
    </br >
* To deploy the Heroku app:
    * Click on the <mark style="background-color: grey">Deploy</mark> tab and select <mark style="background-color: grey">Github-Connect to Github</mark>.
    * Enter the repository name and click <mark style="background-color: grey">Search</mark>.
    * Choose the repository that holds the correct files and click <mark style="background-color: grey">Connect</mark>.
    * A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub. For this app automatic was selected.
    * Once the deployment method has been chosen the app will be built and can be launched by clicking the <mark style="background-color: grey">Open app</mark> button at the top of the page.<br />
    <br />

### 6.2 GitHub
#### Forking the repository
* The GitHub repository can be forked to make a copy of the original. This copy can then be viewed or changed without affecting the original repository via the following steps:
    * In the Respository section, select the [ecommerce](https://github.com/cmikedev/ecommerce) repository
    * At the top right of the page select <mark style="background-color: grey">fork</mark> from the menu below your profile
    * A copy of the repository will now be created in your account

#### Creating a local clone
* To create a local clone via GitHub:
    * In the Respository section, select the [ecommerce](https://github.com/cmikedev/ecommerce) repository
    * From the horizontal menu above the repository contents select <mark style="background-color: grey">Code</mark>
    * __Copy__ the link that that is shown
    * Within __Gitpod__ change the directory to where you would like the location of the cloned directory to be
    * Type __git clone__ and paste the link that you copied
    * Press <mark style="background-color: grey">Enter</mark> and the local clone will be created<br />
    <br />




## 7. References

[Codemy.com Youtube tutorial](https://www.youtube.com/watch?v=EqjRhO5CK6A&t=617s)


----
</br>

## 8. Acknowledgements
I would like to thank my course mentor Harry Dhillon for providing guidance on this project.
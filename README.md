# Moto Madness


### Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://moto-madness.herokuapp.com/).


### Repository
The GitHub repository can be found [here](https://github.com/cmikedev/ecommerce).


____



## 1. Design


## 3. Testing

This section focuses on testing the website from the point of view of the user in line with the user stories utilised in this project's Kanban. The testing is spread across four areas:

1. User Story Testing
2. Admin / Superuser CRUD Capability Testing
3. Authentication Testing
4. Code and Responsiveness Testing

### User Story Testing
___
User Story:

* As a Site User I can register an account so that add items to my cart
    * User can register an account
    * User can login
    * User is made aware of their login status
    * User can logout
    * User is made aware of their logout status
___

### Admin / Superuser CRUD Capability Testing

Adding a Product
___
User Story:

* As a Superuser I can add a product to the main product page so that the inventory is kept up to date
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
* As a Superuser I can edit a product so that I can correct any errors or make changes to the details
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

* As a Superuser I can delete a product so that I can keep the inventory up to date
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

### Authentication Testing

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


### Code and Responsiveness Testing
All code and site responsiveness has been tested as available [here](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/testing.md).
This document details:

1. Python PEP8 Testing
2. HTML W3C Testing
3. CSS W3C Testing
4. JavaScript JShint Testing
5. Lighthouse Testing
6. Responsiveness Testing


### Bugs
#### Fixed Bugs

* Mixed Content Error

This appeared in the Console when a file was requested from Cloudinary through Django context (e.g. src="{{product.image.url}}" ). </br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/bugs/mixed-content.png?raw=true)</br>
</br>

Requests using standard URLs were over https. Requests as above had to be converted. This error was fixed by adding "http-equiv" and content="upgrade-insecure-requests" to the meta tags in the base.html head.</br >
</br >


#### Unfixed Bugs

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

![!image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/bugs/paypal-timeout.png?raw=true)</br>
</br>






## 4. Deployment

### 4.1 Deploying the repository via Heroku
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

### 4.2 GitHub
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




## 5. References



----

## 6. Acknowledgements
I would like to thank my course mentor Harry Dhillon for providing guidance on this project.
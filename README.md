# Moto Madness
Battleship is a single-player python version of the classic turn-based guess game.</br >
</br > 

![image](https://github.com/cmikedev/battleship/blob/main/assets/readme-images/am-i-responsive.png?raw=true)</br >
</br >
Image created using [Am I responsive](https://ui.dev/amiresponsive)</br >
</br >

### Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://moto-madness.herokuapp.com/).


### Repository
The GitHub repository can be found [here](https://github.com/cmikedev/ecommerce).


____



## 1. Design


## 3. Testing

### User Story Testing

#### Site Users


#### Admin / Superuser

When a Superuser logs in and navigates to the Store they are presented with additional options on the main body ("Add Product") and in each of the product cards ("Edit", "Delete").</br>
</br>

![image]()</br>
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
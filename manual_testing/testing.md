# Manual Testing

The purpose of this section is to visually document the manual testing carried out on the Python, HTML, CSS and JavaScript code using online tools. 

### Contents:
1. Python PEP8 Testing
2. HTML W3C Testing
3. CSS W3C Testing
4. JavaScript JShint Testing
5. Lighthouse Testing
6. Responsiveness Testing</br>
</br>

___
</br>

## 1. Python PEP8 Testing
The python code was tested using Code Institute's [PEP8 Python Linter](https://pep8ci.herokuapp.com/)


The following pages were tested:

1. Members App:
    * urls.py
    * views.py</br>
    </br>

2. Store App:
    * models.py
    * admin.py
    * forms.py
    * views.py
    * urls.py

All Python code was returned error free and in accordance with PEP8.</br>
</br>

___
</br>

## 2. HTML W3C Testing
The HTML was tested using W3C's [Nu HTML Checker](https://validator.w3.org/nu/#textarea). The HTML was manually inputted so as to be able to distinguish errors thrown up by the use of Bootstrap or Django.

### 2.1 Members App:

* Login page - login.html
    * There were no warnings or errors returned</br >
</br >

* Registration page - register_user.html
    * The W3C Validator returned four errors. These were not errors within the HTML code but due to the make-up of Django's "UserCreationForm" included to register users.</br>
</br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/1%20-%20w3c%20-%20register.png?raw=true)</br >
</br >

### 2.2 Store App:

* Welcome page - welcome.html
* Store page - store.html
* Detail page - detail.html
* Comment page - add-comment.html
* Cart page - cart.html
* Checkout page - checkout.html
* Payment page - payment.html
* Add Product page - add-product.html
* Update Product page - update-product.html
* Delete Product page - delete-product.html
    
There were no warnings or errors returned for any of the pages.</br>
</br>

___
</br>

## 3. CSS W3C Testing
The CSS was tested using W3C's [Nu HTML Checker](https://validator.w3.org/nu/#textarea) and selecting 'CSS'. Additionally the CSS was also put through W3C's [Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri).


* W3C Nu HTML Checker
    * no errors were returned by inputting the CSS code as it was written within Django.</br>
    </br>
    
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/css/1%20-%20w3c%20-%20css.png?raw=true)</br >
</br >

* W3C Jigsaw
    * Testing the CSS of the deployed site by passing a URL through to W3C's Jigsaw Validator returned a parsing error for each of the main pages and multiple vendor extension warnings. The parsing error related to Bootstrap's included CSS and the warnings related to Bootstrap, Cloudinary and Font-Awesome vendor extensions.</br>
    </br>

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/css/2%20-%20w3c%20-%20css%20jigsaw.png?raw=true)</br >
</br >

___
</br>


## 4. JavaScript JShint Testing
The JavaScript was tested using [JShint](https://jshint.com/). In each instance there were no errors returned.

* JS static file
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/js/1%20-%20jshint%20-%20js.png?raw=true)</br >
</br >

* Base page - base.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/js/2%20-%20jshint%20-%20base.png?raw=true)</br >
</br >

* Checkout page - PayPal checkout code - login.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/js/3%20-%20jshint%20-%20paypal%20-%20checkout.png?raw=true)</br >
</br >

* Checkout page (cont.) - Order processing - login.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/js/3.1%20-%20jshint%20-%20order%20-%20checkout.png?raw=true)</br >
</br >

___
</br>

## 5. Lighthouse Testing

Lighthouse through [web.dev](https://pagespeed.web.dev/) was used to test the site for: 
* Performance
* Accessibility
* Best Practice
* SEO

Of each page, the store.html had the poorest overall scores, in particular the performance. This performance was particularly impacted on mobile devices as shown here.

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/lighthouse/results.png?raw=true)</br >
</br >

![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/lighthouse/performance.png?raw=true)</br >
</br >

___
</br>

## 6. Responsiveness Testing

* The responsiveness tests were carried out manually using Google Chrome's [Inspect Function](https://developer.chrome.com/docs/devtools/open/) with also some real world testing on actual devices. Some of the devices tested included (but not limited to):

    * Nest Hub Max
    * iPad Mini
    * iPad Air
    * Samsung Galaxy S8+
    * iPhone SE
    * Samsung Galaxy S8 (real-world test on device)
    * Samsung Galaxy S9 (real-world test on device)
    * Apple MacBook Air (real-world test on device) <br />
    <br />
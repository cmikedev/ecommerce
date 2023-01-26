# Manual Testing

The purpose of this section is to visually document the manual testing carried out on the Python, HTML, CSS and JavaScript code using online tools. 

### Contents:
1. Python PEP8 Testing
2. HTML W3C Testing
3. CSS W3C Testing
4. JavaScript JShint Testing
5. Lighthouse Testing
6. Responsiveness Testing


## 1. Python PEP8 Testing
The python code was tested using Code Institute's [PEP8 Python Linter](https://pep8ci.herokuapp.com/)

All Python code was returned error free and in accordance with PEP8.

### Members App:

* Members - urls.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/1%20-%20members%20-%20urls.png?raw=true)</br >
</br >

* Members - views.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/2%20-%20members%20-%20views.png?raw=true)</br >
</br >

### Store App:

* Store - models.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/3%20-%20store%20-%20models.png?raw=true)</br >
</br >

* Store - admin.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/4%20-%20store%20-%20admin.png?raw=true)</br >
</br >

* Store - forms.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/5%20-%20store%20-%20forms.png?raw=true)</br >
</br >

* Store - views.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/6%20-%20store%20-%20views.png?raw=true)</br >
</br >

* Store - urls.py
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/python/7%20-%20store%20-%20urls.png?raw=true)</br >
</br >


## 2. HTML W3C Testing
The HTML was tested using W3C's [Nu HTML Checker](https://validator.w3.org/nu/#textarea). The HTML was manually inputted so as to be able to distinguish errors thrown up by the use of Bootstrap or Django.

## 2.1 Members App:

* Login page - login.html
    * There were no warnings or errors returned</br >
</br >

* Registration page - register_user.html
    * The W3C Validator returned four errors. These were not errors within the HTML code but due to the make-up of Django's "UserCreationForm" included to register users.</br>
</br>
![]()</br >
</br >

## 2.2 Store App:

* Welcome page - welcome.html
    * There were no warnings or errors returned</br>
</br>

* Store page - store.html
    * There were no warnings or errors returned</br>
</br>

* Detail page - detail.html
    * There were no warnings or errors returned</br>
</br>

* Comment page - add-comment.html
    * There were no warnings or errors returned</br>
</br>

* Cart page - cart.html
    * There were no warnings or errors returned</br>
</br>

* Checkout page - checkout.html
    * There were no warnings or errors returned</br>
</br>

* Payment page - payment.html
    * There were no warnings or errors returned</br>
</br>

* Add Product page - add-product.html
    * There were no warnings or errors returned</br>
</br>

* Update Product page - update-product.html
    * There were no warnings or errors returned</br>
</br>

* Delete Product page - delete-product.html
    * There were no warnings or errors returned</br>
</br>

## 3. CSS W3C Testing
The CSS was tested using W3C's [Nu HTML Checker](https://validator.w3.org/nu/#textarea) and selecting 'CSS'. Additionally the CSS was also put through W3C's [Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

In each instance there were no errors returned.


* W3C Nu HTML Checker
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/css/1%20-%20w3c%20-%20css.png?raw=true)</br >
</br >

* W3C Jigsaw
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/css/2%20-%20w3c%20-%20css%20jigsaw.png?raw=true)</br >
</br >


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
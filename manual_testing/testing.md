# Manual Testing

The purpose of this section is to visually document the manual testing carried out on the Python, HTML, CSS and JavaScript code using online tools. 

### Contents:
* Python PEP8 Testing
* HTML W3C Testing
* CSS W3C Testing
* JavaScript JShint Testing


## Python PEP8 Testing
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


## HTML W3C Testing
The HTML was tested using W3C's [Nu HTML Checker](https://validator.w3.org/nu/#textarea). The HTML was manually inputted so as to be able to distinguish errors thrown up by the use of Bootstrap or Django.

Each page returned errors which related to Django conventions. For example the validator could not recognise the use of Django context such as {% url 'link' %} within a html link tag.

### Members App:

* Login page - login.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/1%20-%20w3c%20-%20login.png?raw=true)</br >
</br >

* Registration page - register_user.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/2%20-%20w3c%20-%20register.png?raw=true)</br >
</br >

### Store App:

* Base page - head - base.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/3%20-%20w3c%20-%20base%20-%20head.png?raw=true)</br >
</br >

* Base page - body - base.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/3.1%20-%20w3c%20-%20base%20-%20body%20-%201.png?raw=true)</br >
</br >

* Base page - body (cont.) - base.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/3.2%20-%20w3c%20-%20base%20-%20body%20-%202.png?raw=true)</br >
</br >

* Welcome page - welcome.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/4%20-%20w3c%20-%20welcome.png?raw=true)</br >
</br >

* Store page - store.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/5%20-%20w3c%20-%20store.png?raw=true)</br >
</br >

* Store page (cont.) - store.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/5.1%20-%20w3c%20-%20store.png?raw=true)</br >
</br >

* Detail page - detail.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/6%20-%20w3c%20-%20detail.png?raw=true)</br >
</br >

* Detail page (cont.) - detail.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/6.1%20-%20w3c%20-%20detail.png?raw=true)</br >
</br >

* Detail page (cont.) - detail.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/6.2%20-%20w3c%20-%20detail.png?raw=true)</br >
</br >

* Comment page - add-comment.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/7%20-%20w3c%20-%20add-comment.png?raw=true)</br >
</br >

* Cart page - cart.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/8%20-%20w3c%20-%20cart.png?raw=true)</br >
</br >

* Checkout page - checkout.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/9%20-%20w3c%20-%20checkout.png?raw=true)</br >
</br >

* Checkout page (cont.) - checkout.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/9.1%20-%20w3c%20-%20checkout.png?raw=true)</br >
</br >

* Payment page - payment.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/10%20-%20w3c%20-%20payment.png?raw=true)</br >
</br >

* Add product page - add-product.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/11%20-%20w3c%20-%20add-product.png?raw=true)</br >
</br >

* Update product page - update-product.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/12%20-%20w3c%20-%20update-product.png?raw=true)</br >
</br >

* Delete product page - delete-product.html
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/html/13%20-%20w3c%20-%20delete-product.png?raw=true)</br >
</br >

## CSS W3C Testing
The CSS was tested using W3C's [Nu HTML Checker](https://validator.w3.org/nu/#textarea) and selecting 'CSS'. Additionally the CSS was also put through W3C's [Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

In each instance there were no errors returned.


* W3C Nu HTML Checker
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/css/1%20-%20w3c%20-%20css.png?raw=true)</br >
</br >

* W3C Jigsaw
![image](https://github.com/cmikedev/ecommerce/blob/main/manual_testing/images/css/2%20-%20w3c%20-%20css%20jigsaw.png?raw=true)</br >
</br >


## JavaScript JShint Testing
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
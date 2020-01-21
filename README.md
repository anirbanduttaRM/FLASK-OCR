# FLASK-OCR
Demonstrating Flask to create a simple Web-API which upon receiving a particular image produces as output OCR of the image
Demonstrating Flask to create a simple Web-API which upon receiving a particular image produces as output OCR of the image
Most of the time the real use of the Machine Learning code lies at the heart of an application which integrates the ML code to becomes a smart application.
“Consider the following situation:
You have built a super cool machine learning model that can predict if a particular transaction is fraudulent or not. Now, a friend of yours is developing an android application for general banking activities and wants to integrate your machine learning model in their application for its super objective.
But your friend found out that, you have coded your model in Python while your friend is building his application in Java. So? Won't it be possible to integrate your machine learning model into your friend's application?
Fortunately enough, you have the power of APIs. And the above situation is one of the many where the need of turning your machine learning models into APIs is extremely important.” - https://www.datacamp.com/community/tutorials/machine-learning-models-api-python
The below code demonstrates how you can use Flask - A web services' framework in Python, to wrap a machine learning Python code into an API.
Github link:
Few things to note:
•	Here it is assumed the image is already in the path of the python code. That is we are not inputting the image from API. Since that was not the primary object of the exercise.
•	You will find 2 OCR functions –
        image  = Image.open("screenshot.jpg")
        image.filter(ImageFilter.SHARPEN)
        new_size = tuple(2*x for x in image.size)
        image = image.resize(new_size, Image.ANTIALIAS)
        txt1 = pytesseract.image_to_string(image)
        #return jsonify({'Converted OCR A': str(txt1)})  
    
        image = cv2.imread("screenshot.jpg") 
        image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)
        cv2.threshold(cv2.bilateralFilter(image, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        txt2 = pytesseract.image_to_string(image)    
        return jsonify({'Converted OCR ': str(txt1)})
Use any of the one. Add return at the end of the one you prefer to use. I will suggest you should try the accuracy of both.
•	I used postman to check the result. You can do the same.
•	After running flask if you need to check if it has been installed properly again refer to the article I have mentioned above from datacamp to check the screen shots. And from the same link you can refer how to run and check your code in postman.
•	Please note here since the objective was to demonstrate the flask I haven’t chosen a model that needed to be trained. IF you have a model which needs to be trained write and train the model in a separate py file and call that file from the flask py file.
Resource that was referred: 
https://www.datacamp.com/community/tutorials/machine-learning-models-api-python

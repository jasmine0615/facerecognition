# facerecognition
✨Face recognition project to track employee attendance✨


✨Features of the project:
----------------------------------
•Login system for the administrator
•Employee registration portal
•Data set training 
•Face recognition done through the images that have been trained
•Marking employee attendance through face recognition system day-wise

✨This project has been made using python and MYSQL database
The libraries used for this project include opencv,tkinter,PIL,etc.

☑️Project flow & explaination
-----------------------------
•After you run the project you will find a login page 
![Screenshot 2022-05-28 184801](https://user-images.githubusercontent.com/101412448/170827304-aa1edf2d-4284-4fba-adfe-fce48dafe6af.png)
•You can login using the credentials (username/email=jasp@gmail.com,password=jasmine11) and if you are a new user then click on the register button
Once the registration is done the data gets stored in the database and now you can login with your credentials.
![image](https://user-images.githubusercontent.com/101412448/170827375-d93b5d90-df60-4ff4-af5b-156a910dbbb0.png)
•You will be redirected to a page which has various option such as ✨employee information where you can find the details of the employee in your company,✨ data training button is to train the model using the algorithm,and✨  a face recognition button which will redirect you to the system and the employee can be detected
![image](https://user-images.githubusercontent.com/101412448/170827416-7bedf915-4374-4f83-a728-8d0a90c1faee.png)
•Upon clicking on the employee details button you will be redirected to a page where you can save the new employee details,update the old employee details,delete the employee details,take photo button where the sample pictures of each employee are taken and stored into database once converted into grayscale
![image](https://user-images.githubusercontent.com/101412448/170827563-37fbfac6-70db-44dd-9c05-59a2049dab1d.png)
•Once the images have been captured ,which can be done by clicking upon the Train your data button➡️Train Dataset. Here the images get converted inside the machine with the help of the algorithm used
![image](https://user-images.githubusercontent.com/101412448/170827776-f1202124-4d37-42d1-a7a6-c5e78c28fc74.png)
•Once this process is done, you can start your face recognition process by clicking upon the button Face Recognition➡️Start face recognition and it opens the camera on your device and recognises the person if his/her photo has been stored inside the database 
![image](https://user-images.githubusercontent.com/101412448/170828076-7bfc7d48-79e7-4055-bfd0-5713227b0aef.png)
•Once the Face has been recognised the employee's id,name,designation,time when the face has been recognised,date will get stored in a csv file... and this will be done day-wise. (For eg: The below image show the entry of the data into csv file)
![image](https://user-images.githubusercontent.com/101412448/170828276-83b29aaa-4d15-41c0-b2be-49750cf7efb7.png)

![video1381475171_AdobeCreativeCloudExpress](https://user-images.githubusercontent.com/101412448/170828730-4b3aad58-2a69-4b51-82ee-416fe25e857a.gif)



# Clone this project




$ git clone https://github.com/jasmine0615/facerecognition.git

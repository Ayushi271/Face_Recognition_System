#######################################################    FIGHT BY TECH    ###################################################################

This main goal or objective of this project is to make use of technology and get information easily in the difficult times of the COVID ERA.


Packages should already have to be installed:

* VS CODE is suggested to open the file and you can download it from "https://code.visualstudio.com/download"

* Python should be installed version "3.10.4" only .You can download it from here "https://www.python.org/downloads/"

* Make sure to add path of python to environment variables.

* By clicking again on the python installer choose modify this time and at second page choose Add path to environment variables.

* Install the extension of Python in VS Code or click Ctrl+Shift+X and search python extension and download it.

* Install mysql community and then workbench "https://dev.mysql.com/downloads/file/?id=511552" and set up the whole process. Can take help from the link "https://www.youtube.com/watch?v=OM4aZJW_Ojs"

# Please use host= localhost, username = root, password=Ayushi1730@, database= face_recognition

Now after setting the database click on the Server option present in mysql workbench. Check image in this folder named "mysql.png"

Inside it please select Data Import option

Then choose Import from Self-Contained File and set Default_Target_Schema = face_recognition only 

And in front of Import from self-contained file write the path name as    C:\Face_Recognition_System\Dump20220528.sql   copy link 

At bottom choose Start Import 

* Clone the repository by running git clone in the git bash with help of a folder. Name the folder as Face_Recognition_System

* Run the command in git bash of by selecting Face_Recognition_Folder in your C drive. Right Click and then choose show more option and then git bash. Command is  :   git clone https://github.com/Ayushi271/Face_Recognition_System.git

* By doing this a folder named Face_Recognition_System will include inside a same name folder. 

* Now copy that folder and paste directly in C:/ having same name Face_Recognition_System. It will replace a folder and by clicking Face_Recognition_System inside C:\  directly all the files will show there.

* Now open the file by use of Visual Studio Code. Open vs code and select open folder  in upper File section and open this folder.


* Run these commands in the  the terminal  of the vs code or command prompt .
<!-- Version can be different. But check if it is different so there is no error otherwise these versions are favoured-->
 
  pip install beautifulsoup4               4.11.1

  pip install  bs4                         0.0.1

  <!-- pip install cmake                        3.22.4

  pip install dlib                         19.22.99 -->

  pip install Flask                        2.1.2

  pip install imutils                      0.5.4

  pip install  keras                       2.9.0

  pip install  Keras-Preprocessing         1.1.2

  pip install  matplotlib                  3.5.2
  
  pip install wheel                         0.37.1

  <!-- pip install  mediapipe                   0.8.10 -->

  pip install  mysql-connector-python      8.0.29

  pip install  numpy                       1.22.3

  pip install opencv-contrib-python        4.5.5.64
  
  pip install opencv-python                4.5.5.64

  pip install  Pillow                      9.1.0

  pip install sklearn

  pip install pyautogui==0.9.35

  pip install  pywhatkit                   5.3

  pip install  requests                    2.27.1
                
  pip install tensorflow                   2.9.0

  pip install urllib3                      1.26.9


  After installing all packages please reopen the folder with vs code. so that every package will be there correctly present.

The project cover a landing page and six features.

The landing page can be opened by "index.py" file.



# SET UP

* 1:Clone the repository by clicking "https://github.com/Ayushi271/FIGHT-BY-TECH"

* 2:And clone it inside the Windows C or "C". It will get cloned as Face_Recognition_System or otherwise change its name to Face_Recognition_System


# Covid Patient Details

This feature work as a database where you can search a person details or you can fill the data to upload it in the database.
For the database part I have used MYSQL Workbench 8.0 CE
For downloading it go through the link ("https://www.mysql.com/products/workbench/")

This feature is going to help us  to get  correct data of covid death cases without any fraud. This feature can be available for common public so that they can also feed data of death cases around them. That's how it will cover more data and more cases and data will be transparent to common public too and government can't use forgery methods. 

In left section there are four sections:
# Information:

In this you can fill the data like choose Profession, Place of Death, Month of Death,Year of Death.

# Information of Covid Patient

In this section you can fill more details about the covid patient.
Like Patient Name,age,gender,exact place of death.
if you want to take photo currently then click "Take photo as sample" otherwise click "No photo as sample"

# Buttons Section

In this section you have four options such as Save the data. You can update the data which is already there, You can reset the data that are filled and you delete the data too.

# Photo Button section

In this section you can click the photo in present time and upload it and save it.

In right section there are section like:

# Search results

Here you can see all the data what you feed or what has already fed to it.

# RUN COVID PATIENT DETAILS


1: Clone the project and go to index.py

2: Install all the packages and dependencies.

3: Run the python file by clicking run option (in VS CODE )or you can use the terminal too.

4: Click on the Covid Patient Details option.

5: Fill the information to feed data. and check on the right section to see data.

6: All the code of this is present in covid.py.

7: All the dataset is present and will get upload to the data1.

5: It is highly recommended to run the covid.py file which include the covid patient details feature's code via index.py otherwise the page of GUI will not be clearly available. It is due to installation of pywhatkit. It always reduce the window size of GUI application.

# TRAIN  DATA

This feature is going to train the dta for us.

Click Train Data option inside the Train data feature.

The image which has to be trained must be in folder data1 to be get trained.

# RUN TRAIN DATA

1: Install all the depedencies and packages list above.

2: Click on the train data

3: The code for Train data is stored in the train_face.py.

4: Again it is highly recommended to run the file via index.py otherwise there be difference in size of window size if you open it directly.

# SEARCH FACES

This feature is mainly for finding people who died of covid.

As we all know last few years due to covid there were many people who were living far from their home mainly labours who went out in different state in the search of job died of covid, many of them were unidentified and many families did even got to know that their family member had died because they were not able to travel so much and also don't know more about that place or where to find them.

# RUN SEARCH FACES

1: Run index.py and then Click on the Search Faces.

2: Inside it a page will open and then click Recognize the face.

3: Press "q" or "Q" for exit.

4: The code of this page is in the face_recognition.py

5: Again it is highly recommended to run the file via index.py otherwise there be difference in size of window size if you open it directly.

#  Mask Detection

This feature will detect the mask on the face and tell about that the person has wore the mask or not. For saving the data press "a" so that a data of yours can be stored. This will help to check that in a organization how many people come with mask and without mask.

# RUN MASK DETECTION

Clone the repository and then,

1: Run index.py then click on the Mask Detecction 

2: Then Click again on Mask Detection and the camera will open and detect your mask and also gives the percentage.

3: All te code for mask detection is in the detect_mask_video.py and all the training data code are in train_mask_detector.py and the dataset are present in dataset folder having two subfolders mask and withoutmask.

4: It is highly recommended to run the file via index.py otherwise there be difference in size of window size if you open it directly due to import of pywhatkit in another file of python.

# HEAL YOUR SOUL

As we all know that music is one of the best medicine for the curing any type of illness. So this feature can be used by hospitals or anyone in which the camera will detect the emotion and will recommend songs.

Clone the repository and then,

1: Run index.py and click on the Heal your Soul option.

2: On the next page also click on the Heal you soul option.

3: Camera will start. Then click a for snapping or taking screeshot of your images. then press q for exit.

4:Now it will recommend you a song.

5:Your emotion must be precise and be in Happy, Sad , Neutral , Angry , Surprised , Disgust ,Fear

6: All the codes are present in the test_emotion.py.

7: The training of dataset is present in main_emotion_train.py and all the dataset are in the data folder in train and test folder.

8: It is highly recommended to run the file via index.py otherwise there be difference in size of window size if you open it directly due to import of pywhatkit in this python file.

# COVID CASES

The main aim of this feature is to inform us about the number of covid cases, death cases and recovered patient cases.

Clone the repository and then,

1: Run index.py and click on Covid Cases option.

2: A page will open  and then click on Covid cases.

3: Again a page will open which will give the total data of covid cases.

4: In the blank you can type any country name and can find the cases count in that country.

5: The coding of the page is stored in the corona_cases.py.

6: It is highly recommended to run the file via index.py otherwise there be difference in size of window size if you open it directly due to import of pywhatkit in another file of python.



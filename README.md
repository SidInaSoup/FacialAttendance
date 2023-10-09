# Facial_Recognition_Attendance

A django web app to keep track of your employess'/students' attendance using just a cctv camera.

Features:
- Connects to usb device
- Connects to ip camera (CCTV camera hosted on a server)
- Requires only a single clear picture of your employee to track them
- All details and pictures can be uploaded easily on the front end
- Department wise management
- Allows for easy viewing/deletion/updation of all records including attendance, employee list (picture updation as well), department list

  Steps to use:
  1) Clone repo to your local system
  2) Activate the venv by typing Scripts/activate on the root folder.
  3) cd to 'facialattendance' and type **_python manage.py runserver_**
  4) open the index.html file located in the **ui** folder of the root directory
     ![image](https://github.com/SidInaSoup/FacialAttendance/assets/91547590/643cd42c-a217-4993-b236-50ceadff2baa)

  App features:
  1) Start a live cam to either your computer's webcam or a usb device by clicking start (checks default device)
     ![image](https://github.com/SidInaSoup/FacialAttendance/assets/91547590/904b8829-33a2-447a-b2a7-e7624474ee13)
  2) Use the enter IP button to enter the IP address of your webcam
     ![image](https://github.com/SidInaSoup/FacialAttendance/assets/91547590/175d0d04-b898-4d7d-900c-a99e7db3e23a)
  3) Use the view attendance button to view the recorded attendance upto this point.
     ![image](https://github.com/SidInaSoup/FacialAttendance/assets/91547590/f82cea1f-3d84-43db-ad00-afcfa1f2ff97)

  Updating Employee names and pictures:
  1) Use the Employee tab to view,add,update or delete employee records:
     ![image](https://github.com/SidInaSoup/FacialAttendance/assets/91547590/5432701b-78d1-4170-9fd0-a4a055591377)
     **IMP: Make sure the picture is a clear frontal view as this is used in face detection**
  2) Use the departments tab to view,add,update or delete department records:
     ![image](https://github.com/SidInaSoup/FacialAttendance/assets/91547590/17918458-1cc5-47c6-8bd3-e1f3af07f8a8)






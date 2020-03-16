import cv2
import os
import numpy as np
import faceRecognition as fr
import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line

#This module takes images  stored in diskand performs face recognition
test_img=cv2.imread('TestImages/rohit.jpg')#test_img path
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

#Comment belows lines when running this program second time.Since it saves training.yml file in directory
#faces,faceID=fr.labels_for_training_data('trainingImages')
#face_recognizer=fr.train_classifier(faces,faceID)
#face_recognizer.write('trainingData.yml')


#Uncomment below line for subsequent runs
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#use this to load training data for subsequent runs

name={0:"bhanu",1:"kangana"}#creating dictionary containing names for each label

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>37):#If confidence more than 37 then don't print predicted face text on screen
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(500,500))
cv2.imshow("face dtecetion ",resized_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows
# User configuration
sender_email = 'xyz@gmail.com'
sender_name = 'xyz'
password = input('Please, type your password:\n')

receiver_emails = ['abc@gmail.com']
receiver_names = ['abc']

# Email body
email_html = open('email.html')
email_body = email_html.read()
face = input('please enter the co-ordinates : \n')
filename = "frame5.jpg"

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
	print("Sending the email...")
	# Configurating user's info
	msg = MIMEMultipart()
	msg['To'] = formataddr((receiver_name, receiver_email))
	msg['From'] = formataddr((sender_name, sender_email))
	msg['Subject'] = 'Hello, my friend ' + receiver_name + face
	msg.attach(MIMEText(email_body, 'html'))
	
  # if i comment try block below one i'm getting mail but not image
  try:
		with open(filename, "rb") as attachment:
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		# Encode file in ASCII characters to send by email
		encoders.encode_base64(part)

		# Add header as key/value pair to attachment part
		part.add_header(
				"Content-Disposition",
				f"attachment; filename= {filename}",
		)

		msg.attach(part)
	except Exception as e:
			print(f'Oh no! We didn\'t found the attachment!\n{e}')
			break

	try:
			# Creating a SMTP session | use 587 with TLS, 465 SSL and 25
			server = smtplib.SMTP('smtp.gmail.com', 587)
			# Encrypts the email
			context = ssl.create_default_context()
			server.starttls(context=context)
			# We log in into our Google account
			server.login(sender_email, password)
			# Sending email from sender, to receiver with the email body
			server.sendmail(sender_email, receiver_email, msg.as_string())
			print('Email sent!')
	except Exception as e:
			print(f'Oh no! Something bad happened!\n{e}')
			break
	finally:
			print('Closing the server...')
			server.quit()

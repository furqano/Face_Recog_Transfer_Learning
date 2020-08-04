import streamlit as st 
import cv2
import numpy as np 
import os
import time

def web_cam(user,choice):
    if user != '':
        os.makedirs(user)
        ss = os.path.join(user+'\\')
        prog = st.progress(0)
        if choice == 'Capture':
            face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            st.subheader("Face Authentication")
            cap = cv2.VideoCapture(0)
            count = 0
            while True:
                ret, frame = cap.read()
                if face_extractor(frame) is not None:
                    count += 1
                    face = cv2.resize(face_extractor(frame), (200, 200))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    # Save file in specified directory with unique name
                    file_name_path = ss  + str(count) + '.jpg'
                    cv2.imwrite(file_name_path, face)
                    # Put count on images and display live count
                    cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                    cv2.imshow('Face Cropper', face)
                    prog.progress(count)
                            

                else:
                    print("Face not found")
                    st.spinner('we are working on it ...')
                    pass

                        
                if cv2.waitKey(1) == 13 or count == 100: #13 is the Enter Key
                    break
                
            cap.release()
            cv2.destroyAllWindows()
            st.text("Collecting Samples Complete")

def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face






def main():
    """Face Detection App"""
    st.title("TRANSFER LEARNING")
    st.text("Build you're own face detection models")
    st.text("Build with Streamlit and OpenCV")
    user_input = st.text_input("Enter Your Name ... ")
    Activities=["Capture" , "About"]
    choice = st.sidebar.selectbox("Selected" , Activities)
    #str1=('D:\\Dataset')
    user = (user_input)
    if st.button('Start'):
        web_cam(user,choice) 
    elif choice == 'About':
        st.subheader("About Face Detection App")
        st.markdown("Built with Streamlit by [FateDaeth]")
        st.text("FateDaeth")
        st.success("FateDaeth")
if __name__ == '__main__':
    main()
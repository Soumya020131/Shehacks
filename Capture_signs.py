import cv2
import os
import time
import uuid

IMAGES_PATH = 'RealTimeObjectDetection\Tensorflow\workspace\images'
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    dir = label
    path = os.path.join(IMAGES_PATH, dir) 
    os.makedirs(path)
    '''os.mkdir (IMAGES_PATH + label)'''
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(10)
    if cap.isOpened():
        for imgnum in range(number_imgs):
            ret, frame = cap.read()
            print(ret)
            imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imagename, frame)
            cv2.imshow('frame', frame)
            time.sleep(5)

            if cv2.waitKey(3) & 0xFF == ord('q'):
                break

    else:
        print('no')

    cap.release()
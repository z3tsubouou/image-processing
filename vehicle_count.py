
import cv2
import numpy as np
from tracker import *

#tanilt hiigchiig oruulah
tracker = EuclideanDistTracker()

#bichleg oruulahiig oruulah
cap = cv2.VideoCapture('video2.mp4')
input_size = 320

#treshold hiih tohirgoo
confThreshold =0.2
nmsThreshold= 0.2

font_color = (0, 0, 255)
font_size = 0.5
font_thickness = 2

#unguruh zuraasnii zai
middle_line_position = 225   
up_line_position = middle_line_position - 15
down_line_position = middle_line_position + 15


#coco nersiin jigsaalt
classesFile = "coco.names"
classNames = open(classesFile).read().strip().split('\n')
# print(classNames)
# print(len(classNames))

# class index for our required detection classes
#heregtei classiin index
required_class_index = [2, 3, 5, 7]

detected_classNames = []

#modeliin ners
modelConfiguration = 'yolov3-320.cfg'
modelWeigheights = 'yolov3-320.weights'

#holbolt hiih modeliin tohirgoo
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigheights)

#holboltiin backend tohirgoo
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

#class bolgond sanaandgui baidlaar uur ungu olgoh
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classNames), 3), dtype='uint8')

#tegsh untsugtiin gol tsegiig oloh
def find_center(x, y, w, h):
    x1=int(w/2)
    y1=int(h/2)
    cx = x+x1
    cy=y+y1
    return cx, cy
    
#mashiniig toolj oruulah husnegt
temp_up_list = []
temp_down_list = []
up_list = [0, 0, 0, 0]
down_list = [0, 0, 0, 0]

#mashiniig toolj bui function
def count_vehicle(box_id, img):

    x, y, w, h, id, index = box_id

    #tegsh untsugtiin goliig n oloh
    center = find_center(x, y, w, h)
    ix, iy = center
    
    #tuhain mashinii baigaa gazriig oloh
    if (iy > up_line_position) and (iy < middle_line_position):

        if id not in temp_up_list:
            temp_up_list.append(id)

    elif iy < down_line_position and iy > middle_line_position:
        if id not in temp_down_list:
            temp_down_list.append(id)
            
    elif iy < up_line_position:
        if id in temp_down_list:
            temp_down_list.remove(id)
            up_list[index] = up_list[index]+1

    elif iy > down_line_position:
        if id in temp_up_list:
            temp_up_list.remove(id)
            down_list[index] = down_list[index] + 1

    #tegsh untsugtiin gold tseg zurah
    cv2.circle(img, center, 2, (0, 0, 255), -1)

#oldson mashinaas ali n wee gedgiig oloh function
def postProcess(outputs,img):
    global detected_classNames 
    height, width = img.shape[:2]
    boxes = []
    classIds = []
    confidence_scores = []
    detection = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if classId in required_class_index:
                if confidence > confThreshold:
                    # print(classId)
                    w,h = int(det[2]*width) , int(det[3]*height)
                    x,y = int((det[0]*width)-w/2) , int((det[1]*height)-h/2)
                    boxes.append([x,y,w,h])
                    classIds.append(classId)
                    confidence_scores.append(float(confidence))

    #non-max suppression oruulj ugnu. Ene olon dawharlagdsan object yum
    indices = cv2.dnn.NMSBoxes(boxes, confidence_scores, confThreshold, nmsThreshold)
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]
            # print(x,y,w,h)

            color = [int(c) for c in colors[classIds[i]]]
            name = classNames[classIds[i]]
            detected_classNames.append(name)
            cv2.putText(img,f'{name.upper()} {int(confidence_scores[i]*100)}%',
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            detection.append([x, y, w, h, required_class_index.index(classIds[i])])

    #object buriig neg burchlen shinechlene
    boxes_ids = tracker.update(detection)
    for box_id in boxes_ids:
        count_vehicle(box_id, img)


def realTime():
    while True:
        success, img = cap.read()
        img = cv2.resize(img,(0,0),None,0.5,0.5)
        ih, iw, channels = img.shape
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False)

        #holboltiin utgiig oruulj uguh
        net.setInput(blob)
        layersNames = net.getLayerNames()
        outputNames = [(layersNames[i - 1]) for i in net.getUnconnectedOutLayers()]
        #holboltond ugugdult oruulj uguh
        outputs = net.forward(outputNames)
    
        #holboltond taarahaar object oruulj uguh
        postProcess(outputs,img)

        #unguruh zuraasiig tawij ugnu baina
        cv2.line(img, (0, middle_line_position), (iw, middle_line_position), (255, 0, 255), 2)
        cv2.line(img, (0, up_line_position), (iw, up_line_position), (0, 0, 255), 2)
        cv2.line(img, (0, down_line_position), (iw, down_line_position), (0, 0, 255), 2)

        #neg frame buriig haruulah
        cv2.imshow('Output', img)

        if cv2.waitKey(1) == ord('q'):
            break

    #ashiglaj baigaa buh tsonhiig utgah
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #bichlegnees tanilt hiih
    realTime()
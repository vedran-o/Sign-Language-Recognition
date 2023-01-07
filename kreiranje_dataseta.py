import os
import copy
import cv2
import uuid
## Funkcija za postavljanje direktroija

def Izradi_direktorij_geste(directory):
    global prva_gesta
    if not os.path.exists(directory):
        os.makedirs(directory)
        return None
    else:
        prva_gesta

def Izradi_direktorij_train_test(link):
    global prva_gesta
    if not os.path.exists(link):
        os.makedirs(link)
        return None
    else:
        prva_gesta

    

# Izgradnja dataseta pomoću OpenCV-a

cap = cv2.VideoCapture(0) # Defaultni camera module

i = 3
ukupan_broj_slika = 0
ogranicenje_snimljenih_slika = 0

ogranicenje_snimljenih_slika_TRAIN = 0
ogranicenje_snimljenih_slika_TEST = 0

izlaz = ""
dialog = ""
prva_gesta = ""
resetiranje_dataseta = ""

temp_TRAIN = 0
temp_TEST = 0

glavniDIR = "./Dataset gestikulacije"
trainDS = "./Dataset gestikulacije/train"
testDS = "./Dataset gestikulacije/test"

print("Molim vas odredite velicinu TRAIN - DSa za sve klase: ")
ogranicenje_snimljenih_slika_TRAIN = int(input())

print("Molim vas odredite velicinu TEST - DSa za sve klase: ")
ogranicenje_snimljenih_slika_TEST = int(input())

Izradi_direktorij_train_test(trainDS)
Izradi_direktorij_train_test(testDS)

print("Unesite ime klase za koju zelite izraditi dataset: ")
dialog = input()














while ( izlaz != "DA" ):

    ## Čitanje videa
    
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    ## Definiranje regije interesa ( ROI )
    
    ROI = frame[100:400, 320:620]
    cv2.imshow('Regija interesa', ROI)
    ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    ROI = cv2.resize(ROI, (28, 28), interpolation = cv2.INTER_AREA)
    
    cv2.imshow('Skalirana regija interesa', ROI)
    kopija_frame = frame.copy()
    cv2.rectangle(kopija_frame, (320, 100), (620, 420), (255, 0, 0), 5)
    
    if ((i == 0) and ((ogranicenje_snimljenih_slika_TRAIN == 0) and (ogranicenje_snimljenih_slika_TEST == 0))):
        print("Molim vas odredite velicinu TRAIN - DSa za sve klase: ")
        ogranicenje_snimljenih_slika_TRAIN = int(input())

        print("Molim vas odredite velicinu TEST - DSa za sve klase: ")
        ogranicenje_snimljenih_slika_TEST = int(input())

        print("Unesite ime klase za koju zelite izraditi dataset: ")
        dialog = input()
        prva_gesta = "./Dataset gestikulacije/train/" + dialog + "/"
        
        Izradi_direktorij_train_test(trainDS)
        Izradi_direktorij_train_test(testDS)

        
        if ((ogranicenje_snimljenih_slika_TRAIN != 0) and (ogranicenje_snimljenih_slika_TEST != 0)):
            i = 3
    if i == 3:
        ukupan_broj_slika = 0
        cv2.putText(kopija_frame, "Kada ste spremni pritisnite tipku [ENTER] kako bi zapoceli snimanje TRAIN slika za dataset " + dialog, (100, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 255, 100), 4)
    
    
    if (( i == 4 ) and (ogranicenje_snimljenih_slika_TRAIN > ukupan_broj_slika)):
        ukupan_broj_slika = ukupan_broj_slika + 1
        cv2.rectangle(kopija_frame, (320, 100), (620, 420), (0, 0, 255), 5)
        cv2.putText(kopija_frame, "Snimanje fotografija za TRAIN DATASET - Klasa: " + dialog, (100, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 4)
        cv2.putText(kopija_frame, "Trenutni broj snimljenih slika: ", (150, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
        cv2.putText(kopija_frame, str(ukupan_broj_slika), (750, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        prva_gesta = "./Dataset gestikulacije/train/" + dialog + "/"
        Izradi_direktorij_geste(prva_gesta)
        cv2.imwrite(prva_gesta + str(uuid.uuid4()) + ".jpg", ROI)
        if (ogranicenje_snimljenih_slika_TRAIN == ukupan_broj_slika):
            i = i + 1
            ukupan_broj_slika = 0
        
    if i == 5:
        ukupan_broj_slika = 0
        cv2.putText(kopija_frame, "Kada ste spremni pritisnite tipku [ENTER] kako bi započeli snimanje TEST slika za dataset " + dialog, (100, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 4)
    
    if ((i == 6) and (ogranicenje_snimljenih_slika_TEST > ukupan_broj_slika)):
        ukupan_broj_slika = ukupan_broj_slika + 1
        cv2.rectangle(kopija_frame, (320, 100), (620, 420), (0, 0, 255), 5)
        cv2.putText(kopija_frame, "Snimanje fotografija za TEST DATASET - Klasa: " + dialog, (100, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 4)
        cv2.putText(kopija_frame, "Trenutni broj snimljenih slika: ", (150, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
        cv2.putText(kopija_frame, str(ukupan_broj_slika), (750, 480), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        prva_gesta = "./Dataset gestikulacije/test/" + dialog + "/"
        Izradi_direktorij_geste(prva_gesta)
        cv2.imwrite(prva_gesta + str(uuid.uuid4()) + ".jpg", ROI)
        if (ogranicenje_snimljenih_slika_TEST == ukupan_broj_slika):
            i = i + 1
            ukupan_broj_slika = 0

    if i == 7:
        cv2.putText(kopija_frame, "Pritisni [ENTER] za izlaz", (100, 60),
        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
    
    cv2.imshow('Frame', kopija_frame)

    if i == 8:
        print("Želite li prekinuti ovaj program?")
        print("Jedino 'DA' će prekinuti program")
        izlaz = input()
        if izlaz == "DA":
            ukupan_broj_slika = 0
            i = 0
            ogranicenje_snimljenih_slika_TRAIN = 0
            ogranicenje_snimljenih_slika_TEST = 0
            
        else:
            temp_TRAIN = ogranicenje_snimljenih_slika_TRAIN
            temp_TEST = ogranicenje_snimljenih_slika_TEST
            print("\nDali zelite koristiti istu kolicniu ( broj slika ) za novi dataset?")
            print("Podsjetnik:\nTrain = {}\nTest = {}\n".format(ogranicenje_snimljenih_slika_TRAIN, ogranicenje_snimljenih_slika_TEST))
            print("Molim Vas odgovorite pomocu DA ili NE: ")
            resetiranje_dataseta = input()
            if resetiranje_dataseta == "DA":
                ukupan_broj_slika = 0
                i = 3
            
                ogranicenje_snimljenih_slika_TRAIN = temp_TRAIN
                ogranicenje_snimljenih_slika_TEST = temp_TEST
                
                print("Unesite ime klase za koju zelite izraditi dataset: ")
                dialog = input()
                prva_gesta = "./Dataset gestikulacije/train/" + dialog + "/"
                
            else:
                ogranicenje_snimljenih_slika_TRAIN = 0
                ogranicenje_snimljenih_slika_TEST = 0
                
                ukupan_broj_slika = 0
                i = 0

    if cv2.waitKey(1) == 13:
            i = i + 1
            
cap.release()
cv2.destroyAllWindows()
        



    

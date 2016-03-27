import numpy
import cv2


def play(img):
    '''

    * Function Name:	train
    * Input:            none
    * Output:		Knearest trained object
    * Logic:		Taking sample input and output array to train the k n nearest oject 
    * Example Call:	train();
    *
    '''
    def train() :
        """TRAINING DATA FROM TESTIMAGE1 HuMoments[0:4] and applying log Transform"""
        #humoments data [0:4]      
        data=[[0.69655012005942729, 2.1964907950759005, 2.6562449644775565,4.4595057809897538],
              [0.45095214332527545, 1.0664771939672364,2.357612208789142, 2.8895776359610186],
              [0.50128198441868876, 1.4317594719473725, 2.6254613478624056, 3.3223959855270406],
             [0.45634714937084686, 1.0891489602158844, 2.3108875237071937,2.8614528093296032],
              [0.70018112731777782, 2.1682834890437248,3.1781546828006659, 3.5564186869878167],
               [0.70018112731777782, 2.1682834890437248,3.1781546828006659, 3.5564186869878167],
               [0.70018112731777782, 2.1682834890437248,3.1781546828006659, 3.5564186869878167],
              [0.49864038808901384,1.4211567894276607, 2.6058502856786059, 3.2847516295032593],
        [0.46332612991059258, 1.3480546357511025, 2.7068882507464314,3.2954996507337349],
              [0.45262305255094742, 1.0803524562919025,2.283601736950942, 2.8233216922776876], [0.46714363945446885,
        1.3582846382985159, 2.6964466421665603, 3.2982051729774455],
        [0.42787640917239905, 1.2376479517621892, 1.675033377313554,
        2.4359045357232056], [0.76203933647414734, 2.3434426372459969,
        6.533402249372581, 7.8750721681434541], [0.46219117548353256,
        1.3495661999732242, 2.6762050710495409, 3.2457746643455265],
        [0.45085272959920814, 1.0676536568575248, 2.3549438684146313,
        2.886717391315643], [0.76197563623041698, 2.3431245165351364,
        7.1787935401282006, 8.6432743822863412], [0.50412749371557952,
        1.4734192740271703, 3.4256012141326804, 4.0557873193974761],
        [0.45362646400605144, 1.0829073441256898, 2.3055795704932458,
        2.8534145011890013], [0.7118727769921489, 2.2254067399042672,
        3.2390017885404645, 3.679615702385004],[0.7118727769921489, 2.2254067399042672,
        3.2390017885404645, 3.679615702385004], [0.72467567787030329,
        2.1084550319337692, 4.3373430008596348, 5.4043891889075333]]
        traindata = numpy.array(data).astype(numpy.float32)#storing sample input data
        resp =[4,1,3,1,9,9,9,3,2,1,2,7,0,2,1,0,5,1,6,6,8]#storing expected ouput data
        respdata =numpy.array(resp).astype(numpy.float32)
        knn = cv2.KNearest()
        knn.train(traindata,respdata)#training with the sample input and expected output
        return knn
    ############################################
    '''

    * Function Name:	find()
    * Input:		mom -> moments of the number ,knn -> k n nearest trained object
    * Output:		nearest numbers that match
    * Logic:		find hu moments from the moments and pass it to the knn object to get the nearest neighbours
    * Example Call:	find(Moments,KNN object)
    *
    '''
    def find(mom,knn) :
        """RECOGNIZING THE DIGIT"""
        # finding hu moments from the moments data
        huk=[]
        for hu in cv2.HuMoments(mom).tolist():
            hu[0]=-numpy.sign(hu[0])*numpy.log10(numpy.abs(hu[0]))
            huk.append(hu[0])
        t=[]
        t.append(huk[0:4])
        newcomer = numpy.array(t).astype(numpy.float32)
        ret, results, neighbours ,dist = knn.find_nearest(newcomer,6 )#finding matching number
        return neighbours[0].tolist()[0],dist
    ############################################
    """START"""
    knn=train()
    
    i = 0
    #finding contours
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in range(l,(len(contours))) :
                    res = cv2.drawContours(img,contours,i,(0,255,0),2)
                    mom = cv2.moments(contours[j])
                    num,dist=find(mom,knn)
                    print num,":"
    return
if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('Puzzle Solver O.jpg')
    play(img)

    cv2.imshow('image',im1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


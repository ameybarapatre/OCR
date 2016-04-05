import numpy
import cv2


def play(img):
    '''

    * Function Name:	find()
    * Input:		mom -> moments of the number 
    * Output:		humoments[0:4] of contours
    * Example Call:	find(Moments)
    *
    '''
    def find(mom) :
        """RECOGNIZING THE DIGIT"""
        # finding hu moments from the moments data
        huk=[]
        for hu in cv2.HuMoments(mom).tolist():
            hu[0]=-numpy.sign(hu[0])*numpy.log10(numpy.abs(hu[0]))
            huk.append(hu[0])
        t=[]
        t.append(huk[0:4])
        return t
    ############################################
    """START"""
    
    i = 0
    #finding contours
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for i in range(1,(len(contours))) :
        res = cv2.drawContours(img,contours,i,(0,255,0),2)
        mom = cv2.moments(contours[i])
        num=find(mom)
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        x = raw_input("Needed value ?")
        print num ,":",x  
        
    return
if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('Puzzle Solver O.jpg')
    play(img)

   
    


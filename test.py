pt1=starting_point
		pt1[2]=pt1[2]-(bl*mf_cl-bl*mf_ab)*mf_150
		pt1[1]=pt1[1]+0.5*sw*mf_150
		
		pt2=pt1
		pt2[2]=pt2[2]+(bl+2*bl*mf_cl)*mf_150
        print 
        return pt1, pt2
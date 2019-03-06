import cv2

def grayscale(filename):

	image = cv2.imread(filename)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cv2.imshow('Original image',image)
	cv2.imshow('Gray image', gray)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imwrite('b1_grayscale.jpg', gray)

if __name__ == '__main__':
	grayscale('b1.jpg')
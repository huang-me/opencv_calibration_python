import sys
import glob
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from mainWindow import Ui_mainWindow
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)
		# connect buttons to functions
		self.ui.BTN_CORNER.clicked.connect(self.corner_clicked)
		self.ui.BTN_INTRINSIC.clicked.connect(self.intrinsic)
		self.ui.BTN_DISTORTION.clicked.connect(self.distort)
		self.ui.ID_IMAGE.currentIndexChanged.connect(self.choosefile)
		self.ui.BTN_EXTRINSIC.clicked.connect(self.extrinsic)
		self.ui.BTN_AUGMENTED.clicked.connect(self.augmented)
		self.ui.BTN_DISPARITY.clicked.connect(self.disparity)
		self.ui.BTN_KEYPOINT.clicked.connect(self.find_keypoint)
		self.ui.BTN_MATCHKEY.clicked.connect(self.draw_matchkey)
		# initialize the combo box
		self.ui.ID_IMAGE.addItems(['1', '2', '3', '4', '5', '6', \
									'7', '8', '9', '10', '11', '12', \
									'13', '14', '15'])
		# class variables for question 1
		self.extrinsic_num = 0
		self.mtx = []
		self.dist = []
		self.tvecs = []
		self.rvecs = []
		# initial calculate
		self.calibrate()

	def draw_matchkey(self):
		# load images
		img = cv.imread('Q4_Image/Aerial1.jpg', 0)
		img2 = cv.imread('Q4_Image/Aerial2.jpg', 0)

		sift = cv.SIFT_create(6, sigma=1.14)
		kp, des = sift.detectAndCompute(img, None)

		sift2 = cv.SIFT_create(6, sigma=1.14)
		kp2, des2 = sift.detectAndCompute(img2, None)

		img = cv.drawKeypoints(img, kp, img)
		img2 = cv.drawKeypoints(img2, kp2, img2)

		# create BFMatcher object
		bf = cv.BFMatcher()
		matches = bf.knnMatch(des, des2, k=2)

		# Apply ratio test
		good = []
		for m,n in matches:
			if m.distance < 0.75*n.distance:
				good.append([m])

		# Draw first 10 matches.
		img3 = img
		img3 = cv.drawMatchesKnn(img, kp, img2, kp2, good[:10], None, flags=2)

		plt.ion()
		plt.figure(2)
		plt.imshow(img3)
		plt.show()
		plt.savefig('figure2.jpg')

	def find_keypoint(self):
		# load images
		img = cv.imread('Q4_Image/Aerial1.jpg')
		img2 = cv.imread('Q4_Image/Aerial2.jpg')
		# convert images into gray
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

		sift = cv.SIFT_create(6, sigma=1.14)
		kp, des = sift.detectAndCompute(gray, None)

		sift2 = cv.SIFT_create(6, sigma=1.14)
		kp2, des2 = sift.detectAndCompute(gray2, None)

		cv.drawKeypoints(gray, kp, img, (255,255,0))
		cv.drawKeypoints(gray2, kp2, img2, (255,255,0))

		plt.ion()
		plt.subplot(1, 2, 1)
		plt.imshow(img)
		plt.subplot(1, 2, 2)
		plt.imshow(img2)
		plt.show()
		plt.savefig('figure1.jpg')

	def disparity(self):
		imgL = cv.imread('Q3_Image/imL.png', 0)
		imgR = cv.imread('Q3_Image/imR.png', 0)

		stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
		disparity = stereo.compute(imgL, imgR)
		# make plt use one thread to prevent conflict with main loop
		plt.ion()
		plt.imshow(disparity, 'gray')
		plt.show()

	def augmented(self):
		# camera calibration to compute K
		criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		w = 8
		h = 11
		objp=np.zeros((w*h, 3), np.float32)
		objp[:, :2]=np.mgrid[0:w, 0:h].T.reshape(-1, 2)
		#store the world coord. and image coord. points
		objpoints=[]
		imgpoints=[]
		images=glob.glob('Q2_Image/*.bmp')

		for fname in images:
			img=cv.imread(fname)
			gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			#find the corner of checkboard
			ret, corners=cv.findChessboardCorners(gray, (w,h), None)
			#save the points as long as find enough pair points
			if ret == True:
				cv.cornerSubPix(gray,corners,(8,11),(-1,-1),criteria)
				objpoints.append(objp)
				imgpoints.append(corners)

		#calibration
		ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

		# variables to calculate Extrinsic matrix
		objp = np.float32(objpoints).reshape(-1,3)
		imgp = np.float32(imgpoints).reshape(-1,2)

		i = 0
		for fname in images:
			# reload the image
			img = cv.imread(fname)
			# vertex and corner of tetrahedron
			tetrahedron = [(3,3,-3), (1,1,0), (3,5,0), (5,1,0)]
			# find vertex and corners of tetrahedron in 2D
			imgp, jaco = cv.projectPoints(np.float32(tetrahedron), rvecs[i], tvecs[i], mtx, dist)
			imgp = imgp.reshape(-1,2)
			# point out the corner and draw the lines	
			for point in imgp:
				point = (int(point[0]), int(point[1]))
				cv.circle(img, point, 20, (0,255,255), -1)
				for point2 in imgp:
					point2 = (int(point2[0]), int(point2[1]))
					cv.line(img, point, point2, (0,255,255), 5)
			# set the window to show image for 0.5 secs
			cv.namedWindow('image', 0)
			cv.resizeWindow('image', 500, 500)
			cv.imshow('image', img)
			cv.waitKey(500)
			# variable to count the image number
			i += 1
		# destroy all windows after showing images
		cv.destroyAllWindows()

	def calibrate(self):
		# camera calibration to compute K
		criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		w = 8
		h = 11
		objp=np.zeros((w*h, 3), np.float32)
		objp[:, :2]=np.mgrid[0:w, 0:h].T.reshape(-1, 2)
		#store the world coord. and image coord. points
		objpoints=[]
		imgpoints=[]
		images=glob.glob('Q1_Image/*.bmp')

		for fname in images:
			img=cv.imread(fname)
			gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			#find the corner of checkboard
			ret, corners=cv.findChessboardCorners(gray, (w,h), None)
			#save the points as long as find enough pair points
			if ret == True:
				cv.cornerSubPix(gray,corners,(8,11),(-1,-1),criteria)
				objpoints.append(objp)
				imgpoints.append(corners)

		#calibration
		ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
	
		# variables to calculate Extrinsic matrix
		objp = np.float32(objpoints).reshape(-1,3)
		imgp = np.float32(imgpoints).reshape(-1,2)
		ret, rvec, tvec = cv.solvePnP(objp, imgp, mtx, dist)

		# set the variable of the class
		self.mtx = mtx
		self.dist = dist
		self.tvecs = tvecs
		self.rvecs = rvecs

	def extrinsic(self):
		R, _ = cv.Rodrigues(np.float32(self.rvecs[self.extrinsic_num - 1]))
		tvec = np.float32(self.tvecs[self.extrinsic_num - 1])
		# append R and T -> extrinsic matrix
		ext = np.append(R, tvec, axis=1)
		print(ext)
	
	def choosefile(self):
		file_id = self.ui.ID_IMAGE.currentIndex() + 1
		self.extrinsic_num = file_id

	def distort(self):
		print(self.dist)

	def intrinsic(self):
		print(self.mtx)

	def corner_clicked(self):
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "1.1 Find Corners")
		criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		for i in range(1, 16):
			# load image name
			filename = ("Q1_Image/{}.bmp".format(i))
			# read the file
			img = cv.imread(filename)
			# convert image into black and white
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			# find corners of the chess board and draw points on image
			ret, corners = cv.findChessboardCorners(gray, (8, 11), None)
			if ret == True:
				corners2 = cv.cornerSubPix(gray, corners, (8, 11), (-1, -1), criteria)
				cv.drawChessboardCorners(img, (8, 11), corners2, ret)
			## window of images
			#windowName = ("Display Window {}".format(i))
			windowName = "Display Window"
			cv.namedWindow(windowName, 0)
			cv.resizeWindow(windowName, 500, 500)
			cv.imshow(windowName, img)
			cv.waitKey(500)

		cv.destroyAllWindows()
			
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "Main Window")

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

import sys
import glob
import cv2 as cv
import numpy as np
from mainWindow import Ui_mainWindow
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)
		# connect buttons to functions
		self.ui.BTN_CORNER.clicked.connect(self.corner_clicked)
		self.ui.CLOSE_ALL_WINDOW.clicked.connect(self.close_win)
		self.ui.BTN_INTRINSIC.clicked.connect(self.intrinsic)
		self.ui.BTN_DISTORTION.clicked.connect(self.distort)
		self.ui.ID_IMAGE.currentIndexChanged.connect(self.choosefile)
		self.ui.BTN_EXTRINSIC.clicked.connect(self.extrinsic)
		# initialize the combo box
		self.ui.ID_IMAGE.addItems(['1', '2', '3', '4', '5', '6', \
									'7', '8', '9', '10', '11', '12', \
									'13', '14', '15'])
		# class variables
		self.extrinsic_num = 0
		self.mtx = []
		self.dist = []
		self.tvecs = []
		self.rvecs = []
		# initial calculate
		self.calibrate()

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
			# window of images
			windowName = ("Display Window {}".format(i))
			cv.namedWindow(windowName, 0);
			cv.resizeWindow(windowName, 500, 500);
			cv.imshow(windowName, img)
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "Main Window")

	def close_win(self):
		cv.destroyAllWindows()

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

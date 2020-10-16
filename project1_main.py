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
		self.ui.BTN_CORNER.clicked.connect(self.corner_clicked)
		self.ui.CLOSE_ALL_WINDOW.clicked.connect(self.close_win)
		self.ui.BTN_INTRINSIC.clicked.connect(self.intrinsic)
		self.ui.BTN_DISTORTION.clicked.connect(self.distort)
		self.ui.BTN_FILE.clicked.connect(self.choosefile)
		self.extrinsic_file = ""
	
	def choosefile(self):
		fileDir = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Image", "./Q1_Image/")
		if fileDir == "":
			print("Didn't choose any image file.")
		else:
			self.extrinsic_file = fileDir[0]

	def distort(self):
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "1.4 Find Distortion")
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
		print(dist)
		QtWidgets.QMainWindow.setWindowTitle(self, "Main Window")


	def intrinsic(self):
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "1.2 Find Intrinsic")
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
		print(mtx)
		QtWidgets.QMainWindow.setWindowTitle(self, "Main Window")


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

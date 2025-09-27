try: 
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapIinstance
except:
	from PySide2 import QtCore, QtGui,QtWidgets
	from shiboken2 import wrapIinstance

import maya.OpenMaya as omui

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle('Primitive Creator')

def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapIinstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatoeDialog(parent=ptr)
	ui.show()
import maya.cmds as cmds

def onCreateClicked(primitive):
	
		if primitive == "cone":
			cmds.polyCone()
		elif primitive == "cube":
			cmds.polyCube()
		elif primitive == "sphere":
			cmds.polySphere()
		elif primitive == "torus":
			cmds.polyTorus()

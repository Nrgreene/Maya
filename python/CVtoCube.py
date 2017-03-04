#This script generates Cubes using the position of CVs in a NURB curve
import maya.cmds as nrg 

selCVs = nrg.ls(sl=True, fl=True)

selSize_CV = len(selCVs)

for cvs in range(0, selSize_CV, 1):
    findCV_X = nrg.getAttr(selCVs[cvs] + ".xValue")
    findCV_Y = nrg.getAttr(selCVs[cvs] + ".yValue")
    findCV_Z = nrg.getAttr(selCVs[cvs] + ".zValue")
    nrg.select(cl=True)
    mkJnt = nrg.polyCube()
    nrg.setAttr(mkJnt[0] + ".tx", findCV_X)
    nrg.setAttr(mkJnt[0] + ".ty", findCV_Y)
    nrg.setAttr(mkJnt[0] + ".tz", findCV_Z)

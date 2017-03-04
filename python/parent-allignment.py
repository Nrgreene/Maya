#Object allignment using parent constraints
import maya.cmds as nrg

#prevents the window from being duplicated
if nrg.window("objAligner", ex=True):
    nrg.deleteUI("objAligner", window=True)


nrg.window("objAligner", title="Object Allignment Tool", s=False, wh=(300,100))
nrg.columnLayout(adj=True)
nrg.text(l="select the source, then target")
nrg.button(l="Alignment", w=300, h=100, c="aligner()")
nrg.showWindow("objAligner")

def aligner():
  #Create a parentConstraint without the offset
  prtCns = nrg.parentConstraint()
  #The parentConstraint is then removed
  nrg.delete(prtCns)

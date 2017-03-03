#Object allignment using parent constraints

#Create a parentConstraint without the offset
prtCns = nrg.parentConstraint()
#The parentConstraint is then removed
nrg.delete(prtCns)

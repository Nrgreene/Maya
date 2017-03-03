import maya.cmds as nrg
nrg.polySphere(r=1, sx=40, sy=20, ax=(2, 1, 2), cuv=2, ch=1);

nrg.setAttr ("polySphere1.radius", 10);

nrg.rename("pSphere1","nrgSphere");

import maya.cmds as nrg

storeCmds = ""

#find selection
selPose = nrg.ls(sl=True)

if len(selPose) < 1:
    nrg.warning("have at least 1 selection")
else:
    for all in selPose:
        keyable = nrg.listAttr(all, k=True, r=True, w=True, c=True, u=True)
        print keyable
        #defines current value of channel attributes
        for vals in keyable:
            getVal = nrg.getAttr(all + "." + vals)
            print getVal
            startCode = "setAttr "
            endCode = ";/n"
            saveToShelf = (startCode + (all + "." + vals) + " %f" + endCode) % getVal
            storeCmds += saveToShelf
            print storeCmds
            
    pd_pose = nrg.promptDialog(t="Saved Pose", m="Pose Name?", b="Save")
    
    if pd_pose == "Save":
        
        pd_pose_name = nrg.promptDialog(q=True, text = True)
        
        nrg.internalVar(usd=True)
        nrg.shelfButton(l=pd_pose_name, annotation=pd_pose_name, imageOverlayLabel=pd_pose_name) # ,ill= "insert desired 'image_name.jpg' as shelf button", command=storeCmds, p="DT_PYTHON", sourcetype="mel")
            
         

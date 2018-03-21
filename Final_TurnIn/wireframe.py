

def makeWireframe():
 
    #Create and Name AOV
    wireAOV = cmds.createNode( 'aiAOV' , name= 'Wireframe' )
    cmds.setAttr( wireAOV + '.name' , 'Wireframe' , type='string')
    cmds.setAttr( wireAOV + '.type' , 5 )
    #Basic AOV Connections
    cmds.connectAttr( wireAOV + '.message' , 'defaultArnoldRenderOptions.aovList', nextAvailable=True )
    cmds.connectAttr( 'defaultArnoldDriver.message' , wireAOV + '.outputs[0].driver' )
    cmds.connectAttr( 'defaultArnoldFilter.message' , wireAOV + '.outputs[0].filter' )
    #Create Shader and Connect
    wireShader = cmds.createNode('aiWireframe', name = 'wireframeMtl')
    cmds.setAttr(wireShader + '.edgeType' , 1)
    cmds.connectAttr(wireShader + '.outColor' , wireAOV + '.defaultValue')
    
makeWireframe()
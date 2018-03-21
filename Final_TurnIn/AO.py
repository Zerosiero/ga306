
def makeOcclusion():
 
    #Create and Name AOV
    occlusionAOV = cmds.createNode( 'aiAOV' , name= 'Occlusion' )
    cmds.setAttr( occlusionAOV + '.name' , 'Occlusion' , type='string')
    cmds.setAttr( occlusionAOV + '.type' , 5 )
    #Basic AOV Connections
    cmds.connectAttr( occlusionAOV + '.message' , 'defaultArnoldRenderOptions.aovList', nextAvailable=True )
    cmds.connectAttr( 'defaultArnoldDriver.message' , occlusionAOV + '.outputs[0].driver' )
    cmds.connectAttr( 'defaultArnoldFilter.message' , occlusionAOV + '.outputs[0].filter' )
    #Create Occlusion Shader and Connect
    occShader = cmds.createNode('aiAmbientOcclusion' , name = 'occMtl')
    cmds.setAttr(occShader + '.falloff' , 1)
    cmds.connectAttr(occShader + '.outColor' , occlusionAOV + '.defaultValue')
    
makeOcclusions()
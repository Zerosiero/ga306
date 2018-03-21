import maya.cmds
from mtoa.cmds.arnoldRender import arnoldRender


def rosiesFunction():
    renderCamera = cmds.camera(name="renderCamera")
    cmds.rename(renderCamera[0], "renderCamera")

    DirectionalLight = maya.cmds.directionalLight(rotation=(-30, -10, -15))

    arnoldRender(1, 1, True, True,'renderCamera', ' -layer defaultRenderLayer')
    cmds.setAttr("defaultArnoldDriver.ai_translator", "png", type="string")
    cmds.setAttr("defaultArnoldDriver.pre", "file_name", type="string")
    arnoldRender(1980, 1024, True, True,'renderCamera', ' -layer defaultRenderLayer')
    


rosiesFunction()

#panda3d engine
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
#from panda3d.core import AmbientLight
#from panda3d.core import Vec4


from application import Application

class Panda3DApplication(ShowBase, Application):
    def __init__(self):
        ShowBase.__init__(self)


        #loading scene
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-10, 40, 0)

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.setScale(0.05, 0.05, 0.05)
        self.pandaActor.loop("walk")

        #set light
        """"
        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLight)"""
        
    
    #Methods   
    def app_launch(self):
        ...

    def app_main_menu(self):
        pass

    def app_quit(self):
        ...

    def options(self):
        ...

#temporary main guard
if __name__=="__main__":
    panda3d_instance = Panda3DApplication()
    panda3d_instance.run()
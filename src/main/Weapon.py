class Weapon(object):
    
    def __init__(self, mainReference):
        self.mainRef = mainReference
        self.weaponModel = None
    def shootAnim(self):
        seq=None

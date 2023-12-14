class ToolBox:
    """Boite a outils"""

    def __init__(self):
        """attributs d'instances """
        self.tools = []

    """Methodes d'instances """

    def add_tool(self,tool):
        """Ajouter un outil"""
        self.tools.append(tool)

    def enlever(self,tool):
        """Enlever un outil"""
        index = self.tools.index(tool)
        del self.tools[index]

class Screw:
    """Vis"""

    MAX_TIGHTNESS = 5
    def __init__(self):
        """initialise son degre de serage"""
        self.tightness = 0
    
    def loosen(self):
        """Deserre le vis."""
        if self.tightness>0:
            self.tightness-=1

    def tighten(self):
        """Serre le vis"""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness+=1

    def __str__(self):
        """Retourne une forme lisible de l'objet"""
        return f"Vis avec un serrage de {self.tightness}"

class Hammer:
    """creation de la classe marteau """

    def __init__(self,color="red"):
        """attributs d'instances """
        self.color = color

    def paint(self,color):
        """paint le marteau"""
        self.color = color

    """Methodes d'instances """
    def hammer_in(self,nail):
        """enfoncer un clou"""
        nail.nail_in()

    def remove(self,nail):
        """Enleve un clou"""
        nail.remove()

    def __repr__(self):
        """Representation de l'objet"""
        return f"Marteau de couleur {self.color}"

class Screwdriver:
    """Tournevis"""

    def __init__(self,size=3):
        """Initialise la taille"""
        self.size = size

    """Methodes d'instances """

    def tighten(self,screw):
        """serrer une vis"""
        screw.tighten()
        
    def loosen(self,screw):
        """Desserre une vis"""
        screw.loosen()

    def __repr__(self):
        """Representation de l'objet"""
        return f"Tournevis de taille {self.size}"


clou = Screw()
clou.tighten()
clou.tighten()
clou1 =clou.__str__()
print(clou1)

tool = ToolBox()
boite1 = tool.add_tool(clou.tightness)
print(boite1)
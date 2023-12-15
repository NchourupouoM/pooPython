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

class Nail:
    """Clou"""

    def __init__(self):
        """Initialise son status dans le mur """
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans le mur"""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """enleve le clou dans le mur"""
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """Retoune une forme lisible de l'objet"""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"clou {wall_state}"


# operations sur les outils
"""Essayez d’accomplir les actions suivantes :

1- Instanciez une boîte à outils, un tournevis, et un marteau.
2- Placez le marteau et le tournevis dans la boîte à outils.
3- Instanciez une vis, et serrez-la avec le tournevis. Affichez la vis avant et après avoir été serrée.
4- Instanciez un clou, puis enfoncez-le avec le marteau. Affichez le clou avant et après avoir été enfoncé."""

tournevis1 = Screwdriver(size=4)

vis1 = Screw()
print("avant de visser: ",vis1.__str__())
tournevis1.tighten(vis1)
print("Apres avoir visser: ",vis1.__str__())

marteau1 = Hammer(color="yellow")

clou1 = Nail()
print("Avant de taper: ",clou1.__str__())
marteau1.hammer_in(clou1)
print("Apres avoir taper: ", clou1.__str__())


tool = ToolBox()
tool.add_tool(marteau1)
tool.add_tool(tournevis1)

print(tool.__dict__)
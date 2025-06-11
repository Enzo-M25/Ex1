from .animal import Animal

class Chien(Animal):
    """
    Classe définissant un chien

    nom : nom de l'animal
    """

    def __init__(self, nom):
        super().__init__(nom)


    def parler(self):
        """
        le chien aboie

        Returns:
            le son émis par l'animal.
        """
        return f"{self.nom} aboie : Woof !"

from .animal import Animal

class Oiseau(Animal):
    """
    Classe définissant un oiseau

    nom : nom de l'animal
    """

    def __init__(self, nom):
        super().__init__(nom)

    def parler(self):
        """
        l'oiseau chante

        Returns:
            le son émis par l'animal.
        """
        return f"{self.nom} chante : Cui cui !"

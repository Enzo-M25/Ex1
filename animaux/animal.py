class Animal:
    """
    Classe définissant un animal

    nom : nom de l'animal
    """

    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        """
        fct parler.

        Returns:
            le son émis par l'animal.
        """
        raise NotImplementedError("Chaque animal doit implémenter sa propre méthode 'parler'.")

from animaux.chien import Chien
from animaux.oiseau import Oiseau

def main():
    animaux = [
        Chien("Rex"),
        Oiseau("Tweety")
    ]

    for animal in animaux:
        print(animal.parler())

if __name__ == "__main__":
    main()

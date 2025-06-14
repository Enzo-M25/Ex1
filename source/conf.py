# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Animal coding test'
copyright = '2025, Enzo'
author = 'Enzo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",      # pour importer et documenter vos modules
    "sphinx.ext.autosummary",  # pour générer des pages résumées automatiquement
    "sphinx.ext.napoleon",     # si vous utilisez les styles Google/NumPy
]

# Pour que Sphinx trouve votre code :
import os, sys
sys.path.insert(0, os.path.abspath("../"))


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

add_module_names = False



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 2,      # profondeur d’affichage de la table des matières
    'collapse_navigation': False,
    'titles_only': False,
}
html_static_path = ['_static']

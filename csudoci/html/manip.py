'''

``manip.py``
===========

Bibliothèque de classes et fonctions permettant de manipuler un arbre HTML
généré par ``csudoci.html.parser``.

'''

from csudoci.html.htmltree import Ul, Li, ElementList
from csudoci.html.parser import HTMLTreeParser
from csudoci.html import htmltree
from csudoci.html.htmltree import *
from csudoci.html.template import FileTemplate
from csudoci.html.parser import *
from csudoci.ds.stack import Stack


def get_links(tree):
    links = []
    root = tree
    
    if root.tag == 'a':
        links.append(tree)
    else:
        for c in tree.children:
            links += get_links(c)

    return links


def get_links_as_ul(tree):
    ul_links = Ul()

    for link in get_links(tree):
        link < Li() < ul_links

    return ul_links


def get_links_as_ul2(tree):
    link_ul = Ul() > [
        Li().add_child(link) for link in get_links(tree)
    ]
    return link_ul


def test():
    test_html = '''
    <html>
      <head>...</head>
      <body>
         <ul>
            <li><a href="...">...</a></li>
            <li><a href="...">...</a></li>
            <li><a href="...">...</a></li>
         </ul>

         <p>
            La page du collège du Sud se trouve sur
            <a href="http://www.collegedusud.ch">http://www.collegedusud.ch</a>
         </p>
      </body>
    </html>
    '''

    tree = HTMLTreeParser(test_html).get_tree()

    list_of_links = get_links_as_ul(tree)
    html = list_of_links.html()
    print(html)

    list_of_links2 = get_links_as_ul2(tree)
    html = list_of_links2.html()
    print(html)

if __name__ == '__main__':
    test()

def get_elements(tree, selectors):
    elements = []
    root = tree
    
    if root.tag in selectors:
        elements.append(tree)
    else:
        for c in tree.children:
            elements += get_elements(c, selectors)

    return elements


def table_matieres(tree, level=2):
    table = Div()
    selectors = ['h' + str(i + 1) for i in range(level)]  # je sais pas si je peux faire ça comme ça (God help me (/^^)/ )
    elements = get_elements(tree, selectors) 
    
    for element in elements:
        table > element

    return table

    
def remove_links(tree):

    if tree.tag == 'a':
     
     # enlèver de cet arbre tous les liens, tout en conservant leur texte.
     ... # I give up
     
     
    return tree




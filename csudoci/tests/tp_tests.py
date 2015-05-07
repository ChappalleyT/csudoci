from csudoci.html.parser import html_to_tree
from csudoci.html.manip import get_links_as_ul
from csudoci.html.manip import get_links_as_ul, get_links_as_ul2
from csudoci.html.manip import get_elements
from csudoci.html.manip import table_matieres
from csudoci.html.manip import remove_links

from tp_html import *

with open('test.html','r',encoding='utf8') as fd:
    html = file.read()
    tree = html_to_tree(html)


def test_get_elements():
   # rédiger le test ici
   link_list = get_elements(tree, ['a'])
   header_list = get_elements(tree, ['h1', 'h2'])
   
   print link_list
   print header_list
   

def test_table_matieres():

   # rédiger le test ici
   
    table_matiere = table_matieres(tree , 2)
    
    print table_matiere.html()


def test_remove_links():
   # rédiger le test ici
   
    print(remove_links(tree).html())
    
   




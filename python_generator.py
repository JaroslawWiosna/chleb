#-*- coding: utf-8 -*- 

import json
import codecs

def get_sth_from_json():
    with open('json/data.json') as f:
        data = json.load(f)

def print_recipe_as_table(recipe):
    s = ""
    s += "<div class=\"recipe\">"
    if 'name' in recipe:
        s += "<div class=\"title\">"
        s += recipe['name']
        s += "</div>"

    s += "<div class=\"timestamp\">"
    s += recipe['date']
    s += "</div>"

    s += "<div class=\"ingredients\">"
    s += "<table>"
    s += "<tr>"
    s += "<td>"

    s += "<img src=\"img/water.png\"></img>"
    s += "<br />"
    s += "woda " 
    s += recipe['ingredients']['woda']
    s += "<br />"

    s += "</td>"
    s += "<td>"

    s += "<img src=\"img/sourdough.png\"></img>"
    s += "<br />"
    s += "zakwas " 
    s += recipe['ingredients']['zakwas']
    s += "<br />"

    s += "</td>"
    s += "<td>"

    s += "<img src=\"img/sourdough.png\"></img>"
    s += "<br />"
    s += "zakwas " 
    s += recipe['ingredients']['zakwas']
    s += "<br />"

    s += "</td>"
    s += "<td>"
    if 'maka_zytnia' in recipe['ingredients']:
        s += "<img src=\"img/flour_whole_wheat.png\"></img>"
        s += "<br />"
        s += u'mąka żytnia '
        s += recipe['ingredients']['maka_zytnia']
        s += "<br />"

    s += "</td>"
    s += "<td>"
    s += "<img src=\"img/flour_plain.png\"></img>"
    s += "<br />"
    s += u"mąka pszenna " 
    s += recipe['ingredients']['maka_pszenna']
    s += "<br />"
            
    s += "</tr>"
    s += "</table>"
    s += "</div>"
    s += "</div>"
    return s

def print_recipes():
    with codecs.open('json/data.json', 'r', 'utf-8') as f:
        d = json.load(f)
        s = ""
        for recipe in d['recipes']:
            s += print_recipe(recipe)
        return s

def print_baking(baking):
    s = ""
    s += "<div class=\"baking\">"
    s += baking['date']
    s += "<br />"
    s += baking['tasty']
    s += "<div class=\"logs\">"
    s += "<table>"
    for key, value in sorted(baking['logs'].items(), key=lambda item: item[0]):
        s += "<tr>"
        s += "<td>"
        s += key
        s += "</td>"
        s += "<td>"
        s += value
        s += "</td>"
        s += "</tr>"
            
    s += "</table>"
    s += "</div>"
    s += "</div>"
    return s
    
def print_recipe(recipe):
    s = ""
    s += "<div class=\"recipe\">"
    if 'name' in recipe:
        s += "<div class=\"title\">"
        s += recipe['name']
        s += "</div>"

    s += "<div class=\"timestamp\">"
    s += recipe['date']
    s += "</div>"

    s += "<img src=\"img/water.png\"></img>"
    s += "<br />"
    s += "woda " 
    s += recipe['ingredients']['woda']
    s += "<br />"

    s += "<img src=\"img/sourdough.png\"></img>"
    s += "<br />"
    s += "zakwas " 
    s += recipe['ingredients']['zakwas']
    s += "<br />"

    if 'maka_zytnia' in recipe['ingredients']:
        s += "<img src=\"img/flour_whole_wheat.png\"></img>"
        s += "<br />"
        s += u'mąka żytnia '
        s += recipe['ingredients']['maka_zytnia']
        s += "<br />"

    s += "<img src=\"img/flour_plain.png\"></img>"
    s += "<br />"
    s += u"mąka pszenna " 
    s += recipe['ingredients']['maka_pszenna']
    s += "<br />"

    s += "<br />"
    s += "</div>"
    return s

def print_recipes():
    with codecs.open('json/data.json', 'r', 'utf-8') as f:
        d = json.load(f)
        s = ""
        for recipe in d['recipes']:
            s += print_recipe_as_table(recipe)
        return s

def print_baking(baking):
    s = ""
    s += "<div class=\"baking\">"
    s += baking['date']
    s += "<br />"
    s += baking['tasty']
    s += "<div class=\"logs\">"
    s += "<table>"
    for key, value in sorted(baking['logs'].items(), key=lambda item: item[0]):
        s += "<tr>"
        s += "<td>"
        s += key
        s += "</td>"
        s += "<td>"
        s += value
        s += "</td>"
        s += "</tr>"
            
    s += "</table>"
    s += "</div>"
    s += "</div>"
    return s
    
    
def print_bakings():
    with codecs.open('json/data.json', 'r', 'utf-8') as f:
        d = json.load(f)
        s = ""
        s += "<h1>"
        s += "        Chleb "
        s += "    </h1>"
        for baking in d['bakings']:
            s += print_baking(baking)
        return s

def print_html_head():
    s = ""
    s += "<head lang=\"en\">"
    s += "<meta charset=\"UTF-8\">"
    s += "<title></title>"
    s += "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/quiz.css\" />"
    s += "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/chleb.css\" />"
    s += "</head>"
    return s

def print_html_body():
    s = ""
    s += "<body>"
    s += "<div class=\"header\">"
    s += "<h1>"
    s += "        Chleb "
    s += "    </h1>"
    s += u"    Jak zrobić chleb w domu?"
    s += "</div>"
    s += print_recipes()
    s += print_bakings()

    s += "</body>"
    return s

s = ""
s += "<html>"

s += print_html_head()
s += print_html_body()

s += "</html>"
with codecs.open('index.html', 'w', 'utf-8') as out:
    out.write(s)



Apps level Project Setup:
Step:1 
1. apps create: python manage.py startapp blog/shop/or anything_folder_name
2. main project er settings a jabo -> apps a jabo -> "folder_name add kore dibo",
3. main project er moddhe akta template folder create koro.
4. abar main project er settings a jeye -> templates -> DIR [BASE_DIR / ''templates"]

etho tuku te temaplte folder er sathe main project folder er cone ction hoye geche.

Step-2:
1. template folder er bitore index.html ba j kunu nam a akta html file create kora.
2. akon jabo apps er moddhe : j kunu apps folder
3. apps er bitore views.py er jawa
4. views.py a from django.shortcuts import render kora
5. function create kora oi apps er moddhe ja korte chai sei onujai ak ak kore
6. function gula return hobe render(request,"apps_folder_name/temapltes_folder/apps_folder_html_file_name")
7. Finally main projects er url a jawa, include import kora
8. urlspatterns=[
path('  apps_folder_name/  ', include("apps_folder.urls"))
]

Step-3:
1. apps_folder  a jeye urls.py file create kora
2. from django.urls import path
3. from . import views
4. urlspatterns=[
path(''apps_folder_name', views.functions_name, name="function er normal akta name set kora")

views a joto function create hobe sob function ei jaygya ese path kore dite hobe
]



Project Templates connect with apps: 
mane project er temaplte er html file k apps er bitore templates er html file er moddhe connect:

Step-1: 
1. index.html -> title->{% block title %} My django projects {% endblock%}
2. mainbody-> {%  block content %}  {%  endblock %}

Step-2: 
1. html file a sob bad dibo
2.  {% extends "index.html"%}
3. {% block title %} blogds {% endblock%}
4. {%  block content %} 
p
h1
ja mon chay tha tag
 {%  endblock %}

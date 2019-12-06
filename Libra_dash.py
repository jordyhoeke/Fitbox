import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from scipy.signal import find_peaks

#open csv file in pandas
data = pd.read_csv("outputWindows.csv", delimiter=",")
'''
a/n+1 * x^n+1

a = versnelling
n = 2
x = delta(tijd)
'''

'''
#################################################
#################################################
############# DIT HELE BLOK IS VOOR #############
############# DE Z-VERSNELLING      #############
#################################################
#################################################
'''

afstandz = [0,]
iz = -1
for iz in range(0,len(data)-1):
    #a = x_a_eind - x_a_start
    az = float(data[' z-versnelling'][iz+1])-float(data[' z-versnelling'][iz])
    nz = 2
    deltatz = data['tijd'][iz+1]-data['tijd'][iz]
    xz = float(deltatz)/1000
    #print x

    snelheidz = (az/(nz+1))*(xz**(nz+1))

    #print snelheid

    sz = (snelheidz/xz)*100
    
    afstandz.append(sz)
    iz += 1

#afstand2 array begint bij 0
afstandz2 = [0,]
#nieuwe counter begint bij 0
countz = 0

#voor elke count in het bereik 0 tot de lengte van afstand variabele - 1 doe:
for countz in range(0, len(afstandz)-1):
    #l = afstand i+1 + afstand i
    lz = (float(afstandz[countz+1])+float(afstandz[countz]))/1000000
    #voeg l toe aan afstand2
    afstandz2.append(lz)
    #count + 1
    countz += 1

df = pd.DataFrame(afstandz2,data['tijd'][0:len(data['tijd'])])
    
dfs = df.rolling(4).mean()

times = dfs[0].keys()
afstandz3 = []
for time in times:
    afstandz3.append(dfs[0][time])
# plt.figure(figsize=(17,7))
# #bereik van de y as van -0.4 tot 0.4
# plt.ylim([-0.9, 0.9])
#plot de grafiek met data['Tijd'] van 0 tot de lengte data['tijd'] op de x-as en afstand2 op de y-as

# plt.plot(df, color='blue', alpha=0.2)
# plt.plot(dfs, color='red',alpha=0.8)
pieken = []
piekenz = find_peaks(afstandz2, height=(0.02))
print(piekenz[0])
print( "er zitten", len(piekenz[0]), "pieken in de grafiek")


'''
#################################################
#################################################
############# DIT HELE BLOK IS VOOR #############
############# DE Y-VERSNELLING      #############
#################################################
################ #################################
'''

afstandy = [0,]
iy = -1
for iy in range(0,len(data)-1):
    #a = x_a_eind - x_a_start
    ay = float(data[' y-versnelling'][iy+1])-float(data[' y-versnelling'][iy])
    ny = 2
    deltaty = data['tijd'][iy+1]-data['tijd'][iy]
    xy = float(deltaty)/1000
    #print x

    snelheidy = (ay/(ny+1))*(xy**(ny+1))

    #print snelheid

    sy = (snelheidy/xy)*100
    
    afstandy.append(sy)
    iy += 1

#afstand2 array begint bij 0
afstandy2 = [0,]
#nieuwe counter begint bij 0
county = 0

#voor elke count in het bereik 0 tot de lengte van afstand variabele - 1 doe:
for county in range(0, len(afstandy)-1):
    #l = afstand i+1 + afstand i
    ly = (float(afstandy[county+1])+float(afstandy[county]))/1000000
    #voeg l toe aan afstand2
    afstandy2.append(ly)
    #count + 1
    county += 1

df = pd.DataFrame(afstandy2,data['tijd'][0:len(data['tijd'])])
    
dfs = df.rolling(4).mean()

times = dfs[0].keys()
afstandy3 = []
for time in times:
    afstandy3.append(dfs[0][time])
# plt.figure(figsize=(17,7))
# #bereik van de y as van -0.4 tot 0.4
# plt.ylim([-0.9, 0.9])
#plot de grafiek met data['Tijd'] van 0 tot de lengte data['tijd'] op de x-as en afstand2 op de y-as

# plt.plot(df, color='blue', alpha=0.2)
# plt.plot(dfs, color='red',alpha=0.8)


'''
#################################################
#################################################
############# DIT HELE BLOK IS VOOR #############
############# DE X-VERSNELLING      #############
#################################################
#################################################
'''

afstandx = [0,]
ix = -1
for ix in range(0,len(data)-1):
    #a = x_a_eind - x_a_start
    ax = float(data[' x-versnelling'][ix+1])-float(data[' x-versnelling'][ix])
    nx = 2
    deltatx = data['tijd'][ix+1]-data['tijd'][ix]
    xx = float(deltatx)/1000
    #print x

    snelheidx = (ax/(nx+1))*(xx**(nx+1))

    #print snelheid

    sx = (snelheidx/xx)*100
    
    afstandx.append(sx)
    ix += 1

#afstand2 array begint bij 0
afstandx2 = [0,]
#nieuwe counter begint bij 0
countx = 0

#voor elke count in het bereik 0 tot de lengte van afstand variabele - 1 doe:
for countx in range(0, len(afstandx)-1):
    #l = afstand i+1 + afstand i
    lx = (float(afstandx[countx+1])+float(afstandx[countx]))/1000000
    #voeg l toe aan afstand2
    afstandx2.append(lx)
    #count + 1
    countx += 1

df = pd.DataFrame(afstandx2,data['tijd'][0:len(data['tijd'])])
    
dfs = df.rolling(4).mean()

times = dfs[0].keys()
afstandx3 = []
for time in times:
    afstandx3.append(dfs[0][time])





external_stylesheets = ['https://codepen.io/chriddyp/pen/dZVMbK.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[

    html.Div(className="container", children=[
    html.Img(src="https://www.mytylschooleindhoven.nl/sites/default/files/media/partners/logos/Logo%20Libra%20cmyk.jpg", style={"width": "10%", "height": "10%", "display":"inline","float": "left"}),
    html.H1(children=' Libra dashboard', style={"text-align": "center"})]
    ),
    html.Div(className="one.column", children=[
        html.H2(style={"text-align": "right", "margin-right": "10%"}, children='Aantal herhalingen: 7')
    ]),
    html.Div(style={"margin-top": '5%'},children='''
        Measurements: times * distance
    '''),

  

    dcc.Graph(
        id='z-afstand',
        figure={
            'data': [
                {'x': times, 'y': afstandz2, 'type': 'scatter', 'name': 'Data-Z', 'opacity':'0.2'},
                {'x': times, 'y': afstandz3, 'type': 'scatter', 'name': 'Rolling mean-Z'},
            ],
            'layout': {
                'title': "Z-afstand ten opzichte van Tijd"
            },
            
        }
        
    ),
    dcc.Graph(
    id='x-afstand',
    figure={
        'data': [
            {'x': times, 'y': afstandx2, 'type': 'scatter', 'name': 'Data-Y', 'opacity':'0.2'},
            {'x': times, 'y': afstandx3, 'type': 'scatter', 'name': 'Rolling mean-Y'},
        ],
        'layout': {
                'title': "X-afstand ten opzichte van Tijd"
            },        
    },
    
    ),
        dcc.Graph(
    id='y-afstand',
    figure={
        'data': [
            {'x': times, 'y': afstandy2, 'type': 'scatter', 'name': 'Data-Y', 'opacity':'0.2'},
            {'x': times, 'y': afstandy3, 'type': 'scatter', 'name': 'Rolling mean-Y'},
        ],
        'layout': {
                'title': "Y-afstand ten opzichte van Tijd"
            },        
    },
    
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


import csv
from PIL import Image, ImageDraw, ImageFont
import os

certfont = 'fonts/JBM_bold.ttf'
fontsize = 60
fontsize2 = 29
textcolor = (20, 40, 50)
datafile = 'data/data.csv'
imgfirst = os.getcwd()+'/templates/gold.png'
imgSilver = os.getcwd()+'/templates/silver.png'
imgBronze = os.getcwd()+'/templates/bronze.png'
imgOrganising = os.getcwd()+'/templates/organising.png'
if not os.path.exists("Exports"):
    os.makedirs("Exports")
output = os.getcwd() + '/Exports'

k = 0.6 * fontsize / 2
name_x = 975
name_y = 630 + fontsize
event_x = 710
event_y = 850 + fontsize2

with open(datafile, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    nameindex = header.index('Name')
    eventindex = header.index('Event')
    positionindex = header.index('Position')

def first():
    with open(datafile, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[positionindex] == '1':
                name = row[nameindex]
                event = row[eventindex]
                img = Image.open(imgfirst)
                if 'Event' in header:
                    if not os.path.exists(output+'/'+event):
                        os.makedirs(output+'/'+event)
                outpath = output+'/'+event
                namex = (name_x - (len(name) * k))
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(certfont, fontsize)
                draw.text((namex, name_y), name, fill=textcolor, font=font)
                name=name.replace(' ', '_')
                img.save(outpath+'/'+name+'_'+event+'.png')
                print('Certificate for', name, 'in', event, 'created successfully')

def second():
    with open(datafile, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[positionindex] == '2':
                name = row[nameindex]
                event = row[eventindex]
                img = Image.open(imgSilver)
                if 'Event' in header:
                    if not os.path.exists(output+'/'+event):
                        os.makedirs(output+'/'+event)
                outpath = output+'/'+event
                namex = (name_x - (len(name) * k))
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(certfont, fontsize)
                draw.text((namex, name_y), name, fill=textcolor, font=font)
                name=name.replace(' ', '_')
                img.save(outpath+'/'+name+'_'+event+'.png')
                print('Certificate for', name, 'in', event, 'created successfully')

def third():
    with open(datafile, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[positionindex] == '3':
                name = row[nameindex]
                event = row[eventindex]
                img = Image.open(imgBronze)
                if 'Event' in header:
                    if not os.path.exists(output+'/'+event):
                        os.makedirs(output+'/'+event)
                outpath = output+'/'+event
                namex = (name_x - (len(name) * k))
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(certfont, fontsize)
                draw.text((namex, name_y), name, fill=textcolor, font=font)
                name=name.replace(' ', '_')
                img.save(outpath+'/'+name+'_'+event+'.png')
                print('Certificate for', name, 'in', event, 'created successfully')

def organising():
    with open(datafile, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[positionindex] == '4':
                name = row[nameindex]
                event = row[eventindex]
                img = Image.open(imgOrganising)
                if not os.path.exists(output+'/Organising'):
                    os.makedirs(output+'/Organising')
                outpath = output+'/Organising'
                namex = (name_x - (len(name) * k))
                eventx = (event_x - (len(event) * k))
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(certfont, fontsize)
                font2 = ImageFont.truetype(certfont, fontsize2)
                draw.text((namex, name_y), name, fill=textcolor, font=font)
                draw.text((eventx, event_y), event, fill=textcolor, font=font2)
                name=name.replace(' ', '_')
                img.save(outpath+'/'+name+'_'+event+'.png')
                print('Certificate for', name, 'as', event, 'created successfully')

first()
second()
third()
organising()
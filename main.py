import csv
from PIL import Image, ImageDraw, ImageFont
import os

certfont = 'fonts/JBM_bold.ttf'
fontsize = 60
textcolor = (20, 20, 20)
datafile = 'data/data.csv'
imgfirst = 'templates/gold.jpg'
imgSilver = 'templates/silver.jpg'
imgBronze = 'templates/bronze.jpg'
imgCopper = 'templates/copper.jpg'
imgParticipation = 'templates/participation.jpg'
imgOrganising = 'templates/organising.jpg'
imgExtra = 'templates/extra.jpg'

if not os.path.exists("Exports"):
    os.makedirs("Exports")
output = 'Exports'

x = 1000
y = 670
x2 = 500
y2 = 1460

k = 0.6 * fontsize / 2

with open(datafile, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    if 'School' in header:
        if 'Event' in header:
            placeindex = header.index('Place')
            schoolindex = header.index('School')
            eventindex = header.index('Event')

        else:
            placeindex = header.index('Place')
            schoolindex = header.index('School')

    else:
        if 'Event' in header:
            placeindex = header.index('Place')
            eventindex = header.index('Event')
            
        else: 
            placeindex = header.index('Place')

    data = [row for row in reader]


def participation():
    for row in data:
        name = row[0]
        if row[placeindex] =='6':
            pass
        if 'School' in header:
            if not os.path.exists(output + row[schoolindex]):
                os.makedirs(output + row[schoolindex])
                if not os.path.exists(output + row[schoolindex] + '/Participation'):
                    os.makedirs(output + row[schoolindex] + '/Participation')
            outpath = output + row[schoolindex] + '/Participation'
        else:
            if not os.path.exists(output + '/Participation'):
                os.makedirs(output + '/Participation')
            outpath = output + '/Participation'
        x1 = (x- len(name)*k)
        y1 = y
        img = Image.open(imgParticipation)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(certfont, fontsize) 
        draw.text((x1, y1), name, textcolor, font=font)
        img.save('{}/{}.jpg'.format(outpath, name))

def organising():
    if not os.path.exists(output + '/Organising'):
        os.makedirs(output + '/Organising')
    outpath = output + '/Organising'
    for row in data:
        if row[placeindex] == '6':
            name = row[0]
            x1 = (x- len(name)*k)
            y1 = y
            img = Image.open(imgParticipation)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(certfont, fontsize) 
            draw.text((x1, y1), name, textcolor, font=font)
            img.save('{}/{}.jpg'.format(outpath, name))

def first():
    for row in data:
        if row[placeindex] == '1':
            name = row[0]
            if 'School' in header:
                if not os.path.exists(output + row[schoolindex]):
                    os.makedirs(output + row[schoolindex])
                    if not os.path.exists(output + row[schoolindex] + '/first'):
                        os.makedirs(output + row[schoolindex] + '/first')
                outpath = output + row[schoolindex] + '/first'
            else:
                if not os.path.exists(output + '/first'):
                    os.makedirs(output + '/first')
                outpath = output + '/first'
            x1 = (x- len(name)*k)
            y1 = y
            img = Image.open(imgfirst)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(certfont, fontsize) 
            draw.text((x1, y1), name, textcolor, font=font)
            img.save('{}/{}.jpg'.format(outpath, name))

def second():
    for row in data:
        if row[placeindex] == '2':
            name = row[0]
            if 'School' in header:
                if not os.path.exists(output + row[schoolindex]):
                    os.makedirs(output + row[schoolindex])
                    if not os.path.exists(output + row[schoolindex] + '/second'):
                        os.makedirs(output + row[schoolindex] + '/second')
                outpath = output + row[schoolindex] + '/second'
            else:
                if not os.path.exists(output + '/second'):
                    os.makedirs(output + '/second')
                outpath = output + '/second'
            x1 = (x- len(name)*k)
            y1 = y
            img = Image.open(imgSilver)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(certfont, fontsize) 
            draw.text((x1, y1), name, textcolor, font=font)
            img.save('{}/{}.jpg'.format(outpath, name))

def third():
    for row in data:
        if row[placeindex] == '3':
            name = row[0]
            if 'School' in header:
                if not os.path.exists(output + row[schoolindex]):
                    os.makedirs(output + row[schoolindex])
                    if not os.path.exists(output + row[schoolindex] + '/third'):
                        os.makedirs(output + row[schoolindex] + '/third')
                outpath = output + row[schoolindex] + '/third'
            else:
                if not os.path.exists(output + '/third'):
                    os.makedirs(output + '/third')
                outpath = output + '/third'
            x1 = (x- len(name)*k)
            y1 = y
            img = Image.open(imgBronze)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(certfont, fontsize) 
            draw.text((x1, y1), name, textcolor, font=font)
            img.save('{}/{}.jpg'.format(outpath, name))

def fourth():
    for row in data:
        if row[placeindex] == '4':
            name = row[0]
            if 'School' in header:
                if not os.path.exists(output + row[schoolindex]):
                    os.makedirs(output + row[schoolindex])
                    if not os.path.exists(output + row[schoolindex] + '/fourth'):
                        os.makedirs(output + row[schoolindex] + '/fourth')
                outpath = output + row[schoolindex] + '/fourth'
            else:
                if not os.path.exists(output + '/fourth'):
                    os.makedirs(output + '/fourth')
                outpath = output + '/fourth'
            x1 = (x- len(name)*k)
            y1 = y
            img = Image.open(imgBronze)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(certfont, fontsize) 
            draw.text((x1, y1), name, textcolor, font=font)
            img.save('{}/{}.jpg'.format(outpath, name))

def extra():
    for row in data:
        if row[placeindex] == '5':
            name = row[0]
            if 'School' in header:
                if not os.path.exists(output + row[schoolindex]):
                    os.makedirs(output + row[schoolindex])
                    if not os.path.exists(output + row[schoolindex] + '/extra'):
                        os.makedirs(output + row[schoolindex] + '/extra')
                outpath = output + row[schoolindex] + '/extra'
            else:
                if not os.path.exists(output + '/extra'):
                    os.makedirs(output + '/extra')
                outpath = output + '/extra'
            x1 = (x- len(name)*k)
            y1 = y
            img = Image.open(imgBronze)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(certfont, fontsize) 
            draw.text((x1, y1), name, textcolor, font=font)
            img.save('{}/{}.jpg'.format(outpath, name))

participation()
first()
second()
third()
fourth()
extra()
organising()
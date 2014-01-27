
from PIL import Image

def open_and_edit(file,*levels):   
    try:
        original = Image.open(file)
    except:
        print "Unable to load image"
    
    for level in levels:
        edited = original.copy()
        for i in range(original.size[0]):
            for j in range(original.size[1]):
                [r,g,b] =  map(lambda k : ((k / level) * level),edited.getpixel( (i,j) ))
                edited.putpixel((i,j),(r,g,b))
        out_name = "outfile_{x}.jpg".format(x = level)
        edited.save(out_name)        

if __name__ == "__main__":    
    open_and_edit("vmworld.jpg",32,128)

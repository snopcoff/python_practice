import tkinter

# Initialize Window
window = tkinter.Tk()

# Window setting
window.title( "Lili's question" )
window.minsize( 640, 480 )

# Background setting
canvas = tkinter.Canvas( bg = "pink", width = 640, height = 480 )
canvas.place( x = 0, y = 0 )

img = tkinter.PhotoImage( file = "./img3/chap3-back.png" )
canvas.create_image( img.width()/2, img.height()/2, image = img )

# Main loop
window.mainloop()

import tkinter

# Initialize Window
window = tkinter.Tk()

# Window setting
window.title( "Lili's question" )
window.minsize( 640, 480 )
window.option_add( "*font", [ "Comic Sans MS", 19 ] )

# Background setting
canvas = tkinter.Canvas( bg = "pink", width = 640, height = 480 )
canvas.place( x = 0, y = 0 )

img = tkinter.PhotoImage( file = "./img3/chap3-back.png" )
canvas.create_image( img.width() / 2, img.height() / 2, image = img )

# Window elements
question = tkinter.Label( text = "How many minutes you want to ask about?",
                          bg = "white" )
question.place( x = 100, y = 40 )

entry = tkinter.Entry( width = 15, bd = 4 )
entry.place( x = 50, y = 130 )

button = tkinter.Button( text = "Ask", bg = "pink" )
button.config( font = [ "Comic Sans MS", 13 ] )
button.place( x = 290, y = 130 )

answer = tkinter.Label( text = "...........................", bg = "white" )
answer.place( x = 130, y = 230 )

# Main loop
window.mainloop()

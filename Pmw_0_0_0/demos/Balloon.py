title = 'Pmw.Balloon demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):
	# Create the Balloon.
	self.balloon = Pmw.Balloon(parent)

	# Create some widgets and megawidgets with balloon help.
	frame = Tkinter.Frame(parent)
	frame.pack(padx = 10, pady = 5)
	field = Pmw.EntryField(frame,
		labelpos = 'nw',
		label_text = 'Command:')
	field.setentry('mycommand -name foo')
	field.pack(side = 'left', padx = 10)
	self.balloon.bind(field, 'Command to\nstart/stop',
		'Enter the shell command to control')

	start = Tkinter.Button(frame, text='Start')
	start.pack(side='left', padx = 10)
	self.balloon.bind(start, 'Start the command')

	stop = Tkinter.Button(frame, text='Stop')
	stop.pack(side='left', padx = 10)
	self.balloon.bind(stop, 'Stop the command')

	scrolledCanvas = Pmw.ScrolledCanvas(parent,
		canvas_width = 200,
		canvas_height = 115,
	)
	scrolledCanvas.pack()
        canvas = scrolledCanvas.component('canvas')

	# Create some canvas items and individual help.
	item = canvas.create_arc(5, 5, 35, 35, fill = 'red', extent = 315)
	self.balloon.tagbind(canvas, item, 'This is help for\nan arc item')
	item = canvas.create_bitmap(20, 150, bitmap = 'question')
	self.balloon.tagbind(canvas, item, 'This is help for\na bitmap')
	item = canvas.create_line(50, 60, 70, 80, 85, 20, width = 5)
	self.balloon.tagbind(canvas, item, 'This is help for\na line item')
	item = canvas.create_text(80, 90, text = 'Canvas items with balloons')
	self.balloon.tagbind(canvas, item, 'This is help for\na text item')

	# Create two canvas items which have the same tag and which use
	# the same help.
	item = canvas.create_rectangle(100, 10, 170, 50, fill = 'aliceblue',
		tags = 'TAG1')
	item = canvas.create_oval(110, 30, 160, 80, fill = 'blue',
		tags = 'TAG1')
	self.balloon.tagbind(canvas, 'TAG1',
		'This is help for the two blue items' + '\n' * 10 +
                    'It is very, very big.',
                'This is help for the two blue items')
	scrolledCanvas.resizescrollregion()

	scrolledText = Pmw.ScrolledText(parent,
		text_width = 32,
		text_height = 4,
                text_wrap = 'none',
        )
	scrolledText.pack(pady = 5)
        text = scrolledText.component('text')

	text.insert('end',
		'This is a text widget with ', '',
		' balloon', 'TAG1',
		'\nhelp. Find the ', '',
		' text ', 'TAG1',
		' tagged with', '',
		' help.', 'TAG2',
		'\n\nAnother line.\nAnd another', '',
	)
	text.tag_configure('TAG1', borderwidth = 2, relief = 'raised')

	self.balloon.tagbind(text, 'TAG1',
		'There is one secret\nballoon help.\nCan you find it?')
	self.balloon.tagbind(text, 'TAG2',
		'Well done!\nYou found it!')

	frame = Tkinter.Frame(parent)
	frame.pack(padx = 10)
	self.toggleBalloonVar = Tkinter.IntVar()
	self.toggleBalloonVar.set(1)
	toggle = Tkinter.Checkbutton(frame,
		variable = self.toggleBalloonVar,
		text = 'Balloon help', command = self.toggle)
	toggle.pack(side = 'left', padx = 10)
	self.balloon.bind(toggle, 'Toggle balloon help\non and off')

	self.toggleStatusVar = Tkinter.IntVar()
	self.toggleStatusVar.set(1)
	toggle = Tkinter.Checkbutton(frame,
		variable = self.toggleStatusVar,
		text = 'Status help', command = self.toggle)
	toggle.pack(side = 'left', padx = 10)
	self.balloon.bind(toggle,
                'Toggle status help on and off, on and off' + '\n' * 10 +
                    'It is very, very big, too.',
                'Toggle status help on and off')

	# Create and pack the MessageBar.
	messageBar = Pmw.MessageBar(parent,
		entry_width = 40,
		entry_relief='groove',
		labelpos = 'w',
	        label_text = 'Status:')
	messageBar.pack(fill = 'x', expand = 1, padx = 10, pady = 5)

	# Configure the balloon to display its status messages in the
	# message bar.
	self.balloon.configure(statuscommand = messageBar.helpmessage)

    def toggle(self):
	if self.toggleBalloonVar.get():
	    if self.toggleStatusVar.get():
		self.balloon.configure(state = 'both')
	    else:
		self.balloon.configure(state = 'balloon')
	else:
	    if self.toggleStatusVar.get():
		self.balloon.configure(state = 'status')
	    else:
		self.balloon.configure(state = 'none')

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root, fontScheme = 'pmw1')
    root.title(title)

    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()

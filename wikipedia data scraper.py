from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

app = Tk()
app.title("Wikipedia Data Scraper")
app.geometry("800x700")

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'green'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

label = Label(app,
			  text = "WIKISCRAPA",
			  foreground= 'black', font=('Perpetua', 15))

# label.grid(row = 0, column=0)
label.pack()

search_text = StringVar()
text = Entry(app, textvariable=search_text, font= 'Kalinga')
# text.grid(row=0, column= 2)
text.focus_set()
text.pack()

button = ttk.Button(app, text = 'Search Wiki', width = 12, style = "C.TButton", command= lambda:search_wiki(search_text.get()))
button.pack(side = TOP)
# button.grid(row=1, column=2)

text_area = Text(app, height = 30, width= 70, border= 10, font= ('Euphemia', 10))

# text_area.grid(row = 2, column=2)


scrollbar = Scrollbar(app)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.pack(side=TOP, fill=Y)
text_area.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command = text_area.yview)


def search_wiki(search_text):
	text_area.delete("1.0","end")

	url = f"https://en.wikipedia.org/wiki/{search_text}"

	req = requests.get(url)

	html_content = req.content

	text = BeautifulSoup(html_content, 'html.parser')
	text_area.delete("1.0","end")
	for x in text.find_all('p'):
		text_area.insert( END, x.get_text())

if __name__ == "__main__":
	app.mainloop()
import re
import tkinter as tk
import urllib
from idlelib.grep import grep
from idlelib.multicall import r
from lxml import html
from tkinter import ttk
from tkinter import messagebox

import requests
import bs4

from thonny import get_workbench

class LahendusView(ttk.Frame):
    #https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    def __init__(self,master):
        super().__init__(master)
        #tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(CoursesView)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#toDO: loginview
#toDo: logout?

class CoursesView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #resp = requests.get("https://lahendus.ut.ee/courses")
        #content = resp.text

        #veryugly
        txt = ttk.Label(self, text = "Sinu ained:")
        txt.grid(row=0, column=0, padx=0, pady=5)

        # currently own writing
        courses_list = [["Programmeerimine", "https://lahendus.ut.ee/courses/7/exercises"],
                        ["Tarkvaraarendus", "https://lahendus.ut.ee/courses/8/exercises"]]

        btns = {}
        r = 2
        for i in courses_list:
            btns[i[0]] = ttk.Button(self, text=i[0], width=30 , command=lambda :
                master.switch_frame(ExeciseView))
            btns[i[0]].grid(row=r, column=0, padx=50, pady=5)
            r+=1

        #ex_txt = tk.Text(self, height=10, width=30, wrap="word")
        #ex_txt.grid(row=1, column=0, padx=10, pady=10)
        #ex_txt.insert(tk.END,list)

        #btn = ttk.Button(self, text="Esita", command=self.on_click)
        #btn.grid(row=2, column=0, padx=50, pady=10)

    #def courses(self):
        # takes courses from html and adds them to list, courses will be
        # clickable buttons,saves both title and href(redirect)
        #https://docs.python-guide.org/scenarios/scrape/
        #page = requests.get("https://lahendus.ut.ee/courses")
        #content = html.fromstring(page.content)
        #list = content.xpath('//a[@class="collection-item course-item"]/text()')


    #def on_click(self,master):
     #   master.switch_frame(ExeciseView).pack()
       # messagebox.showinfo("Info", "Juhuu!!!")

        
def load_plugin():    
    get_workbench().add_view(LahendusView, "Lahendus", "ne")



class ExeciseView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        btn = ttk.Button(self, text="Tagasi", width=10, command=lambda:
        master.switch_frame(CoursesView))
        btn.grid(row=0, column=0, padx=10, pady=5)

        #page = requests.get("https://lahendus.ut.ee/courses/7/exercises")
        #content = html.fromstring(page.content)
        #list = content.xpath('//div[@class="exercise-item"]/text()')
        #get href from CoursesView to parse all Exercises from HTML

        #list should be similar to courses_list
        exercises_list= ["Exercise 1", "Exercise 2", "Exercise 3"]
        #exercises_list should have it's href as well, optionmenu taking
        # the first variable
        drop_down = ttk.Combobox(self, values = exercises_list, state = 'readonly')
        #drop_down.grid(row=1, column=0)
        drop_down.set("Sinu ülesanded")
        drop_down.grid(row = 0, column = 1)

#toDo:summary etc. buttons
        #selected exrecise will get information from the correct href
        #summary / what happens with pictures on lahendus site?





        #selected exercise, corresponding href will generate exercise text

        #messagebox.showinfo("Info", list)

#just in case
#soup = bs4.BeautifulSoup(content, 'html.parser')
        #match = soup.findAll("script")
        #re.findall(r'src="(.*)/>', content)
        #if len(match) > 0:
        #   for m in match:
        #      courses.append(str(m))
        # between_script_tags = re.search('<script>(.*)</script>', html)
        #stripped = re.sub('<[^<]+?>','' , content)



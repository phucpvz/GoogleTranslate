#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jul 18, 2021 01:33:34 PM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import google_translate_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    google_translate_gui_support.set_Tk_var()
    top = window (root)
    google_translate_gui_support.init(root, top)
    root.mainloop()

w = None
def create_window(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_window(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    google_translate_gui_support.set_Tk_var()
    top = window (w)
    google_translate_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_window():
    global w
    w.destroy()
    w = None

class window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1536x811+-6+0")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Google D???ch")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.txtSrc = tk.Text(top)
        self.txtSrc.place(relx=0.052, rely=0.185, relheight=0.263
                , relwidth=0.879)
        self.txtSrc.configure(background="white")
        self.txtSrc.configure(font="-family {Segoe UI} -size 15")
        self.txtSrc.configure(foreground="black")
        self.txtSrc.configure(highlightbackground="#d9d9d9")
        self.txtSrc.configure(highlightcolor="black")
        self.txtSrc.configure(insertbackground="black")
        self.txtSrc.configure(selectbackground="blue")
        self.txtSrc.configure(selectforeground="white")
        self.txtSrc.configure(wrap="word")

        self.lbTranslator = tk.Label(top)
        self.lbTranslator.place(relx=0.391, rely=0.037, height=39, width=283)
        self.lbTranslator.configure(activebackground="#f9f9f9")
        self.lbTranslator.configure(activeforeground="black")
        self.lbTranslator.configure(background="#d9d9d9")
        self.lbTranslator.configure(disabledforeground="#a3a3a3")
        self.lbTranslator.configure(font="-family {Transformers Movie} -size 24 -weight bold")
        self.lbTranslator.configure(foreground="#ffffff")
        self.lbTranslator.configure(highlightbackground="#d9d9d9")
        self.lbTranslator.configure(highlightcolor="black")
        self.lbTranslator.configure(text='''Translator''')

        self.txtDest = tk.Text(top)
        self.txtDest.place(relx=0.052, rely=0.53, relheight=0.263
                , relwidth=0.879)
        self.txtDest.configure(background="#c0c0c0")
        self.txtDest.configure(font="-family {Segoe UI} -size 15")
        self.txtDest.configure(foreground="black")
        self.txtDest.configure(highlightbackground="#d9d9d9")
        self.txtDest.configure(highlightcolor="black")
        self.txtDest.configure(insertbackground="black")
        self.txtDest.configure(selectbackground="blue")
        self.txtDest.configure(selectforeground="white")
        self.txtDest.configure(wrap="word")

        self.cbSelectLangSrc = ttk.Combobox(top)
        self.cbSelectLangSrc.place(relx=0.82, rely=0.148, relheight=0.027
                , relwidth=0.11)
        self.cbSelectLangSrc.configure(textvariable=google_translate_gui_support.cbSrc)
        self.cbSelectLangSrc.configure(background="#ffffff")
        self.cbSelectLangSrc.configure(takefocus="")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.742, rely=0.148, height=22, width=106)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Select Language:''')

        self.btListenSrc = tk.Button(top)
        self.btListenSrc.place(relx=0.052, rely=0.136, height=34, width=97)
        self.btListenSrc.configure(activebackground="#ececec")
        self.btListenSrc.configure(activeforeground="#000000")
        self.btListenSrc.configure(background="#000000")
        self.btListenSrc.configure(disabledforeground="#a3a3a3")
        self.btListenSrc.configure(foreground="#ffffff")
        self.btListenSrc.configure(highlightbackground="#d9d9d9")
        self.btListenSrc.configure(highlightcolor="black")
        self.btListenSrc.configure(pady="0")
        self.btListenSrc.configure(text='''Nghe''')

        self.lbCredit = tk.Label(top)
        self.lbCredit.place(relx=0.397, rely=0.863, height=31, width=273)
        self.lbCredit.configure(activebackground="#f9f9f9")
        self.lbCredit.configure(activeforeground="black")
        self.lbCredit.configure(background="#d9d9d9")
        self.lbCredit.configure(disabledforeground="#a3a3a3")
        self.lbCredit.configure(font="-family {Segoe UI} -size 15")
        self.lbCredit.configure(foreground="#ffffff")
        self.lbCredit.configure(highlightbackground="#d9d9d9")
        self.lbCredit.configure(highlightcolor="black")
        self.lbCredit.configure(text='''Created by Phu Phuc''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.742, rely=0.493, height=22, width=106)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#ffffff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Select Language:''')

        self.cbSelectLangDest = ttk.Combobox(top)
        self.cbSelectLangDest.place(relx=0.82, rely=0.493, relheight=0.027
                , relwidth=0.11)
        self.cbSelectLangDest.configure(textvariable=google_translate_gui_support.cbDest)
        self.cbSelectLangDest.configure(takefocus="")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btListenDest = tk.Button(top)
        self.btListenDest.place(relx=0.052, rely=0.481, height=34, width=97)
        self.btListenDest.configure(activebackground="#ececec")
        self.btListenDest.configure(activeforeground="#000000")
        self.btListenDest.configure(background="#000000")
        self.btListenDest.configure(disabledforeground="#a3a3a3")
        self.btListenDest.configure(foreground="#ffffff")
        self.btListenDest.configure(highlightbackground="#d9d9d9")
        self.btListenDest.configure(highlightcolor="black")
        self.btListenDest.configure(pady="0")
        self.btListenDest.configure(text='''Nghe''')

        self.btSpeakSrc = tk.Button(top)
        self.btSpeakSrc.place(relx=0.124, rely=0.136, height=34, width=97)
        self.btSpeakSrc.configure(activebackground="#ececec")
        self.btSpeakSrc.configure(activeforeground="#000000")
        self.btSpeakSrc.configure(background="#000000")
        self.btSpeakSrc.configure(disabledforeground="#a3a3a3")
        self.btSpeakSrc.configure(foreground="#ffffff")
        self.btSpeakSrc.configure(highlightbackground="#d9d9d9")
        self.btSpeakSrc.configure(highlightcolor="black")
        self.btSpeakSrc.configure(pady="0")
        self.btSpeakSrc.configure(text='''N??i''')

        self.btCopySrc = tk.Button(top)
        self.btCopySrc.place(relx=0.28, rely=0.136, height=34, width=97)
        self.btCopySrc.configure(activebackground="#ececec")
        self.btCopySrc.configure(activeforeground="#000000")
        self.btCopySrc.configure(background="#000000")
        self.btCopySrc.configure(disabledforeground="#a3a3a3")
        self.btCopySrc.configure(foreground="#ffffff")
        self.btCopySrc.configure(highlightbackground="#d9d9d9")
        self.btCopySrc.configure(highlightcolor="black")
        self.btCopySrc.configure(pady="0")
        self.btCopySrc.configure(text='''Sao ch??p''')

        self.btPasteSrc = tk.Button(top)
        self.btPasteSrc.place(relx=0.352, rely=0.136, height=34, width=97)
        self.btPasteSrc.configure(activebackground="#ececec")
        self.btPasteSrc.configure(activeforeground="#000000")
        self.btPasteSrc.configure(background="#000000")
        self.btPasteSrc.configure(disabledforeground="#a3a3a3")
        self.btPasteSrc.configure(foreground="#ffffff")
        self.btPasteSrc.configure(highlightbackground="#d9d9d9")
        self.btPasteSrc.configure(highlightcolor="black")
        self.btPasteSrc.configure(pady="0")
        self.btPasteSrc.configure(text='''D??n''')

        self.btLanguageSwap = tk.Button(top)
        self.btLanguageSwap.place(relx=0.625, rely=0.136, height=34, width=157)
        self.btLanguageSwap.configure(activebackground="#ececec")
        self.btLanguageSwap.configure(activeforeground="#000000")
        self.btLanguageSwap.configure(background="#000000")
        self.btLanguageSwap.configure(disabledforeground="#a3a3a3")
        self.btLanguageSwap.configure(foreground="#ffffff")
        self.btLanguageSwap.configure(highlightbackground="#d9d9d9")
        self.btLanguageSwap.configure(highlightcolor="black")
        self.btLanguageSwap.configure(pady="0")
        self.btLanguageSwap.configure(text='''Ho??n ?????i ng??n ng???''')

        self.btCopyDest = tk.Button(top)
        self.btCopyDest.place(relx=0.28, rely=0.481, height=34, width=97)
        self.btCopyDest.configure(activebackground="#ececec")
        self.btCopyDest.configure(activeforeground="#000000")
        self.btCopyDest.configure(background="#000000")
        self.btCopyDest.configure(disabledforeground="#a3a3a3")
        self.btCopyDest.configure(foreground="#ffffff")
        self.btCopyDest.configure(highlightbackground="#d9d9d9")
        self.btCopyDest.configure(highlightcolor="black")
        self.btCopyDest.configure(pady="0")
        self.btCopyDest.configure(text='''Sao ch??p''')

        self.btRemoveSrc = tk.Button(top)
        self.btRemoveSrc.place(relx=0.423, rely=0.136, height=34, width=97)
        self.btRemoveSrc.configure(activebackground="#ececec")
        self.btRemoveSrc.configure(activeforeground="#000000")
        self.btRemoveSrc.configure(background="#000000")
        self.btRemoveSrc.configure(disabledforeground="#a3a3a3")
        self.btRemoveSrc.configure(foreground="#ffffff")
        self.btRemoveSrc.configure(highlightbackground="#d9d9d9")
        self.btRemoveSrc.configure(highlightcolor="black")
        self.btRemoveSrc.configure(pady="0")
        self.btRemoveSrc.configure(text='''X??a''')

        self.btTranslate = tk.Button(top)
        self.btTranslate.place(relx=0.495, rely=0.136, height=34, width=97)
        self.btTranslate.configure(activebackground="#ececec")
        self.btTranslate.configure(activeforeground="#000000")
        self.btTranslate.configure(background="#000000")
        self.btTranslate.configure(disabledforeground="#a3a3a3")
        self.btTranslate.configure(foreground="#ffffff")
        self.btTranslate.configure(highlightbackground="#d9d9d9")
        self.btTranslate.configure(highlightcolor="black")
        self.btTranslate.configure(pady="0")
        self.btTranslate.configure(text='''D???ch''')

if __name__ == '__main__':
    vp_start_gui()






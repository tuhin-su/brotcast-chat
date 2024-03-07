from json import dumps, loads
from tkinter import *
from base64 import b64decode
from modules import TX, lisener


class UI:
    def __init__(self) -> None:
        self.tx = TX.TX()
        self.rx = lisener.RX()
        self.rx.set(ui=self)
        self.t1 = None
        self.appTitle="BChat"
        self.height=600
        self.width=400

        
        self.cLc = 0
        self.label_list = []
        self.last_place = 400
        self.name_login = None

        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.stop_server)
        self.window.title(self.appTitle)
        

        self.Tchaticon = PhotoImage(data=b64decode(
            '''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'''))
        self.me_icon = PhotoImage(data=b64decode(
            '''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'''))
        self.next_icon = PhotoImage(data=b64decode(
            '''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'''))


        self.chatframe = Frame(self.window, height=600, width=400)
        self.login_frame = Frame(self.window, height=600, width=400, )
        self.logincanv = Canvas(self.login_frame, height=600, width=400, background="white")
        self.enter_name = Entry(self.login_frame, font=("Bell MT", 15), width=30, bg="#E6D39E", )
        self.chatcanv = Canvas(self.chatframe, height=600, width=400)
        self.msg_canv = Canvas(self.chatframe, height=450, width=350)
        self.text_enter = Entry(self.chatframe, font=("Amasis MT Pro", 15), bg="#000B0D", fg="white", width=28)

        
    def go_up(self, event):
        if self.label_list[self.cLc - 1].winfo_y() != 400:
            for i in self.label_list:
                x_val, y_val = i.winfo_x(), i.winfo_y()
                i.place(x=x_val, y=(y_val - 50))

    def go_down(self, event):
        if self.label_list[0].winfo_y() < 0:
            for i in self.label_list:
                x_val, y_val = i.winfo_x(), i.winfo_y()
                i.place(x=x_val, y=(y_val + 50))

    def scroll_wil_me(self, event):
        delta = event.delta // 120
        if delta > 0:
            if self.label_list[self.cLc - 1].winfo_y() == 400:
                pass

            else:
                for i in self.label_list:
                    x_val, y_val = i.winfo_x(), i.winfo_y()
                    i.place(x=x_val, y=(y_val - 50))

        elif delta < 0:
            if self.label_list[0].winfo_y() < 0:
                for i in self.label_list:
                    x_val, y_val = i.winfo_x(), i.winfo_y()
                    i.place(x=x_val, y=(y_val + 50))

    def recive_msg(self, data: bytes):
        data=loads(data.decode())
        if type(data)==dict():
            print("it is dict")
        
        current_msg = str(data["msg"])
        sender_id = data["user"]

        if current_msg.isspace() == True and sender_id != self.name_login:
            for i in range(self.cLc):
                x_val, y_val = self.label_list[i].winfo_x(), self.label_list[i].winfo_y()
                self.label_list[i].place(x=x_val, y=(y_val - 50))
                self.last_place = self.label_list[i].winfo_y()

            label = Canvas(self.msg_canv, height=50, width=350)
            label.create_image(5, 5, image=self.me_icon, anchor=NW)
            label.create_text(5, 35, text=sender_id, fill="black", anchor=NW)
            label_msg = Label(label, text=current_msg, font=("arial", 12, "bold"), bg="#FFFFFF", fg="black")
            label_msg.place(x=50, y=10)
            self.label_list.append(label)
            self.label_list[self.cLc].place(x=0, y=self.last_place)
            self.cLc += 1

    def send_msg(self, event):
        current_msg = self.text_enter.get()
        self.text_enter.delete(0, END)

        if current_msg.isspace() == False:
            data = {
                "user": self.name_login,
                "msg": current_msg
            }

            for i in range(self.cLc):
                x_val, y_val = self.label_list[i].winfo_x(), self.label_list[i].winfo_y()
                self.label_list[i].place(x=x_val, y=(y_val - 50))
                self.last_place = self.label_list[i].winfo_y()

            if self.tx.send(msg=dumps(data).encode()):
                label = Canvas(self.msg_canv, height=50, width=350, )
                label.create_image(310, 5, image=self.me_icon, anchor=NW)
                label.create_text(340, 35, text=self.name_login, fill="black", anchor=NE)
                label_msg = Label(label, text=current_msg, font=("arial", 12, "bold"), bg="#FFFFFF", fg="black")
                label_msg.place(x=300 - label_msg.winfo_reqwidth(), y=10)
                self.label_list.append(label)
                self.label_list[self.cLc].place(x=0, y=self.last_place)
                self.cLc += 1

    def login(self, event):
        self.name_login = self.enter_name.get()
        if self.name_login.isalpha():
            self.login_frame.destroy()
            self.chatframe.place(x=0, y=0)

    def create_window(self):
        self.window.minsize(self.width, self.height)
        self.window.maxsize(self.width, self.height)
        self.window.iconphoto(True, self.Tchaticon)

        self.login_frame.pack(side="left", fill="both", expand=TRUE)
        self.logincanv.pack(side="left", fill="both", expand=TRUE)


        next_button = self.logincanv.create_image(165, 440, image=self.next_icon, anchor=NW)
        self.logincanv.tag_bind(next_button, "<Button-1>", self.login)

        self.enter_name.place(x=50, y=360, height=40)
        self.enter_name.bind("<Return>", self.login)

        self.chatcanv.place(x=-1, y=0)

        send_button = self.chatcanv.create_text(345, 545, text="Send", anchor=NW)  # continue here
        self.chatcanv.tag_bind(send_button, "<Button-1>", self.send_msg)

        self.msg_canv.place(x=25, y=80)
        self.msg_canv.bind_all("<MouseWheel>", self.scroll_wil_me)
        self.msg_canv.bind_all("<B1-Motion>", self.scroll_wil_me)

        self.text_enter.place(x=20, y=550, height=40)
        self.text_enter.bind("<Return>", self.send_msg)
        self.window.bind("<Up>", self.go_up)
        self.window.bind("<Down>", self.go_down)
        
    def loop(self):
        self.window.mainloop()
    
    def stop_server(self):
        self.t1.stop()

    def run(self):
        self.t1 = lisener.server_demon(rx=self.rx)
        self.t1.start()
        self.loop()
   



if __name__ == '__main__':
    core = UI()
    core.create_window()
    core.run()

class Facebook:
    def __init__(self):
        self.username= ''
        self.password= ''
        self.loggedin= False
        self.menu()
        
    
    def menu(self):
        user_input = input("""Welcome to the facebook !! How whould you like to proceed? 
                    1. Press 1 to signup
                    2. Press 2 to signin
                    3. Press 3 to write a message
                    4. Press 4 to message a friend
                    5. Press 5 to exit""")
        
        if user_input == "1":
            self.sign_up()
        elif user_input == "2":
            self.sign_in()
        elif user_input == "3":
            self.post_mess()
        elif user_input == "4":
            self.friend()
        elif user_input == "5":
            exit()
            
    
    def sign_up(self):
        email = input("Enter you email here -> ")
        passwd = input("Enter you password here -> ")
        
        self.username = email
        self.password = passwd
        print("You hvae successfully created  you account!!")
        print('\n')
        self.menu()
        
    def sign_in(self):
        if self.username=='' and self.password=='':
            print("Please sign up first using the main menu")
        else:
            uname = input("Enter you email here -> ")
            pwd = input("Enter you password here -> ")
            #now we will match that enterned username and pass is same or not
            if self.username==uname and self.password==pwd:
                print(f"Welcome {uname}")
                self.loggedin=True
            else:
                print("Wrong username or password. Please provide the correct credentials")
        
        print("\n")
        self.menu()
        
    
    def post_mess(self):
        if self.loggedin==True:
            txt = input("Enter your message here to post -> ")
            print(f"following content have been posted {txt}")
        else:
            print("Please sign in from the main menu")
            print('\n')
            self.menu()
    
    def friend(self):
        if self.loggedin==True:
            mess = input("Enter your message here -> ")
            friend_name = input("Ennter you friend name who to send the message -> ")
            print(f"Your message have been send to {friend_name}")
        else:
            print("Please sign in from the main menu")
            print('\n')
            self.menu()
            
            
            
            
user1 = Facebook()
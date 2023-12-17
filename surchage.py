class File:
    """fichier"""
    def __init__(self,name,size):
        self.name = name
        self.size = size

    def display(self):
        """affiche le fichier"""
        print(f"fichier {self.name}")

class Imagefile(File):
    """fichier image"""
    def __init__(self, name, size):
        super().__init__(name, size)

class ImageJPG(Imagefile):
    """Image de type JPG"""
    def __init__(self, name, size):
        super().__init__(name, size)
        
    """surchage la methode display()"""
    def display(self,type):
        super().display()
        print("cette image est de type JPG")

class ImageGIF(Imagefile):
    """Image de type GIF"""

    def __init__(self,name,size):
        super().__init__(name,size)

    """surchage de la methode display()"""
    def display(self):
        super().display()
        print("cette image est de type GIF")

class User:
    """Utilisateur"""

    def __init__(self,username,password):
        """initialise le nom d'utilisateur et le mot de passe"""
        self.username = username
        self.password = password

    def login(self):
        """connecte l'utilisateur"""
        print(f"l'utilisateur {self.username} est connecte.")

    def post(self,thread,content,file=None):
        """Poste un message dans un file de discussion"""
        if file :
            post = Filepost(self,"aujourd'hui",content,file)
        else:
            post = Post(user=self,time_posted="aujourd'hui",content=content)
        thread.add_poste(post)
        return post


    def make_thread(self,title,content):
        """creer un nouveau file de discussion"""
        post = Post(self,"aujourd'hui",content=content)
        return Thread(title=title,time_posted="aujourd'hui",posts=post)
    
    def __str__(self):
        """representation de l'utilisateur"""
        return self.username

class Moderator(User):
    """Utilisateur moderateur"""
    def __init__(self,username,password):
        super().__init__(username,password)

    def edit(self,post,content):
        """Modifie un message"""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]



class Post:
    """Message"""
    
    def __init__(self,user,time_posted,content):
        """initialise l'utilisateur, la date et le contenu"""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """affiche le message"""
        print(f"Message poste par {self.user} le {self.time_posted}")
        print(self.content)

class Filepost(Post):
    """Message comportant un fichier"""
    def __init__(self,user,time_posted,content,file):
        super().__init__(user,time_posted,content)
        self.file = file

    def display(self):
        """affiche le contenu et le message"""
        super().display()
        print("piece jointe")
        self.file.display()


class Thread:
    """Fil de discussion"""

    def __init__(self,title,time_posted,posts):
        """initialise le titre, la date, et le poste"""
        self.title = title
        self.time_posted = time_posted
        self.posts = [posts]
    
    def display(self):
        """affiche le fil de discussion"""
        print("...THREAD...")
        print(f"titre: {self.title},date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("...............")

    def add_poste(self,post):
        """Ajoute un post."""
        self.posts.append(post)

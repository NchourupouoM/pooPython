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
    pass

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

file1 = File(name="image palais royale foumban",size="23'")
user1 = User(username="Mohamed",password="1234")
user2 = User(username="Ibrahim",password="pass")
moderateur1 = Moderator(username="Mohamed",password="123")
post1 = Post(user=user1,time_posted="15/12/2023",content="le cameroun a l'aire de l'ia")
postfile1 = Filepost(user=user2,time_posted="14/12/2023",content="Le cameroun a l'aire de l'ia",file=file1)
fil_dis1 = Thread(title="file de discution 1",time_posted="aujourd'hui",posts=post1)
print(fil_dis1.display())
print(postfile1.display())
print("-------------Modefication--------------")
moderateur1.edit(post=post1,content="Le cameroun dans le tiere monde")
print(postfile1.display())
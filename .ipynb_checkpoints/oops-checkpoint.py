class User:
    def __init__(self,username:str,email:str):
        self.username=username
        self.email=email


class Post:
    def __init__(self,title:str,content:str,user_data:object):
        self.title=title
        self.content=content
        self.user_data=user_data

class Forum:
   
    def __init__(self):
        self.all_user=[]
        self.all_posts=[]

    def create_user(self,username:str,email:str):
        user=User(username,email)
        self.all_user.append(user)
        return user
    
    def crate_post(self,title:str,content:str,user_data:object):
        post=Post(title,content,user_data)
        self.all_posts.append(post)
        return post
    
    
    def find_user_by_name(self,username):
        for user in self.all_user:
            if(user.username==username):
                return user
            
    def find_all_post_of_username(self,username):
        collect_post=[]
        for post in self.all_posts:
            if(post.user_data.username==username):
                collect_post.append(post)
        return collect_post

            
forum=Forum()

user=forum.create_user("jack","jack@gmail.com")

post=forum.crate_post("new_life","starting new phase",user)
post=forum.crate_post("second_phase","starting new job",user)
post=forum.crate_post("third","starting new jon",user)

get_value=forum.find_user_by_name("jack")
if get_value:
    print(get_value.username)
    print(get_value.email)
else:
    print("did not get user")


get_all_post=forum.find_all_post_of_username("jack")
for post in get_all_post:
    print(post.content)




print(setattr(user,"username","rohan"))
print(getattr(user,"username"))

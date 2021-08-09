

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

        
def is_authenticated_decorator(function):
    def wrapper_function(**kwargs):
        if kwargs["user"].is_logged_in == True:
            function(kwargs["user"])
            print(function.__name__)
    return wrapper_function


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

@is_authenticated_decorator
def make_an_official_tweet(user):
    print(f"This is a tweet made by {user.name}")


new_user = User("angela")
create_blog_post(user=new_user)
make_an_official_tweet(user=new_user)

#Doing without decorator

# wrapper_function = is_authenticated_decorator(create_blog_post)
# wrapper_function(new_user)



from populate import base
from account.models import User

def populate():
    print('Creating user accounts ... ', end='')
    User.objects.exclude(is_superuser=True).delete()
    for i in range(10):
        username = 'user' + str(i)
        user = User.objects.create_user(username=username, password=username,
                                        first_name=username, email='isccyut2@gmail.com')
        if i < 3:
            user.is_staff = True
            user.save()
    
    print('done')
    
    

if __name__ == '__main__':
    populate()
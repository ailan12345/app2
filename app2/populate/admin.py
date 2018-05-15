from populate import base
from account.models import User





def populate():
    print('Creating admin account ... ', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='admin2', password='admin2', email='isccyut2@gmail.com')
    print('done')
    
    

if __name__ == '__main__':
    populate()
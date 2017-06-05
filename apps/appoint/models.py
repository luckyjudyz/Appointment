from __future__ import unicode_literals

from django.db import models
import datetime
import bcrypt, re
EMAILREG = re.compile(r'[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.-_+]+\.[a-zA-Z]*$')

# Create your models here.

class UserDBManager(models.Manager):
    def hash_pass(self, password):
        return bcrypt.hashpw(password,bcrypt.gensalt())

    def check_create(self, data):
        errors = []
        if len(data['username']) < 2:
            errors.append(['username', "Username must be at least 2 characters in length"])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid email address"])
        if len(data['password']) < 8:
            errors.append(['password',"Password must be at least eight characters"])
        if not data['password'] == data['confirmpass']:
            errors.append(['confirmpass', 'Passwords do not match'])
        if not data['dob']:
            errors.append(['dob','Date of birth is empty'])
        if errors:
            return [False, errors]
        else:
            current_user = UserDB.objects.filter(email=data['email'])
            for user in current_user:
                print user
            if current_user:
                errors.append(['current_user',"User already exist, please use alternative information"])
                return [False, errors]
            print data['dob']
            print data['dob']
            print data['dob']
            print data['dob']
            print data['dob']
            newUser = UserDB(username=data['username'], email=data['email'],dob=data['dob'],hashpw=self.hash_pass(data['password'].encode()))
            newUser.save()
            return [True, newUser]
    def check_log(self, data):
        errors = []
        current_user = UserDB.objects.filter(email=data['email'])
        print "yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes111111"
        print current_user
        print "yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyesyes222222"
        if not current_user:
            errors.append(['account',"Email or password incorrect"])
        elif not bcrypt.checkpw(data['password'].encode(),current_user[0].hashpw.encode()):
            errors.append(['account', "Email or password incorrect"])
        if errors:
            return [False, errors]
        else:
            return [True, current_user[0]]

class AppointDBManager(models.Manager):
    def create(self, data, userid):
        errors = []
        print data['date']
        print data['date']
        print data['date']
        print data['date']
        print datetime.date.today()
        print datetime.date.today()
        print datetime.date.today()
        print datetime.date.today()

        if len(data['task']) < 1:
            errors.append(['task', "Task cannot be empty."])
        if data['date'] < str(datetime.date.today()):
            errors.append(['date', "Only allow current and future dates."])
        if errors:
            return [False, errors]
        else:
            user = UserDB.objects.get(id=userid)
            newAppoint = AppointDB(user=user, task = data['task'], date = data['date'], time = data['time'], status = 0)
            newAppoint.save()
        return [True, newAppoint]

    def delete(self, id):
        appoint=AppointDB.objects.get(id=id)
        appoint.delete()
        return True

    def edit(self,data,id,userid):
        delete(id)
        return creat(data,userid)


class UserDB(models.Model):
    username = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=200)
    dob = models.DateField()
    hashpw = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserDBManager()


class AppointDB(models.Model):
    user = models.ForeignKey(UserDB)
    task = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField() # 0 means pending, 1 means done, 2 means missed
    objects = AppointDBManager()

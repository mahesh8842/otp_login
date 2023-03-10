from django.contrib.auth.models import BaseUserManager


class Usermanager(BaseUserManager):
    use_in_migrations =  True

    def create_user(self,username,password=None,**extra_fields):
        # if not phone_num:
        #     raise ValueError('Phone number is required!')
        if not username:
            raise ValueError('username is required!')
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(username,password,**extra_fields)

from django.db import models


# Create your models here.
class WfaMobilUser(models.Model):
    wfauser = models.CharField(max_length=20)
    wfapassword = models.CharField(max_length=20)
    wfakullanici = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name="Kullanıcı")
    wfaMobilUserAktif = models.BooleanField(default=True, verbose_name="silmek için Onayı kaldırın..!!!")

    def __str__(self):
        return self.wfauser

from django.db import models, transaction, connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.timezone import now
import django


settings.configure(
    USE_TZ=True,
    TIME_ZONE='UTC',
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',  
        '__main__',  
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  
        }
    },
)

django.setup()


class MyModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = '__main__'


@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
   
    transaction.on_commit(lambda: print(f"Signal: post_save triggered for {instance.name} at {now()}"))


with connection.schema_editor() as schema_editor:
    schema_editor.create_model(MyModel)


def create_instance_with_transaction():
    try:
        with transaction.atomic():  
            instance = MyModel.objects.create(name="Test Instance")
            print(f"Instance created at {now()} but waiting for commit...")
            raise Exception("Simulate transaction failure")  
    except Exception as e:
        print(f"Transaction rolled back due to: {e}")


create_instance_with_transaction()


if MyModel.objects.exists():
    print("Instance was committed.")
else:
    print("Instance was rolled back, signal should not be committed.")

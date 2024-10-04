import time
import django.dispatch
from django.utils.timezone import now
from django.conf import settings
import django

settings.configure(
    USE_TZ=True,
    TIME_ZONE='UTC',  
)

django.setup()

my_signal = django.dispatch.Signal()

def my_signal_handler(sender, **kwargs):
    print(f"Signal received at {now()}. Processing signal...")
   
    time.sleep(5)
    print(f"Signal processed at {now()}")

my_signal.connect(my_signal_handler)

start_time = now()
print(f"Signal sent at {start_time}")
my_signal.send(sender=None)
end_time = now()
print(f"Signal completed at {end_time}")

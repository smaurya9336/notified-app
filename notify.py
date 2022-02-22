from email import message
from socket import timeout
from matplotlib.pyplot import title
from plyer import notification
title='hello everyone'
message='thankyou for joining this session'

notification.notify (title=title,
            message=message,
            app_icon=None,
            timeout=10,
            toast=False)
from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def notifications(request):
    goto=request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.COMMENT:
            return redirect('view_follow', follow=notification.extra_id)
        elif notification.notification_type == Notification.FOLLOW:
            return redirect('view_comment', comment=notification.extra_id)

    return render(request, 'notifications/notifications.html')
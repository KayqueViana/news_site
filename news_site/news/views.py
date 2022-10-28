from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Notice

from .serializers import NoticeSerializer

def index(request):
    notices = Notice.objects.all()
    serializer = NoticeSerializer(notices, many=True)
    return render(request, "news/homepage.html", {"notices": serializer.data})

def noticeInternal(request, id):
   notice = get_object_or_404(Notice, pk=id)
   serializer = NoticeSerializer(notice)
   return render(request, "news/notice.html", {"notice": serializer.data})

def sendEmail(request):
    subject = 'That’s your subject'
    message = "Texto"
    from_email = settings.EMAIL_HOST_USER
    to = request.POST["email-to"]
    send_mail(subject, message, from_email, [to])
    return redirect("/")
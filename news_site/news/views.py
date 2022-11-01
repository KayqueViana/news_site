from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .models import Notice, Comment
from .forms import NewsletterForm, CommentForm

from .serializers import NoticeSerializer, CommentSerializer

def index(request):
    notices = Notice.objects.all()
    comments = Comment.objects.all()
    noticeSerializer = NoticeSerializer(notices, many=True)
    commentSerializer = CommentSerializer(comments, many=True)
    for notice in  noticeSerializer.data:
        if len(notice["description"]) > 150:
            notice["description"] = notice["description"][0:150] + "..."
    return render(request, "news/homepage.html", {"notices": noticeSerializer.data, "comments": commentSerializer.data})

def noticeInternal(request, id):
   notice = get_object_or_404(Notice, pk=id)
   serializer = NoticeSerializer(notice)
   return render(request, "news/notice.html", {"notice": serializer.data})

def commentPage(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CommentForm()
        return render(request, "news/comment.html", {"form": form})

def sendEmail(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        
        if form.is_valid():
            form.save()
            subject = 'That’s your subject'
            message = "Texto"
            from_email = settings.EMAIL_HOST_USER
            to = request.POST["email"]
            send_mail(subject, message, from_email, [to])
            messages.info(request, "Email enviado com sucesso!!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
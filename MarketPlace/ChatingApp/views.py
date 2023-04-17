from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from ChatingApp.models import Thread, ChatMessage
from Buyer.views import Chat_Thread


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    print(threads)
    
    msg = ChatMessage.objects.all()
    print(msg)
    
    # for i in msg:
    #     print(i.message)
    context = {
        'Threads': threads
    }
    return render(request, 'chat1/chat-index.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messenger/inbox.html', {'users': users})

@login_required
def conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.sender = request.user
            mensaje.receiver = other_user
            mensaje.save()
            return redirect('conversation', user_id=other_user.id)
    else:
        form = MessageForm()

    return render(request, 'messenger/conversation.html', {
        'form': form,
        'messages': messages,
        'other_user': other_user
    })

@login_required
def send_message(request, user_id):
    recipient = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.sender = request.user
            mensaje.receiver = recipient
            mensaje.save()
            return redirect('inbox')
    else:
        form = MessageForm()

    return render(request, 'messenger/send_message.html', {
        'form': form,
        'recipient': recipient
    })

@login_required
def new_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.sender = request.user
            mensaje.receiver = receiver
            mensaje.save()
            return redirect('inbox')
    else:
        form = MessageForm()

    return render(request, 'messenger/new_message.html', {
        'form': form,
        'receiver': receiver
    })

from django.shortcuts import render,redirect
from .models import member
# Create your views here.

def member_list(request):
    members=member.objects.all()
    context={
        'member':members
    }

    return render(request, 'list.html',context)

from .forms import MemberForm

def member_create(request):
    form = MemberForm()

    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1/list')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def member_edit(request,id):
    Member = member.objects.get(id=id)
    form = MemberForm(instance=Member)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=Member)
        if form.is_valid():
            form.save()
            return redirect('app1/list')

    context = {
        'Member': Member,
        'form': form,
    }
    return render(request, 'edit.html', context)

def member_delete(request,id):
    if request.method =="POST":
        pi=member.objects.get(pk=id)
        pi.delete()
        return redirect('app1/list')
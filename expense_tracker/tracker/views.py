from django.shortcuts import render, redirect
from .models import Expense
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'expense_list.html', {
        'expenses': expenses,
        'total': total
    })

@login_required
def add_expense(request):
    if request.method == 'POST':
        Expense.objects.create(
            user=request.user,  
            amount=request.POST['amount'],
            category=request.POST['category'],
            date=request.POST['date'],
            note=request.POST['note']
        )
        return redirect('/')
    return render(request, 'add_expense.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            User.objects.create_user(
                username=username,
                password=password
            )
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('/login/')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'signup.html')

@login_required
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id, user=request.user)
    expense.delete()
    return redirect('/')

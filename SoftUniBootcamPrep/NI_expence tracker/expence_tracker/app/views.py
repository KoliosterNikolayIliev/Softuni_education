from django.shortcuts import render, redirect

from .models import Profile, Expense
from .forms import ProfileCreate, ExpenseCreate, DeleteExpenseForm


def home(request):
    if Profile.objects.exists():

        profile = Profile.objects.all().first()
        expenses = Expense.objects.all()

        profile.budget_left = budget_calc(profile, expenses)

        context = {'expenses': expenses,
                   'profile': profile
                   }

        return render(request, 'home-with-profile.html', context)

    else:
        form = ProfileCreate()
        context = {'form': form, }
        return render(request, 'home-no-profile.html', context)


def create_profile(request):
    form = ProfileCreate(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return redirect('home')


def profile(request):
    profile = Profile.objects.all().first()
    expenses = Expense.objects.all()
    profile.budget_left = budget_calc(profile, expenses)
    context = {'profile': profile, }
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.all().first()
    if request.method == 'GET':
        form = ProfileCreate(instance=profile)
        context = {'form': form, 'profile': profile}
        return render(request, 'profile-edit.html', context)
    else:
        form = ProfileCreate(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {'form': form, 'profile': profile}
        return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.all().first()
    if request.method == 'GET':
        context = {'profile': profile}
        return render(request, 'profile-delete.html', context)
    else:
        profile.delete()
        return redirect('home')


def expense_create(request):
    if request.method == 'GET':
        form = ExpenseCreate()
        context = {'form': form, }
        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {'form': form, }
        return render(request, 'expense-create.html', context)


def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseCreate(instance=expense)
        context = {'form': form, 'expense': expense}
        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseCreate(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {'form': form, 'expense': expense}
        return render(request, 'expense-edit.html', context)


def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteExpenseForm(instance=expense)
        context = {'form': form, 'expense': expense}
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('home')


def budget_calc(profile, expenses):
    expenses_cost = float(sum([x.price for x in expenses]))
    budget_left = float(profile.budget) - expenses_cost
    return budget_left

from django.shortcuts import render


def plans(request):
    """ display users plans"""
    template = 'plans/plans.html'
    context = {}

    return render(request, template, context)
    
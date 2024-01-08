from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RepairRequest
from django.utils import timezone
from datetime import timedelta

@login_required
def create_request(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        RepairRequest.objects.create(title=title, description=description, user=user)
        return redirect('view_requests')

    return render(request, 'create_request.html')

@login_required
def view_requests(request):
    user = request.user
    if user.is_staff:
        requests = RepairRequest.objects.exclude(status='Заявка закрыта')
    else:
        requests = RepairRequest.objects.filter(user=user).exclude(status='Заявка закрыта')
    return render(request, 'view_requests.html', {'repair_requests': requests})

@login_required
def take_request(request, request_id):
    repair_request = get_object_or_404(RepairRequest, id=request_id, status='Ожидание', engineer=None)
    repair_request.engineer = request.user
    repair_request.status = 'В процессе'
    repair_request.save()
    return redirect('view_requests')

@login_required
def view_solution(request, request_id):
    repair_request = get_object_or_404(RepairRequest, id=request_id)
    return render(request, 'view_solution.html', {'repair_request': repair_request})

@login_required
def close_request(request, request_id):
    repair_request = get_object_or_404(RepairRequest, id=request_id)

    if request.method == 'POST':
        solution = request.POST.get('solution')
        repair_request.solution = solution
        repair_request.status = 'Заявка закрыта'
        if not repair_request.engineer:
            repair_request.engineer = request.user
        repair_request.save()
        return redirect('view_requests')

    return render(request, 'close_request.html', {'repair_request': repair_request})

@login_required
def view_closed_requests(request):
    if not request.user.is_staff:
        return redirect('view_requests')

    closed_requests = RepairRequest.objects.filter(status='Заявка закрыта')
    return render(request, 'view_closed_requests.html', {'closed_requests': closed_requests})


@login_required
def closed_requests_report(request):
    if not request.user.is_staff:
        return redirect('view_requests')

    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)

    closed_requests = RepairRequest.objects.filter(
        status='Заявка закрыта',
        updated_at__range=[start_date, end_date],
        engineer=request.user
    )

    return render(request, 'closed_requests_report.html', {'closed_requests': closed_requests})

@login_required
def view_engineer_requests(request):
    if not request.user.is_staff:
        return redirect('view_requests')

    engineer_requests = RepairRequest.objects.filter(
        status='В процессе',
        engineer=request.user
    )

    return render(request, 'view_engineer_requests.html', {'engineer_requests': engineer_requests})


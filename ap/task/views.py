from django.shortcuts import render
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request,'tasks/index.html',{'tasks':tasks})

@csrf_exempt
def update_task(request):
    if request.method == "POST":
        task_id = request.POST.get("id")
        field = request.POST.get("field")
        value = request.POST.get("value")

        try:
            task = Task.objects.get(id=task_id)
            setattr(task, field, value)
            task.save()
            return JsonResponse({"message": "Update successful"})
        except Task.DoesNotExist:
            return JsonResponse({"message": "Task not found"}, status=404)
    return JsonResponse({"message": "Invalid request"}, status=400)
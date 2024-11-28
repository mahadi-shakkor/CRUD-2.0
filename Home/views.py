from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from Home.models import Entry

# Create your views here.

def home(request):
    # Render the home page with any potential messages (msg)
    return render(request, "home.html")

def show(request):
    # Retrieve all data from the Entry model and pass to the 'show.html' template
    data = Entry.objects.all()
    return render(request, "show.html", {'data': data})

def send(request):
    # Handle POST request to store new data
    if request.method == 'POST':
        ID = request.POST.get('id')  # Use .get() for safer access
        data1 = request.POST.get('data1')
        data2 = request.POST.get('data2')

        # Check if the ID already exists to prevent duplicates
        if Entry.objects.filter(ID=ID).exists():
            msg = "This ID already exists. Please use a different ID."
            return render(request, "home.html", {'msg': msg})
        
        # Save new entry to the database
        Entry(ID=ID, data1=data1, data2=data2).save()
        msg = "Data Stored Successfully"
        return render(request, "home.html", {'msg': msg})
    
    # If the request method is not POST, return a 404 error
    raise Http404("Method not allowed")

def delete(request):
    # Handle deletion of an entry by ID
    ID = request.GET.get('id')  # Safely retrieve 'id' from the query string
    if not ID:
        raise Http404("ID not provided.")  # Raise a 404 if ID is missing
    
    # Attempt to find and delete the Entry object by ID
    entry = get_object_or_404(Entry, ID=ID)
    entry.delete()
    
    # Redirect to the show page after deletion
    return HttpResponseRedirect(reverse('show'))

def edit(request):
    # Handle the edit view by retrieving the entry by ID
    ID = request.GET.get('id')  # Safely retrieve 'id' from the query string
    if not ID:
        raise Http404("ID not provided.")  # Raise a 404 if ID is missing
    
    # Get the entry with the provided ID, or set default values
    entry = get_object_or_404(Entry, ID=ID)
    data1 = entry.data1
    data2 = entry.data2
    
    # Render the edit form with the existing data
    return render(request, "edit.html", {'ID': ID, 'data1': data1, 'data2': data2})

def RecordEdited(request):
    # Handle POST request to update an existing entry
    if request.method == 'POST':
        ID = request.POST.get('id')
        data1 = request.POST.get('data1')
        data2 = request.POST.get('data2')

        # Update the entry with the provided ID
        entry = get_object_or_404(Entry, ID=ID)
        entry.data1 = data1
        entry.data2 = data2
        entry.save()  # Save the updated entry
        
        # Redirect to the show page after editing
        return HttpResponseRedirect(reverse('show'))
    
    # If the request method is not POST, return a 404 error
    raise Http404("Method not allowed")

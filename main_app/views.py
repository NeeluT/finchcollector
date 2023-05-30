from django.shortcuts import render

finches = [
  {'name': 'American Goldfish', 'description': 'The state bird of New Jersey', 'age': 3},
  {'name': 'Black Rosy-Finch', 'description': 'Seemingly oblivious to cold and snow', 'age': 2},
  {'name': 'Black-headed Grosbeak', 'description': 'The sweet singer', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
    'finches': finches
  })
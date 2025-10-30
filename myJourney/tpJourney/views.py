from django.shortcuts import render


journeys = [
    {"title": "Learn Django", "description": "Built a web app", "duration": "2 weeks"},
    {"title": "Learn HTML/CSS", "description": "Styled my pages", "duration": "1 week"},
]

def index(request):
    return render(request, 'tpJourney/journey_list.html', {'journeys': journeys})

def about_me(request):
    return render(request, 'tpJourney/about_me.html')
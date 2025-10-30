from django.shortcuts import render
from .models import PassageModel
import random
from django.db.models import Count

# Create your views here.
def passage_view(request):
    rows = PassageModel.objects.all()
    shown_ids = request.session.get('shown_passage_ids',[])
    available_passages = [row for row in rows if row.id not in shown_ids]
    if not available_passages:
        shown_ids = []
        available_passages = rows
    passage = random.choice(available_passages)
    shown_ids.append(passage.id)
    request.session['shown_passage_ids'] = shown_ids
    context = {'passage':passage.passage,}
    # print(context)
    return render(request,'home.html',context)
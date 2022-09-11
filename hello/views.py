from django.utils.timezone import datetime
from django.shortcuts import render,redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView

# My views
def hello_there(request,name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name':name,
            'date':datetime.now()
        }
    )

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def flask(request):
    return render(request,'hello/flask.html')


def fast_api(request):
    return render(request,"hello/fast_api.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("django")
    else:
        return render(request, "hello/log_message.html", {"form": form})




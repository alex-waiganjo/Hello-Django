from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/django.html",
)
urlpatterns = [
    path("", home_list_view, name="home"),
    path("flask",views.flask , name="flask"),
    path("fast_api",views.fast_api , name="fast_api"),
    path('hello/<name>',views.hello_there, name='hello_there'),
    path("log/", views.log_message, name="log"),
  
]



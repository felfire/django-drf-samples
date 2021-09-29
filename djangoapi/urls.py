from django.urls import path, include

urlpatterns = [
    path('v1/', include([
        path('code-samples/', include('app.codesamples.urls')),
    ]))
]

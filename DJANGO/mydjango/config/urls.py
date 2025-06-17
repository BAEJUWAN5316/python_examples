from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # chat/urls에 있는 모든 url패턴에 일방적으로
    # chat/이라는 prefix주소를 부여하겠다 라는 의미
    path('chat/', include('chat.urls'))
]

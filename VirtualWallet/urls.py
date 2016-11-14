"""VirtualWallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include,handler404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wallet/', include('wallet.urls',namespace='wallet')),
    url(r'^', include('wallet.urls')),
     url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'wallet.views.login_user', name='password_reset_complete'),
]
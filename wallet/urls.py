from django.conf.urls import url,handler404
from . import views
from django.conf.urls import patterns, url

app_name = 'wallet'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^register_user$', views.register_user, name='register_user'),
    url(r'^add_user_details/$', views.add_user_details, name='add_user_details'),
    url(r'^recharge$', views.recharge, name='recharge'),
    url(r'^my_wallet$', views.my_wallet, name='my_wallet'),
    url(r'^add_debit$', views.add_debit, name='add_debit'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),
    url(r'^add_balance$', views.add_balance, name='add_balance'),
    url(r'^all_orders$', views.all_orders, name='all_orders'),
    url(r'^transfer_balance$', views.transfer_balance, name='transfer_balance'),
    url(r'^aboutus$', views.aboutus, name='aboutus'),
    url(r'^contactus$', views.contactus, name='contactus'),
    url(r'^termsandconditions$', views.termsandconditions, name='termsandconditions'),
    url(r'^developers$', views.developers, name='developers'),
    url(r'^account_verify$', views.account_verify, name='account_verify'),
    # url(r'^user/password/reset/$',
    #     'django.contrib.auth.views.password_reset',
    #     {'post_reset_redirect' : '/user/password/reset/done/'},
    #     name="password_reset"),
    # url(r'^user/password/reset/done/$',
    #     'django.contrib.auth.views.password_reset_done'),
    # url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    #
    #
    # url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]

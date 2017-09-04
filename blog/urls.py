from django.conf.urls import url, include
from django.contrib import admin
from post.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^hakkimizda/$', hakkimizda, name="hakkimizda"),
    url(r'^tekara/$', tekara, name="tekara"),

    url(r'^kisi_ekle/$', kisi_ekle, name='kisi_ekle'),
    url(r'^kitap_ekle/$', kitap_ekle, name='kitap_ekle'),

    url(r'^hareket_ekle/$', hareket_ekle, name='hareket_ekle'),

    url(r'^liste/$', liste, name="liste"),


    url(r'^(?P<slug>[\w-]+)/kitap_incele/$', kitap_incele, name='kitap_incele'),
    url(r'^(?P<slug>[\w-]+)/kitap_incelefull/$', kitap_incelefull, name='kitap_incelefull'),

    url(r'^(?P<slug>[\w-]+)/kisi_incele/$', kisi_incele, name='kisi_incele'),
    url(r'^(?P<slug>[\w-]+)/kisi_incelefull/$', kisi_incelefull, name='kisi_incelefull'),

    url(r'^(?P<slug>[\w-]+)/hareket_incele/$', hareket_incele, name='hareket_incele'),
    url(r'^(?P<slug>[\w-]+)/hareket_incelefull/$', hareket_incelefull, name='hareket_incelefull'),

    url(r'^(?P<slug>[\w-]+)/kisi_delete/$', kisi_delete, name='kisi_delete'),
    url(r'^(?P<slug>[\w-]+)/kitap_delete/$', kitap_delete, name='kitap_delete'),
    url(r'^(?P<slug>[\w-]+)/hareket_delete/$', hareket_delete, name='hareket_delete'),

    url(r'^(?P<slug>[\w-]+)/kisi_update/$', kisi_update, name="kisi_update"),
    url(r'^(?P<slug>[\w-]+)/kitap_update/$', kitap_update, name="kitap_update"),
    url(r'^(?P<slug>[\w-]+)/hareket_update/$', hareket_update, name="hareket_update"),

    url(r'^post/', include('post.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


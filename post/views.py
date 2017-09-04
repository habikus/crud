from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Kisiler , Kitaplar, Hareketler
from .forms import KisiForm, KitapForm, HareketForm
from django.contrib import messages
from django.db.models import Q
from django.utils.text import slugify


def home(request):
    return render(request, 'home.html', locals())

def hakkimizda(request):
    # return HttpResponse('Selam geldi')
    return render(request, 'hakkimizda.html', locals())

def liste(request):
    kisi_liste = Kisiler.objects.all()
    kitap_liste = Kitaplar.objects.all()
    hareket_liste = Hareketler.objects.all()
    return render(request, 'liste.html', locals())

def kisiler_liste(request):
    kisi_liste = Kitaplar.objects.all()
    return render(request, 'liste.html', locals())

def kitaplar_liste(request):
    kitap_liste = Kitaplar.objects.all()
    return render(request, 'liste.html', locals())

def kisi_incele(request, slug):
    kisi = get_object_or_404(Kisiler, slug=slug)
    return render(request, 'kisi_incele.html', locals())

def kisi_incelefull(request, slug):
    kisi = get_object_or_404(Kisiler, slug=slug)
    return render(request, 'kisi_incelefull.html', locals())

def kitap_incele(request, slug):
    kitap = get_object_or_404(Kitaplar,  slug=slug)
    return render(request, 'kitap_incele.html', locals())

def kitap_incelefull(request, slug):
    kitap = get_object_or_404(Kitaplar,  slug=slug)
    return render(request, 'kitap_incelefull.html', locals())

def hareket_incele(request, slug):
    hareket = get_object_or_404(Hareketler,  slug=slug)
    return render(request, 'hareket_incele.html', locals())

def hareket_incelefull(request, slug):
    hareket = get_object_or_404(Hareketler,  slug=slug)
    return render(request, 'hareket_incelefull.html', locals())

def tekara(request):
    tek = Kisiler.objects.all()
    query = request.GET.get('q')
    if query:
        tek = tek.filter(
            Q(adsoyad__icontains=query) |
            Q(nosu__icontains=query) |
            Q(telefonu__icontains=query)
        ).distinct()
    return render(request, 'tek.html', locals())

def kisi_ekle(request):
    form = KisiForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        kisi = form.save(commit=False)
        kisi.user = request.user
        kisi.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(kisi.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'form_kisi.html', context)

def kitap_ekle(request):
    form = KitapForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        kitap = form.save(commit=False)
        kitap.user = request.user
        kitap.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(kitap.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'form_kitap.html', context)

def hareket_ekle(request):
    form = HareketForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        hareket = form.save(commit=False)
        hareket.user = request.user
        hareket.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(hareket.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'form_hareket.html', context)

def kisi_delete(request, slug):
    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()
    kisi = get_object_or_404(Kisiler, slug=slug)
    kisi.delete()
    return redirect('liste')

def kisi_update(request, slug):
    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()
    kisi = get_object_or_404(Kisiler, slug=slug)
    form = KisiForm(request.POST or None, request.FILES or None, instance=kisi)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(kisi.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, "form_kisi.html", context)

def kitap_delete(request, slug):
    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()
    kitap = get_object_or_404(Kitaplar, slug=slug)
    kitap.delete()
    return redirect('liste')

def kitap_update(request, slug):
    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()
    kitap = get_object_or_404(Kitaplar, slug=slug)
    form = KitapForm(request.POST or None, request.FILES or None, instance=kitap)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(kitap.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, "form_kitap.html", context)

def hareket_delete(request, slug):
    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()
    hareket = get_object_or_404(Hareketler, slug=slug)
    hareket.delete()
    return redirect('liste')

def hareket_update(request, slug):
    if not request.user.is_authenticated():
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()
    hareket = get_object_or_404(Hareketler, slug=slug)
    form = HareketForm(request.POST or None, request.FILES or None, instance=hareket)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(hareket.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, "form_hareket.html", context)


# Daha önce oluşturulan model den bilgi alıp template'e iletir.
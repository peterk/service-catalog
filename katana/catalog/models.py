# -*- coding: utf-8 -*-
from django.db import models


class Organization(models.Model):
    """En organisation som har tjänster i katalogen"""
    name = models.CharField(u"Namn", max_length=255)
    number = models.CharField(u"Organisations-nummer", max_length=11)
    website = models.URLField(u"Länk", verify_exists = False)
    phone = models.CharField(u"Telefon", max_length=255)
    email = models.EmailField(u"E-post", blank=True)
    address = models.CharField(u"Adress", max_length=255, blank=True)
    other = models.TextField(u"Övrig info", blank=True)

    slug = models.SlugField(max_length=255, help_text=u"Kortnamn i länkar",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Organisation" 
        verbose_name_plural = u"Organisationer"
        ordering = ('name',)


class ContactPerson(models.Model):
    """Person i en organisation som agerar kontakt för en eller flera tjänster."""
    name = models.CharField(u"Namn t.ex. 'Karl Karlsson'", max_length=255)
    email = models.EmailField(u"E-post")
    phone = models.CharField(u"Telefon", max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Kontaktperson" 
        verbose_name_plural = u"Kontaktpersoner"
        ordering = ('name',)


class Category(models.Model):
    """Kategori"""
    name = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning", blank=True)

    slug = models.SlugField(max_length=255, help_text=u"Kortnamn i länkar",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Kategori" 
        verbose_name_plural = u"Kategorier"
        ordering = ('name',)



class LifeCycleState(models.Model):
    """Livscykelstatus"""
    name = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning", blank=True)
    slug = models.SlugField(max_length=255, help_text=u"Kortnamn i länkar",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Livscykelstatus" 
        verbose_name_plural = u"Livscykelstatusar"
        ordering = ('name',)


class Protocol(models.Model):
    """Protokoll som tjänsten använder"""
    name = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning", blank=True)
    slug = models.SlugField(max_length=255, help_text=u"Kortnamn i länkar",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Protokoll" 
        verbose_name_plural = u"Protokoll"
        ordering = ('name',)



class Service(models.Model):
    """En tjänst i katalogen"""
    name = models.CharField(u"Namn", max_length=255)
    description = models.TextField(u"Beskrivning")
    terms = models.TextField(u"Villkor för nyttjande", blank=True)
    price = models.TextField(u"Kostnad för användning", blank=True)
    availability = models.TextField(u"Tillgänglighet", blank=True)
    authentication = models.TextField(u"Inloggning och behörighet", blank=True)
    
    version = models.CharField(u"Version", max_length=100)
    URL_info = models.URLField(u"Infosida", verify_exists = False, blank=True)
    URL_service = models.URLField(u"Länk till tjänst", verify_exists = False, blank=True)
    URL_test = models.URLField(u"Länk till testversion", verify_exists = False, blank=True)

    keywords = models.TextField(u"Nyckelord, kommaseparerade", blank=True)
    other = models.TextField(u"Övrig information", blank=True)

    # Relationer
    protocol = models.ForeignKey(Protocol, verbose_name="Protokoll")
    contact_person = models.ForeignKey(ContactPerson, verbose_name=u"Kontaktperson")
    lifecycle_state = models.ForeignKey(LifeCycleState, verbose_name=u"Livscykel-status") #Livscykelstatus
    categories = models.ManyToManyField(Category, related_name='services', verbose_name=u"Kategorier")

    slug = models.SlugField(max_length=255, help_text=u"Kortnamn i länkar",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= u"Tjänst" 
        verbose_name_plural = u"Tjänster"
        ordering = ('name',)


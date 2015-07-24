from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('monitoreo.views',
    # Examples:
    # url(r'^$', 'canicacao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^$', 'IndexView', name='index'),
    url(r'^consulta', 'consulta', name='consulta'),
    url(r'^dashboard', 'dashboard', name='dashboard'),
    url(r'^organizacion', 'get_organizacion', name='organizacion'),
    #indicadores
    url(r'^educacion', 'educacion', name='educacion'),
    url(r'^propiedad', 'propiedad', name='propiedad'),
    #mapa
    url(r'^mapa/$', 'obtener_lista', name='obtener-lista'),
    #filtros
    url(r'^ajax/fechas/$', 'get_fecha', name='get_fecha'),
    url(r'^ajax/organi/$', 'get_organi', name='get-organi'),
    url(r'^ajax/munis/$', 'get_munis', name='get-munis'),
    url(r'^ajax/comunies/$', 'get_comunies', name='get-comunies'),
)

import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

with open('data-398-2018-08-30.csv', mode='r', encoding='utf-8-sig') as f:
    DictReader_object = csv.DictReader(f, fieldnames=(
        "ID", "Name", "Longitude_WGS84", "Latitude_WGS84",
        "Street", "AdmArea", "District", "RouteNumbers",
        "StationName", "Direction", "Pavilion", "OperatingOrgName",
        "EntryState", "global_id", "geoData"))
    list_bus_stations = [dict(item) for item in DictReader_object]

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(list_bus_stations[1:], 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

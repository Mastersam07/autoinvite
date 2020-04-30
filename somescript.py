import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
import sys

from invite.forms import InviteForm


# def get_name(request, username):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = InviteForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             add_to_org(sys.argv[1])
#             # redirect to a new URL:
#             return HttpResponseRedirect('/success')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = InviteForm()
#
#     return render(request, 'index.html', {'form': form})


# def add(request):
#     url = 'https://api.github.com/orgs/gdgikorodu/memberships/geektutor'
#     r = requests.get(url, headers={'Authorization': 'Bearer %s' % 'ed4daa9aa17780a960297976ee8bdbb82f54a390'})
#     main = r.json()
#     if r.status_code == 200 and main['state'] == 'pending':
#         pass
#     if r.status_code == 200 and main['state'] == 'active':
#         pass


# check if user exists
def user_exists(user):
    url = 'https://api.github.com/search/users?q=' + user
    r = requests.get(url)
    main = r.json()
    if main['total_count'] == 0:
        return False
    else:
        return True


# check if organization exists
def get_org_exists(org_name):
    url = 'https://api.github.com/orgs/' + org_name
    r = requests.get(url)
    org = r.json()
    if org['avatar_url']:
        return True
    else:
        return False


# check organization avatar
def get_org_avatar_url(org_name):
    url = 'https://api.github.com/orgs/' + org_name
    r = requests.get(url)
    org = r.json()
    if 'avatar_url' in org:
        return org['avatar_url']
    elif 'message' in org:
        return org['message']


# check organization id
def get_org_id(org_name):
    url = 'https://api.github.com/orgs/' + org_name
    r = requests.get(url)
    org = r.json()
    if 'id' in org:
        return org['id']
    elif 'message' in org:
        return org['message']


# adding user to organization
def add_to_org(username):
    url = 'https://api.github.com/orgs/gdgikorodu/memberships/' + username + '?role=member'
    if user_exists(username):
        r = requests.put(url, headers={'Authorization': 'Bearer %s' % '39fb57190b3650777c30738f57cd7a1f50cba34c'})
        main = r.json()
        if 'state' in main and main['state'] == 'pending':
            return "OK, Check your EMAIL"
        else:
            return main['message']
    else:
        return 'User not found. Please check your spelling'


output = add_to_org(sys.argv[1])
print(output)
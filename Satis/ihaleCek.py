@permission_required('Satis.view_STSihaletakip')
@login_required(login_url="user:login")
def STSihaletakip(request, ihale):
    if request.user.is_superuser != True:
        return HttpResponseForbidden()
    Uygulamas = STSIhaleTakip.objects.filter(IhaleAktif=True)

    url = 'https://www.turksat.com.tr/tr/satin-alma-ilanlari/tr/satin-alma-ilanlari'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    jobs = soup.find("div", attrs={"class": "item-list"}).ul.find_all("li")
    for job in jobs:
        tarih = job.find("span",attrs={"date-display-single"}).next
        ihale = job.find("span", attrs={"field-content"}).text
        
        print(tarih ,ihale,sep="\n")
        print("-"*60)

    birlestir = str(len(jobs))
    print(birlestir)

    return render(request, "STS/STSihaletakip.html", {"Uygulamas":Uygulamas,"jobs":ihale ,"tarih":tarih,"uzunluk": birlestir})


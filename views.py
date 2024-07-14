@login_required(login_url='signin')
def courses_marketing(request):
    page_title = f"Explore our courses"
    user = request.user
    site = SiteInformation.objects.first()
    domain = get_current_site(request).domain
    is_secure = request.is_secure()
    courses = Course.objects.filter(active=True)[0:3]
    context = {'page_title':page_title,'user':user,'site':site,'courses':courses}
    return render(request,'base/email-templates/courses-marketing.html',context)

urls.py


path('courses-marketing/',views.courses_marketing,name='courses-marketing'),
]


git push -f origin ken
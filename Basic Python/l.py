class Signup_web(View):
    form_class = AccountForm
    second_form = SignupForm
    initial = {'key': 'value'}
    template_name = 'web/signup.html'
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id','None')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form,'id':id,'title':'Signup'})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form_second = self.second_form(request.POST)
        email = request.POST.get('email')
        mobile_number = str(int(request.POST.get('mobile_number')))
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        full_name = name +" "+ lname 
        dob = datetime.datetime.strptime(request.POST.get('dob'), "%d-%m-%Y").strftime("%Y-%m-%d")
        password = request.POST.get('password')
        countrycode = request.POST.get('countrycode')
        confirm_password = request.POST.get('confirm_password')
        try:
            user = Account.objects.get(mobile_number=mobile_number)

        except:
            user = ""
        if user:
            if user.is_verified_phone == False:
                user.delete()
        if Account.objects.filter(email= email):
             return JsonResponse({"message":"Email address already registered. Created an account before?","id":"email-error"})
        if Account.objects.filter(mobile_number= mobile_number):
            return JsonResponse({"message":"Phone number already registered. Created an account before?","id":"phone-error"})
        if form.is_valid():
            # <process form cleaned data>
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' :  recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode("utf-8")
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            result = json.load(response)
            if result["success"]:
                form_obj= form.save(commit=False)
                form_obj.set_password(form_obj.password)
                form_obj.mobile_number = str(int(request.POST.get('mobile_number')))
                form_obj.save()
                form_obj.send_otp()
                send_OTP(mobile=form_obj.mobile_number, country_code=form_obj.countrycode,otp_code=form_obj.otp, hash_Key=None)
                user = User.objects.create(name=full_name, first_name=name,last_name=lname,dob = dob ,account = form_obj,join_date = datetime.date.today(),status_date=datetime.date.today())
                user.custom_id = "Ramp"+str(random.randint(1000,9999))+str(user.account.id)
                user.save()
                Account.objects.filter(id=user.account.id).update(is_active=True)
                Application.objects.get_or_create(user=form_obj,client_type=Application.CLIENT_CONFIDENTIAL,authorization_grant_type=Application.GRANT_PASSWORD)
                request.session['mobile_number'] = mobile_number
                request.session['user_id'] = form_obj.id
                return JsonResponse({"message":"success"})
            else:
                return JsonResponse({'message':'Invalid reCAPTCHA. Please try again.',"id":"invalid_captacha"})
        return render(request, self.template_name, {'form': form,'form_second':form_second})
    
class Logout(View):
    def get(self, request):
        if request.session.get('user_id'):
            del request.session['user_id'] 
        if request.session.get('mobile_number'):
            del request.session['mobile_number']
        return redirect('login')

class Check_otp_web(View): 
    initial = {'key': 'value'}
    template_name = 'web/verify_account.html'
    @method_decorator(check_logged_in)
    def get(self, request, *args, **kwargs):
        mobile_number = request.session.get('mobile_number')
        otp_obj = Account.objects.get(mobile_number = mobile_number)
        referer = request.META.get('HTTP_REFERER', '')
        if referer == "":
            return redirect('/login/')
        return render(request, self.template_name,{'account':otp_obj,'title':'Verify'})

    def post(self,request,*args, **kwargs):
        id = request.GET.get('id')
        otp1 = str(request.POST.get('otp1'))
        otp2 = str(request.POST.get('otp2'))
        otp3 = str(request.POST.get('otp3'))
        otp4 = str(request.POST.get('otp4'))
        otp5 = str(request.POST.get('otp5'))
        otp6 = str(request.POST.get('otp6'))
        otp = str(''.join([otp1,otp2,otp3,otp4,otp5,otp6]))
        mobile_number = request.session.get('mobile_number')
        otp_obj = Account.objects.get(mobile_number = mobile_number)
        user_obj = User.objects.get(account=otp_obj)
        username = otp_obj.email
        password = otp_obj.password
        if otp == otp_obj.otp:
            current_time = datetime.datetime.now(datetime.timezone.utc)
            sent_time = otp_obj.otp_created
            difference = current_time-sent_time
            if int(difference.total_seconds()) <= 85:
                otp_obj.is_verified_phone = True
                otp_obj.is_active = True
                otp_obj.save()
                user_f = Account.objects.filter(email="support@ramprewards.com.au")
                if user_f:
                    user_f = Account.objects.get(email="support@ramprewards.com.au")
                    UserFriend.objects.create(from_user=User.objects.get(account=user_f),to_user=user_obj,status=True)
                    message = "Hi, I am Rae, short for RAMP Assistant Epicentre your new friend on RAMP.  So glad to see you here and happy to be of service!"
                    UserMessage.objects.create(from_user=User.objects.get(account=user_f),to_user=user_obj,message=message,is_read= False,date=datetime.date.today())
                    message = "We are here to help you navigate the site, listen to your feedback and answer any questions you might have about RAMP."
                    UserMessage.objects.create(from_user=User.objects.get(account=user_f),to_user=user_obj,message=message,is_read= False,date=datetime.date.today())
                    message = "We really know our stuff, so whatever is on your mind, don't hesitate to ask. Shoot us a message any time, and we can tell you about Engagement Status Points, how to earn more RAMP Cash, or any other RAMP question. Don't worry, I'm not some kind of a bot. We are as true friends always are, here to support you in all things shopping!"
                    UserMessage.objects.create(from_user=User.objects.get(account=user_f),to_user=user_obj,message=message,is_read= False,date=datetime.date.today())
                    message = "Thanks for being friends and welcome to RAMP."
                    UserMessage.objects.create(from_user=User.objects.get(account=user_f),to_user=user_obj,message=message,is_read= False,date=datetime.date.today())					
                if id != None:
                    account = User.objects.get(custom_id = id)
                    user = User.objects.get(account=otp_obj)
                    UserFriend.objects.create(from_user=account,to_user=user,status=True)
                   
                return redirect('/set-pin/')
            else:
                messages.error(request, "Code expired. Please <a href='/resend-otp/' class='expired_otp_link'>request a new one</a>." )      
        else:
            messages.error(request, 'Invalid code entered. Please check and try again.' )
        return render(request, self.template_name,{'account':otp_obj,'title':'Verify'})

class Forget_Password_phone(View):
    def get(self,request, *args, **kwargs):
        return render(request,'web/forget_password_number_enter.html',{'title':'Rewards'})
    def post(self,request,*args, **kwargs):
        mobile_number = str(int(request.POST.get('mobile_number')))
        try:
            user_obj = Account.objects.get(mobile_number=mobile_number)
            request.session['mobile_number'] = mobile_number
            request.session['user_id'] = user_obj.id
            user_obj.send_otp()
            send_OTP(mobile=user_obj.mobile_number, country_code=user_obj.countrycode,otp_code=user_obj.otp, hash_Key=None)
            return redirect('forget-password')
        except:
            messages.error(request, 'Please enter the number currently registered in your account.' )
        return render(request,'web/forget_password_number_enter.html',{'title':'Rewards'})

class Resend_Otp(View):
    @method_decorator(check_logged_in)
    def get(self,request,*args, **kwargs):
        mobile_number = request.session.get('mobile_number')
        user_obj = Account.objects.get(mobile_number=mobile_number)
        user_obj.send_otp()
        send_OTP(mobile=user_obj.mobile_number, country_code=user_obj.countrycode,otp_code=user_obj.otp, hash_Key=None)
        return redirect(request.META['HTTP_REFERER'])
    
class Login_view(View):
    initial = {'key': 'value'}
    template_name = 'web/login.html'
    def get(self, request, *args, **kwargs):
        id= request.GET.get('id',"None")
        return render(request, self.template_name,{'id':id,'title':'Login'})
    def post(self,request,*args, **kwargs):
        link = request.POST.get('link')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not re.search(r'\w+@\w+',username):
            try:
                user_obj = Account.objects.get(mobile_number = str(int(request.POST.get('username'))))
                email = user_obj.email
                if user_obj.is_active == False:
                    user = 0 
                    messages.error(request, 'Your account is currently deactivated. Please contact support.' )
                else:
                    user = authenticate(username = email,password = password)
            except:
                user= ""
                messages.error(request, 'Mobile number not found. Please check and try again.' )
        else:
            try:
                user_obj = Account.objects.get(email = username)
                if user_obj.is_active == False:
                    user = 0 
                    messages.error(request, 'Your account is currently deactivated. Please contact support.' )
                else:
                    user = authenticate(username = user_obj.email,password = password)
            except:
                user= ""
                messages.error(request, 'Email address not found. Please check and try again.' )   
        if user:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' :  recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode("utf-8")
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            result = json.load(response)
            if result["success"]:
                if user.is_active :
                    if link:
                        login(request, user)
                        request.session['user_id'] = user.id
                        request.session['mobile_number'] = user.mobile_number
                        return redirect(link)
                    else:
                        login(request, user)
                        request.session['user_id'] = user.id
                        request.session['mobile_number'] = user.mobile_number
                        return redirect('web_dashboard')
                else:
                    messages.error(request, 'Your account is currently deactivated. Please contact support.' )
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        if user == None:
            messages.error(request, 'Incorrect login or password.' )
        return render(request, self.template_name,{'title':'Login'})

class Check_otp_forget_password(View):
    initial = {'key': 'value'}
    template_name = 'web/forgot_password.html'
    @method_decorator(check_logged_in)
    def get(self, request, *args, **kwargs):
        mobile_number = request.session.get('mobile_number')
        request.session['user_enter'] = "check"
        otp_obj = Account.objects.get(mobile_number = mobile_number)
        return render(request, self.template_name,{'account':otp_obj,'title':'Verify'})
    def post(self,request,*args, **kwargs):
        otp1 = str(request.POST.get('otp1'))
        otp2 = str(request.POST.get('otp2'))
        otp3 = str(request.POST.get('otp3'))
        otp4 = str(request.POST.get('otp4'))
        otp5 = str(request.POST.get('otp5'))
        otp6 = str(request.POST.get('otp6'))
        otp = str(''.join([otp1,otp2,otp3,otp4,otp5,otp6]))
        mobile_number = request.session.get('mobile_number')
        otp_obj = Account.objects.get(mobile_number = mobile_number)
        if otp == otp_obj.otp:
            current_time = datetime.datetime.now(datetime.timezone.utc)
            sent_time = otp_obj.otp_created
            difference = current_time-sent_time
            if int(difference.total_seconds()) <= 85:
                otp_obj.is_verified_phone = True
                otp_obj.save()
                return redirect('password-change')
            else:
                messages.error(request, "Code expired. Please <a href='/resend-otp/' class='expired_otp_link'>request a new one</a>." )
        else:
            messages.error(request, 'Invalid code entered. Please check and try again.' )
        return render(request, self.template_name,{'account':otp_obj,'title':'Verify'})

class Password_change(View):
    template_name = 'web/reset_password.html'
    @method_decorator(check_logged_in)
    def get(self,request,*args, **kwargs):
        if request.session.get('user_enter'):
            return render(request,self.template_name,{'title':'Password Change'})
        else:
            return redirect('login')
    def post(self,request,*args, **kwargs):
        password = request.POST.get('password')
        mobile_number = request.session.get('mobile_number')
        try:
            user_obj = Account.objects.get(mobile_number=mobile_number)
            user_obj.set_password(password)
            user_obj.save()
            user=User.objects.get(account=user_obj)
            del request.session['user_enter']
            return redirect('login')     
        except:
            messages.error(request, 'Mobile number not found. Please check and try again.' )


class Logout(View):
    def get(self, request):
        if request.session.get('user_id'):
            del request.session['user_id']
        return redirect('/login/')


class Signup_view(View):
    form_class = AccountForm
    template_name = 'web_webapp/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        try:
            user = Account.objects.get(email=email)

        except:
            user = ""
        if user:
            if user.is_verified_phone == False:
                user.delete()
        if Account.objects.filter(email=email):
            messages.error(request, "Email address already registered. Created an account before?")
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.set_password(form_obj.password)
            form_obj.name = name
            form_obj.save()
            Account.objects.filter(email=email).update(is_active=True, is_verified_phone=True)
            request.session['user_id'] = form_obj.id
            return redirect('/')
        return render(request, self.template_name, {'form': form, })


class Shop(View):
    template_name = 'web_webapp/shop.html'

    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        header_template = define_header(user_id)
        category = Category.objects.filter(is_delete=False)
        categorys = []
        categoryes = []
        list_cate = []
        sub_list = []
        sub_list_cate = []
        main_category = []
        cate_id = request.GET
        for categories in category:

            product_obj = Product.objects.filter(category=categories, is_approved=True)
            if product_obj:
                categorys.append({
                    'id': categories.id,
                    "name": categories.name,
                    "url": categories.url,
                    'parent_cate': categories.parent_category.name

                })
                main_category.append({
                    'name': categories.parent_category.name
                })
                sub_list = []
                sub_cate = SubCategory.objects.filter(parent_category=categories)
                for sub_cate in sub_cate:
                    sub_list.append({
                        'id': sub_cate.id,
                        "name": sub_cate.name,
                        'parent_cate': sub_cate.parent_category.id

                    })
        main_categorys = []
        for i in range(len(main_category)):
            if main_category[i] not in main_category[i + 1:]:
                main_categorys.append(main_category[i])
        categoryss = []
        for i in range(len(categorys)):
            if categorys[i] not in categorys[i + 1:]:
                categoryss.append(categorys[i])
        sub_lists = []
        if sub_list:
            for i in range(len(sub_list)):
                if sub_list[i] not in sub_list[i + 1:]:
                    sub_lists.append(sub_list[i])
        if cate_id:
            for key, value in cate_id.items():
                if (key.find('sub')) == -1:
                    category_obj = Category.objects.get(id=value)
                    product_obj = Product.objects.filter(category=category_obj, is_approved=True)
                    if product_obj:
                        categoryes.append({
                            'id': category_obj.id,
                            "name": category_obj.name,
                            "url": category_obj.url,
                        })
                        list_cate.append(int(value))
                else:
                    category_obj = SubCategory.objects.get(id=value)
                    product_obj = Product.objects.filter(sub_category=category_obj, is_approved=True)
                    if product_obj:
                        categoryes.append({
                            'id': category_obj.parent_category.id,
                            "name": category_obj.parent_category.name,
                            "url": category_obj.parent_category.url,
                            "parent_id": category_obj.id
                        })
                        sub_list_cate.append(int(value))


        else:
            for categories in category:
                product_obj = Product.objects.filter(category=categories, is_approved=True)
                if product_obj:
                    categoryes.append({
                        'id': categories.id,
                        "name": categories.name,
                        "url": categories.url,
                    })
        categoryesss = []
        for i in range(len(categoryes)):
            if categoryes[i] not in categoryes[i + 1:]:
                categoryesss.append(categoryes[i])
        fetured_campaign = []
        fetured_campaigns = BannerCampaign.objects.filter(is_delete=False, is_active=True)
        for fetured_campaignss in fetured_campaigns:
            if fetured_campaignss.expiry_date == "":
                fetured_campaign.append(fetured_campaignss)
            elif str(fetured_campaignss.expiry_date) >= str(datetime.date.today()):
                if str(fetured_campaignss.start_date) <= str(datetime.date.today()):
                    fetured_campaign.append(fetured_campaignss)
        return render(request, self.template_name,
                      {"category": categoryesss, 'main_category': main_categorys, "category_list": categoryss,
                       'header_template': header_template, 'list_cate': list_cate, 'fetured_campaign': fetured_campaign,
                       "sub_list": sub_lists, "sub_list_cate": sub_list_cate})


class Login_view(View):
    initial = {'key': 'value'}
    template_name = 'web_webapp/login.html'

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', "None")
        return render(request, self.template_name, {'id': id, 'title': 'Login'})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = Account.objects.get(email=username)
            if user_obj.is_active == False:
                user = 0
                messages.error(request, 'Your account is currently deactivated. Please contact support.')
            else:
                user = authenticate(username=user_obj.email, password=password)
        except:
            user = ""
            messages.error(request, 'Email address not found. Please check and try again.')
        if user:

            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                # request.session['mobile_number'] = user.mobile_number
                return redirect('/')
            else:
                messages.error(request, 'Your account is currently deactivated. Please contact support.')

        if user == None:
            messages.error(request, 'Incorrect login or password.')
        return render(request, self.template_name, {'title': 'Login'})

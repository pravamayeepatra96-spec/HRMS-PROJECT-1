from django.shortcuts import render, redirect

from .models import TelegramDetails


def telegram_list(request):

    telegram_users = TelegramDetails.objects.all()

    return render(
        request,
        'telegram_list.html',
        {'telegram_users': telegram_users}
    )


def telegram_details(request, id):

    telegram_user = TelegramDetails.objects.get(id=id)

    return render(
        request,
        'telegram_details.html',
        {'telegram_user': telegram_user}
    )


def telegram_profile(request):

    if request.method == "POST":

        empid = request.POST.get('empid')

        user_id = request.POST.get('user_id')

        comp_code = request.POST.get('comp_code')

        phone_no = request.POST.get('phone_no')

        telegram_name = request.POST.get('telegram_name')

        TelegramDetails.objects.create(

            empid=empid,

            user_id=user_id,

            comp_code=comp_code,

            phone_no=phone_no,

            telegram_name=telegram_name,

            status=1
        )

        return redirect('/telegram-list/')

    return render(
        request,
        'telegram_profile.html'
    )
from django.shortcuts import render
# "EmailMessage" is for dvanced features, such as BCC’ed recipients,
#  file attachments, or multi-part email
from django.core.mail import send_mail, send_mass_mail,\
                             EmailMessage ,BadHeaderError
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    try:
        send_mail(
            subject = 'this is the email subject',
            message = 'this is the email Message.',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = ['amin.akhras1@gmail.com'],
            fail_silently = False
        )
    # if the user is trying to inject a header injection
    # (security exploit) to control to and from emails
    except BadHeaderError:
        # deactivate his account and log him out
        request.user.is_active = False
        print(f"the user {user.username} is trying to use header injection")
        HttpResponseRedirect("logout/")
    return HttpResponse("the email has been sent")

## another option to sending multiple emails separated from each other

# datatuple = (
#     ('this is the email subject', 'this is the email Message.', 'amin603123@gmail.com', ['amin602123@gmail.com']),
#     ('this is the email subject', 'this is the email Message.', 'amin603123@gmail.com', ['amin.akhras1@gmail.com']),
# )
# send_mass_mail(datatuple)



# from django.core.mail import EmailMessage
#
# email = EmailMessage(
#     'Hello',
#     'Body goes here',
#     'from@example.com',
#     ['to1@example.com', 'to2@example.com'],
#     ['bcc@example.com'],
#     reply_to=['another@example.com'],
#     headers={'Message-ID': 'foo'},
# )
# email.attach_file('/images/weather_map.png')
# email.attach('design.png', img_data, 'image/png')
# email.send()



# from django.core.mail import EmailMultiAlternatives
#
# subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
# text_content = 'This is an important message.'
# html_content = '<p>This is an <strong>important</strong> message.</p>'
# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# msg.attach_alternative(html_content, "text/html")
# msg.send()

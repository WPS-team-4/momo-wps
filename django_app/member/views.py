try:
    from utils.email import send_mail
except:
    from django.core.mail import send_mail


def user_auth_mail(to_mail):
    subject = "MOMO에 가입하신 것을 환영합니다."
    from_mail = "kizmo04@gmail.com"
    send_mail(subject, 'Here is the message.', from_mail, [to_mail], fail_silently=False)

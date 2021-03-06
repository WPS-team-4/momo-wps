from passlib.handlers.pbkdf2 import pbkdf2_sha256

try:
    from utils.email import send_mail
except:
    from django.core.mail import send_mail


def send_auth_mail(user):
    hash = pbkdf2_sha256.encrypt(user.username, rounds=200000, salt_size=16)
    user.hash_username = hash.replace("$pbkdf2-sha256$", "")
    user.save()
    subject = "MOMO에 가입하신 것을 환영합니다."
    from_mail = "kizmo04@gmail.com"
    to_mail = user.email
    url = 'http://eb-client.ap-northeast-2.elasticbeanstalk.com/api/member/activate/?key={}'.format(user.hash_username)
    html_message = "<a href='{}'>여기를 눌러 계정을 활성화해주세요.</a>".format(url)
    send_mail(subject, '', from_mail, [to_mail], fail_silently=False, html=html_message)

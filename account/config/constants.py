MYROLE = {
    "MEMBER": 1,
    "ADMIN": 2,
}

ERROR_CODE = {
    'TICKET_INVALID': 40001,
    'TICKET_EXPIRED': 40002,
    'OTP_INVALID': 40003,
    'OTP_EXPIRED': 40004,
    'USERNAME_PASSWORD_INCORECT': 40005,
    'SEND_OTP_ERROR': 40006,
    'SEND_MAIL_ERROR': 40007,
    'USER_NOT_EXIST': 40008,
    'OLD_NEW_PASSWORD_NOT_SAME': 40009,
    'OLD_PASSWORD_NOT_CORRECT': 40010,
    'PERMISSION_DENIED': 40011,
    'RATE_LIMIT_CLICK': 40012,
    'NOT_LOGIN_NO_ACCESS_TOKEN': 40013,
}

COUNTRY_CHOICES = [
    ('us', 'United States'),
    ('ca', 'Canada'),
    ('uk', 'United Kingdom'),
    ('au', 'Australia'),
    ('fr', 'France'),
    ('de', 'Germany'),
    ('jp', 'Japan'),
    ('vn', 'Viet Nam')
]
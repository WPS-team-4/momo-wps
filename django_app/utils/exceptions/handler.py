from rest_framework.views import exception_handler

__all__ = (
    'custom_exception_handler',
)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {}
        errors = []
        for field, value in response.data.items():
            errors.append("{} : {}".format(field, " ".join(value)))

        response.data['errors'] = errors
        response.data['status_code'] = '{} - {}'.format(response.status_code, response.status_text)
        response.data['detail'] = str(exc)

    return response

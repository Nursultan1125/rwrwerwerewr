from footer_data.models import TitleFooter


def footer_info(requesr):
    footer = TitleFooter.objects.all()
    return locals()



# Função pra usar em todos os templates
def user_full_name(request):
    if request.user.is_authenticated:
        return {'user_full_name': request.user.get_full_name()}
    return {}

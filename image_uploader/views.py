from django.http import JsonResponse

def test(request):
	return JsonResponse(['wow', {'json': True}], safe=False)

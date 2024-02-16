from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import LinearForm, CyclicForm, BranchesForm
from .algorithms import linear_algorithm, branches_algorithm, cyclic_algorithm


def home(request):
    return HttpResponse("home page")


class AlgorithmView(TemplateView):
    template_name = 'algorithm_pages/algorithm_page.html'
    algorithms = {
        'linear': {'name': 'linear', 'algorithm': linear_algorithm, 'form': LinearForm()},
        'branches': {'name': 'branches', 'algorithm': branches_algorithm, 'form': BranchesForm()},
        'cyclic': {'name': 'cyclic', 'algorithm': cyclic_algorithm, 'form': CyclicForm()}
    }

    def get(self, request, *args, **kwargs):
        algorithm = self.algorithms[kwargs['algorithm']]
        return render(request, self.template_name, context={'algorithm': algorithm})

    def post(self, request, *args, **kwargs):
        arguments = list(request.POST.values())[1:]
        algorithm_type = kwargs['algorithm']
        algorithm_function = self.algorithms[algorithm_type]['algorithm']
        result = algorithm_function(*map(int, arguments))
        return HttpResponse(result)

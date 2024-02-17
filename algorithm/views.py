from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import LinearForm, CyclicForm, BranchesForm, FileForm
from .algorithms import linear_algorithm, branches_algorithm, cyclic_algorithm
from .file_handler import algorithm_result_from_file


def home(request):
    return HttpResponse("home page")


class AlgorithmView(TemplateView):
    template_name = 'algorithm_pages/algorithm_page.html'
    algorithms = {
        'linear': {'name': 'linear', 'algorithm': linear_algorithm, 'form': LinearForm(), 'class': LinearForm},
        'branches': {'name': 'branches', 'algorithm': branches_algorithm, 'form': BranchesForm(),
                     'class': BranchesForm},
        'cyclic': {'name': 'cyclic', 'algorithm': cyclic_algorithm, 'form': CyclicForm(), 'class': CyclicForm}
    }

    def get(self, request, *args, **kwargs):
        algorithm = self.algorithms[kwargs['algorithm']]
        return render(request, self.template_name, context={'algorithm': algorithm, 'file_form': FileForm})

    def post(self, request, *args, **kwargs):
        algorithm_type = kwargs['algorithm']
        algorithm_function = self.algorithms[algorithm_type]['algorithm']
        algorithm = self.algorithms[algorithm_type]
        result = 'invalid data'
        if request.FILES.get('file'):
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                result = algorithm_result_from_file(algorithm_function, form.cleaned_data['file'])

        form = algorithm['class'](request.POST)
        if form.is_valid():
            arguments = list(request.POST.values())[1:]
            result = algorithm_function(*map(int, arguments))
        return render(request, self.template_name,
                      context={'algorithm': algorithm, 'file_form': FileForm, 'result': result})

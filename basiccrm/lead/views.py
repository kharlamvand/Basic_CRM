from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.views import View
from .forms import AddCommentForm, AddFileForm
from .models import Lead

from client.models import Client, Comment as ClientComment
from team.models import Team


class LeadListView(LoginRequiredMixin, ListView):  # список заявок
    model = Lead

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, converted_to_client=False)


class LeadDetailView(LoginRequiredMixin, DetailView):  # детали заявок
    model = Lead

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        context['fileform'] = AddFileForm()

        return context

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))


class LeadDeleteView(LoginRequiredMixin, DeleteView):  # удалить заявку
    model = Lead
    success_url = reverse_lazy('leads:list')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class LeadUpdateView(LoginRequiredMixin, UpdateView):  # редактировать заявку
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:list')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit lead'

        return context

    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))


class LeadCreateView(LoginRequiredMixin, CreateView):  # создать заявку
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:list')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = Team.objects.filter(created_by=self.request.user)[0]
        context['team'] = team
        context['title'] = 'Add lead'

        return context

    def form_valid(self, form):
        team = Team.objects.filter(created_by=self.request.user)[0]

        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = team
        self.object.save()

        return redirect(self.get_success_url())


class AddFileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            file = form.save(commit=False)
            file.team = team
            file.lead_id = pk
            file.created_by = request.user
            file.save()

        return redirect('leads:detail', pk=pk)


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        form = AddCommentForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.lead_id = pk
            comment.save()

        return redirect('leads:detail', pk=pk)


class ConvertToClientView(LoginRequiredMixin, View):  # добавить в потенциальные клиенты
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        team = Team.objects.filter(created_by=request.user)[0]

        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            description=lead.description,
            created_by=request.user,
            team=team,
        )

        lead.converted_to_client = True
        lead.save()

        # Преобразовываем комментарии заявок в комментарии клиентов

        comments = lead.comments.all()

        for comment in comments:
            ClientComment.objects.create(
                client=client,
                content=comment.content,
                created_by=comment.created_by,
                team=team
            )

        # Показать сообщение перенаправить и сохранить сообщение
        messages.success(request, 'The lead was converted to a client.')

        return redirect('leads:list')

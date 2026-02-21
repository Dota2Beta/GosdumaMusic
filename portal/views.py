from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView

from .forms import ApplicationForm, ApplicationStatusForm, LoginForm, RegisterForm
from .models import Application


class UserLoginView(LoginView):
    template_name = 'portal/login.html'
    authentication_form = LoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'Неверный логин или пароль.')
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    template_name = 'portal/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Регистрация прошла успешно.')
        return response

    def get_success_url(self):
        return '/dashboard/'


@login_required
def dashboard(request):
    user_apps = request.user.applications.all()
    return render(request, 'portal/dashboard.html', {'applications': user_apps})


@login_required
def create_application(request):
    form = ApplicationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        app = form.save(commit=False)
        app.user = request.user
        app.save()
        messages.success(request, 'Заявка отправлена со статусом «Новая».')
        return redirect('dashboard')
    return render(request, 'portal/create_application.html', {'form': form})


@login_required
def admin_panel(request):
    if request.user.username != 'BraveGuap':
        messages.error(request, 'Доступ разрешен только администратору.')
        return redirect('dashboard')

    applications = Application.objects.select_related('user').all()
    return render(request, 'portal/admin_panel.html', {'applications': applications, 'status_form': ApplicationStatusForm})


@login_required
def update_application_status(request, app_id):
    if request.user.username != 'BraveGuap':
        messages.error(request, 'Недостаточно прав.')
        return redirect('dashboard')

    app = get_object_or_404(Application, id=app_id)
    form = ApplicationStatusForm(request.POST, instance=app)
    if form.is_valid():
        form.save()
        messages.success(request, 'Статус заявки обновлен.')
    else:
        messages.error(request, 'Не удалось обновить статус заявки.')
    return redirect('admin_panel')

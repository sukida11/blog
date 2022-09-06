from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *


# Create your views here.
class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['channels'] = Chanel.objects.order_by('-reg_date')[:5]
        context['posts'] = Post.objects.order_by('-date_pub')[:5]
        return context


class RegistrationUserView(CreateView):
    template_name = 'blog/reg.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('blog:profile', kwargs={'pk':user.id}))


class LoginUserView(LoginView):
    template_name = 'blog/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse('blog:profile', kwargs={'pk':self.request.user.id})


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'blog/profile.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['adm_ch'] = UserRoot.objects.filter(
            worker_id=self.kwargs['pk']
        ).all()
        return context


class CreateProfileInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/create_profile.html'

    def post(self,request):
        if request.POST['age'] and request.POST['bio'] and request.POST['city']:
            p = Profile(
                user = request.user,
                city = request.POST['city'],
                bio = request.POST['bio'],
                age = request.POST['age']
            )
            p.save()

            user = User.objects.get(pk=request.user.id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

        return HttpResponseRedirect(reverse('blog:profile', kwargs={'pk':user.id}))


class ChangeProfileInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/change_profile_info.html'

    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        profile = user.profile

        for k, v in request.POST.items():
            if k == 'csrfmiddlewaretoken':
                continue

            elif v:

                if k == 'first_name' or k == 'last_name' or k == 'email':
                    setattr(user, k, v)

                else:

                    if k == 'age' and v=='':
                        continue

                    setattr(profile, k, v)


        profile.save()
        user.save()

        return HttpResponseRedirect(f"{reverse('blog:profile', kwargs={'pk':user.id})}?all_data=True")


class CreateChanelView(LoginRequiredMixin,TemplateView):
    template_name = 'blog/create_chanel.html'

    def post(self, request):
        
        try:
            c = Chanel(
                owner = request.user,
                name = request.POST['name'],
                description = request.POST['description']
            )
            c.save()

        except:
            messages.add_message(request, messages.ERROR, 'Попробуйте снова. Имя канала не уникально.')
            return HttpResponseRedirect(reverse('blog:create_chanel'))

        return HttpResponseRedirect(reverse('blog:my_chanel'))


class MyChanel(LoginRequiredMixin,ListView):
    template_name = 'blog/my_chanel.html'
    context_object_name = 'chanel_list'
    paginate_by = 5

    def get_queryset(self):
        return Chanel.objects.filter(owner_id=self.request.user.id)


class ChannelView(LoginRequiredMixin, DetailView):
    model = Chanel
    template_name = 'blog/channel_view.html'
    context_object_name = 'channel'

    def post(self, request, pk):
        c = Chanel.objects.get(pk=pk)

        for k, v in request.POST.items():
            if not v:
                continue
            else:
                setattr(c, k, v)

        c.save()

        if 'sub' in request.POST:
            s = Subscriber(
                user = request.user,
                chanel = Chanel.objects.get(pk=pk)
            )
            s.save()

        if 'unsub' in request.POST:
            if request.POST['unsub'] == 'Отписаться':
                Subscriber.objects.filter(chanel_id=pk).filter(user_id=request.user.id).first().delete()

        return HttpResponseRedirect(reverse('blog:admin_channels', kwargs={'pk':pk}))


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['adm_ch'] = UserRoot.objects.filter(
            worker_id=self.request.user.id
        ).filter(
            channel_id=self.kwargs['pk']
        ).first()

        context['usr_sub'] = Subscriber.objects.filter(
            chanel_id=self.kwargs['pk']
        ).filter(
            user_id=self.request.user
        ).first()

        context['adm_ch'] = UserRoot.objects.filter(
            worker_id=self.request.user.id
        ).filter(
            channel_id=self.kwargs['pk']
        ).all()

        context['count_sub'] = len(Subscriber.objects.filter(
            chanel_id = self.kwargs['pk']
        ).all())

        return context


class AllChannelsView(LoginRequiredMixin,ListView):
    template_name = 'blog/all_channels.html'
    context_object_name = 'channels'
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET:
            if not self.request.GET['name_find']:
                return Chanel.objects.order_by('-reg_date')
            elif self.request.GET['name_find']:
                return Chanel.objects.filter(name__startswith=self.request.GET['name_find'])
            else:
                return Chanel.objects.order_by('-reg_date')

        return Chanel.objects.order_by('-reg_date')


class CreatePostView(LoginRequiredMixin,TemplateView):
    template_name = 'blog/create_post.html'

    def post(self, request):
        # print(request.POST['channel'])
        u = User.objects.get(pk=request.user.id)
        channel = Chanel.objects.filter(name=request.POST['channel'])[0]

        if request.POST:
            if request.POST['title'] and request.POST['text']:
                p = Post(
                    author = u,
                    channel = channel,
                    title = request.POST['title'],
                    text = request.POST['text']
                )
                p.save()

                return HttpResponseRedirect(reverse('blog:view_channel', kwargs={'pk':channel.id}))

        return HttpResponseRedirect(reverse('blog:index'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['roots'] = UserRoot.objects.filter(
            worker_id=self.request.user.id
        ).all()

        return context



class AllPostView(LoginRequiredMixin,ListView):
    template_name = 'blog/post_list.html'
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.GET:
            if self.request.GET['name_find']:
                return Post.objects.filter(title__startswith=self.request.GET['name_find']).all()
            else:
                return Post.objects.order_by('-date_pub').all()

        return Post.objects.order_by('-date_pub').all()


class PostView(LoginRequiredMixin,DetailView):
    template_name = 'blog/check_post.html'
    context_object_name = 'post'
    model = Post

    def post(self, request, pk):
        p = Post.objects.get(pk=pk)

        if request.POST:
            if 'comment_text' in request.POST:
                c = Comment(
                    author = request.user,
                    post = p,
                    comment_text = request.POST['comment_text']
                )
                c.save()

            if 'reply_text' in request.POST:
                pass
                cr = CommentReply(

                    author = request.user,
                    post = p,
                    comment_to_reply = Comment.objects.get(pk=int(request.GET['reply_for_comment_id'])),
                    reply_text = request.POST['reply_text']
                )
                cr.save()

            if 'like' in request.POST:
                ul = UserLiked(
                    user = request.user,
                    post = p
                )
                ul.save()


        return HttpResponseRedirect(reverse_lazy('blog:check_post', kwargs={'pk': p.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['likes_count_all'] = len(UserLiked.objects.filter(post_id=self.kwargs['pk']).all())

        context['user_liking'] = UserLiked.objects.filter(
            user_id=self.request.user.id
        ).filter(
            post_id=self.kwargs['pk']
        ).first()

        context['roots'] = UserRoot.objects.filter(
            worker_id=self.request.user.id
        ).all()

        return context


class ChangePostView(LoginRequiredMixin,DetailView):
    template_name = 'blog/change_post.html'
    model = Post
    context_object_name = 'post'

    def post(self, request, pk):
        p = Post.objects.get(pk=pk)

        if 'title' in request.POST or 'text' in request.POST:
            for k, v in request.POST.items():
                if v and k:
                    setattr(p, k, v)

                else:
                    continue
        elif 'delete_post' in request.POST:
            channel_id = Post.objects.get(pk=pk).channel.id
            Post.objects.get(pk=pk).delete()

            return HttpResponseRedirect(reverse('blog:admin_channels', kwargs={'pk':channel_id}))

        p.save()

        return HttpResponseRedirect(reverse('blog:check_post', kwargs={'pk':p.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['roots'] = UserRoot.objects.filter(
            worker_id=self.request.user.id
        ).all()

        return context


class AddAdminView(LoginRequiredMixin,DetailView):
    template_name = 'blog/add_admin.html'
    model = Chanel
    context_object_name = 'chanel'

    def post(self, request, pk):
        if 'worker_id' in request.POST:
            chanel_owner = request.user
            chanel_worker = User.objects.get(pk=request.POST['worker_id'])

            r = UserRoot(
                owner = chanel_owner,
                worker = chanel_worker,
                channel = Chanel.objects.get(pk=pk),
                roots = request.POST['user_root']
            )
            r.save()

        return HttpResponseRedirect(reverse('blog:admin_channels', kwargs={'pk':pk}))


class FindUserView(LoginRequiredMixin,TemplateView):
    template_name = 'blog/find_user.html'

    def post(self, request):
        if 'username' in request.POST or 'id' in request.POST:
            if request.POST['username'] != '':
                try:
                    u = User.objects.get(username=request.POST['username'])

                    return HttpResponseRedirect(reverse('blog:profile', kwargs={'pk':u.id}))

                except:
                    messages.add_message(
                        request, 
                        messages.ERROR, 
                        'Пользователь с этим username не найден!')

            elif request.POST['id'] != '':
                try:
                    u = User.objects.get(pk=request.POST['id'])

                    return HttpResponseRedirect(reverse('blog:profile', kwargs={'pk':u.id}))

                except:
                    messages.add_message(
                        request, 
                        messages.ERROR, 
                        'Пользователь с этим ID не найден!')

        return HttpResponseRedirect(reverse('blog:find_user'))

        

@login_required
def logout_func(request):
    logout(request)

    return HttpResponseRedirect(reverse('blog:login'))


@login_required
def delete_chanel(request, pk):
    chanel = Chanel.objects.get(pk=pk)

    if request.POST:
        if request.POST['delete_chanel'] == 'Удалить':
            Chanel.objects.get(pk=pk).delete()

            return HttpResponseRedirect(reverse('blog:my_chanel'))

    return render(request, 'blog/delete_chanel.html', context={'chanel':chanel})


def error_404_view(request, exception):
    return render(request, 'blog/404.html', status=404)

def error_500_view(exception):
    return render(request, 'blog/500.html', status=500)
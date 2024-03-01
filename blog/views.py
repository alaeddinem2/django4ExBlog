from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView 
from .models import Post
# Create your views here.

def post_list(request):
    all_posts = Post.published.all()
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/post_list.html',{'posts':posts})


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug = post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request,'blog/post/post_detail.html',{'post':post})

#CLASS BASED VIEW

class ListPostView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = 'blog/post/post_list.html'
    paginate_by = 3
    page_kwarg = 'my_page'  # Use 'my_page' as the query parameter for the page number

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['page_obj']
        return context
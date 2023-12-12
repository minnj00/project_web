from django.shortcuts import render, redirect
from .models import Post, Ingred, RecipeIngred, RecipeDetail
from .forms import PostForm
from django.contrib.auth.decorators import login_required
import logging

# settings.py 파일에서 설정된 로거를 취득
logger = logging.getLogger('mylogger')

def my_view(request):
    logger.info('info레벨로 출력')


# Create your views here.
def index(request):
    # order_by('-id') 최근에 생성된 게시물이 위에 보여지도록!
    posts = Post.objects.all().order_by('-id')

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.serving = form.cleaned_data['serving']
            post.cate1 = form.cleaned_data['cate1']
            post.cate2 = form.cleaned_data['cate2']
            post.cate3 = form.cleaned_data['cate3']
            post.save()

            ingreddetails = form.cleaned_data['ingredsdetails'].split(",")
            recipedetails = form.cleaned_data['recipedetails'].split(",")

        
            for ingreddetail in ingreddetails:
                recipeingred = RecipeIngred()
                if ingreddetail:
                    if not ingreddetail:
                        continue
                    ingred = ingreddetail.split('/')[0]
                    amount = ingreddetail.split('/')[1]
                    _ingred, created = Ingred.objects.get_or_create(ingred_name=ingred)

                    # post.ingred.add(_ingred)

                    recipeingred.post = post
                    recipeingred.ingred = _ingred
                    recipeingred.amount = amount

                    recipeingred.save()

                    
            for recipe in recipedetails:
                recipedetail = RecipeDetail()
                if recipe:
                    if not recipe:
                        continue
                    step = recipe.split('/')[0]
                    recipecontent = recipe.split('/')[1]
                    
                    recipedetail.post = post
                    recipedetail.step = step
                    recipedetail.contents = recipecontent

                    recipedetail.save()

            return redirect("/posts/")
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def index_cate1_1(request):
    # order_by('-id') 최근에 생성된 게시물이 위에 보여지도록!
    posts = Post.objects.filter(cate1='한식').order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def index_cate1_2(request):
    # order_by('-id') 최근에 생성된 게시물이 위에 보여지도록!
    posts = Post.objects.filter(cate1='양식').order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def index_cate1_3(request):
    # order_by('-id') 최근에 생성된 게시물이 위에 보여지도록!
    posts = Post.objects.filter(cate1='일식').order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
def index_cate2_1(request):
    posts = Post.objects.filter(cate2='모임용').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate2_2(request):
    posts = Post.objects.filter(cate2='원팬/스피디').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate2_3(request):
    posts = Post.objects.filter(cate2='술안주').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate2_4(request):
    posts = Post.objects.filter(cate2='일상').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate2_5(request):
    posts = Post.objects.filter(cate2='다이어트').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate2_6(request):
    posts = Post.objects.filter(cate2='디저트').order_by('-id')
    return render(request, 'index.html', {'posts': posts})

def index_cate3_1(request):
    posts = Post.objects.filter(cate3='소고기').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_2(request):
    posts = Post.objects.filter(cate3='돼지고기').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_3(request):
    posts = Post.objects.filter(cate3='닭고기').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_4(request):
    posts = Post.objects.filter(cate3='육류').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_5(request):
    posts = Post.objects.filter(cate3='채소').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_6(request):
    posts = Post.objects.filter(cate3='생선').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_7(request):
    posts = Post.objects.filter(cate3='해물').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_8(request):
    posts = Post.objects.filter(cate3='쌀').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_9(request):
    posts = Post.objects.filter(cate3='밀가루').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_10(request):
    posts = Post.objects.filter(cate3='콩/견과류').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_11(request):
    posts = Post.objects.filter(cate3='달걀/유제품').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_12(request):
    posts = Post.objects.filter(cate3='가공식품류').order_by('-id')
    return render(request, 'index.html', {'posts': posts})
def index_cate3_13(request):
    posts = Post.objects.filter(cate3='기타').order_by('-id')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    ingreds = RecipeIngred.objects.filter(post_id = post_id)
    recipes = RecipeDetail.objects.filter(post_id = post_id)

    context = {
        'post': post,
        'ingreds': ingreds,
        'recipes': recipes

    }

    return render(request, 'post_detail.html', context)
        


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']      
        recipes = Post.objects.filter(
            Q(title__icontains=searched) | Q(cate1__icontains=searched)|
            Q(cate2__icontains=searched) | Q(cate3__icontains=searched))
        # recipes = Post.objects.filter(title__icontains=searched) # 제목만으로 필터링 
        context = {
            'searched': searched, 
            'recipes': recipes,  
        }
        return render(request, 'searched.html', context)
    else:
        return render(request, 'searched.html', {})


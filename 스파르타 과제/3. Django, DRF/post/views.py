from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.db.models import Q

from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    """
    게시글 목록 및 검색 기능
    """
    search_query = request.GET.get('search', '').strip()
    posts = Post.objects.all()
    
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    posts = posts.order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    
    try:
        page_obj = paginator.page(page_number)
    except (ValueError, EmptyPage):
        # 유효하지 않은 페이지 번호의 경우 첫 페이지로 설정
        page_obj = paginator.page(1)
    
    return render(request, 'post/post_list.html', {
        'posts': page_obj,
        'search_query': search_query,
        'paginator': paginator
    })

def post_detail(request, pk):
    """
    게시글 상세 정보 및 댓글 기능
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    comment_form = CommentForm()
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, '댓글이 성공적으로 작성되었습니다.')
            return redirect('post:post_detail', pk=pk)
        else:
            messages.error(request, '댓글 작성에 실패했습니다. 다시 확인해주세요.')
            
    return render(request, 'post/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def post_create(request):
    """
    새 게시글 작성
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '게시글이 성공적으로 작성되었습니다.')
            return redirect('post:post_detail', pk=post.pk)
        else:
            messages.error(request, '게시글 작성에 실패했습니다. 다시 확인해주세요.')
    else:
        form = PostForm()
    
    return render(request, 'post/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    """
    게시글 수정
    """
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 수정 가능
    if request.user != post.author:
        messages.error(request, '게시글을 수정할 권한이 없습니다.')
        return redirect('post:post_detail', pk=pk)
        
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '게시글이 성공적으로 수정되었습니다.')
            return redirect('post:post_detail', pk=post.pk)
        else:
            messages.error(request, '게시글 수정에 실패했습니다. 다시 확인해주세요.')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'post/post_form.html', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
    """
    게시글 삭제
    """
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 삭제 가능
    if request.user != post.author:
        messages.error(request, '게시글을 삭제할 권한이 없습니다.')
        return redirect('post:post_detail', pk=pk)
        
    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시글이 성공적으로 삭제되었습니다.')
        return redirect('post:post_list')
    
    return render(request, 'post/post_confirm_delete.html', {'post': post})

@login_required
def comment_delete(request, post_pk, comment_pk):
    """
    댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    # 작성자만 삭제 가능
    if request.user != comment.author:
        messages.error(request, '댓글을 삭제할 권한이 없습니다.')
        return redirect('post:post_detail', pk=post_pk)
    
    comment.delete()
    messages.success(request, '댓글이 성공적으로 삭제되었습니다.')
    return redirect('post:post_detail', pk=post_pk)

@login_required
def comment_update(request, post_pk, comment_pk):
    """
    댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    # 작성자만 수정 가능
    if request.user != comment.author:
        messages.error(request, '댓글을 수정할 권한이 없습니다.')
        return redirect('post:post_detail', pk=post_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, '댓글이 성공적으로 수정되었습니다.')
            return redirect('post:post_detail', pk=post_pk)
        else:
            messages.error(request, '댓글 수정에 실패했습니다. 다시 확인해주세요.')
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'post/comment_form.html', {
        'form': form, 
        'comment': comment,
        'post_pk': post_pk
    })

@login_required
def like_post(request, pk):
    """
    게시글 좋아요/좋아요 취소
    """
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        
        return JsonResponse({
            'liked': liked,
            'total_likes': post.likes.count()
        })
    
    return redirect('post:post_detail', pk=pk)
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from accounts.admin import *
from django.http import HttpResponse
from videos.views import moderate_content
# from django.contrib.auth.decorators import check_captcha
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.shortcuts import render

from videos.forms import CommentEditForm
from videos.models import Comments


def create_comment(request):
    if request.method == 'POST':
        text_content = request.POST.get('text_content')
        toxicity_score = moderate_content(text_content)

        if toxicity_score is not None and toxicity_score >= 0.5:
            # The content is deemed toxic, take appropriate action (e.g., reject the comment)
            return render(request, 'toxic_content.html')
        else:
            # Save the comment to the database and display it
            Comments.objects.create(text_content=text_content)
            return render(request, 'comment_created.html')


# Create your views here.
@login_required
def edit_comment(request, comment_id):
    template_name = 'videos/video_details.html'
    try:
        comment = Comments.objects.get(id=comment_id)
    except Comments.DoesNotExist:
        return HttpResponse('Comment not found ', status=404)
    if request.method == 'POST':
        form = CommentEditForm(request.POST)
        if comment.user == request.user:
            comment_text = request.POST.get('comment_text')
            comment.text = comment_text
            comment.save()
            return HttpResponse('Comment updated successfully')
        else:
            return redirect('videos:video_details', video_id=comment.video.pk)
    else:
        form = CommentEditForm()
        return render(request, template_name, {'form': form})


def like_comment(request, comment_id):
    template_name = 'videos/video_details.html'
    if request.method == 'POST':
        comment = Comments.objects.get(pk=comment_id)
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        return JsonResponse({'likes_count': comment.likes.count()})
    else:
        comment = Comments.objects.get(pk=comment_id)
        return render(request, template_name, {'comment': comment})


def delete_comment(request, comment_id):
    template_name = 'videos/video_details.html'
    if request.method == 'POST':
        comment = get_object_or_404(Comments, pk=comment_id)
        # comment = Comment.objects.get(pk=comment_id)
        if comment.user == request.user:
            comment.delete()

        return redirect('videos:video_details', video_id=comment.video.pk)
    else:
        comment = get_object_or_404(Comments, pk=comment_id)
        return render(request, template_name, {'comment': comment})



from django.urls import path

from . import views

app_name = 'videos'

urlpatterns = [
    path('admin_dashboard', views.admin_dashboard, name='your_videos'),
    path('record_short_videos/', views.record_short_videos, name='record_short_videos'),
    path('upload_short_videos/', views.upload_short_videos, name='upload_short_videos'),
    path('short_video_list/', views.short_video_list, name='short_video_list'),
    path('short_video_details/<int:short_id>/', views.short_video_details, name='short_video_details'),
    path('video/<int:video_id>/', views.video_details, name='video_details'),
    path('create_video/', views.create_video, name='create_video'),
    path('search/', views.video_search, name='video_search'),
    path('video/', views.admin_dashboard, name='video'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('upload_video/', views.upload_form, name='upload_video'),
    path('library', views.library, name='library'),
    path('video_history/', views.VideoHistoryListView.as_view(), name='video_history'),
    path('liked_videos', views.liked_videos, name='liked_videos'),
    path('recommended_videos/', views.recommended, name='recommended_videos'),
    path('favorite_videos/', views.favorite_videos, name='favorite_videos'),
#    path('watched_videos/', views.watched_videos, name='watched_videos'),
    path('trending/', views.trending, name='trending'),
    path('watch_later/', views.watch_later, name='watch_later'),
    path('add_to_watch_later/<int:video_id>/', views.add_watch_later, name='add_to_watch_later'),
    path('remove_from_watch_later/<int:watch_later_id>/', views.remove_watch_later, name='remove_from_watch_later'),
    path('your_videos/', views.your_videos, name='your_videos'),
    path('coming_events/', views.coming_events, name='coming_events'),
    path('overview/', views.overview, name='overview'),
    path('video_details/<int:video_id>/status/', views.status, name='status'),
    path('video_details/like/<int:video_id>/', views.like_video, name='like_video'),
    path('video_details/add_comment/<int:video_id>/', views.post_comment, name='add_comment'),
    path('add_to_favorites/<int:video_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('report_content/<int:video_id>/', views.report_content, name='report_success'),
#    path('video_details/<int:video_id>/', views.video_details_one, name='video_details'),
    path('video_details/<int:video_id>/share/', views.share_video, name='share_video'),
    path('video_details/<int:video_id>/', views.post_comment, name='post_comment'),
    path('video_details/<int:video_id>/dislike/', views.dislike_video, name='dislike_video'),
    # path('video_details/delete_comment/<int:comment_id>/')
    path('subscription_success/', views.subscription_success, name='subscription_success'),
    path('content_submission_success/', views.submit_content, name='content_submission_success'),
    path('approve_content/<int:video_id>', views.approve_content, name='approve_content'),
    path('approved_videos/', views.approved_videos, name='approved_videos'),
    path('pending_videos/', views.pending_videos, name='pending_videos'),
    path('blocked_videos/', views.blocked_videos, name='blocked_videos'),
    path('blocked_video_details/<int:video_id>/', views.blocked_video_details, name='blocked_video_details'),
    path('content_guidelines/', views.view_content_guidelines, name='content_guidelines'),
    path('upload_success/', views.upload_success, name='upload_success'),
    path('record_video/', views.record_upload_video, name='record_video'),
   # path('video_settings/', views.settings, name='video_settings'),
    path('moderation_dashboard/', views.moderation_dashboard, name='moderation_dashboard'),
    path('moderation_requests/', views.moderation_request, name='moderation_requests'),
    path('create_channel/', views.create_channel, name='create_channel'),
    path('channel_details/<int:channel_id>/', views.channel_details, name='channel_details'),
    path('channels/', views.channel_list, name='channel_list'),
    path('home', views.home, name='home'),
    path('public_terms_of_service', views.public_terms_of_service, name='public_terms_of_service'),
    # path('', views.all_videos, name='all_videos'),
    path('praise_and_worship/', views.praise_and_worship, name='praise_and_worship_videos'),
    path('live_videos/ ', views.live_videos, name='live_videos'),
    path('live_stream/', views.live_stream, name='live_stream'),
    path('music_videos/', views.music, name='music_videos'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    #path('search_for_video/', views.video_search, name='video_search'),
    path('<int:comment_id>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('<int:comment_id>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('add_comment/', views.post_comment, name='add_comment'),
    path('total_playlist_videos/', views.playlist_videos, name='playlist_videos'),
    path('camera_home/', views.camera_home, name='camera_home'),
    path('generate_captions/', views.generate_captions, name='generate_captions'),
    path('video_details/<int:video_id>/add_comment/', views.create_comment, name='add_comments'),
    # path('comments/', views.Requirement.as_view(), name='requirements'),
    # path('requirement/<int:comment_id>/<str:opinion>/', views.UpdateCommentVote.as_view(), name='requirement_comment_vote'),
    path('reply_comment/', views.reply_comment, name='reply_comment'),
    path('sub_load/<int:id>/', views.subscription_load, name='sub_load'),
    path('add_sub/<int:id>/', views.add_subscriptions, name='add_sub'),
#    path('subscribe/', views.SubChannelSubscriptionView.as_view, name='subscribe'),
    path('<uuid:video_id>/like/', views.like_video, name='like_video'),
    path('all_videos/', views.all_videos, name='all_gospel_videos'),
    path('sermons/', views.sermons, name='sermons'),
    path('gospel_made_for_kids/', views.gospel_made_for_kids, name='gospel_made_for_kids'),
    path('praise_and_worship/', views.praise_and_worship, name='praise_and_worship'),
    path('music/', views.music, name='music_videos'),
    path('testimonies/', views.testimonies, name='testimonies'),
    path('evangelism/', views.evangelism, name='evangelism'),
    path('bible_lesson_discussions /', views.bible_discussions, name='bible_discussions'),
    path('detect_text_from_image/',views.detect_text_from_image,name='detect_text_from_image'),
    path('video_results/', views.video_search,name='video_results'),
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.content_by_category, name='content_by_category'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-content/', views.create_content, name='create_content'),
    path('queue/add/<str:video_id>/', views.add_video_to_queue, name='add_video_to_queue'),
    path('queue/remove/<str:video_id>/', views.remove_video_from_queue, name='remove_video_from_queue'),
    path('queue/clear/', views.clear_video_queue, name='clear_video_queue'),
    path('queue/display/', views.display_video_queue, name='display_video_queue'),


]

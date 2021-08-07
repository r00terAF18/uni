from django.urls import path

from .views import *

from .views_college import *
from .views_header import *
from .views_lecture import *
from .views_professor import *
from .views_sidebar import *
from .views_uni_system import *
from .views_news import *
from .views_event import *

urlpatterns = [
    path("", index_admin, name="index-admin"),
    # COLLEGE
    path("College/all/", CollegeList.as_view(), name="college-all"),
    path("College/create/", college_add, name="college-add"),
    path("College/edit/<int:id>/", college_edit, name="college-edit"),
    path("College/update/<int:id>/", college_update, name="college-update"),
    path("College/delet/<int:id>/", college_delete, name="college-delete"),
    # EVENT
    path("Event/admin/all/", event_admin_all, name="event-admin-all"),
    path("Event/create/", event_create, name="event-create"),
    path("Event/edit/<int:id>/", event_edit, name="event-edit"),
    path("Event/delete/<int:id>", event_delete, name="event-delete"),
    # HEADER
    path("Header/create/", header_create, name="header-create"),
    path(
        "Header/create/single/submit/",
        header_single_submit,
        name="header-single-submit",
    ),
    path(
        "Header/create/multi/submit/", header_multi_submit, name="header-multi-submit"
    ),
    path("Page/all/", page_all, name="page-all"),
    path("Page/create/", page_create, name="page-create"),
    path("Page/create/submit/", page_submit, name="page-submit"),
    path("Page/delete/<int:id>/", page_delete, name="page-delete"),
    path("Page/edit/<int:id>/", page_edit, name="page-edit"),
    path("Page/update/<int:id>/", page_update, name="page-update"),
    # SIDEBAR
    path("Sidebar/all/", sidebar_all, name="sidebar-all"),
    path("Sidebar/create/", sidebar_create, name="sidebar-create"),
    path("Sidebar/create/submit/", sidebar_submit, name="sidebar-submit"),
    path("Sidebar/edit/<int:id>/", sidebar_edit, name="sidebar-edit"),
    path("Sidebar/update/", sidebar_update, name="sidebar-update"),
    path("Sidebar/delete/<int:id>/", sidebar_delete, name="sidebar-delete"),
    # PROFESSOR
    path("Professor/add/", professor_add, name="professor-add"),
    path(
        "Professor/create/submit/",
        professor_create_user,
        name="professor-create-submit",
    ),
    path("Professor/all/", professor_upload_all, name="professor-all"),
    path("Professor/post/create/", professor_post_create, name="professor-post-create"),
    path(
        "Professor/post/edit/<int:id>/", professor_post_edit, name="professor-post-edit"
    ),
    path(
        "Professor/post/delete/<int:id>/",
        professor_post_delete,
        name="professor-post-delete",
    ),
    path("Professor/upload/", professor_upload, name="professor-upload"),
    # LECTURES
    path("Lecture/admin/all/", lecture_admin_all, name="lecture-admin-all"),
    path("Lecture/create/", lecture_create, name="lecture-create"),
    path("Lecture/edit/<int:id>/", lecture_edit, name="lecture-edit"),
    path("Lecture/delete/<int:id>", lecture_delete, name="lecture-delete"),
    # NEWSPOST
    path("News/admin/all/", news_admin_all, name="news-admin-all"),
    path("News/create/", news_create, name="news-create"),
    path("News/edit/<int:id>/", news_edit, name="news-edit"),
    path("News/delete/<int:id>", news_delete, name="news-delete"),
    # UNIVERSITY-SYSTEM
    path("University-System/all/", UniSystemList.as_view(), name="uni-system-all"),
    path(
        "University-System/create/",
        uni_system_create,
        name="uni-system-create",
    ),
    path(
        "University-System/delete/<int:id>/",
        uni_system_delete,
        name="uni-system-delete",
    ),
    path("University-System/edit/<int:id>/", uni_system_edit, name="uni-system-edit"),
    path("login/", professor_login, name="login"),
    path("logout/", professor_logout, name="logout"),
]

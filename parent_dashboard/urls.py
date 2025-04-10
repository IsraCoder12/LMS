
from django.urls import path
from .views import dashboard, academic_overview, subject_wise_performance, subject_graphs_view  # Import both views

app_name = "parent_dashboard"  # ✅ App name define karein

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),  # ✅ 'dashboard' URL
    path('academic-overview/', academic_overview, name='academic_overview'),  # Added here
    path('subject-performance/', subject_wise_performance, name='subject_performance'),
    path('subject-graphs/', subject_graphs_view, name='subject_graphs'),
]


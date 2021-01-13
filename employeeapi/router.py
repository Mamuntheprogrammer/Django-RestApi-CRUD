from employeeapi.viewsets import EmployeeViewsets
from rest_framework import routers

router = routers.DefaultRouter()

router.register('employee',EmployeeViewsets)


urlpatterns =[

]
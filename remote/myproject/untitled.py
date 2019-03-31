class employeeList(viewsets.ModelViewSet):

	def get(self,request):
		employees = employee.objects.all()
		serializer = employeeSerializer(employees,many=True)
		return Response(serializer.data)

	def post(self,request):
		data = request.body
		print(data)
		emp = employee()
		emp.firstname=data['firstname']
		emp.lastname=data['lastname']
		emp.emp_id=data['emp_id']
		emp.save()
		employees = employee.objects.all()
		serializer = UpdateemployeeSerializer(employees,many=True)
		return Response(serializer.data)


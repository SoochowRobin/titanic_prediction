from django.shortcuts import render
from . import fake_model
from . import ml_predict


def home(request):
	return render(request, 'index.html')

# get user input and output prediction based on model trained before 
def result(request):
	pclass = int(request.GET['pclass'])
	sex = int(request.GET['sex'])
	age = int(request.GET['age'])
	sibsp = int(request.GET['sibsp'])
	parch = int(request.GET['parch'])
	fare = int(request.GET['fare'])
	embarked = int(request.GET['embarked'])
	title = int(request.GET['title'])
	prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
	# if else condition here
	if prediction == 0:
		prediction = "Not survived"
	elif prediction == 1:
		prediction = "Survived"
	else:
		prediction = "Error"
	return render(request, 'result.html', {'result': prediction})
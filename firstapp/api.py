from .models import Question
from .serializers import QuestionSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

class QuestionList(APIView):
	def get(self, request):
		question = Question.objects.all()
		serialized_question = QuestionSerializer(question, many=True)
		return Response(serialized_question.data)
	
class QuestionDetail(APIView):	
	def get_object(self, pk):
		try:
			return Question.objects.all(pk=pk)
		except Question.DoesNotExist:
			raise Http404
			
	def get(self, request, pk, format=None):
		question = self.get_object(pk)
		serialized_question = QuestionSerializer(question)
		return Response(serialized_question.data)
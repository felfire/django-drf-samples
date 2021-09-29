from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from PyDictionary import PyDictionary

dictionary = PyDictionary()

class WordLookupView(APIView):

    # POST example: { "word": "building" }

    def post(self, request, *args, **kwargs):
        word = request.data.get('word', None)
        return Response({
            'word': word,
            'meaning': dictionary.meaning(word)
        })

        return Response({
            'error': 'Missing word.'
        }, status=status.HTTP_400_BAD_REQUEST)

class WordRegexView(APIView):

    # POST example: { "word": "building" }

    def post(self, request, *args, **kwargs):
        try:
            word = request.data.get('word', None)
            if word:
                return Response({
                    'word': word,
                    'meaning': dictionary.meaning(word)
                })
        except Exception as e:
            print(e)

        return Response({
            'error': 'Missing word.'
        }, status=status.HTTP_400_BAD_REQUEST)

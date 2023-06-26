from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(["GET"])
# Create your views here.
def getRoutes(request):
    routes = [
        {
            "Endpoint":"/notes",
            "method":"GET",
            "body":None,
            "description":"Return an array of notes"
        },

        {
            "Endpoint":"/notes/id",
            "method":"GET",
            "body":None,
            "description":"Return single note object"
        },

        {
            "Endpoint":"/notes/create/",
            "method":"POST",
            "body":{'body':""},
            "description":"Create new note woth data with sent post reqest"
        },
        {
            "Endpoint":"/notes/id/update/",
            "method":"PUT",
            "body":{"bpdy":""},
            "description":"Creates an existiong note with data sent in"
        },
        {
            "Endpoint":"/notes/id/delete/",
            "method":"GET",
            "body":None,
            "description":"Deletes exiting note"
        },
    ]
    return Response(routes)

@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many = True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request,pk):
    note = Note.objects.get(id = pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)

@api_view(["POST"])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data["body"]
    )
    serializer = NoteSerializer(note,many = False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateNote(request,pk):
    data = request.data
    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(note,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def deletNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted!")
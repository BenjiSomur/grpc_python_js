import notes_pb2
import notes_pb2_grpc
import grpc

e = notes_pb2.Empty()
nota = notes_pb2.Note()
nota.title = "Nota 5000"
nota.content = "Contenido 5000"


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = notes_pb2_grpc.NoteServiceStub(channel)
    nota2 = stub.insert(nota)
    print(nota2)


if __name__ == '__main__':
    run()

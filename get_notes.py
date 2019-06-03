import notes_pb2
import notes_pb2_grpc
import grpc

e = notes_pb2.Empty()


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = notes_pb2_grpc.NoteServiceStub(channel)
    lista = stub.list(e)
    print(lista)


if __name__ == '__main__':
    run()

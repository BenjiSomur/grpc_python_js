import notes_pb2
import notes_pb2_grpc
import grpc

with grpc.insecure_channel('grpcapi:50051') as channel:
    try:
        stub = notes_pb2_grpc.NoteServiceStub(channel)
        lista = stub.list(notes_pb2.Empty)
        print(lista)
    except Exception as ex:
        print(ex)

import grpc
import time
import notes_pb2
import notes_pb2_grpc
from concurrent import futures

ONE_DAY_IN_SECONDS = 60 * 60 * 24

list_notas = []

for x in range(0, 10):
    notaAux = notes_pb2.Note()
    notaAux.id = str(x)
    notaAux.title = "Nota "+str(x)
    notaAux.content = "Contenido "+str(x)
    list_notas.append(notaAux)


class NOTE(notes_pb2_grpc.NoteServiceServicer):
    def list(self, request, context):
        return list_notas


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_pb2_grpc.add_NoteServiceServicer_to_server(NOTE(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt as e:
        server.stop(0)


serve()

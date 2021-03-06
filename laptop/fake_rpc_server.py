from concurrent import futures
import logging
import numpy as np
import random

import grpc

from protos import jetsonrpc_pb2_grpc, jetsonrpc_pb2

import cv2

class Greeter(jetsonrpc_pb2_grpc.JetsonRPC):


    def cam_stream(self):
        cap = cv2.VideoCapture(0)
        while(True):
            ret, frame = cap.read()
            # convert frame to image

    def StreamMotorCurrent(self, request, context):
        while True:
            randoms = np.array([random.randint(0, 10) for i in range(8)], 'uint8') # 8 motors
            randoms = randoms.view('uint64') # combine into one value, as specified by the proto file
            yield jetsonrpc_pb2.MotorCurrent(values=randoms[0])
            
    def StreamIMU(self, request, context):
        while True:
            randomVals = []
            for i in range(6): # six values, 3 for linear acc, 3 for angular acc
                x = random.random()* 10 # random float between 0 and 10
                randomVals.append(x)
            yield jetsonrpc_pb2.IMUData(values = randomVals)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jetsonrpc_pb2_grpc.add_JetsonRPCServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()





if __name__ == '__main__':
    logging.basicConfig()
    serve()
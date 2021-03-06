# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import time
import sys

import helloworld_pb2
import gnmi_pb2

def generate_requests():
  requests = [gnmi_pb2.SubscribeRequest()]
  for req in requests:
     yield req
     time.sleep(2)  

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = gnmi_pb2.gNMIStub(channel)
  request = gnmi_pb2.SubscribeRequest()
  #up = gnmi_pb2.SubscribeRequest
  count = 0
  for response in stub.Subscribe(generate_requests()):
      #print("%s" % response)
      #print("%s" % response.update)
      #print("%s" % response.update.prefix)
      #for i in len(response.update):  # Loops and print
      #################
      sys.stdout = open('file', 'a')  
      print ("------------------------------------------------------------")
      print ("%s" % count)
      print("timestamp: %s" % response.update.timestamp) 
      #print("prefix: %s" % response.update.prefix) 
      prefix = "" 
      for p in response.update.prefix.element:
        prefix += "/" + p
      print("prefix: %s" % prefix) 
      for up in response.update.update:
        path = ""
        for p in up.path.element:
          path += p
        print(path + ":" + up.value.value) 
        
        #print ("%s",u)
       
      #print("%s:%s" % (response.update.update[0].path.element[0],response.update.update[0].value.value))
      #print("%s" % response.update.update[0].value.value)
      #################
      #print("%s" % response.update.timestamp)
      #print response
      time.sleep(2)
      count += 1
  print("------------------------------------------------------------")    

if __name__ == '__main__':
  run()

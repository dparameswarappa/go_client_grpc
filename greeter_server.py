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

"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import helloworld_pb2
import gnmi_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(gnmi_pb2.gNMIServicer):

  def Subscribe(self, request, context):
    while True:
      resp = gnmi_pb2.SubscribeResponse()
      resp.update.timestamp = 12142142334534543
      #resp.update.prefix.element = "alias-3"
      #bid_response = realtime_bidding_pb2.BidResponse()

      resp.update.prefix.element.append("system")
      resp.update.prefix.element.append("nettype")
      up = resp.update.update.add()
      up.path.element.append("temp-average")
      up.value.value = b"37"
      up = resp.update.update.add()
      up.path.element.append("temp-current")
      up.value.value = b"38"
      #resp.update.prefix = "alias-3"		
      yield resp


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  gnmi_pb2.add_gNMIServicer_to_server(Greeter(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()

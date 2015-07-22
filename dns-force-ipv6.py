#!/usr/bin/env python
from dnslib.server import *
from dnslib import *
class TestResolv:
    def resolve(self,request,handler):
        ipv4=False
        if request.q.qtype == QTYPE.A:
            ipv4=True
            request.q.qtype=QTYPE.AAAA
        fw=DNSRecord(q=request.q)
        b=fw.send("2a03:f80:ed15:ca7:ea75:b12d:714:d234",port=53,tcp=True,ipv6=True)
        reply=request.reply()
        answer = DNSRecord.parse(b)
        result_a = []
        result_aaaa = []
        for i in answer.rr:
            if i.rtype == QTYPE.AAAA:
                result_aaaa.append(i)
            elif i.rtype == QTYPE.A:
                result_a.append(i)
            else:
                reply.add_answer(i)
        if ipv4:
            if result_aaaa == []:
                request.q.qtype=QTYPE.A
                b=DNSRecord(q=request.q).send("2a03:f80:ed15:ca7:ea75:b12d:714:d234",tcp=True,ipv6=True)
                for i in DNSRecord.parse(b).rr:
                    reply.add_answer(i)
                return reply
            else:
                for i in result_aaaa:
                    reply.add_answer(i)
            for i in reply.questions:
                i.qtype=QTYPE.A
            reply.set_header_qa()
        return reply

resolver = TestResolv()
logger = DNSLogger(prefix=False)
server = DNSServer(resolver,port=53)
server.start()


##################################################
# file: VisualizerService_v3_0_0_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/local/bin/wsdl2py --complexType --lazy visualizerservice300.wsdl
# 
##################################################

from VisualizerService_v3_0_0_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class VisualizerService_v3_0_0Locator:
    VisualizerServiceEndpoint_address = "http://localhost:8080/visualizerservice202/services/visualizerservice"
    def getVisualizerServiceEndpointAddress(self):
        return VisualizerService_v3_0_0Locator.VisualizerServiceEndpoint_address
    def getVisualizerServiceEndpoint(self, url=None, **kw):
        return VisualizerServiceBindingSOAP(url or VisualizerService_v3_0_0Locator.VisualizerServiceEndpoint_address, **kw)

# Methods
class VisualizerServiceBindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: runVisualization
    def runVisualization(self, request, **kw):
        if isinstance(request, runVisualizationRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://service.apollo.pitt.edu/visualizerservice/v3_0_0/runVisualization", **kw)
        # no output wsaction
        response = self.binding.Receive(runVisualizationResponse.typecode)
        return response

runVisualizationRequest = GED("http://service.apollo.pitt.edu/visualizerservice/v3_0_0/", "runVisualization").pyclass

runVisualizationResponse = GED("http://service.apollo.pitt.edu/visualizerservice/v3_0_0/", "runVisualizationResponse").pyclass
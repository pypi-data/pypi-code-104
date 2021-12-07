# pylint:disable=line-too-long
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("mi.dll")
prototypes = \
    {
        # 
        'MI_Application_InitializeV1': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), SimTypePointer(SimTypePointer(SimStruct({"ft": SimTypePointer(SimStruct({"Clone": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Destruct": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Delete": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "IsA": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetClassNameA": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "SetNameSpace": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetNameSpace": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetElementCount": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "AddElement": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "SetElement": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "SetElementAt": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetElement": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetElementAt": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ClearElement": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ClearElementAt": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetServerName": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "SetServerName": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "GetClass": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="MI_InstanceFT", pack=False, align=None), offset=0), "classDecl": SimTypePointer(SimStruct({"flags": SimTypeInt(signed=False, label="UInt32"), "code": SimTypeInt(signed=False, label="UInt32"), "name": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "qualifiers": SimTypePointer(SimTypePointer(SimTypeBottom(label="MI_Qualifier"), offset=0), offset=0), "numQualifiers": SimTypeInt(signed=False, label="UInt32"), "properties": SimTypePointer(SimTypePointer(SimTypeBottom(label="MI_PropertyDecl"), offset=0), offset=0), "numProperties": SimTypeInt(signed=False, label="UInt32"), "size": SimTypeInt(signed=False, label="UInt32"), "superClass": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "superClassDecl": SimTypePointer(SimTypeBottom(label="MI_ClassDecl"), offset=0), "methods": SimTypePointer(SimTypePointer(SimTypeBottom(label="MI_MethodDecl"), offset=0), offset=0), "numMethods": SimTypeInt(signed=False, label="UInt32"), "schema": SimTypePointer(SimTypeBottom(label="MI_SchemaDecl"), offset=0), "providerFT": SimTypePointer(SimTypeBottom(label="MI_ProviderFT"), offset=0), "owningClass": SimTypePointer(SimTypeBottom(label="MI_Class"), offset=0)}, name="MI_ClassDecl", pack=False, align=None), offset=0), "serverName": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "nameSpace": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "reserved": SimTypeFixedSizeArray(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), 4)}, name="MI_Instance", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimStruct({"reserved1": SimTypeLongLong(signed=False, label="UInt64"), "reserved2": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ft": SimTypePointer(SimStruct({"Close": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewSession": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewHostedProvider": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewInstance": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewDestinationOptions": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewOperationOptions": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewSubscriptionDeliveryOptions": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewSerializer": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewDeserializer": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewInstanceFromClass": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "NewClass": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)}, name="MI_ApplicationFT", pack=False, align=None), offset=0)}, name="MI_Application", pack=False, align=None), offset=0)], SimTypeInt(signed=False, label="MI_Result"), arg_names=["flags", "applicationID", "extendedError", "application"]),
    }

lib.set_prototypes(prototypes)

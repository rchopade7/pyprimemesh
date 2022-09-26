""" Auto-generated file. DO NOT MODIFY """
# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
import enum
from typing import Dict, Any, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class MaterialPointType(enum.IntEnum):
    """Defines define type of material point.
    """
    DEAD = 0
    """Used to define dead material point."""
    LIVE = 1
    """Used to define live material point."""

class CreateMaterialPointParams(CoreObject):
    """Defines parameters to create material point.
    """
    _default_params = {}

    def __initialize(
            self,
            type: MaterialPointType):
        self._type = MaterialPointType(type)

    def __init__(
            self,
            model: CommunicationManager=None,
            type: MaterialPointType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateMaterialPointParams.

        Parameters
        ----------
        model: Model
            Model to create a CreateMaterialPointParams object with default parameters.
        type: MaterialPointType, optional
            Defines the type of material point.
        json_data: dict, optional
            JSON dictionary to create a CreateMaterialPointParams object with provided parameters.

        Examples
        --------
        >>> create_material_point_params = prime.CreateMaterialPointParams(model = model)
        """
        if json_data:
            self.__initialize(
                MaterialPointType(json_data["type"]))
        else:
            all_field_specified = all(arg is not None for arg in [type])
            if all_field_specified:
                self.__initialize(
                    type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "CreateMaterialPointParams")["CreateMaterialPointParams"]
                    self.__initialize(
                        type if type is not None else ( CreateMaterialPointParams._default_params["type"] if "type" in CreateMaterialPointParams._default_params else MaterialPointType(json_data["type"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            type: MaterialPointType = None):
        """Set the default values of CreateMaterialPointParams.

        Parameters
        ----------
        type: MaterialPointType, optional
            Defines the type of material point.
        """
        args = locals()
        [CreateMaterialPointParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateMaterialPointParams.

        Examples
        --------
        >>> CreateMaterialPointParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateMaterialPointParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["type"] = self._type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "type :  %s" % (self._type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def type(self) -> MaterialPointType:
        """Defines the type of material point.
        """
        return self._type

    @type.setter
    def type(self, value: MaterialPointType):
        self._type = value

class CreateMaterialPointResults(CoreObject):
    """Results structure associated with create material point operation.
    """
    _default_params = {}

    def __initialize(
            self,
            id: int,
            assigned_name: str,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._id = id
        self._assigned_name = assigned_name
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            id: int = None,
            assigned_name: str = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateMaterialPointResults.

        Parameters
        ----------
        model: Model
            Model to create a CreateMaterialPointResults object with default parameters.
        id: int, optional
            Id of the material point created.
        assigned_name: str, optional
            Assigned name of the material point created.
        error_code: ErrorCode, optional
            Error code associated with create material point operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with create material point operation.
        json_data: dict, optional
            JSON dictionary to create a CreateMaterialPointResults object with provided parameters.

        Examples
        --------
        >>> create_material_point_results = prime.CreateMaterialPointResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["id"],
                json_data["assignedName"],
                ErrorCode(json_data["errorCode"]),
                [WarningCode(data) for data in json_data["warningCodes"]])
        else:
            all_field_specified = all(arg is not None for arg in [id, assigned_name, error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    id,
                    assigned_name,
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "CreateMaterialPointResults")["CreateMaterialPointResults"]
                    self.__initialize(
                        id if id is not None else ( CreateMaterialPointResults._default_params["id"] if "id" in CreateMaterialPointResults._default_params else json_data["id"]),
                        assigned_name if assigned_name is not None else ( CreateMaterialPointResults._default_params["assigned_name"] if "assigned_name" in CreateMaterialPointResults._default_params else json_data["assignedName"]),
                        error_code if error_code is not None else ( CreateMaterialPointResults._default_params["error_code"] if "error_code" in CreateMaterialPointResults._default_params else ErrorCode(json_data["errorCode"])),
                        warning_codes if warning_codes is not None else ( CreateMaterialPointResults._default_params["warning_codes"] if "warning_codes" in CreateMaterialPointResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            id: int = None,
            assigned_name: str = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of CreateMaterialPointResults.

        Parameters
        ----------
        id: int, optional
            Id of the material point created.
        assigned_name: str, optional
            Assigned name of the material point created.
        error_code: ErrorCode, optional
            Error code associated with create material point operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with create material point operation.
        """
        args = locals()
        [CreateMaterialPointResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateMaterialPointResults.

        Examples
        --------
        >>> CreateMaterialPointResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateMaterialPointResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["id"] = self._id
        json_data["assignedName"] = self._assigned_name
        json_data["errorCode"] = self._error_code
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "id :  %s\nassigned_name :  %s\nerror_code :  %s\nwarning_codes :  %s" % (self._id, self._assigned_name, self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def id(self) -> int:
        """Id of the material point created.
        """
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def assigned_name(self) -> str:
        """Assigned name of the material point created.
        """
        return self._assigned_name

    @assigned_name.setter
    def assigned_name(self, value: str):
        self._assigned_name = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with create material point operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with create material point operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value
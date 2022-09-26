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

class SurferParams(CoreObject):
    """Parameters used to generate surface mesh.
    """
    _default_params = {}

    def __initialize(
            self,
            size_field_type: SizeFieldType,
            min_size: float,
            max_size: float,
            growth_rate: float,
            constant_size: float,
            generate_quads: bool,
            smooth_size_transition: bool,
            enable_multi_threading: bool):
        self._size_field_type = SizeFieldType(size_field_type)
        self._min_size = min_size
        self._max_size = max_size
        self._growth_rate = growth_rate
        self._constant_size = constant_size
        self._generate_quads = generate_quads
        self._smooth_size_transition = smooth_size_transition
        self._enable_multi_threading = enable_multi_threading

    def __init__(
            self,
            model: CommunicationManager=None,
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            generate_quads: bool = None,
            smooth_size_transition: bool = None,
            enable_multi_threading: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurferParams.

        Parameters
        ----------
        model: Model
            Model to create a SurferParams object with default parameters.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Size used in constant size surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        smooth_size_transition: bool, optional
            Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.
        enable_multi_threading: bool, optional
            Option to perform surface meshing in parallel using multithreads.
        json_data: dict, optional
            JSON dictionary to create a SurferParams object with provided parameters.

        Examples
        --------
        >>> surfer_params = prime.SurferParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["sizeFieldType"]),
                json_data["minSize"],
                json_data["maxSize"],
                json_data["growthRate"],
                json_data["constantSize"],
                json_data["generateQuads"],
                json_data["smoothSizeTransition"],
                json_data["enableMultiThreading"])
        else:
            all_field_specified = all(arg is not None for arg in [size_field_type, min_size, max_size, growth_rate, constant_size, generate_quads, smooth_size_transition, enable_multi_threading])
            if all_field_specified:
                self.__initialize(
                    size_field_type,
                    min_size,
                    max_size,
                    growth_rate,
                    constant_size,
                    generate_quads,
                    smooth_size_transition,
                    enable_multi_threading)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SurferParams")["SurferParams"]
                    self.__initialize(
                        size_field_type if size_field_type is not None else ( SurferParams._default_params["size_field_type"] if "size_field_type" in SurferParams._default_params else SizeFieldType(json_data["sizeFieldType"])),
                        min_size if min_size is not None else ( SurferParams._default_params["min_size"] if "min_size" in SurferParams._default_params else json_data["minSize"]),
                        max_size if max_size is not None else ( SurferParams._default_params["max_size"] if "max_size" in SurferParams._default_params else json_data["maxSize"]),
                        growth_rate if growth_rate is not None else ( SurferParams._default_params["growth_rate"] if "growth_rate" in SurferParams._default_params else json_data["growthRate"]),
                        constant_size if constant_size is not None else ( SurferParams._default_params["constant_size"] if "constant_size" in SurferParams._default_params else json_data["constantSize"]),
                        generate_quads if generate_quads is not None else ( SurferParams._default_params["generate_quads"] if "generate_quads" in SurferParams._default_params else json_data["generateQuads"]),
                        smooth_size_transition if smooth_size_transition is not None else ( SurferParams._default_params["smooth_size_transition"] if "smooth_size_transition" in SurferParams._default_params else json_data["smoothSizeTransition"]),
                        enable_multi_threading if enable_multi_threading is not None else ( SurferParams._default_params["enable_multi_threading"] if "enable_multi_threading" in SurferParams._default_params else json_data["enableMultiThreading"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            generate_quads: bool = None,
            smooth_size_transition: bool = None,
            enable_multi_threading: bool = None):
        """Set the default values of SurferParams.

        Parameters
        ----------
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Size used in constant size surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        smooth_size_transition: bool, optional
            Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.
        enable_multi_threading: bool, optional
            Option to perform surface meshing in parallel using multithreads.
        """
        args = locals()
        [SurferParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurferParams.

        Examples
        --------
        >>> SurferParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurferParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["sizeFieldType"] = self._size_field_type
        json_data["minSize"] = self._min_size
        json_data["maxSize"] = self._max_size
        json_data["growthRate"] = self._growth_rate
        json_data["constantSize"] = self._constant_size
        json_data["generateQuads"] = self._generate_quads
        json_data["smoothSizeTransition"] = self._smooth_size_transition
        json_data["enableMultiThreading"] = self._enable_multi_threading
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "size_field_type :  %s\nmin_size :  %s\nmax_size :  %s\ngrowth_rate :  %s\nconstant_size :  %s\ngenerate_quads :  %s\nsmooth_size_transition :  %s\nenable_multi_threading :  %s" % (self._size_field_type, self._min_size, self._max_size, self._growth_rate, self._constant_size, self._generate_quads, self._smooth_size_transition, self._enable_multi_threading)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def size_field_type(self) -> SizeFieldType:
        """Size field type used to generate surface mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def min_size(self) -> float:
        """Minimum size to be used in sizing for the surfer.
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value: float):
        self._min_size = value

    @property
    def max_size(self) -> float:
        """Maximum size to be used in sizing for the surfer.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def growth_rate(self) -> float:
        """Growth rate to be used to propagate sizes.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def constant_size(self) -> float:
        """Size used in constant size surface meshing.
        """
        return self._constant_size

    @constant_size.setter
    def constant_size(self, value: float):
        self._constant_size = value

    @property
    def generate_quads(self) -> bool:
        """Option to generate quadrilateral surface mesh.
        """
        return self._generate_quads

    @generate_quads.setter
    def generate_quads(self, value: bool):
        self._generate_quads = value

    @property
    def smooth_size_transition(self) -> bool:
        """Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.

        Notes
         -----
          - Input facets or mesh with finer sizes compared to neighboring face edge sizes are required for this option to work.
          - Valid min, max sizes and growth rate are required to include the neighboring face edges sizes in sizing.
        """
        return self._smooth_size_transition

    @smooth_size_transition.setter
    def smooth_size_transition(self, value: bool):
        self._smooth_size_transition = value

    @property
    def enable_multi_threading(self) -> bool:
        """Option to perform surface meshing in parallel using multithreads.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value

class SurferResults(CoreObject):
    """Results associated with the surface mesh.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurferResults.

        Parameters
        ----------
        model: Model
            Model to create a SurferResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a SurferResults object with provided parameters.

        Examples
        --------
        >>> surfer_results = prime.SurferResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SurferResults")["SurferResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( SurferResults._default_params["error_code"] if "error_code" in SurferResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of SurferResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [SurferResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurferResults.

        Examples
        --------
        >>> SurferResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurferResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class LocalSurferParams(CoreObject):
    """Parameters to perform local surface remeshing.
    """
    _default_params = {}

    def __initialize(
            self,
            size_field_type: SizeFieldType,
            min_size: float,
            max_size: float,
            growth_rate: float,
            constant_size: float,
            smooth_boundary: bool,
            n_rings: int):
        self._size_field_type = SizeFieldType(size_field_type)
        self._min_size = min_size
        self._max_size = max_size
        self._growth_rate = growth_rate
        self._constant_size = constant_size
        self._smooth_boundary = smooth_boundary
        self._n_rings = n_rings

    def __init__(
            self,
            model: CommunicationManager=None,
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            smooth_boundary: bool = None,
            n_rings: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the LocalSurferParams.

        Parameters
        ----------
        model: Model
            Model to create a LocalSurferParams object with default parameters.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Constant size to be used in case of constant size field.
        smooth_boundary: bool, optional
            Option to extend local selection to get smooth boundary of selected elements.
        n_rings: int, optional
            Number of rings to extend the registered face selection for remeshing.
        json_data: dict, optional
            JSON dictionary to create a LocalSurferParams object with provided parameters.

        Examples
        --------
        >>> local_surfer_params = prime.LocalSurferParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["sizeFieldType"]),
                json_data["minSize"],
                json_data["maxSize"],
                json_data["growthRate"],
                json_data["constantSize"],
                json_data["smoothBoundary"],
                json_data["nRings"])
        else:
            all_field_specified = all(arg is not None for arg in [size_field_type, min_size, max_size, growth_rate, constant_size, smooth_boundary, n_rings])
            if all_field_specified:
                self.__initialize(
                    size_field_type,
                    min_size,
                    max_size,
                    growth_rate,
                    constant_size,
                    smooth_boundary,
                    n_rings)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "LocalSurferParams")["LocalSurferParams"]
                    self.__initialize(
                        size_field_type if size_field_type is not None else ( LocalSurferParams._default_params["size_field_type"] if "size_field_type" in LocalSurferParams._default_params else SizeFieldType(json_data["sizeFieldType"])),
                        min_size if min_size is not None else ( LocalSurferParams._default_params["min_size"] if "min_size" in LocalSurferParams._default_params else json_data["minSize"]),
                        max_size if max_size is not None else ( LocalSurferParams._default_params["max_size"] if "max_size" in LocalSurferParams._default_params else json_data["maxSize"]),
                        growth_rate if growth_rate is not None else ( LocalSurferParams._default_params["growth_rate"] if "growth_rate" in LocalSurferParams._default_params else json_data["growthRate"]),
                        constant_size if constant_size is not None else ( LocalSurferParams._default_params["constant_size"] if "constant_size" in LocalSurferParams._default_params else json_data["constantSize"]),
                        smooth_boundary if smooth_boundary is not None else ( LocalSurferParams._default_params["smooth_boundary"] if "smooth_boundary" in LocalSurferParams._default_params else json_data["smoothBoundary"]),
                        n_rings if n_rings is not None else ( LocalSurferParams._default_params["n_rings"] if "n_rings" in LocalSurferParams._default_params else json_data["nRings"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            smooth_boundary: bool = None,
            n_rings: int = None):
        """Set the default values of LocalSurferParams.

        Parameters
        ----------
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Constant size to be used in case of constant size field.
        smooth_boundary: bool, optional
            Option to extend local selection to get smooth boundary of selected elements.
        n_rings: int, optional
            Number of rings to extend the registered face selection for remeshing.
        """
        args = locals()
        [LocalSurferParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of LocalSurferParams.

        Examples
        --------
        >>> LocalSurferParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in LocalSurferParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["sizeFieldType"] = self._size_field_type
        json_data["minSize"] = self._min_size
        json_data["maxSize"] = self._max_size
        json_data["growthRate"] = self._growth_rate
        json_data["constantSize"] = self._constant_size
        json_data["smoothBoundary"] = self._smooth_boundary
        json_data["nRings"] = self._n_rings
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "size_field_type :  %s\nmin_size :  %s\nmax_size :  %s\ngrowth_rate :  %s\nconstant_size :  %s\nsmooth_boundary :  %s\nn_rings :  %s" % (self._size_field_type, self._min_size, self._max_size, self._growth_rate, self._constant_size, self._smooth_boundary, self._n_rings)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def size_field_type(self) -> SizeFieldType:
        """Size field type used to generate surface mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def min_size(self) -> float:
        """Minimum size to be used in sizing for the surfer.
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value: float):
        self._min_size = value

    @property
    def max_size(self) -> float:
        """Maximum size to be used in sizing for the surfer.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def growth_rate(self) -> float:
        """Growth rate to be used to propagate sizes.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def constant_size(self) -> float:
        """Constant size to be used in case of constant size field.
        """
        return self._constant_size

    @constant_size.setter
    def constant_size(self, value: float):
        self._constant_size = value

    @property
    def smooth_boundary(self) -> bool:
        """Option to extend local selection to get smooth boundary of selected elements.
        """
        return self._smooth_boundary

    @smooth_boundary.setter
    def smooth_boundary(self, value: bool):
        self._smooth_boundary = value

    @property
    def n_rings(self) -> int:
        """Number of rings to extend the registered face selection for remeshing.
        """
        return self._n_rings

    @n_rings.setter
    def n_rings(self, value: int):
        self._n_rings = value

class LocalSurferResults(CoreObject):
    """Results associated with the local surface mesh.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the LocalSurferResults.

        Parameters
        ----------
        model: Model
            Model to create a LocalSurferResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        json_data: dict, optional
            JSON dictionary to create a LocalSurferResults object with provided parameters.

        Examples
        --------
        >>> local_surfer_results = prime.LocalSurferResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                [WarningCode(data) for data in json_data["warningCodes"]])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "LocalSurferResults")["LocalSurferResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( LocalSurferResults._default_params["error_code"] if "error_code" in LocalSurferResults._default_params else ErrorCode(json_data["errorCode"])),
                        warning_codes if warning_codes is not None else ( LocalSurferResults._default_params["warning_codes"] if "warning_codes" in LocalSurferResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of LocalSurferResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [LocalSurferResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of LocalSurferResults.

        Examples
        --------
        >>> LocalSurferResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in LocalSurferResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value
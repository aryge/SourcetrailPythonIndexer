# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_sourcetraildb')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_sourcetraildb')
    _sourcetraildb = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sourcetraildb', [dirname(__file__)])
        except ImportError:
            import _sourcetraildb
            return _sourcetraildb
        try:
            _mod = imp.load_module('_sourcetraildb', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _sourcetraildb = swig_import_helper()
    del swig_import_helper
else:
    import _sourcetraildb
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

DEFINITION_IMPLICIT = _sourcetraildb.DEFINITION_IMPLICIT
DEFINITION_EXPLICIT = _sourcetraildb.DEFINITION_EXPLICIT
SYMBOL_TYPE = _sourcetraildb.SYMBOL_TYPE
SYMBOL_BUILTIN_TYPE = _sourcetraildb.SYMBOL_BUILTIN_TYPE
SYMBOL_MODULE = _sourcetraildb.SYMBOL_MODULE
SYMBOL_NAMESPACE = _sourcetraildb.SYMBOL_NAMESPACE
SYMBOL_PACKAGE = _sourcetraildb.SYMBOL_PACKAGE
SYMBOL_STRUCT = _sourcetraildb.SYMBOL_STRUCT
SYMBOL_CLASS = _sourcetraildb.SYMBOL_CLASS
SYMBOL_INTERFACE = _sourcetraildb.SYMBOL_INTERFACE
SYMBOL_ANNOTATION = _sourcetraildb.SYMBOL_ANNOTATION
SYMBOL_GLOBAL_VARIABLE = _sourcetraildb.SYMBOL_GLOBAL_VARIABLE
SYMBOL_FIELD = _sourcetraildb.SYMBOL_FIELD
SYMBOL_FUNCTION = _sourcetraildb.SYMBOL_FUNCTION
SYMBOL_METHOD = _sourcetraildb.SYMBOL_METHOD
SYMBOL_ENUM = _sourcetraildb.SYMBOL_ENUM
SYMBOL_ENUM_CONSTANT = _sourcetraildb.SYMBOL_ENUM_CONSTANT
SYMBOL_TYPEDEF = _sourcetraildb.SYMBOL_TYPEDEF
SYMBOL_TEMPLATE_PARAMETER = _sourcetraildb.SYMBOL_TEMPLATE_PARAMETER
SYMBOL_TYPE_PARAMETER = _sourcetraildb.SYMBOL_TYPE_PARAMETER
SYMBOL_MACRO = _sourcetraildb.SYMBOL_MACRO
SYMBOL_UNION = _sourcetraildb.SYMBOL_UNION
REFERENCE_TYPE_USAGE = _sourcetraildb.REFERENCE_TYPE_USAGE
REFERENCE_USAGE = _sourcetraildb.REFERENCE_USAGE
REFERENCE_CALL = _sourcetraildb.REFERENCE_CALL
REFERENCE_INHERITANCE = _sourcetraildb.REFERENCE_INHERITANCE
REFERENCE_OVERRIDE = _sourcetraildb.REFERENCE_OVERRIDE
REFERENCE_TEMPLATE_ARGUMENT = _sourcetraildb.REFERENCE_TEMPLATE_ARGUMENT
REFERENCE_TYPE_ARGUMENT = _sourcetraildb.REFERENCE_TYPE_ARGUMENT
REFERENCE_TEMPLATE_DEFAULT_ARGUMENT = _sourcetraildb.REFERENCE_TEMPLATE_DEFAULT_ARGUMENT
REFERENCE_TEMPLATE_SPECIALIZATION = _sourcetraildb.REFERENCE_TEMPLATE_SPECIALIZATION
REFERENCE_TEMPLATE_MEMBER_SPECIALIZATION = _sourcetraildb.REFERENCE_TEMPLATE_MEMBER_SPECIALIZATION
REFERENCE_INCLUDE = _sourcetraildb.REFERENCE_INCLUDE
REFERENCE_IMPORT = _sourcetraildb.REFERENCE_IMPORT
REFERENCE_MACRO_USAGE = _sourcetraildb.REFERENCE_MACRO_USAGE
REFERENCE_ANNOTATION_USAGE = _sourcetraildb.REFERENCE_ANNOTATION_USAGE

def getSupportedDatabaseVersion():
    """getSupportedDatabaseVersion() -> int"""
    return _sourcetraildb.getSupportedDatabaseVersion()

def getLastError():
    """getLastError() -> std::string"""
    return _sourcetraildb.getLastError()

def clearLastError():
    """clearLastError()"""
    return _sourcetraildb.clearLastError()

def open(databaseFilePath):
    """open(std::string databaseFilePath) -> bool"""
    return _sourcetraildb.open(databaseFilePath)

def close():
    """close() -> bool"""
    return _sourcetraildb.close()

def clear():
    """clear() -> bool"""
    return _sourcetraildb.clear()

def isEmpty():
    """isEmpty() -> bool"""
    return _sourcetraildb.isEmpty()

def isCompatible():
    """isCompatible() -> bool"""
    return _sourcetraildb.isCompatible()

def getLoadedDatabaseVersion():
    """getLoadedDatabaseVersion() -> int"""
    return _sourcetraildb.getLoadedDatabaseVersion()

def beginTransaction():
    """beginTransaction() -> bool"""
    return _sourcetraildb.beginTransaction()

def commitTransaction():
    """commitTransaction() -> bool"""
    return _sourcetraildb.commitTransaction()

def rollbackTransaction():
    """rollbackTransaction() -> bool"""
    return _sourcetraildb.rollbackTransaction()

def optimizeDatabaseMemory():
    """optimizeDatabaseMemory() -> bool"""
    return _sourcetraildb.optimizeDatabaseMemory()

def recordSymbol(serializedNameHierarchy):
    """recordSymbol(std::string serializedNameHierarchy) -> int"""
    return _sourcetraildb.recordSymbol(serializedNameHierarchy)

def recordSymbolDefinitionKind(symbolId, symbolDefinitionKind):
    """recordSymbolDefinitionKind(int symbolId, DefinitionKind symbolDefinitionKind) -> bool"""
    return _sourcetraildb.recordSymbolDefinitionKind(symbolId, symbolDefinitionKind)

def recordSymbolKind(symbolId, symbolKind):
    """recordSymbolKind(int symbolId, SymbolKind symbolKind) -> bool"""
    return _sourcetraildb.recordSymbolKind(symbolId, symbolKind)

def recordSymbolLocation(symbolId, fileId, startLine, startColumn, endLine, endColumn):
    """recordSymbolLocation(int symbolId, int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordSymbolLocation(symbolId, fileId, startLine, startColumn, endLine, endColumn)

def recordSymbolScopeLocation(symbolId, fileId, startLine, startColumn, endLine, endColumn):
    """recordSymbolScopeLocation(int symbolId, int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordSymbolScopeLocation(symbolId, fileId, startLine, startColumn, endLine, endColumn)

def recordSymbolSignatureLocation(symbolId, fileId, startLine, startColumn, endLine, endColumn):
    """recordSymbolSignatureLocation(int symbolId, int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordSymbolSignatureLocation(symbolId, fileId, startLine, startColumn, endLine, endColumn)

def recordReference(contextSymbolId, referencedSymbolId, referenceKind):
    """recordReference(int contextSymbolId, int referencedSymbolId, ReferenceKind referenceKind) -> int"""
    return _sourcetraildb.recordReference(contextSymbolId, referencedSymbolId, referenceKind)

def recordReferenceLocation(referenceId, fileId, startLine, startColumn, endLine, endColumn):
    """recordReferenceLocation(int referenceId, int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordReferenceLocation(referenceId, fileId, startLine, startColumn, endLine, endColumn)

def recordFile(filePath):
    """recordFile(std::string filePath) -> int"""
    return _sourcetraildb.recordFile(filePath)

def recordFileLanguage(fileId, languageIdentifier):
    """recordFileLanguage(int fileId, std::string languageIdentifier) -> bool"""
    return _sourcetraildb.recordFileLanguage(fileId, languageIdentifier)

def recordLocalSymbol(name):
    """recordLocalSymbol(std::string name) -> int"""
    return _sourcetraildb.recordLocalSymbol(name)

def recordLocalSymbolLocation(localSymbolId, fileId, startLine, startColumn, endLine, endColumn):
    """recordLocalSymbolLocation(int localSymbolId, int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordLocalSymbolLocation(localSymbolId, fileId, startLine, startColumn, endLine, endColumn)

def recordCommentLocation(fileId, startLine, startColumn, endLine, endColumn):
    """recordCommentLocation(int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordCommentLocation(fileId, startLine, startColumn, endLine, endColumn)

def recordError(message, fatal, fileId, startLine, startColumn, endLine, endColumn):
    """recordError(std::string message, bool fatal, int fileId, int startLine, int startColumn, int endLine, int endColumn) -> bool"""
    return _sourcetraildb.recordError(message, fatal, fileId, startLine, startColumn, endLine, endColumn)
# This file is compatible with both classic and new-style classes.



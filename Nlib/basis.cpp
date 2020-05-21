#include "module.h"

// Definitions /////////////////////////////////////////////////////////////////
PyObject* BasisException = NULL;

PyObject* PyInit_BasisInitHandler(PyObject*);

static void      BASIS_dealloc(BASIS*);
static PyObject* BASIS_new(PyTypeObject*, PyObject*, PyObject*);
static int       BASIS_init(BASIS*, PyObject*, PyObject*);

static PyObject* BASIS_setbasis(BASIS*);

// Static declared /////////////////////////////////////////////////////////////
void
BASIS_dealloc(BASIS* self)
{
    Py_XDECREF(self->arg_num);
    Py_XDECREF(self->test_str);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

// instance initialize
PyObject*
BASIS_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
    BASIS* self = NULL;
    self = (BASIS* )type->tp_alloc(type, 0);
     
    if (self != NULL) {
        self->arg_num             = NULL;
        self->test_str             = NULL;
    }

    return (PyObject*)self;
}

// argument initialize
int
BASIS_init(BASIS* self, PyObject* args, PyObject* kwds)
{
    PyObject*       arg_num = NULL, *tmp;
    static char*    kwlist[] = {"arg", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|S", kwlist, &arg_num))
        return -1;

    if (arg_num)
    {
        tmp = self->arg_num;
        Py_INCREF(arg_num);
        self->arg_num = arg_num;
        Py_XDECREF(tmp);
    }

    return 0;
}

// instance member initialize
static PyMemberDef BASIS_members[] = {
    {"arg_num", T_OBJECT_EX, offsetof(BASIS, arg_num), 0, "arg_num"},
    {"test_str", T_OBJECT_EX, offsetof(BASIS, test_str), 0, "test_str"},
    {NULL}  /* Sentinel */
};

// instance method initialize
static PyMethodDef BASIS_methods[] = {
    {"setbasis", (PyCFunction)BASIS_setbasis, METH_NOARGS, "set the vandor"},
    {NULL}  /* Sentinel */
};

// create class type
static PyTypeObject BASISType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "LibTest.BASIS",             /* tp_name */
    sizeof(BASIS),             /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)BASIS_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "BASIS objects",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    BASIS_methods,             /* tp_methods */
    BASIS_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)BASIS_init,      /* tp_init */
    0,                         /* tp_alloc */
    BASIS_new,                 /* tp_new */
};


// API implementation //////////////////////////////////////////////////////////
// module initialize
static PyMethodDef module_methods[] = {
    {NULL}  /* Sentinel */
};


void
BASIS_setArray(PyObject** membername, const char* _str)
{
    PyObject*       strobj=NULL, *rstrobj=NULL;
    long i = 0;

    *membername = PyList_New(4);
    for (i = 0; i < 4; i++)
    {
        strobj = PyString_FromString(_str);
        rstrobj = PyObject_Repr(strobj);

        Py_XDECREF(strobj);
        PyList_SetItem(*membername, i, rstrobj);
    }       
}

PyObject *
BASIS_setbasis(BASIS* self)
{

    //BASIS_EXCEPTION(-1, "Faile Exception");

    BASIS_setArray(&self->test_str, "hello world");
    
    return Py_BuildValue("i", -1);
}


PyObject*
PyInit_BasisInitHandler(PyObject* parent)
{
	PyObject* m = NULL;

	if (PyType_Ready(&BASISType) < 0)
        return Py_BuildValue("i", -1);

    if(NULL == (BasisException = PyErr_NewException("BasisHandler.BasisException",
                                                       PyExc_Exception,
                                                       NULL)))
    {
        DEPRINT("NewException");
        return Py_BuildValue("i", -1);
    }
    m = Py_InitModule("LibTest", module_methods);

    Py_INCREF(&BASISType);
    PyModule_AddObject(m, "BasisException", BasisException);
    PyModule_AddObject(parent, "BASIS", (PyObject *)&BASISType);

    return m;
}

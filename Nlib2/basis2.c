#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"



// Definitions /////////////////////////////////////////////////////////////////
typedef struct {
    PyObject_HEAD

	PyObject *first;
	PyObject *last;
	int number;
} spamObject;

static PyObject* SpamException = NULL;
static void spam_dealloc(spamObject* );
static PyObject* spam_new(PyTypeObject*, PyObject*, PyObject*);
static int spam_init(spamObject*, PyObject*, PyObject*);

static PyObject *
spam_name(spamObject*, PyObject*);



// Static declared /////////////////////////////////////////////////////////////
static PyMemberDef spamMembers[] = {
	{"first", T_OBJECT_EX, offsetof(spamObject, first), 0, "first name"},
	{"last", T_OBJECT_EX, offsetof(spamObject, last), 0, "last name"},
	{"number", T_INT, offsetof(spamObject, number), 0, "custom number"},
	{NULL}
};

static PyMethodDef SpamMethods[] = {
    {"name", (PyCFunction) spam_name, METH_NOARGS,
     "Return the name, combining the first and last name"},
    {NULL}
};

static PyTypeObject spamType = {
	PyVarObject_HEAD_INIT(NULL, 0)

	.tp_name 		= "spam.Spam",
    .tp_doc 		= "spam objects",
    .tp_basicsize 	= sizeof(spamObject),
    .tp_itemsize 	= 0,
    .tp_flags 		= Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_members		= spamMembers,
    .tp_methods 	= SpamMethods,
    .tp_new 		= spam_new,
    .tp_dealloc 	= (destructor) spam_dealloc,
    .tp_init 		= (initproc) spam_init,
};


static struct PyModuleDef spamModule = {
	PyModuleDef_HEAD_INIT,
	"spam",
	"INit",
	-1,
};



// Static implementation //////////////////////////////////////////////////////////
static PyObject*
spam_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    spamObject* self;

    self = (spamObject*) type->tp_alloc(type, 0);

    if (self != NULL)
    {
        self->first = PyUnicode_FromString("");
        if (self->first == NULL)
        {
            Py_DECREF(self);
            return NULL;
        }

        self->last = PyUnicode_FromString("");
        if (self->last == NULL)
        {
            Py_DECREF(self);
            return NULL;
        }
        self->number = 0;
    }

    return (PyObject*) self;
}


static int
spam_init(spamObject *self, PyObject *args, PyObject *kwds)
{
    PyObject *first = NULL, *last = NULL, *tmp;
    static char *kwlist[] = {"first", "last", "number", NULL};    

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first)
    {
        tmp = self->first;
        Py_INCREF(first);

        self->first = first;
        Py_XDECREF(tmp);
    }

    if (last)
    {
        tmp = self->last;
        Py_INCREF(last);

        self->last = last;
        Py_XDECREF(tmp);
    }

    return 0;
}


static void
spam_dealloc(spamObject *self)
{
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    Py_TYPE(self)->tp_free((PyObject *) self);
}



// API implementation //////////////////////////////////////////////////////////
static PyObject *
spam_name(spamObject *self, PyObject *Py_UNUSED(ignored))
{
    if (self->first == NULL) {
        PyErr_SetString(PyExc_AttributeError, "first");
        return NULL;
    }
    if (self->last == NULL) {
        PyErr_SetString(PyExc_AttributeError, "last");
        return NULL;
    }
    return PyUnicode_FromFormat("%S %S", self->first, self->last);
}


PyMODINIT_FUNC
PyInit_spam(void)
{
	PyObject* m = NULL;

    if (PyType_Ready(&spamType) < 0)
        return NULL;

	if(NULL == (m = PyModule_Create(&spamModule)))
	{
		//DEPRINT("spam module create");
		return NULL;
	}


	if (NULL == (SpamException = PyErr_NewException("spam.Exception",
													PyExc_Exception,
													NULL)))
	{
		//DEPRINT("NewException");
		return NULL;
	}

	Py_INCREF(SpamException);
	if (PyModule_AddObject(m, "Exception", SpamException) < 0)
	{
		Py_DECREF(SpamException);
		Py_DECREF(m);

		return NULL;
	}

	Py_INCREF(&spamType);
	if (PyModule_AddObject(m, "Spam", (PyObject *) &spamType) < 0)
	{
		Py_DECREF(&spamType);
		Py_DECREF(SpamException);
		Py_DECREF(m);

		return NULL;
	}

	return m;
}

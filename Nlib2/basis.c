#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject* SpamException = NULL;

static PyObject *
spam_strlen(PyObject* self, PyObject* a_args)
{
	const char* args;

	if(!PyArg_ParseTuple(a_args, "s", &args))
		return NULL;

	return Py_BuildValue("i", 12345);
}

static PyMethodDef SpamMethods[] = {
	{"strlen", spam_strlen, METH_VARARGS, "coun"},
	{NULL, NULL, 0, NULL}

};


static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",
	"INit",
	-1,
	SpamMethods

};


PyMODINIT_FUNC
PyInit_spam(void)
{
	PyObject* m = NULL;


	if(NULL == (m = PyModule_Create(&spammodule)))
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
		Py_CLEAR(SpamException);
		Py_DECREF(m);

		return NULL;
	}

	return m;
}

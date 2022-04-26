#include "libmypy.h"

char addfunc_docs[] = "Add two numbers function.";

PyMethodDef cadd_funcs[] = {
	{	"add",
		(PyCFunction)add,
		METH_VARARGS,
		addfunc_docs},

	{	NULL}
};

char helloworldmod_docs[] = "This is hello world module.";

PyModuleDef helloworld_mod = {
	PyModuleDef_HEAD_INIT,
	"cadd",
	helloworldmod_docs,
	-1,
	cadd_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_cadd(void) {
	return PyModule_Create(&helloworld_mod);
}

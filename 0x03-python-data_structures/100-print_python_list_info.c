#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic info about Python lists
 * @p: input
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	PyObject *t;
	PyListObject *list = (PyListObject *)p;
	int i, size, alc;

	size = Py_SIZE(p);
	alc = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alc);
	for (i = 0; i < size; i++)
	{
		t = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(t)->tp_name);
	}
}

#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: A pointer to a PyObject (Python list)
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int j;
	PyObject *element

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);


	for (j = 0; i < size; i++)
	{
		element = PyList_GetItem(p, j);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name); }

}

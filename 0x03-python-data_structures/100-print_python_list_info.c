#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: A pointer to a PyObject (Python list)
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int i;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	i = 0;

	for (i; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name); }

}

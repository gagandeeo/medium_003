#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include<iostream>
#include <vector>

using namespace std;

vector<int> insertionSort(vector<int> arr, int n)
{
    int i, key, j;

    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }

    return arr;
}

PYBIND11_MODULE(cpp_wrapper, m) {
    m.doc() = "pybind11 insertionSort plugin";
    m.def("insertionSort", &insertionSort, "A function to sort");
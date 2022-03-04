use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn insertion_sort(py:Python, obj: PyObject, len: usize) -> PyResult<PyObject> {
    if let Ok(mut s) = obj.extract::<Vec<i32>>(py) {
        for i in 1..len {
            let mut j = i;
            while j > 0 && s[j - 1] > s[j] {
                s.swap(j - 1, j);
                j -= 1;
            }   
        }
        return Ok(s.to_object(py))
    }
    Err(PyTypeError::new_err("Not Supported"))
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_wrapper(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(insertion_sort, m)?)?;
    Ok(())
}